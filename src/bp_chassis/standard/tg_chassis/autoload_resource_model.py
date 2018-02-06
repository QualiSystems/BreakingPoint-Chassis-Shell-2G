#!/usr/bin/python
# -*- coding: utf-8 -*-
from bp_chassis.standard.base import AbstractResource
from bp_chassis.standard.validators import attr_length_validator

AVAILABLE_SHELL_TYPES = ["CS_Switch",
                         "CS_Router",
                         "CS_WirelessController",
                         'CS_TrafficGeneratorChassis']


class GenericResource(AbstractResource):
    RESOURCE_MODEL = "Breaking Point Chassis"
    RELATIVE_PATH_TEMPLATE = ""
    NAME_TEMPLATE = 'Chassis {}'

    def __init__(self, shell_name, name, unique_id, shell_type="CS_TrafficGeneratorChassis"):
        super(GenericResource, self).__init__(shell_name, name, unique_id)

        if shell_name:
            self.shell_name = "{}.".format(shell_name)
            if shell_type in AVAILABLE_SHELL_TYPES:
                self.shell_type = "{}.".format(shell_type)
            else:
                raise Exception(self.__class__.__name__, "Unavailable shell type {shell_type}."
                                                         "Shell type should be one of: {avail}"
                                .format(shell_type=shell_type, avail=", ".join(AVAILABLE_SHELL_TYPES)))
        else:
            self.shell_name = ""
            self.shell_type = ""

    @property
    def version(self):
        """ Return version of the Operating System """

        return self.attributes.get("{}Version".format(self.shell_type))

    @version.setter
    @attr_length_validator
    def version(self, value):
        """ Set version of the Operating System """

        self.attributes["{}Version".format(self.shell_type)] = value

    @property
    def model(self):
        """ Return the device model. This information is typically used for abstract resource filtering """

        return self.attributes.get("{}Model".format(self.shell_type))

    @model.setter
    @attr_length_validator
    def model(self, value=""):
        """ Set the device model. This information is typically used for abstract resource filtering """

        self.attributes["{}Model".format(self.shell_type)] = value

    @property
    def server_description(self):
        """ Return the device model name. This information is typically used for abstract resource filtering """

        return self.attributes.get("{}Server Description".format(self.shell_type))

    @server_description.setter
    @attr_length_validator
    def server_description(self, value=""):
        """ Set the device model name. This information is typically used for abstract resource filtering """

        self.attributes["{}Server Description".format(self.shell_type)] = value


class GenericModule(AbstractResource):
    RESOURCE_MODEL = "Generic Traffic Generator Module"
    RELATIVE_PATH_TEMPLATE = "M"
    NAME_TEMPLATE = 'Module {}'

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Model".format(self.namespace))

    @model.setter
    @attr_length_validator
    def model(self, value=""):
        """

        :type value: str
        """
        self.attributes["{}Model".format(self.namespace)] = value


class GenericPort(AbstractResource):
    RESOURCE_MODEL = "Generic Traffic Generator Port"
    RELATIVE_PATH_TEMPLATE = "P"
    NAME_TEMPLATE = 'Port {}'

    @property
    def media_type(self):
        """
        Interface media type. Possible values are Fiber and/or Copper (comma-separated)
        :rtype: str
        """
        return self.attributes.get("{}Media Type".format(self.namespace))

    @media_type.setter
    @attr_length_validator
    def media_type(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes["{}Media Type".format(self.namespace)] = value

    @property
    def supported_speed(self):
        """
        Speed supported by the interface, comma-separated.
        :rtype: float
        """
        return self.attributes.get("{}Supported Speed".format(self.namespace))

    @supported_speed.setter
    @attr_length_validator
    def supported_speed(self, value):
        """
        Speed supported by the interface, comma-separated.
        :type value: float
        """
        self.attributes["{}Supported Speed".format(self.namespace)] = value

    @property
    def logical_name(self):
        """
        :rtype: float
        """
        return self.attributes.get("{}Logical Name".format(self.namespace))

    @logical_name.setter
    @attr_length_validator
    def logical_name(self, value):
        """
        The current MTU configured on the interface.
        :type value: float
        """
        self.attributes["{}Logical Name".format(self.namespace)] = value


class GenericPowerPort(AbstractResource):
    RESOURCE_MODEL = "Generic Power Port"
    RELATIVE_PATH_TEMPLATE = "PP"
    NAME_TEMPLATE = 'Power Port {}'

    @property
    def model(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Model".format(self.namespace))

    @model.setter
    @attr_length_validator
    def model(self, value):
        """
        The device model. This information is typically used for abstract resource filtering.
        :type value: str
        """
        self.attributes["{}Model".format(self.namespace)] = value

    @property
    def serial_number(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Serial Number".format(self.namespace))

    @serial_number.setter
    @attr_length_validator
    def serial_number(self, value):
        """

        :type value: str
        """
        self.attributes["{}Serial Number".format(self.namespace)] = value

    @property
    def version(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Version".format(self.namespace))

    @version.setter
    @attr_length_validator
    def version(self, value):
        """
        The firmware version of the resource.
        :type value: str
        """
        self.attributes["{}Version".format(self.namespace)] = value

    @property
    def port_description(self):
        """
        :rtype: str
        """
        return self.attributes.get("{}Port Description".format(self.namespace))

    @port_description.setter
    @attr_length_validator
    def port_description(self, value):
        """
        The description of the port as configured in the device.
        :type value: str
        """
        self.attributes["{}Port Description".format(self.namespace)] = value