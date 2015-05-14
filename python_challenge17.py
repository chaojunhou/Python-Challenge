import urllib2
import cookielib
import re
import xmlrpclib
import urllib
import bz2

handler=urllib2.HTTPBasicAuthHandler()
handler.add_password('inflate','www.pythonchallenge.com','huge','file')
cookies=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),handler)
urllib2.install_opener(opener)
number='12345'
infos=[]
count=1
pattern=re.compile(r"(.*?)and the next busynothing is (\d*)")
while True:
    if count>400:
            break
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s'%number
    html=opener.open(urllib2.Request(url)).read() 
    m=re.search('\d\d+',html)#match the at least two numbers
    for cookie in cookies:
        infos.append(cookie.value)
    count+=1
    if m:
        number=str(m.group())
        print number
        if number=='12345':
            break
    else:
        break
print ''.join(infos)
message=urllib.unquote_plus(''.join(infos))
print bz2.BZ2Decompressor().decompress(message)
server=xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone("Leopold")
request=urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
request.add_header('Cookie','info=the flowers are on their way')
response=opener.open(request)
print response.read()

