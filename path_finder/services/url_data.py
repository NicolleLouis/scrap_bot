import requests
from path_finder.repositories.url_data import UrlDataRepository


class UrlDataService:
    @staticmethod
    def save_html_content_from_url():
        url_data = UrlDataRepository.get_or_create_url_data()
        response = requests.get(url_data.url)
        UrlDataRepository.update_html_content(response.text)
