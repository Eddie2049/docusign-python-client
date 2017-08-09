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


class BccEmailAddress(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bcc_email_address_id=None, email=None):
        """
        BccEmailAddress - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bcc_email_address_id': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'bcc_email_address_id': 'bccEmailAddressId',
            'email': 'email'
        }

        self._bcc_email_address_id = bcc_email_address_id
        self._email = email

    @property
    def bcc_email_address_id(self):
        """
        Gets the bcc_email_address_id of this BccEmailAddress.
        Only users with canManageAccount setting can use this option. An array of up to 5 email addresses the envelope is sent to as a BCC email.    Example: If your account has BCC for Email Archive set up for the email address 'archive@mycompany.com' and you send an envelope using the BCC Email Override to send a BCC email to 'salesarchive@mycompany.com', then a copy of the envelope is only sent to the 'salesarchive@mycompany.com' email address.

        :return: The bcc_email_address_id of this BccEmailAddress.
        :rtype: str
        """
        return self._bcc_email_address_id

    @bcc_email_address_id.setter
    def bcc_email_address_id(self, bcc_email_address_id):
        """
        Sets the bcc_email_address_id of this BccEmailAddress.
        Only users with canManageAccount setting can use this option. An array of up to 5 email addresses the envelope is sent to as a BCC email.    Example: If your account has BCC for Email Archive set up for the email address 'archive@mycompany.com' and you send an envelope using the BCC Email Override to send a BCC email to 'salesarchive@mycompany.com', then a copy of the envelope is only sent to the 'salesarchive@mycompany.com' email address.

        :param bcc_email_address_id: The bcc_email_address_id of this BccEmailAddress.
        :type: str
        """

        self._bcc_email_address_id = bcc_email_address_id

    @property
    def email(self):
        """
        Gets the email of this BccEmailAddress.
        Specifies the BCC email address. DocuSign verifies that the email format is correct, but does not verify that the email is active.Using this overrides the BCC for Email Archive information setting for this envelope.  Maximum of length: 100 characters. 

        :return: The email of this BccEmailAddress.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this BccEmailAddress.
        Specifies the BCC email address. DocuSign verifies that the email format is correct, but does not verify that the email is active.Using this overrides the BCC for Email Archive information setting for this envelope.  Maximum of length: 100 characters. 

        :param email: The email of this BccEmailAddress.
        :type: str
        """

        self._email = email

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
