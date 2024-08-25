#!/usr/bin/env python3
"""This modules houses the definition of a class that tests the
GithubOrgClient class, defined in the client.py module"""
import unittest
from client import (
    GithubOrgClient,
    get_json
)
from unittest.mock import (
    patch,
    PropertyMock,
    Mock
)
from parameterized import parameterized  # type: ignore
from typing import (
    Dict,
    Any
)


class TestGithubOrgClient(unittest.TestCase):
    """This class defines various integration tests for the GithubOrgClient
    class with other components from other module(s)"""

    @parameterized.expand([
        ('google', ),
        ('abc', ),
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json: Mock):
        """Tests that GithubOrgClient.org returns the correct value"""
        cls = GithubOrgClient(org)
        cls.org()
        prmtr = cls.ORG_URL.format(org=org)
        mock_get_json.called_with_once(prmtr)

    def test_public_repos_url(self):
        """Tests that GithubOrgCLient._public_repos_url works correctly"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            org = 'google'
            cls = GithubOrgClient(org)
            expected = cls.ORG_URL.format(org=org)
            mock_org.return_value = {'repos_url': expected}
            self.assertEqual(cls._public_repos_url, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock):
        """Tests that GithubOrgClient.public_repos work correctly"""
        response_json = [{'name': 'Org1'}, {'name': 'Org2'}]
        mock_get_json.return_value = response_json
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as _pru:
            _url = 'org public url'
            _pru.return_value = _url
            cls = GithubOrgClient('test_organization')
            response = cls.public_repos()
            output = [org['name'] for org in response_json]

            self.assertEqual(response, output)
            _pru.called_once_with()
            mock_get_json.called_once_with(_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """Teststh that GithubOrgClient.has_license works correctly"""
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected)
