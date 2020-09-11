import requests

from bs4 import BeautifulSoup

from path_finder.repositories.url_data import UrlDataRepository
from path_finder.repositories.link import LinkRepository


class LinkService:
    @staticmethod
    def is_link_recursive(link_url):
        url_data = UrlDataRepository.get_or_create_url_data()
        next_page = "{}{}".format(url_data.url, link_url)
        response = requests.get(next_page)
        soup = BeautifulSoup(response.text, 'html.parser')
        if len(soup.find_all("a", {"href": link_url})) == 0:
            LinkRepository.add_non_recursive_occurrence(link_url)
            return False
        LinkRepository.add_recursive_occurrence(link_url)
        return True
