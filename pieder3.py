#
# Nathan Timmerman
# Dec 2017
#

import urllib2
import htmllib

def parser(file):
    #break html into a sorted tree 
    return

def gethtml(url, query):    
    url += query
    htmlfile = urllib2.urlopen(url)
    return htmlfile

def bingo():
    print('BINGO!!')
    return

def main():
    file = gethtml('https://austin.craigslist.org/search/sss?query=', 'motor')
    

if __name__ == '__main__':
    main()
