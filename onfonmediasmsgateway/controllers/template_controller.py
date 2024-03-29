# -*- coding: utf-8 -*-

"""
    onfonmediasmsgateway

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from onfonmediasmsgateway.api_helper import APIHelper
from onfonmediasmsgateway.configuration import Configuration
from onfonmediasmsgateway.controllers.base_controller import BaseController
from onfonmediasmsgateway.http.auth.custom_query_auth import CustomQueryAuth

class TemplateController(BaseController):

    """A Controller to access Endpoints in the onfonmediasmsgateway API."""


    def get_template_list(self):
        """Does a GET request to /Template.

        Get Template List

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Template'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'AccessKey': Configuration.access_key
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def create_new_template(self,
                            message_template,
                            template_name):
        """Does a POST request to /Template.

        Create New Template

        Args:
            message_template (string): Template text.
            template_name (string): Name of template

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Template'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'AccessKey': Configuration.access_key
        }

        # Prepare form parameters
        _form_parameters = {
            'MessageTemplate': message_template,
            'TemplateName': template_name
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def update_template(self,
                        message_template,
                        template_name,
                        id):
        """Does a PUT request to /Template.

        Update Template

        Args:
            message_template (string): Template text.
            template_name (string): Name of template
            id (int): id of template

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Template'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'AccessKey': Configuration.access_key
        }

        # Prepare form parameters
        _form_parameters = {
            'MessageTemplate': message_template,
            'TemplateName': template_name,
            'id': id
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def delete_template(self,
                        id):
        """Does a DELETE request to /Template.

        Delete Template

        Args:
            id (int): id of template

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Template'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'AccessKey': Configuration.access_key
        }

        # Prepare form parameters
        _form_parameters = {
            'id': id
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers, parameters=_form_parameters)
        CustomQueryAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
