# -*- coding: utf-8 -*-

"""
ccimercuryapigatewaypostman

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from ccimercuryapigatewaypostman.api_helper import APIHelper
from ccimercuryapigatewaypostman.models.mrd_editfunction_group_request import MrdEditfunctionGroupRequest


class EditfunctionGroupControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(EditfunctionGroupControllerTests, cls).setUpClass()
        cls.controller = cls.client.editfunction_group
        cls.response_catcher = cls.controller.http_call_back

    # Todo: Add description for test test_mrd_editfunction_group
    def test_mrd_editfunction_group(self):
        # Parameters for the API call
        accept = 'application/json'
        body = APIHelper.json_deserialize('{"fgId":"1401503","fgName":"Develop","lastModifiedBy":"c36701"}', MrdEditfunctionGroupRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.mrd_editfunction_group(accept, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = None
        expected_headers['access-control-allow-origin'] = None

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Todo: Add description for test test_mrd_editfunction_group_1
    def test_mrd_editfunction_group_1(self):
        # Parameters for the API call
        accept = 'application/json'

        # Perform the API call through the SDK function
        result = self.controller.mrd_editfunction_group_1(accept)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = None
        expected_headers['access-control-allow-origin'] = None
        expected_headers['access-control-allow-methods'] = None
        expected_headers['access-control-allow-headers'] = None

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

