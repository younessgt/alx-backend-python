#!/usr/bin/env python3
"""A github org client
"""
import unittest
from unittest import mock
from unittest.mock import PropertyMock, patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class to test GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    def test_org(self, org_name, test_payload):
        """Test org method of GithubOrgClient class."""

        with mock.patch('client.get_json') as mock_get:
            mock_get.return_value = test_payload
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client.org, test_payload)

    def test_public_repos_url(self):
        """Test public_repos_url method of GithubOrgClient class."""
        org_name = "google"
        test_payload = {"repos_url": "http://google.com"}
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=test_payload)):
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client._public_repos_url,
                             "http://google.com")

    @patch('client.get_json')
    def test_public_repos(self, json_mock):
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
    def test_has_license(self, repo, licence, exp_value):
        """Test has_license method of GithubOrgClient class."""
        obj = GithubOrgClient("google")
        self.assertEqual(obj.has_license(repo, licence), exp_value)
