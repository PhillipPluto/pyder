#
# Nathan Timmerman
# Nov 2017
#

#from __future__ import print_function
import urllib2
import xml.etree.ElementTree as ET

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
    tree = ET.parse(file)
    root = tree.getgroot()
    print ( tree)
#    for item in root.findall('result-info'):
 #       print ('found match')
  #      bingo()#function to do something
#       print (item + '\n\n')

if __name__ == '__main__':
    main()
