# -*- coding: utf-8 -*-

"""
    onfonmediasmsgateway

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from onfonmediasmsgateway.api_helper import APIHelper
from onfonmediasmsgateway.configuration import Configuration
from onfonmediasmsgateway.controllers.base_controller import BaseController
from onfonmediasmsgateway.http.auth.custom_query_auth import CustomQueryAuth

class AccountController(BaseController):

    """A Controller to access Endpoints in the onfonmediasmsgateway API."""


    def get_credit_balance(self):
        """Does a GET request to /Balance.

        Get Credit Balance

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Balance'
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