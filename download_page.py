import urllib2
from collections import Counter
import string
f=open("D://cha.txt",'w')

request=urllib2.Request('http://www.pythonchallenge.com/pc/def/ocr.html')
response=urllib2.urlopen(request)
page=response.read()
f.write(page)

cnt=Counter()

with open("D://cha.txt") as f:
    for eachline in f.readlines():
        for char in eachline:
            cnt[char]+=1
print cnt
f=open("D://cha1.txt")
content=f.read()
f.close()
reps={'@':'', '&':'',')':'','(':'',']':'','#':'','_':'','[':'','}':'','%':'','!':'','+':'','$':'','{':'','*':'','^':'','\n':'','-':''}
for i,j in reps.items():
    content=content.replace(i,j)
print content

            
            
    
