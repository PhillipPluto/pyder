#
# Nathan Timmerman
# Nov 2017
#

from __future__ import print_function
import urllib2
import xml.etree.ElementTree as ET
import shlex, subprocess


import sys#added so program can run in either python2 or python3
import base64#added so program can run in either python2 or python3


from itertools import tee, islice, chain, izip

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
    root=ET.fromstring(data)
    for state in root.findall('State'):#as far as I know from above example there should only be one <State></State>
        print ('state=',state)
        for string in state.findall('String'):
            # from above example there are multiple <String></String> so state.findall('String') is required
            key=string.find('Key').text
            value=string.find('Value').text
            print ('key=',key)
            print ('value=',value)
            if (key== 'state'):
                if (value=='idle'):
                    print ('found match')
                    bingo()#function to do something


if __name__ == '__main__':
    main()
