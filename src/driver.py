from cloudshell.devices.driver_helper import get_logger_with_thread_id, get_api
from cloudshell.devices.standards.traffic.chassis.configuration_attributes_structure import \
    GenericTrafficChassisResource
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.tg.breaking_point.runners.bp_autoload_runner import BPAutoloadRunner


class BreakingPointChassisDriver(ResourceDriverInterface):
    SUPPORTED_OS = ['Breaking Point']
    SHELL_NAME = 'BreakingPoint Chassis 2G'

    def __init__(self):
        pass

    def initialize(self, context):
        """
        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """
        pass

    def cleanup(self):
        pass

    def get_inventory(self, context):
        """ Return device structure with all standard attributes
        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        :rtype: cloudshell.shell.core.driver_context.AutoLoadDetails
        """

        resource_config = GenericTrafficChassisResource.from_context(self.SHELL_NAME, self.SUPPORTED_OS, context)

        logger = get_logger_with_thread_id(context)
        api = get_api(context)
        autoload_runner = BPAutoloadRunner(resource_config, self.SHELL_NAME, api, logger)
        return autoload_runner.discover()
