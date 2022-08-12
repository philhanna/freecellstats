import os
import sys
import configparser
from freecell.statistics import Statistics

INPUT_FILE = os.path.expanduser("~/.config/gnome-games/aisleriot")


class FileReader:
    """ Reads raw data from the configuration file that contains the history """

    def __init__(self, input_file=INPUT_FILE):
        if not os.path.exists(input_file):
            errmsg = f"{input_file} configuration file"
            raise ValueError(errmsg)

        # Read the .ini file
        config = configparser.ConfigParser()
        config.read(input_file)
        section = config["freecell.scm"]
        if not section:
            errmsg = f"configuration does not contain a freecell section"
            raise ValueError(errmsg)
        statistic = config["freecell.scm"]["Statistic"]
        tokens = statistic.split(";")
        wins = int(tokens[0])
        total = int(tokens[1])
        best = int(tokens[2])
        worst = int(tokens[3])

        #   Create the statistics object

        self.stats = Statistics(wins, total, best, worst)

    def __str__(self):
        return str(self.stats)
