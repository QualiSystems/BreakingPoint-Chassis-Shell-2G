from bp_chassis.flows.bp_autoload_flow import BPAutoloadFlow

from cloudshell.tg.breaking_point.rest_api.rest_session_credentials import RestSessionCredentials
from cloudshell.tg.breaking_point.runners.bp_runner import BPRunner


class BPAutoloadRunner(BPRunner):
    def __init__(self, resource_config, logger, api, supported_os):
        """
        :param resource_config:
        :type resource_config: bp_chassis.standard.tg_chassis.resource_configuration.ResourceConfiguration
        :param logger:
        :param api:
        :param supported_os:
        """
        self.resource_config = resource_config
        self.api = api
        self._supported_os = supported_os
        super(BPAutoloadRunner, self).__init__(self._session_credentials(), logger)

    def _session_credentials(self):
        return RestSessionCredentials(self.resource_config.address,
                                      self.resource_config.username,
                                      self.api.DecryptPassword(self.resource_config.password).Value)

    @property
    def _autoload_flow(self):
        return BPAutoloadFlow(self._session_context_manager, self.logger)

    def discover(self):
        return self._autoload_flow.autoload_details(self.resource_config.shell_name)
