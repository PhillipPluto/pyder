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
    try:
        file = urllib2.urlopen(url)
        try:
            data = file.read()
            file.close()
            try:
                root=ET.fromstring(data)        
                for state in root.findall('State'):
                    #as far as I know from above example there should only be one <State></State>
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
            except:
                print ('someting went wrong')
                raise
        except:
            print ('file or data error')
            raise
#I do not know what the error is so 
    
    except urllib2.HTTPError, err:#URLIB2.URLOPEN
        if err.code == 404:
            print ("Page not found!")
        elif err.code == 403:
            print ("Access denied!")
        else:
            print ("Something happened! Error code", err.code)
    except urllib2.URLError, err:#URLIB2.URLOPEN
        pass
        print (err.reason)
    except:
        print ('the unexpected happened')
        raise#I do not know what the error is so 

if __name__ == '__main__':
    main()
