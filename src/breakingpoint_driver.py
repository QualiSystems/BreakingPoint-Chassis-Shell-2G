"""
BreakingPoint chassis shell driver.
"""
import logging
from typing import Dict

import requests
from cloudshell.logging.qs_logger import get_qs_logger
from cloudshell.shell.core.driver_context import AutoLoadDetails, InitCommandContext, ResourceCommandContext
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.shell.core.session.cloudshell_session import CloudShellSessionContext
from cloudshell.traffic.rest_api_helpers import RestClientException, RestClientUnauthorizedException
from requests import Response

from breakingpoint_data_model import BreakingpointChassis2G, GenericTrafficGeneratorModule, GenericTrafficGeneratorPort


def valid(response: Response) -> dict:
    """Validate REST response and return the response json if valid response."""
    if response.status_code in [200, 201, 204]:
        return response.json()
    if response.status_code in [401]:
        raise RestClientUnauthorizedException("Incorrect login or password")
    raise RestClientException(f"Request failed: {response.status_code}, {response.text}")


class BreakingPointChassisDriver(ResourceDriverInterface):
    """BreakingPoint chassis shell driver."""

    def __init__(self) -> None:
        """Initialize object variables, actual initialization is performed in initialize method."""
        self.logger: logging.Logger = None
        self.resource: BreakingPointChassisDriver = None
        self.bps_session: Dict[str, str] = {}
        self.base_url = ""

    def initialize(self, context: InitCommandContext) -> None:
        """Initialize BreakingPoint chassis shell (from API)."""
        self.logger = get_qs_logger(log_group="traffic_shells", log_file_prefix=context.resource.name)
        self.logger.setLevel(logging.DEBUG)

    def cleanup(self) -> None:
        """Cleanup BreakingPoint chassis shell (from API)."""
        super().cleanup()

    def get_inventory(self, context: ResourceCommandContext) -> AutoLoadDetails:
        """Return device structure with all standard attributes."""
        self.resource = BreakingpointChassis2G.create_from_context(context)
        address = context.resource.address
        user = self.resource.user
        self.logger.debug(f"User - {user}")
        self.logger.debug(f"Encrypted password - {self.resource.password}")
        password = CloudShellSessionContext(context).get_api().DecryptPassword(self.resource.password).Value
        self.logger.debug(f"Password - {password}")

        session = requests.Session()
        self.bps_session = valid(
            session.post(f"https://{address}/api/v1/auth/session", json={"username": user, "password": password}, verify=False)
        )
        session_id = valid(session.get(self.bps_session["userAccountUrl"], verify=False))["id"]
        self.base_url = f"https://{address}/bps/api/v2/sessions/{session_id}"

        topology = valid(session.get(self._build_url("bps/topology"), verify=False))

        self.resource.model_name = topology["model"]
        self.resource.serial_number = topology["serialNumber"]
        self.resource.vendor = "Ixia"
        self.resource.version = topology.get("ixos")

        for slot in [slot for slot in topology["slot"] if slot["port"]]:
            self._load_module(slot)

        return self.resource.create_autoload_details()

    def _load_module(self, module: dict) -> None:
        """Get module resource and attributes."""
        module_id = module["id"]
        gen_module = GenericTrafficGeneratorModule(f"Module{module_id}")
        self.resource.add_sub_resource(f"M{module_id}", gen_module)
        gen_module.model_name = module["model"]
        gen_module.serial_number = module.get("serialNumber", "")
        for port in module["port"]:
            self._load_port(gen_module, port)

    @staticmethod
    def _load_port(gen_module: GenericTrafficGeneratorModule, port: dict) -> None:
        """Get port resource and attributes."""
        port_id = str(int(port["id"]) + 1)
        gen_port = GenericTrafficGeneratorPort(f"Port{port_id}")
        gen_module.add_sub_resource(f"P{port_id}", gen_port)
        gen_port.max_speed = port["speed"]

    def _build_url(self, uri: str) -> str:
        """Build full URL for the requested REST API command."""
        return f"{self.base_url}/{uri}"
