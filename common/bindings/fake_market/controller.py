import requests


class FakeStoreController:
    """Класс для хранения адреса и ресурсов Api магазина"""

    root = 'https://fakestoreapi.com'

    products_path = root+'/products'
    #   todo: добавить остальные пути

    @staticmethod
    def create_new_product(
            data=None) -> requests.Response:

        response = requests.post(
            url=FakeStoreController.products_path,
            json=data,
            verify=False
        )
        return response


    # TODO: составить запросы для GET/ PUT/ DELETE
