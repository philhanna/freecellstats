class Statistics:
    """ Calculates the wins, losses, and percentages """

    @staticmethod
    def percent(wins, losses):
        """ Finds the integer value of the winning percentage """
        return round(100 * wins / (wins + losses))

    @staticmethod
    def seconds_to_time(seconds):
        """ Converts a number of seconds into a mm:ss string """
        minutes = seconds // 60
        seconds = seconds - (60 * minutes)
        return f"{minutes:02d}:{seconds:02d}"

    def __init__(self, wins=0, total=0, best=0, worst=0):
        """ Constructor """
        self.wins = wins  # Number of wins
        self.total = total  # Total games
        self.best = best  # Best time (seconds)
        self.worst = worst  # Worst time (seconds)
        self.losses = total - wins  # Number of losses
        self.pct = wins / total if total else 0

    def __repr__(self):
        return "Statistics(wins={},total={},best={},worst={})".format(
            self.wins,
            self.total,
            self.best,
            self.worst)

    def __str__(self):
        pct_wins = str(Statistics.percent(self.wins, self.losses) + 1) + "%"
        pct_losses = str(Statistics.percent(self.wins, self.losses) - 1) + "%"
        str_pct_wins = f"{pct_wins:<13}"
        str_pct_losses = f"{pct_losses:<11}"
        lines = (
            f"Total games          = {self.total}",
            f"Wins                 = {self.wins}",
            f"Losses               = {self.losses}",
            f"Percentage           = {self.pct * 100:.0f}%",
            f"Best time            = {Statistics.seconds_to_time(self.best)}",
            f"Worst time           = {Statistics.seconds_to_time(self.worst)}",
            f"Wins to {str_pct_wins}= {self.wins_to_next_higher()}",
            f"Losses to {str_pct_losses}= {self.losses_to_next_lower()}"
        )
        return "\n".join(lines)

    def wins_to_next_higher(self):
        if not self.losses:
            return None
        wins = self.wins
        losses = self.losses
        current = Statistics.percent(wins, losses)
        next_pct = current + 1
        moves = 0
        while current < next_pct:
            moves += 1
            wins += 1
            current = Statistics.percent(wins, losses)
        return moves

    def losses_to_next_lower(self):
        if not self.losses:
            return None
        wins = self.wins
        losses = self.losses
        current = Statistics.percent(wins, losses)
        next_pct = current - 1
        moves = 0
        while current > next_pct:
            moves += 1
            losses += 1
            current = Statistics.percent(wins, losses)
        return moves
