from unittest import TestCase, skip, skipUnless
from decimal import Decimal
from datetime import datetime, date
from unittest.mock import patch, MagicMock

from testing.simple_functions import sum_two_numbers, print_something, request_some_site_info, \
    request_book_site


def mock_response(*args, **kwargs):
    class MockResponse:
        def __init__(self, *args, **kwargs):
            self.status_code = 200

        def json(self):
            return {
                "today_views": 1000,
                "total_hits": 100000,
                "days_alive": 2400,
            }

        @property
        def text(self):
            return "<html><div><p>SOME P TEXT</p></div></html>"

        def raise_for_status(self):
            return True
    return MockResponse(*args, **kwargs)


class SimpleFunctionsTests(TestCase):
    _today = datetime.now().date()

    def setUp(self) -> None:
        super().setUp()

        self.some_instance_to_use_within_all_tests = "Pesho"

    def test_sum_two_numbers(self):
        # test_cases = [
        #     ((4, 5), 9),
        #     (('4', 5), 9),
        #     ((None, 5), 9),
        #     ((Decimal(5), 5.1), 10.1),
        # ]
        # for (a, b), result in test_cases:
        #     with self.subTest(result=result):
        #         self.assertEqual(sum_two_numbers(a, b), result)

        self.assertEqual(sum_two_numbers(4, 5), 9)
        self.assertIsNone(sum_two_numbers('a', 5))
        # self.assertRaises(TypeError, lambda: sum_two_numbers(None, 5))
        # self.assertRaises(TypeError, lambda: sum_two_numbers(Decimal(5), 5.1))

    @skipUnless(_today >= date(2023, 2, 25), "Not created functionality")
    def test_subtract_numbers(self):
        subtract_number(5, 6)

    @patch("testing.simple_functions.inner_func")
    def test_print_something(self, mock_inner_func):
        print_something("tra", "la", "la", self.some_instance_to_use_within_all_tests)
        mock_inner_func.assert_called()

    @patch("requests.get", side_effect=mock_response)
    def test_request_some_site_info(self, mock_get_request):
        site_response, msg = request_some_site_info("http://somesite-test.com")
        self.assertEqual(site_response.status_code, 200)
        self.assertEqual(msg, "Site has good amount of daily visits")
        mock_get_request.assert_called_with("http://somesite-test.com")

    @patch("requests.get", side_effect=mock_response)
    def test_request_book_site(self, mock_get_request):
        site_response = request_book_site()
        self.assertEqual(site_response, "<html><div><p>SOME P TEXT</p></div></html>")
        mock_get_request.assert_called()

    @patch("datetime.datetime")
    def test_datetime_now(self, mock_datetime):
        mock_datetime.now = lambda: datetime(2023, 1, 29, 10, 0, 0)
        print(mock_datetime.now())

    def test_datetime_version_cm(self):
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now = lambda: datetime(2023, 1, 29, 10, 0, 0)
            mock_datetime.today = lambda: date(2023, 1, 29)
            print(mock_datetime.now())
            print(mock_datetime.today())
            mock_datetime.now = lambda: datetime(2033, 1, 29, 10, 0, 0)
            mock_datetime.today = lambda: date(2033, 1, 29)
            print(mock_datetime.now())
            print(mock_datetime.today())
        print(datetime.now())
