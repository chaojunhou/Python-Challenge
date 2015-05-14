import urllib2
from collections import Counter
import string
import re

f=open("D://python_challenge3.txt",'w')

request=urllib2.Request('http://www.pythonchallenge.com/pc/def/equality.html')
response=urllib2.urlopen(request)
page=response.read()
f.write(page)
f.close()
f=open("D://py3.txt",'r')
contents=f.readlines()
words=''
lister=re.findall(r"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]",str(contents))
for word in lister:
    print 'word:'+word
    words+=word[4]
    print 'words:'+words

print words
    
            
    
