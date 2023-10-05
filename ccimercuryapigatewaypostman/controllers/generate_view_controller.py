# -*- coding: utf-8 -*-

"""
ccimercuryapigatewaypostman

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from ccimercuryapigatewaypostman.api_helper import APIHelper
from ccimercuryapigatewaypostman.configuration import Server
from ccimercuryapigatewaypostman.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from ccimercuryapigatewaypostman.http.http_method_enum import HttpMethodEnum


class GenerateViewController(BaseController):

    """A Controller to access Endpoints in the ccimercuryapigatewaypostman API."""
    def __init__(self, config):
        super(GenerateViewController, self).__init__(config)

    def view_generate_view(self,
                           accept):
        """Does a POST request to /view/generateView.

        TODO: type endpoint description here.

        Args:
            accept (str): TODO: type description here.

        Returns:
            object: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVER_1)
            .path('/view/generateView')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Accept')
                          .value(accept))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def view_generate_view_1(self,
                             accept):
        """Does a GET request to /view/generateView.

        TODO: type endpoint description here.

        Args:
            accept (str): TODO: type description here.

        Returns:
            object: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SERVER_1)
            .path('/view/generateView')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('Accept')
                          .value(accept))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()
