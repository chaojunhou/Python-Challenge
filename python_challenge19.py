import urllib
import re
import base64
import urllib2
import cookielib
import wave

def get_challenge(s):
    return urllib.urlopen(s).read()
text=get_challenge('http://www.pythonchallenge.com/pc/hex/bin.html')
content=re.search('base64\n\n(.*)\n\n',text,re.S).group(1)
open('F://india.wav','wb').write(base64.decodestring(content))
handler=urllib2.HTTPBasicAuthHandler()
handler.add_password('inflate','www.pythonchallenge.com','butter','fly')
cookies=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),handler)
urllib2.install_opener(opener)
request=urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
request.add_header('Cookie','info=sorry')
response=opener.open(request).read()
print response
import xmlrpclib
server=xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('lepold')
iwave=wave.open('F://india.wav')

owave=wave.open('F://out.wav','wb')
owave.setnchannels(1)#set channel
owave.setsampwidth(iwave.getsampwidth())#set samplewidth
owave.setframerate(iwave.getframerate())#set frame rate
for i in range(iwave.getnframes()):
    owave.writeframes(iwave.readframes(1)[::-1])
iwave.close()
owave.close()
 
