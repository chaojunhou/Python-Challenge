
import httplib
import base64
import urllib2
from base64 import encodestring
import re 
headers={'Authorization':'Basic '+base64.b64encode('butter:fly')}#b64encode char
# encodestring  is about the string  encodestring('butter:fly')[:-1]
conn=httplib.HTTPConnection('www.pythonchallenge.com')# http authorization
pattern=re.compile(r'bytes (\d+)-(\d+)')
def get_challenge20(start,end):
    
    for x in range(10):
        headers['Range']='bytes=%s-%s'%(start,end)
        conn.request('GET','/pc/hex/unreal.jpg','',headers)
        r=conn.getresponse()
        data=r.read()
        stp=str(r.getheader('content-range'))
        m=pattern.search(stp)
        if m:
            start=int(m.group(2))+1
            print data
        else:
            start=end
            end=start+1   
get_challenge20(0,2123456743)
headers["Range"] = "bytes=1152983631-1152983632"  
conn.request("GET", "/pc/hex/unreal.jpg", "", headers)  
response = conn.getresponse()  
fp = open("F://data.zip", "wb")  
fp.write(response.read())  
fp.close() 
