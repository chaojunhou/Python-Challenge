from PIL import Image
from PIL import _imaging
import urllib2
import StringIO
def get_challenge(s):
	return urllib2.urlopen(urllib2.Request(s)).read()
def get_image(s):
	return Image.open(StringIO.StringIO(get_challenge(s)))
if __name__=='__main__':
    image=get_image('http://www.pythonchallenge.com/pc/def/oxygen.png')
    w,h=image.size
    image.getpixel((0,h/2))
    for x in range(1,8):
        print ''.join([chr(image.getpixel((i,h/2))[0]) for i in range(0,w,x)])+'\n'     
    result = [105, 110, 116, 101, 103, 114, 105, 116, 121]  
    print(''.join(chr(x) for x in result))
    print ''.join(map(chr,result))
 
    
    
