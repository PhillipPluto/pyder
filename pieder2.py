#
# Nathan Timmerman
# Nov 2017
#

from __future__ import print_function
import urllib2
import xml.etree.ElementTree as ET
#import shlex, subprocess


#import sys#added so program can run in either python2 or python3
#import base64#added so program can run in either python2 or python3


#from itertools import tee, islice, chain, izip

def bingo():
    # Things to do when a match has been found
    print ('BINGO!!')
    return

def main():
    query = 'motor'
    url = 'https://austin.craigslist.org/search/sss?query=' + query
    file = urllib2.urlopen(url)
    data = file.read()
    file.close()
    tree = ET.parse(data)
    root = tree.getgroot()
    for item in root.findall('result-info'):#as far as I know from above example there should only be one <State></State>
        print ('found match')
        bingo()#function to do something
#        print (item + '\n\n')

if __name__ == '__main__':
    main()
