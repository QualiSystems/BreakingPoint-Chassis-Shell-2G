from bp_chassis.runners.bp_autoload_runner import BPAutoloadRunner
from bp_chassis.standard.tg_chassis.resource_configuration import ResourceConfiguration
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.tg.breaking_point.helpers.context_utils import get_logger_with_thread_id, get_api


class BreakingPointChassisDriver(ResourceDriverInterface):
    SUPPORTED_OS = 'Breaking Point'
    SHELL_NAME = 'BreakingPoint Chassis Shell 2G'

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

        resource_config = ResourceConfiguration.from_context(self.SHELL_NAME, self.SUPPORTED_OS, context)

        logger = get_logger_with_thread_id(context)
        api = get_api(context)
        autoload_runner = BPAutoloadRunner(resource_config, logger, api, self.SUPPORTED_OS)
        return autoload_runner.discover()
