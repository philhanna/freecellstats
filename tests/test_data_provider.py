import re

from freecell import DataProvider
from tests import testdata


def get_string():
    infile = testdata.joinpath("aisleriot.ini")
    with open(infile) as fpin:
        for line in fpin:
            line = line.strip()
            m = re.match(r'Statistic=([\d;]+)', line)
            if m:
                return m.group(1)
    raise RuntimeError(f"'Statistic=' line not found in {infile}")


def test_stats(monkeypatch):
    monkeypatch.setattr(DataProvider, "get_statistic_string", get_string)
    data_provider = DataProvider()
    assert data_provider is not None
