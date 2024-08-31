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
    Mock,
    MagicMock
)
from parameterized import parameterized  # type: ignore
from parameterized import parameterized_class  # type: ignore
from typing import (
    Dict,
)
from fixtures import TEST_PAYLOAD as TP


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
        mock_get_json.return_value = '{} organization'.format(org)
        cls = GithubOrgClient(org)
        self.assertEqual(cls.org, '{} organization'.format(org))

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
            _url = 'http://org_github_url'
            _pru.return_value = _url
            cls = GithubOrgClient('test_organization')
            output = [org['name'] for org in response_json]

            self.assertEqual(cls.public_repos(), output)
            _pru.assert_called_once_with()
            mock_get_json.assert_called_once_with(_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """Tests that GithubOrgClient.has_license works correctly"""
        output = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(output, expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TP[0][0], TP[0][1], TP[0][2], TP[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Tests the integration of the GithubOrgClient and the fixtures"""
    @classmethod
    def setUpClass(cls):
        """Sets up an environment before running the unit tests"""
        cls.get_patcher = patch('utils.requests.get')
        cls.mock_get = cls.get_patcher.start()

        def mock_side_effect(url):
            """Mocks json, based on the passed url"""
            reply_mock = MagicMock()
            if url == "https://api.github.com/repos/google/episodes.dart":
                reply_mock.json.return_value = cls.repos_payload[0]
            elif url == "https://api.github.com/repos/google/cpp-netlib":
                reply_mock.json.return_value = cls.repos_payload[1]
            elif url == "https://api.github.com/repos/google/dagger":
                reply_mock.json.return_value = cls.repos_payload[2]
            elif url == "https://api.github.com/repos/google/"\
                        "ios-webkit-debug-proxy":
                reply_mock.json.return_value = cls.repos_payload[3]
            elif url == "https://api.github.com/repos/google/google.github.io":
                reply_mock.json.return_value = cls.repos_payload[4]
            elif url == "https://api.github.com/repos/google/kratu":
                reply_mock.json.return_value = cls.repos_payload[5]
            elif url == "https://api.github.com/repos/google/"\
                        "build-debian-cloud":
                reply_mock.json.return_value = cls.repos_payload[6]
            elif url == "https://api.github.com/repos/google/traceur-compiler":
                reply_mock.json.return_value = cls.repos_payload[7]
            elif url == "https://api.github.com/repos/google/firmata.py":
                reply_mock.json.return_value = cls.repos_payload[8]
            elif url == "https://api.github.com/orgs/google":
                reply_mock.json.return_value = cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                reply_mock.json.return_value = cls.repos_payload
            return reply_mock

        cls.mock_get.side_effect = mock_side_effect

    @classmethod
    def tearDownClass(cls):
        """Cleans up used resources after running all the unit tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests that GithubOrgClient.public_repos works correctly"""
        test_cls = GithubOrgClient('google')
        test_no_license = test_cls.public_repos()
        test_license = test_cls.public_repos("apache-2.0")
        self.assertEqual(test_no_license, self.expected_repos)
        self.assertEqual(test_license, self.apache2_repos)
