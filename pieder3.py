#
# Nathan Timmerman
# Dec 2017
#

import urllib2
import htmllib
import re #regular expresions
#import traceback

class Result :
    type = 'for sale'
    def __init__ (self, id, name, price, date, url):
        self.id = id
        self.name = name
        self.name = price
        self.date = date
        self.url = url


def parser(file): # Iterate and parse html file
    count = 0
    line = file.readline()
    while line:
        result = re.search('class="result-info"', line)
        while result:
            count += 1
            
            result = False
        line = file.readline()
    print (count)



def gethtml(url, query):    
    url += query
    request = urllib2.Request(url)
    try:
        htmlfile = urllib2.urlopen(request)
    except urllib2.URLError, e:
        print('URL Error: ', e)
    except urllib2.HTTPError, e:
        print('HTTP Error: ', e)
    except Exception, e:
        print('Unknown Error: ', e)
    return htmlfile

def bingo():
    print('BINGO!!')
    return

def main():
    file = gethtml('https://austin.craigslist.org/search/sss?query=', 'motor')
    parser(file)
    

if __name__ == '__main__':
    main()
