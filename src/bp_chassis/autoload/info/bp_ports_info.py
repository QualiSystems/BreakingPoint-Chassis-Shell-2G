import re

from bp_chassis.standard.tg_chassis.autoload import GenericResource, GenericModule, GenericPort


class BPPortsInfo(object):
    PORT_PREFIX = 'PORT'
    MOD_PREFIX = 'MOD'

    def __init__(self, autoload_actions, logger):
        """
        :param autoload_actions:
        :type autoload_actions: AutoloadActions
        :param logger:
        :return:
        """
        self.autoload_actions = autoload_actions
        self._logger = logger

    def collect(self, shell_name):
        root_resource = GenericResource(shell_name, GenericResource.NAME_TEMPLATE.format('1'), 'CHASS0')
        modules = {}

        self._logger.debug('Collecting ports info')
        ports_info = self.autoload_actions.get_ports_info()
        data = re.findall(r'\[slot=(\d+),port=(\d+)\]', ports_info)
        for mod_id, port_id in data:
            mod_unique_id = self.MOD_PREFIX + str(mod_id)
            port_unique_id = mod_unique_id + self.PORT_PREFIX + str(port_id)
            if mod_unique_id not in modules:
                module = GenericModule(shell_name, GenericModule.NAME_TEMPLATE.format(mod_id),
                                       mod_unique_id)
                modules[mod_unique_id] = module
                root_resource.add_sub_resource(mod_id, module)
            else:
                module = modules[mod_unique_id]
            port = GenericPort(shell_name, GenericPort.NAME_TEMPLATE.format(port_id),
                               port_unique_id)
            module.add_sub_resource(port_id, port)

        return root_resource
