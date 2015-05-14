import StringIO
import urllib
import urllib2
from PIL import Image
def get_image(s):
    content=urllib.urlopen(s).read()
    return Image.open(StringIO.StringIO(content))

if __name__=='__main__':
    image=get_image('http://www.pythonchallenge.com/pc/return/mozart.gif')
    w,h=image.size
    for y in range(h):
        line=[image.getpixel((x,y))for x in range(w)]
      
        idx=line.index(195)
        line=line[idx:]+line[:idx]
        for x in range(len(line)):
            image.putpixel((x,y),line[x])
    image.save('F://fuck.png')

    image.show()
