import json

import allure

from common.bindings.fake_market.controller import FakeStoreController
import pprint


class TestCrudFakeStore:

    def test_create_new_product(self, data_test_create_product):

        test_product = data_test_create_product['test_data']
        allure.attach(json.dumps(data_test_create_product, indent=4, default=str, ensure_ascii=False),
                      f"built_test_data.txt", allure.attachment_type.TEXT)

        response = FakeStoreController.create_new_product(
            data=test_product
        )
        response_json = response.json()

        assert 200 == response.status_code

        for key, value in test_product.items():
            if key == 'id':
                continue
            assert test_product[key] == response_json[key]

        pprint.pp(response.json())


    # TODO: написать тесты на запросы GET/ PUT/ DELETE

