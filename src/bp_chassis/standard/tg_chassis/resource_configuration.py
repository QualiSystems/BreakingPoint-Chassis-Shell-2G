class ResourceConfiguration(object):

    def __init__(self, attributes, shell_name=None, name=None, supported_os=None):
        """

        :param attributes:
        :param shell_name:
        :param name:
        :param supported_os:
        """
        self._attributes = attributes
        self.shell_name = shell_name
        self.name = name
        self.supported_os = supported_os

        self.fullname = None
        self.address = None  # The IP address of the resource
        self.family = None  # The resource family

        if shell_name:
            self.namespace_prefix = "{}.".format(self.shell_name)
        else:
            self.namespace_prefix = ""

    @property
    def username(self):
        """
        :rtype: str
        """
        return self._attributes.get("{}User".format(self.namespace_prefix), None)

    @property
    def password(self):
        """
        :rtype: string
        """
        return self._attributes.get("{}Password".format(self.namespace_prefix), None)

    @classmethod
    def from_context(cls, shell_name, supported_os, context):
        """
        Creates an instance of Networking Resource by given context
        :param shell_name: Shell Name
        :type shell_name: str
        :param supported_os: list of supported OS
        :type supported_os: list
        :param context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :return:
        :rtype GenericNetworkingResource
        """

        result = cls(dict(context.resource.attributes), shell_name=shell_name, name=context.resource.name,
                     supported_os=supported_os)
        result.address = context.resource.address
        result.family = context.resource.family
        result.fullname = context.resource.fullname
        return result
