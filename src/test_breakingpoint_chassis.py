"""
Tests for BreakingPointChassisDriver.
"""
# pylint: disable=redefined-outer-name
from typing import Iterable

import pytest
from _pytest.fixtures import SubRequest
from cloudshell.api.cloudshell_api import AttributeNameValue, CloudShellAPISession, ResourceInfo
from cloudshell.shell.core.driver_context import AutoLoadCommandContext
from cloudshell.traffic.tg import BREAKINGPOINT_CHASSIS_MODEL, TGN_CHASSIS_FAMILY
from shellfoundry_traffic.test_helpers import TestHelpers, create_session_from_config, print_inventory

from breakingpoint_driver import BreakingPointChassisDriver


@pytest.fixture(params=[("192.168.26.72", "admin", "DxTbqlSgAVPmrDLlHvJrsA==")])
def dut(request: SubRequest) -> list:
    """Yield BreakingPoint device under test parameters."""
    return request.param


@pytest.fixture(scope="session")
def session() -> CloudShellAPISession:
    """Yield session."""
    return create_session_from_config()


@pytest.fixture(scope="session")
def test_helpers(session: CloudShellAPISession) -> TestHelpers:
    """Yield initialized TestHelpers object."""
    return TestHelpers(session)


@pytest.fixture()
def driver(test_helpers: TestHelpers, dut: list) -> Iterable[BreakingPointChassisDriver]:
    """Yield initialized BreakingPointChassisDriver."""
    address, user, password = dut
    attributes = {
        f"{BREAKINGPOINT_CHASSIS_MODEL}.User": user,
        f"{BREAKINGPOINT_CHASSIS_MODEL}.Password": password,
    }
    init_context = test_helpers.resource_init_command_context(
        TGN_CHASSIS_FAMILY, BREAKINGPOINT_CHASSIS_MODEL, address, attributes
    )
    driver = BreakingPointChassisDriver()
    driver.initialize(init_context)
    yield driver
    driver.cleanup()


@pytest.fixture()
def autoload_context(test_helpers: TestHelpers, dut: list) -> AutoLoadCommandContext:
    """Yield BreakingPoint chassis resource for shell autoload testing."""
    address, user, password = dut
    attributes = {
        f"{BREAKINGPOINT_CHASSIS_MODEL}.User": user,
        f"{BREAKINGPOINT_CHASSIS_MODEL}.Password": password,
    }
    return test_helpers.autoload_command_context(TGN_CHASSIS_FAMILY, BREAKINGPOINT_CHASSIS_MODEL, address, attributes)


@pytest.fixture()
def autoload_resource(session: CloudShellAPISession, test_helpers: TestHelpers, dut: list) -> Iterable[ResourceInfo]:
    """Yield BreakingPoint resource for shell autoload testing."""
    address, user, password = dut
    attributes = [
        AttributeNameValue(f"{BREAKINGPOINT_CHASSIS_MODEL}.User", user),
        AttributeNameValue(f"{BREAKINGPOINT_CHASSIS_MODEL}.Password", password),
    ]
    resource = test_helpers.create_autoload_resource(
        BREAKINGPOINT_CHASSIS_MODEL, "tests/test-BreakingPoint", address, attributes
    )
    yield resource
    session.DeleteResource(resource.Name)


def test_autoload(driver: BreakingPointChassisDriver, autoload_context: AutoLoadCommandContext) -> None:
    """Test direct (driver) autoload command."""
    inventory = driver.get_inventory(autoload_context)
    print_inventory(inventory)


def test_autoload_session(session: CloudShellAPISession, autoload_resource: ResourceInfo, dut: list) -> None:
    """Test indirect (shell) autoload command."""
    session.AutoLoad(autoload_resource.Name)
    resource_details = session.GetResourceDetails(autoload_resource.Name)
    assert len(resource_details.ChildResources) == 2
    assert resource_details.ChildResources[0].FullAddress == f"{dut[0]}/M1"
