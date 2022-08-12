import os
import sys
import xml.dom.minidom
from freecell.statistics import Statistics

INPUT_FILE = os.path.expanduser("~/.config/gnome-games/aisleriot")

class FileReader:
    '''
    Reads raw data from the XML file that contains the history
    '''


    @staticmethod
    def getChildText(node):
        '''
        Returns the concatenated text of all child nodes
        '''
        sb = ''
        for child in node.childNodes:
            sb = sb + child.nodeValue
        return sb

    def __init__(self):
        '''
        Constructor
        '''
        inputFile = INPUT_FILE
        if not os.path.exists(inputFile):
            print('{0} input file does not exist'.format(inputFile))
            sys.exit()

        dom = xml.dom.minidom.parse(inputFile)
        elemGconf = dom.documentElement
        elemEntry = None
        nodelist = elemGconf.getElementsByTagName('entry')
        for node in nodelist:
            if node.getAttribute('name') == 'statistics':
                elemEntry = node
        if not elemEntry:
            print('No statistics found')
            sys.exit()

        #   Get the wins, total, best time, and worst time

        nodes = elemEntry.getElementsByTagName('stringvalue')

        wins    = int(FileReader.getChildText(nodes[1]))
        total   = int(FileReader.getChildText(nodes[2]))
        best    = int(FileReader.getChildText(nodes[3]))
        worst   = int(FileReader.getChildText(nodes[4]))

        #   Create the statistics object

        self.stats = Statistics(wins, total, best, worst)

    def __str__(self):
        return str(self.stats)

