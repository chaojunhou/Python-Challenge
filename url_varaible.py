#coding=utf-8
import urllib2
import re

def challenge(s,number):
    page=number
    for x in range(10000):
        request=urllib2.Request(s+page)
        response=urllib2.urlopen(request)
        pagex=response.read()
        try:
            page=''.join(re.findall('[0-9]',pagex))
            print page
        except :
            print pagex
        print 'the count is:'+ str(x+1)
            
challenge('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=','96205')

