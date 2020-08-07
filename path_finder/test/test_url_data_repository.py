from django.test import TestCase

from path_finder.models.url_data import UrlData
from path_finder.repositories.url_data import UrlDataRepository


class UrlDataRepositoryTestCase(TestCase):
    def setUp(self):
        UrlData.objects.create(
            id="1",
            url="test.com"
        )

    def test_update_url(self):
        UrlDataRepository.update_url("facebook.com")
        self.assertEqual(UrlDataRepository.get_or_create_url_data().url, "facebook.com")
