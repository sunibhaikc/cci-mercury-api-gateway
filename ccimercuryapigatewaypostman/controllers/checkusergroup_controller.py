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


class CheckusergroupController(BaseController):

    """A Controller to access Endpoints in the ccimercuryapigatewaypostman API."""
    def __init__(self, config):
        super(CheckusergroupController, self).__init__(config)

    def user_checkusergroup(self,
                            accept,
                            body):
        """Does a POST request to /user/checkusergroup.

        TODO: type endpoint description here.

        Args:
            accept (str): TODO: type description here.
            body (UserCheckusergrouprequest): TODO: type description here.

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
            .path('/user/checkusergroup')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Accept')
                          .value(accept))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def user_checkusergroup_1(self,
                              accept):
        """Does a GET request to /user/checkusergroup.

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
            .path('/user/checkusergroup')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('Accept')
                          .value(accept))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()
