class Statistics:
    """ Calculates the wins, losses, and percentages """

    @staticmethod
    def percent(wins, losses):
        """ Finds the value of the winning percentage """
        return round((100.0 * wins) / float(wins + losses), 2)

    @staticmethod
    def seconds_to_time(seconds):
        """ Converts a number of seconds into a mm:ss string """
        minutes = seconds // 60
        seconds = seconds - (60 * minutes)
        return f"{minutes:02d}:{seconds:02d}"

    def __init__(self, wins=0, total=0, best=0, worst=0):
        """ Constructor """
        self._wins = wins  # Number of wins
        self._total = total  # Total games
        self._best = best  # Best time (seconds)
        self._worst = worst  # Worst time (seconds)
        self._losses = total - wins  # Number of losses
        self._pct = wins / total if total else 0

    @property
    def wins(self):
        return self._wins

    @property
    def total(self):
        return self._total

    @property
    def best(self):
        return self._best

    @property
    def worst(self):
        return self._worst

    @property
    def losses(self):
        return self._losses

    @property
    def pct(self):
        return self._pct

    @property
    def wins_to_next_higher(self) -> int | None:
        """Returns the number of wins needed to raise
        the winning percentage one point"""
        if not self.losses:
            return None
        wins = self.wins
        losses = self.losses
        current = round(Statistics.percent(wins, losses))
        next_pct = current + 1
        moves = 0
        while current < next_pct:
            moves += 1
            wins += 1
            current = round(Statistics.percent(wins, losses))
        return moves

    @property
    def losses_to_next_lower(self) -> int | None:
        """Returns the number of losses needed to raise
        the winning percentage one point"""
        if not self.losses:
            return None
        wins = self.wins
        losses = self.losses
        current = round(Statistics.percent(wins, losses))
        next_pct = current - 1
        moves = 0
        while current > next_pct:
            moves += 1
            losses += 1
            current = round(Statistics.percent(wins, losses))
        return moves

    def __repr__(self) -> str:
        """Returns a constructor representative of this object"""
        return (
            f"Statistics(wins={self.wins}"
            f",total={self.total}"
            f",best={self.best}"
            f",worst={self.worst}"
            ")"
        )

    def __str__(self) -> str:
        """Returns this object as a string"""
        current_pct = Statistics.percent(self.wins, self.losses)
        data = {
            "Total games": self.total,
            "Wins": self.wins,
            "Losses": self.losses,
            "Percentage": f"{self.pct * 100:.0f}%",
            "Best time": Statistics.seconds_to_time(self.best),
            "Worst time": Statistics.seconds_to_time(self.worst),
            f"Wins to {current_pct + 1}%": self.wins_to_next_higher,
            f"Losses to {current_pct - 1}%": self.losses_to_next_lower,
        }
        maxlen = max([len(x) for x in data])
        lines = [f"{k:<{maxlen}} = {v}" for k, v in data.items()]
        result = "\n".join(lines)
        return result
