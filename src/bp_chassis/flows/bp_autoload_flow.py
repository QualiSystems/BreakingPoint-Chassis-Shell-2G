from bp_chassis.actions.autoload_actions import AutoloadActions
from bp_chassis.autoload.info.bp_ports_info import BPPortsInfo
from bp_chassis.standard.autoload_builder import AutoloadDetailsBuilder
from cloudshell.tg.breaking_point.flows.bp_flow import BPFlow


class BPAutoloadFlow(BPFlow):
    def autoload_details(self, shell_name):
        elements = {}
        with self._session_context_manager as session:
            autoload_actions = AutoloadActions(session, self._logger)
            ports_info = BPPortsInfo(autoload_actions, self._logger)
            autoload_builder = AutoloadDetailsBuilder(ports_info.collect(shell_name))
            # self._connect_elements(elements)
            # details = self._build_autoload_details(elements)
            return autoload_builder.autoload_details()
