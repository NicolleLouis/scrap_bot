from django.test import TestCase

from path_finder.models.url_data import UrlData
from path_finder.repositories.url_data import UrlDataRepository


class UrlDataRepositoryTestCase(TestCase):
    def setUp(self):
        UrlData.objects.create(
            id="1",
            url="test.com",
            html_content="test_html"
        )

    def test_update_url(self):
        UrlDataRepository.update_url("facebook.com")
        self.assertEqual(
            UrlDataRepository.get_or_create_url_data().url,
            "facebook.com"
        )

    def test_update_html_content(self):
        UrlDataRepository.update_html_content("new_content.html")
        self.assertEqual(
            UrlDataRepository.get_or_create_url_data().html_content,
            "new_content.html"
        )

    def test_update_url_reset_html_content(self):
        UrlDataRepository.update_url("facebook.com")
        self.assertEqual(
            UrlDataRepository.get_or_create_url_data().html_content,
            ""
        )
