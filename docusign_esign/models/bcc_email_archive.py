# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BccEmailArchive(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_id': 'str',
        'bcc_email_archive_id': 'str',
        'created': 'str',
        'created_by': 'UserInfo',
        'email': 'str',
        'email_notification_id': 'str',
        'modified': 'str',
        'modified_by': 'UserInfo',
        'status': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bcc_email_archive_id': 'bccEmailArchiveId',
        'created': 'created',
        'created_by': 'createdBy',
        'email': 'email',
        'email_notification_id': 'emailNotificationId',
        'modified': 'modified',
        'modified_by': 'modifiedBy',
        'status': 'status',
        'uri': 'uri'
    }

    def __init__(self, account_id=None, bcc_email_archive_id=None, created=None, created_by=None, email=None, email_notification_id=None, modified=None, modified_by=None, status=None, uri=None):  # noqa: E501
        """BccEmailArchive - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._bcc_email_archive_id = None
        self._created = None
        self._created_by = None
        self._email = None
        self._email_notification_id = None
        self._modified = None
        self._modified_by = None
        self._status = None
        self._uri = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bcc_email_archive_id is not None:
            self.bcc_email_archive_id = bcc_email_archive_id
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if email is not None:
            self.email = email
        if email_notification_id is not None:
            self.email_notification_id = email_notification_id
        if modified is not None:
            self.modified = modified
        if modified_by is not None:
            self.modified_by = modified_by
        if status is not None:
            self.status = status
        if uri is not None:
            self.uri = uri

    @property
    def account_id(self):
        """Gets the account_id of this BccEmailArchive.  # noqa: E501

        The account ID associated with the envelope.  # noqa: E501

        :return: The account_id of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BccEmailArchive.

        The account ID associated with the envelope.  # noqa: E501

        :param account_id: The account_id of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bcc_email_archive_id(self):
        """Gets the bcc_email_archive_id of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The bcc_email_archive_id of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._bcc_email_archive_id

    @bcc_email_archive_id.setter
    def bcc_email_archive_id(self, bcc_email_archive_id):
        """Sets the bcc_email_archive_id of this BccEmailArchive.

          # noqa: E501

        :param bcc_email_archive_id: The bcc_email_archive_id of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._bcc_email_archive_id = bcc_email_archive_id

    @property
    def created(self):
        """Gets the created of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The created of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BccEmailArchive.

          # noqa: E501

        :param created: The created of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this BccEmailArchive.  # noqa: E501


        :return: The created_by of this BccEmailArchive.  # noqa: E501
        :rtype: UserInfo
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BccEmailArchive.


        :param created_by: The created_by of this BccEmailArchive.  # noqa: E501
        :type: UserInfo
        """

        self._created_by = created_by

    @property
    def email(self):
        """Gets the email of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The email of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BccEmailArchive.

          # noqa: E501

        :param email: The email of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def email_notification_id(self):
        """Gets the email_notification_id of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The email_notification_id of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._email_notification_id

    @email_notification_id.setter
    def email_notification_id(self, email_notification_id):
        """Sets the email_notification_id of this BccEmailArchive.

          # noqa: E501

        :param email_notification_id: The email_notification_id of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._email_notification_id = email_notification_id

    @property
    def modified(self):
        """Gets the modified of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The modified of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this BccEmailArchive.

          # noqa: E501

        :param modified: The modified of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def modified_by(self):
        """Gets the modified_by of this BccEmailArchive.  # noqa: E501


        :return: The modified_by of this BccEmailArchive.  # noqa: E501
        :rtype: UserInfo
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this BccEmailArchive.


        :param modified_by: The modified_by of this BccEmailArchive.  # noqa: E501
        :type: UserInfo
        """

        self._modified_by = modified_by

    @property
    def status(self):
        """Gets the status of this BccEmailArchive.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BccEmailArchive.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uri(self):
        """Gets the uri of this BccEmailArchive.  # noqa: E501

          # noqa: E501

        :return: The uri of this BccEmailArchive.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this BccEmailArchive.

          # noqa: E501

        :param uri: The uri of this BccEmailArchive.  # noqa: E501
        :type: str
        """

        self._uri = uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(BccEmailArchive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BccEmailArchive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
