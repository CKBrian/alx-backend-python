#!/usr/bin/env python3
'''Defines a module that tests client.GithubOrgClient class'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from client import (
    GithubOrgClient,
    get_json,
)
from typing import (
    Dict,
)

ORG_URL = "https://api.github.com/orgs/{org}"


class TestGithubOrgClient(unittest.TestCase):
    '''Implements methods with client.GithubOrgClient class testcases'''

    @parameterized.expand([
        ('google', {
            'login': 'google',
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }),
        ('abc', {
            'message': 'Not Found',
            'documentation_url': (
                'https://docs.github.com/rest/orgs/orgs#get-an-organization'
            )
        }),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, data: Dict, MockGet: MagicMock) -> None:
        '''Test that GithubOrgClient.org returns the correct value.'''
        # Mock return value
        MockGet.return_value = data
        # Get function output
        client = GithubOrgClient(org)
        res = client.org
        # Assertions
        self.assertEqual(res, data)
        MockGet.assert_called_once_with(ORG_URL.format(org=org))


if __name__ == "__main__":
    unittest.main()
