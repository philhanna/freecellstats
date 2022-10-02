from unittest import TestCase

from freecell import Statistics


class TestStatistics(TestCase):

    def setUp(self):
        statistic = "99;150;144;208;"
        wins, total, best, worst = \
            [int(x)
             for x in statistic.split(";")
             if x] # Skip the trailing semicolon
        self.stat = Statistics(wins, total, best, worst)

    def test_percent(self):
        wins = 99.0
        total = 150.0
        losses = total - wins
        expected = 100 * wins / total
        actual = Statistics.percent(wins, losses)
        self.assertEqual(expected, actual)

    def test_seconds_to_time(self):
        expected = "01:37"
        actual = Statistics.seconds_to_time(97)
        self.assertEqual(expected, actual)

    def test_wins(self):
        expected = 99
        actual = self.stat.wins
        self.assertEqual(expected, actual)

    def test_total(self):
        expected = 150
        actual = self.stat.total
        self.assertEqual(expected, actual)

    def test_best(self):
        expected = 144
        actual = self.stat.best
        self.assertEqual(expected, actual)

    def test_worst(self):
        expected = 208
        actual = self.stat.worst
        self.assertEqual(expected, actual)

    def test_losses(self):
        expected = 51
        actual = self.stat.losses
        self.assertEqual(expected, actual)

    def test_pct(self):
        wins = 99.0
        total = 150.0
        losses = total - wins
        expected = wins / total
        actual = self.stat.pct
        self.assertAlmostEqual(expected, actual)

    def test_wins_to_next_higher(self):
        wins = self.stat.wins
        total = self.stat.total
        pct = round(100.0 * (float(wins) / float(total)))
        next_higher = pct + 1
        count = 0
        while pct < next_higher:
            count += 1
            wins += 1
            total += 1
            pct = round(100.0 * (float(wins) / float(total)))
        expected = count
        actual = self.stat.wins_to_next_higher
        self.assertEqual(expected, actual)

    def test_losses_to_next_lower(self):
        wins = self.stat.wins
        losses = self.stat.losses
        total = self.stat.total
        pct = round(100.0 * (float(wins) / float(total)))
        next_lower = pct - 1
        count = 0
        while pct > next_lower:
            count += 1
            losses += 1
            total += 1
            pct = round(100.0 * (float(wins) / float(total)))
        expected = count
        actual = self.stat.losses_to_next_lower
        self.assertEqual(expected, actual)
