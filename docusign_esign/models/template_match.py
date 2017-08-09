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


class TemplateMatch(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, document_end_page=None, document_start_page=None, match_percentage=None):
        """
        TemplateMatch - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'document_end_page': 'str',
            'document_start_page': 'str',
            'match_percentage': 'str'
        }

        self.attribute_map = {
            'document_end_page': 'documentEndPage',
            'document_start_page': 'documentStartPage',
            'match_percentage': 'matchPercentage'
        }

        self._document_end_page = document_end_page
        self._document_start_page = document_start_page
        self._match_percentage = match_percentage

    @property
    def document_end_page(self):
        """
        Gets the document_end_page of this TemplateMatch.
        

        :return: The document_end_page of this TemplateMatch.
        :rtype: str
        """
        return self._document_end_page

    @document_end_page.setter
    def document_end_page(self, document_end_page):
        """
        Sets the document_end_page of this TemplateMatch.
        

        :param document_end_page: The document_end_page of this TemplateMatch.
        :type: str
        """

        self._document_end_page = document_end_page

    @property
    def document_start_page(self):
        """
        Gets the document_start_page of this TemplateMatch.
        

        :return: The document_start_page of this TemplateMatch.
        :rtype: str
        """
        return self._document_start_page

    @document_start_page.setter
    def document_start_page(self, document_start_page):
        """
        Sets the document_start_page of this TemplateMatch.
        

        :param document_start_page: The document_start_page of this TemplateMatch.
        :type: str
        """

        self._document_start_page = document_start_page

    @property
    def match_percentage(self):
        """
        Gets the match_percentage of this TemplateMatch.
        

        :return: The match_percentage of this TemplateMatch.
        :rtype: str
        """
        return self._match_percentage

    @match_percentage.setter
    def match_percentage(self, match_percentage):
        """
        Sets the match_percentage of this TemplateMatch.
        

        :param match_percentage: The match_percentage of this TemplateMatch.
        :type: str
        """

        self._match_percentage = match_percentage

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
