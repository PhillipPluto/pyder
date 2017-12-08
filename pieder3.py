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
    def __init__ (self):        
        data = {}
                
def parser(file): # Iterate and parse html file
    count = 0
    line = file.readline()
    result = [] # list of Result objects 
    while line:
        if re.search('class="result-info"', line): #returns bool
            result.append(Result())
            count += 1
        if re.search('class="result-date"', line):
            m = re.match('(.*datetime=)"(.*)" (title=.*)', line) #returns list of group() matches
            result[count-1].datetime = m.group(2)
            #print(result[count-1].datetime)
        if re.search (r'<a href="https://austin.craigslist.org', line):
            
        line = file.readline()



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
