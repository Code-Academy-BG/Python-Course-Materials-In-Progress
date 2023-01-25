from unittest import TestCase

from functions_decorators_generators.tiny_kwargs_example import get_request_json_data


class TinyKwargsExampleTests(TestCase):
    def test_get_request_json_data(self):
        self.assertDictEqual(
            get_request_json_data(11),
            {
                "deliverydate": '11',
                "minutes": 86400,
            },
        )
        self.assertDictEqual(
            get_request_json_data("2023-01-10", 11),
            {
                "deliverydate": "2023-01-10",
                "receipt_ids": [{"receiptId": "11"}],
                "minutes": 86400,
            },
        )
        self.assertDictEqual(
            get_request_json_data("2023-01-10", 8391028312983, 11),
            {
                "deliverydate": "2023-01-10",
                "receipt_ids": [{"receiptId": "8391028312983"}],
                "minutes": 11,
            },
        )
