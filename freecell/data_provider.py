import configparser
import os.path

from freecell import Statistics, INPUT_FILE


class DataProvider:
    """Reads raw data from the configuration file that contains the history"""

    def __init__(self):
        """Creates a new DataProvider"""
        statistic: str = DataProvider.get_statistic_string()
        wins, total, best, worst = [int(x)
                                    for x in statistic.split(";")
                                    if x]
        self._statistics = Statistics(wins, total, best, worst)

    @property
    def statistics(self) -> Statistics:
        """Returns the Statistics object"""
        return self._statistics

    @staticmethod
    def get_statistic_string() -> str:
        """Loads the configuration from the default input file.
        This method can be replaced by a mock object in unit tests"""

        # Read the freecell configuration
        input_file = INPUT_FILE
        if not os.path.exists(input_file):
            errmsg = f"'{input_file}' configuration file not found"
            raise RuntimeError(errmsg)

        # Load a configuration parser object from it
        config = configparser.ConfigParser()
        config.read(input_file)

        # Read the statistics string from the freecell.scm section
        section = config["freecell.scm"]
        if not section:
            errmsg = f"configuration does not contain a freecell section"
            raise RuntimeError(errmsg)

        stat_string = config["freecell.scm"]["Statistic"]
        if not stat_string:
            errmsg = f"Section 'freecell.scm' does not contain 'Statistic'"
            raise RuntimeError(errmsg)

        return stat_string
