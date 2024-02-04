#!/usr/bin/env python3
"""A github org client
"""
import unittest
from unittest import mock
from unittest.mock import PropertyMock
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

    def test_public_repos(self):
        """Test public_repos_url method of GithubOrgClient class."""
        org_name = "google"
        test_payload = {"repos_url": "http://google.com"}
        with mock.patch('client.GithubOrgClient.org',
                        PropertyMock(return_value=test_payload)):
            github_org_client = GithubOrgClient(org_name)
            self.assertEqual(github_org_client._public_repos_url,
                             "http://google.com")
