import pytest

from freecell import Statistics


@pytest.fixture
def stat():
    statistic = "99;150;144;208;"
    wins, total, best, worst = \
        [int(x)
         for x in statistic.split(";")
         if x]  # Skip the trailing semicolon
    stat = Statistics(wins, total, best, worst)
    return stat


def test_percent(stat):
    wins = 99.0
    total = 150.0
    losses = total - wins
    expected = 100 * wins / total
    actual = Statistics.percent(wins, losses)
    assert actual == expected


def test_seconds_to_time(stat):
    expected = "01:37"
    actual = Statistics.seconds_to_time(97)
    assert actual == expected


def test_wins(stat):
    expected = 99
    actual = stat.wins
    assert actual == expected


def test_total(stat):
    expected = 150
    actual = stat.total
    assert actual == expected


def test_best(stat):
    expected = 144
    actual = stat.best
    assert actual == expected


def test_worst(stat):
    expected = 208
    actual = stat.worst
    assert actual == expected


def test_losses(stat):
    expected = 51
    actual = stat.losses
    assert actual == expected


def test_pct(stat):
    wins = 99.0
    total = 150.0
    losses = total - wins
    expected = wins / total
    actual = stat.pct
    assert actual == expected


def test_wins_to_next_higher(stat):
    wins = stat.wins
    total = stat.total
    pct = round(100.0 * (float(wins) / float(total)))
    next_higher = pct + 1
    count = 0
    while pct < next_higher:
        count += 1
        wins += 1
        total += 1
        pct = round(100.0 * (float(wins) / float(total)))
    expected = count
    actual = stat.wins_to_next_higher
    assert actual == expected


def test_losses_to_next_lower(stat):
    wins = stat.wins
    losses = stat.losses
    total = stat.total
    pct = round(100.0 * (float(wins) / float(total)))
    next_lower = pct - 1
    count = 0
    while pct > next_lower:
        count += 1
        losses += 1
        total += 1
        pct = round(100.0 * (float(wins) / float(total)))
    expected = count
    actual = stat.losses_to_next_lower
    assert actual == expected
