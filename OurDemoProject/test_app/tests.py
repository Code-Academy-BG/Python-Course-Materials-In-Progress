from datetime import datetime
from unittest.mock import patch, MagicMock

import pytz
from django.test import TestCase
from django.utils import timezone

mock_timezone_now = patch(
    "django.utils.timezone.now",
    MagicMock(return_value=datetime(2023, 1, 29, 10, 0, 0, tzinfo=pytz.UTC)),
)


class SimpleTests(TestCase):
    @mock_timezone_now
    def test_timezone_now_mocked(self):
        print(timezone.now())

    def test_timezone_now(self):
        print(timezone.now())
