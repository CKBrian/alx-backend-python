#!/usr/bin/env python3
'''Defines a module that tests client.GithubOrgClient class'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self) -> None:
        '''Test that GithubOrgClient.test_public_repos_url
           returns the correct value based on mocked payload'''
        # specifing new_callable for functions with @property
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as MockOrg:
            # Mock return value
            repos_url = 'https://api.github.com/orgs/google/repos'
            url_dict = {'repos_url': repos_url}
            MockOrg.return_value = url_dict
            # Get function output
            org = 'google'
            client = GithubOrgClient(org)
            res = client._public_repos_url
            # Assertions
            self.assertEqual(res, repos_url)
            MockOrg.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, MockGet: MagicMock) -> None:
        '''Test that GithubOrgClient.public_repos returns the list of repos
           as expected from the chosen payload.'''
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as MockRepoUrl:
            # Mock return value
            repos_url = 'https://api.github.com/orgs/google/repos'
            MockRepoUrl.return_value = repos_url
            payload = [
                {
                    'id': 1936771,
                    'name': 'truth',
                    'description': 'Fluent assertions for Java and Android',
                    'language': 'Java',
                    'stargazers_count': 2700,
                    "html_url": "https://github.com/google/truth",
                    "description": "Fluent assertions for Java and Android",
                    "fork": False,
                    "url": "https://api.github.com/repos/google/truth"
                },
            ]
            MockGet.return_value = payload

            # Mock returned output
            public_repos = [
                    "truth",
                ]
            # public_repos = ["truth"]

            # Get function output
            org = 'google'
            client = GithubOrgClient(org)
            res = client.public_repos()

            # Assertions
            self.assertEqual(res, public_repos)
            MockRepoUrl.assert_called_once()
            MockGet.assert_called_once_with(repos_url)


if __name__ == "__main__":
    unittest.main()
