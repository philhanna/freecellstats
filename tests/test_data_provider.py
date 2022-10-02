import os.path
import re

from unittest import TestCase
from unittest.mock import patch

from freecell import DataProvider
from tests import testdata


def get_string():
    infile = os.path.join(testdata, "aisleriot.ini")
    with open(infile) as fpin:
        for line in fpin:
            line = line.strip()
            m = re.match(r'Statistic=([\d;]+)', line)
            if m:
                return m.group(1)
    raise RuntimeError(f"'Statistic=' line not found in {infile}")


class TestDataProvider(TestCase):

    @patch.object(DataProvider, 'get_statistic_string', return_value=get_string())
    def setUp(self, mocked_method):
        self.data_provider = DataProvider()

    def tearDown(self) -> None:
        del self.data_provider

    def test_stats(self):
        self.assertIsNotNone(self.data_provider)
