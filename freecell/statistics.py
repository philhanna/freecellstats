class Statistics:
    '''
    Calculates the wins, losses, and percentages
    '''

    @staticmethod
    def percent(wins, losses):
        '''
        Finds the integer value of the winning percentage
        '''
        return round(100 * wins / (wins + losses))

    @staticmethod
    def secondsToTime(seconds):
        '''
        Converts a number of seconds into a mm:ss string
        '''
        minutes = seconds // 60
        seconds = seconds - (60 * minutes)
        return '{0:02d}:{1:02d}'.format(minutes, seconds)

    def __init__(self, wins=0, total=0, best=0, worst=0):
        '''
        Constructor
        '''
        self.wins   = wins      # Number of wins
        self.total  = total     # Total games
        self.best   = best      # Best time (seconds)
        self.worst  = worst     # Worst time (seconds)
        self.losses = total - wins  # Number of losses
        self.pct    = wins / total if total else 0

    def __repr__(self):
        return "Statistics(wins={},total={},best={},worst={})".format(
            self.wins,
            self.total,
            self.best,
            self.worst)

    def __str__(self):
        lines = (
        ('Total games          = {0}'.format(self.total)),
        ('Wins                 = {0}'.format(self.wins)),
        ('Losses               = {0}'.format(self.losses)),
        ('Percentage           = {0:.0f}%'.format(self.pct * 100)),
        ('Best time            = {0}'.format(Statistics.secondsToTime(self.best))),
        ('Worst time           = {0}'.format(Statistics.secondsToTime(self.worst))),
        ('Wins to {0:<13s}= {1}'.format(
                        str(Statistics.percent(self.wins, self.losses) + 1) + '%',
                        self.winsToNextHigher())),
        ('Losses to {0:<11s}= {1}'.format(
                        str(Statistics.percent(self.wins, self.losses) - 1) + '%',
                        self.lossesToNextLower())),
        )
        return '\n'.join(lines)

    def winsToNextHigher(self):
        if self.losses == 0:
            return None
        wins = self.wins
        losses = self.losses
        current = Statistics.percent(wins, losses)
        nextPct = current + 1
        moves = 0
        while current < nextPct:
            moves += 1
            wins += 1
            current = Statistics.percent(wins, losses)
        return moves

    def lossesToNextLower(self):
        if self.wins == 0:
            return None
        wins = self.wins
        losses = self.losses
        current = Statistics.percent(wins, losses)
        nextPct = current - 1
        moves = 0
        while current > nextPct:
            moves += 1
            losses += 1
            current = Statistics.percent(wins, losses)
        return moves