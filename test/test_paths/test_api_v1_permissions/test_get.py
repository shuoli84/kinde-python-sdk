# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import kinde_sdk
from kinde_sdk.paths.api_v1_permissions import get  # noqa: E501
from kinde_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1Permissions(ApiTestMixin, unittest.TestCase):
    """
    ApiV1Permissions unit test stubs
        List Permissions  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
