from path_finder.models.url_data import UrlData


class UrlDataRepository:
    @staticmethod
    def update_url(url_value):
        url_data = UrlDataRepository.get_or_create_url_data()
        url_data.url = url_value
        url_data.save()

    @staticmethod
    def get_or_create_url_data():
        url_data, _created = UrlData.objects.get_or_create(
            id=1
        )
        return url_data
