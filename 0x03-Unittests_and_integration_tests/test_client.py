#!/usr/bin/env python3
"""A github org client
"""
import unittest
from typing import Dict
from unittest import mock
from unittest.mock import PropertyMock, patch, Mock, MagicMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
from requests import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    def test_org(self, org_name: str, test_payload: Dict) -> None:
        """Test org method of GithubOrgClient class."""

        with mock.patch('client.get_json') as mock_get:
            mock_get.return_value = test_payload
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client.org, test_payload)

    def test_public_repos_url(self) -> None:
        """Test public_repos_url method of GithubOrgClient class."""
        org_name = "google"
        test_payload = {"repos_url": "http://google.com"}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=test_payload)):
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client._public_repos_url,
                             "http://google.com")

    @patch('client.get_json')
    def test_public_repos(self, json_mock: MagicMock) -> None:
        """Test public_repos method of GithubOrgClient class."""
        names = [{"name": "name1", "license": {"key": "license1"}},
                 {"name": "name2", "license": {"key": "license2"}},
                 {"name": "name3"}]
        json_mock.return_value = names
        with mock.patch('client.GithubOrgClient._public_repos_url',
                        PropertyMock(return_value="www.test.com")):
            github_org_client = GithubOrgClient("google")
            self.assertEqual(github_org_client.public_repos(),
                             ["name1", "name2", "name3"])
            self.assertEqual(github_org_client.public_repos("license1"),
                             ["name1"])
            self.assertEqual(github_org_client.public_repos("license2"),
                             ["name2"])
            self.assertEqual(github_org_client.public_repos("license3"),
                             [])
        json_mock.assert_called_once_with("www.test.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict,
                         licence: str, exp_value: bool) -> None:
        """Test has_license method of GithubOrgClient class."""
        obj = GithubOrgClient("google")
        self.assertEqual(obj.has_license(repo, licence), exp_value)


@parameterized_class(
    [
        {
            'org_payload': TEST_PAYLOAD[0][0],
            'repos_payload': TEST_PAYLOAD[0][1],
            'expected_repos': TEST_PAYLOAD[0][2],
            'apache2_repos': TEST_PAYLOAD[0][3],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient class to test GithubOrgClient class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class."""
        dict_org_repo = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_dict_payload(url):
            """Get payload method """
            if url in dict_org_repo:
                x = Mock()
                x.json.return_value = dict_org_repo[url]
                return x
            return HTTPError()
        cls.get_patcher = patch('requests.get', side_effect=get_dict_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Test public_repos method of GithubOrgClient class."""
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos_with_license method of GithubOrgClient class."""
        github_org_client = GithubOrgClient("google")
        self.assertEqual(github_org_client.public_repos(licence="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class."""
        cls.get_patcher.stop()
