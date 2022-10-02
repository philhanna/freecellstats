#! /usr/bin/python3

from freecell import DataProvider


def get_version():
    import subprocess, re
    version = None
    cp = subprocess.run(['pip', 'show', 'freecellstats'], capture_output=True, text=True)
    if cp.returncode == 0:
        output = cp.stdout
        for token in output.split('\n'):
            m = re.match(r'^Version: (.*)', token)
            if m:
                version = m.group(1)
                break
    return version


def main():
    fr = DataProvider()
    print(str(fr.statistics))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description=
        """Calculates and displays statistics from the freecell history for this user""")
    parser.add_argument('-v', '--version', action="version",
                        version=f"version={get_version()}",
                        help='displays version number and exit')
    args = parser.parse_args()
    main()
