from path_finder.models.link import Link


class LinkRepository:
    @staticmethod
    def get_or_create_link(url):
        link, _created = Link.objects.get_or_create(
            url=url
        )
        return link

    @staticmethod
    def add_recursive_occurrence(url):
        link = LinkRepository.get_or_create_link(url)
        link.recursive_occurrence += 1
        link.save()

    @staticmethod
    def add_non_recursive_occurrence(url):
        link = LinkRepository.get_or_create_link(url)
        link.non_recursive_occurrence += 1
        link.save()
