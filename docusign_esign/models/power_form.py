# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PowerForm(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created_date_time=None, email_body=None, email_subject=None, envelopes=None, error_details=None, instructions=None, is_active=None, last_used=None, limit_use_interval=None, limit_use_interval_enabled=None, limit_use_interval_units=None, max_use_enabled=None, name=None, power_form_id=None, power_form_url=None, recipients=None, sender_name=None, sender_user_id=None, signing_mode=None, template_id=None, template_name=None, times_used=None, uri=None, uses_remaining=None):
        """
        PowerForm - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created_date_time': 'str',
            'email_body': 'str',
            'email_subject': 'str',
            'envelopes': 'list[Envelope]',
            'error_details': 'ErrorDetails',
            'instructions': 'str',
            'is_active': 'str',
            'last_used': 'str',
            'limit_use_interval': 'str',
            'limit_use_interval_enabled': 'str',
            'limit_use_interval_units': 'str',
            'max_use_enabled': 'str',
            'name': 'str',
            'power_form_id': 'str',
            'power_form_url': 'str',
            'recipients': 'list[PowerFormRecipient]',
            'sender_name': 'str',
            'sender_user_id': 'str',
            'signing_mode': 'str',
            'template_id': 'str',
            'template_name': 'str',
            'times_used': 'str',
            'uri': 'str',
            'uses_remaining': 'str'
        }

        self.attribute_map = {
            'created_date_time': 'createdDateTime',
            'email_body': 'emailBody',
            'email_subject': 'emailSubject',
            'envelopes': 'envelopes',
            'error_details': 'errorDetails',
            'instructions': 'instructions',
            'is_active': 'isActive',
            'last_used': 'lastUsed',
            'limit_use_interval': 'limitUseInterval',
            'limit_use_interval_enabled': 'limitUseIntervalEnabled',
            'limit_use_interval_units': 'limitUseIntervalUnits',
            'max_use_enabled': 'maxUseEnabled',
            'name': 'name',
            'power_form_id': 'powerFormId',
            'power_form_url': 'powerFormUrl',
            'recipients': 'recipients',
            'sender_name': 'senderName',
            'sender_user_id': 'senderUserId',
            'signing_mode': 'signingMode',
            'template_id': 'templateId',
            'template_name': 'templateName',
            'times_used': 'timesUsed',
            'uri': 'uri',
            'uses_remaining': 'usesRemaining'
        }

        self._created_date_time = created_date_time
        self._email_body = email_body
        self._email_subject = email_subject
        self._envelopes = envelopes
        self._error_details = error_details
        self._instructions = instructions
        self._is_active = is_active
        self._last_used = last_used
        self._limit_use_interval = limit_use_interval
        self._limit_use_interval_enabled = limit_use_interval_enabled
        self._limit_use_interval_units = limit_use_interval_units
        self._max_use_enabled = max_use_enabled
        self._name = name
        self._power_form_id = power_form_id
        self._power_form_url = power_form_url
        self._recipients = recipients
        self._sender_name = sender_name
        self._sender_user_id = sender_user_id
        self._signing_mode = signing_mode
        self._template_id = template_id
        self._template_name = template_name
        self._times_used = times_used
        self._uri = uri
        self._uses_remaining = uses_remaining

    @property
    def created_date_time(self):
        """
        Gets the created_date_time of this PowerForm.
        Indicates the date and time the item was created.

        :return: The created_date_time of this PowerForm.
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """
        Sets the created_date_time of this PowerForm.
        Indicates the date and time the item was created.

        :param created_date_time: The created_date_time of this PowerForm.
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def email_body(self):
        """
        Gets the email_body of this PowerForm.
        Specifies the email body of the message sent to the recipient.   Maximum length: 10000 characters. 

        :return: The email_body of this PowerForm.
        :rtype: str
        """
        return self._email_body

    @email_body.setter
    def email_body(self, email_body):
        """
        Sets the email_body of this PowerForm.
        Specifies the email body of the message sent to the recipient.   Maximum length: 10000 characters. 

        :param email_body: The email_body of this PowerForm.
        :type: str
        """

        self._email_body = email_body

    @property
    def email_subject(self):
        """
        Gets the email_subject of this PowerForm.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :return: The email_subject of this PowerForm.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """
        Sets the email_subject of this PowerForm.
        Specifies the subject of the email that is sent to all recipients.  See [ML:Template Email Subject Merge Fields] for information about adding merge field information to the email subject.

        :param email_subject: The email_subject of this PowerForm.
        :type: str
        """

        self._email_subject = email_subject

    @property
    def envelopes(self):
        """
        Gets the envelopes of this PowerForm.
        

        :return: The envelopes of this PowerForm.
        :rtype: list[Envelope]
        """
        return self._envelopes

    @envelopes.setter
    def envelopes(self, envelopes):
        """
        Sets the envelopes of this PowerForm.
        

        :param envelopes: The envelopes of this PowerForm.
        :type: list[Envelope]
        """

        self._envelopes = envelopes

    @property
    def error_details(self):
        """
        Gets the error_details of this PowerForm.

        :return: The error_details of this PowerForm.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this PowerForm.

        :param error_details: The error_details of this PowerForm.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def instructions(self):
        """
        Gets the instructions of this PowerForm.
        

        :return: The instructions of this PowerForm.
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """
        Sets the instructions of this PowerForm.
        

        :param instructions: The instructions of this PowerForm.
        :type: str
        """

        self._instructions = instructions

    @property
    def is_active(self):
        """
        Gets the is_active of this PowerForm.
        

        :return: The is_active of this PowerForm.
        :rtype: str
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this PowerForm.
        

        :param is_active: The is_active of this PowerForm.
        :type: str
        """

        self._is_active = is_active

    @property
    def last_used(self):
        """
        Gets the last_used of this PowerForm.
        

        :return: The last_used of this PowerForm.
        :rtype: str
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """
        Sets the last_used of this PowerForm.
        

        :param last_used: The last_used of this PowerForm.
        :type: str
        """

        self._last_used = last_used

    @property
    def limit_use_interval(self):
        """
        Gets the limit_use_interval of this PowerForm.
        

        :return: The limit_use_interval of this PowerForm.
        :rtype: str
        """
        return self._limit_use_interval

    @limit_use_interval.setter
    def limit_use_interval(self, limit_use_interval):
        """
        Sets the limit_use_interval of this PowerForm.
        

        :param limit_use_interval: The limit_use_interval of this PowerForm.
        :type: str
        """

        self._limit_use_interval = limit_use_interval

    @property
    def limit_use_interval_enabled(self):
        """
        Gets the limit_use_interval_enabled of this PowerForm.
        

        :return: The limit_use_interval_enabled of this PowerForm.
        :rtype: str
        """
        return self._limit_use_interval_enabled

    @limit_use_interval_enabled.setter
    def limit_use_interval_enabled(self, limit_use_interval_enabled):
        """
        Sets the limit_use_interval_enabled of this PowerForm.
        

        :param limit_use_interval_enabled: The limit_use_interval_enabled of this PowerForm.
        :type: str
        """

        self._limit_use_interval_enabled = limit_use_interval_enabled

    @property
    def limit_use_interval_units(self):
        """
        Gets the limit_use_interval_units of this PowerForm.
        

        :return: The limit_use_interval_units of this PowerForm.
        :rtype: str
        """
        return self._limit_use_interval_units

    @limit_use_interval_units.setter
    def limit_use_interval_units(self, limit_use_interval_units):
        """
        Sets the limit_use_interval_units of this PowerForm.
        

        :param limit_use_interval_units: The limit_use_interval_units of this PowerForm.
        :type: str
        """

        self._limit_use_interval_units = limit_use_interval_units

    @property
    def max_use_enabled(self):
        """
        Gets the max_use_enabled of this PowerForm.
        

        :return: The max_use_enabled of this PowerForm.
        :rtype: str
        """
        return self._max_use_enabled

    @max_use_enabled.setter
    def max_use_enabled(self, max_use_enabled):
        """
        Sets the max_use_enabled of this PowerForm.
        

        :param max_use_enabled: The max_use_enabled of this PowerForm.
        :type: str
        """

        self._max_use_enabled = max_use_enabled

    @property
    def name(self):
        """
        Gets the name of this PowerForm.
        

        :return: The name of this PowerForm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PowerForm.
        

        :param name: The name of this PowerForm.
        :type: str
        """

        self._name = name

    @property
    def power_form_id(self):
        """
        Gets the power_form_id of this PowerForm.
        

        :return: The power_form_id of this PowerForm.
        :rtype: str
        """
        return self._power_form_id

    @power_form_id.setter
    def power_form_id(self, power_form_id):
        """
        Sets the power_form_id of this PowerForm.
        

        :param power_form_id: The power_form_id of this PowerForm.
        :type: str
        """

        self._power_form_id = power_form_id

    @property
    def power_form_url(self):
        """
        Gets the power_form_url of this PowerForm.
        

        :return: The power_form_url of this PowerForm.
        :rtype: str
        """
        return self._power_form_url

    @power_form_url.setter
    def power_form_url(self, power_form_url):
        """
        Sets the power_form_url of this PowerForm.
        

        :param power_form_url: The power_form_url of this PowerForm.
        :type: str
        """

        self._power_form_url = power_form_url

    @property
    def recipients(self):
        """
        Gets the recipients of this PowerForm.
        An array of powerform recipients.

        :return: The recipients of this PowerForm.
        :rtype: list[PowerFormRecipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this PowerForm.
        An array of powerform recipients.

        :param recipients: The recipients of this PowerForm.
        :type: list[PowerFormRecipient]
        """

        self._recipients = recipients

    @property
    def sender_name(self):
        """
        Gets the sender_name of this PowerForm.
        

        :return: The sender_name of this PowerForm.
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """
        Sets the sender_name of this PowerForm.
        

        :param sender_name: The sender_name of this PowerForm.
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_user_id(self):
        """
        Gets the sender_user_id of this PowerForm.
        

        :return: The sender_user_id of this PowerForm.
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """
        Sets the sender_user_id of this PowerForm.
        

        :param sender_user_id: The sender_user_id of this PowerForm.
        :type: str
        """

        self._sender_user_id = sender_user_id

    @property
    def signing_mode(self):
        """
        Gets the signing_mode of this PowerForm.
        

        :return: The signing_mode of this PowerForm.
        :rtype: str
        """
        return self._signing_mode

    @signing_mode.setter
    def signing_mode(self, signing_mode):
        """
        Sets the signing_mode of this PowerForm.
        

        :param signing_mode: The signing_mode of this PowerForm.
        :type: str
        """

        self._signing_mode = signing_mode

    @property
    def template_id(self):
        """
        Gets the template_id of this PowerForm.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :return: The template_id of this PowerForm.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this PowerForm.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :param template_id: The template_id of this PowerForm.
        :type: str
        """

        self._template_id = template_id

    @property
    def template_name(self):
        """
        Gets the template_name of this PowerForm.
        

        :return: The template_name of this PowerForm.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """
        Sets the template_name of this PowerForm.
        

        :param template_name: The template_name of this PowerForm.
        :type: str
        """

        self._template_name = template_name

    @property
    def times_used(self):
        """
        Gets the times_used of this PowerForm.
        

        :return: The times_used of this PowerForm.
        :rtype: str
        """
        return self._times_used

    @times_used.setter
    def times_used(self, times_used):
        """
        Sets the times_used of this PowerForm.
        

        :param times_used: The times_used of this PowerForm.
        :type: str
        """

        self._times_used = times_used

    @property
    def uri(self):
        """
        Gets the uri of this PowerForm.
        

        :return: The uri of this PowerForm.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this PowerForm.
        

        :param uri: The uri of this PowerForm.
        :type: str
        """

        self._uri = uri

    @property
    def uses_remaining(self):
        """
        Gets the uses_remaining of this PowerForm.
        

        :return: The uses_remaining of this PowerForm.
        :rtype: str
        """
        return self._uses_remaining

    @uses_remaining.setter
    def uses_remaining(self, uses_remaining):
        """
        Sets the uses_remaining of this PowerForm.
        

        :param uses_remaining: The uses_remaining of this PowerForm.
        :type: str
        """

        self._uses_remaining = uses_remaining

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
