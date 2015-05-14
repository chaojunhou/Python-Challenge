from PIL import Image
import urllib
import urllib2
import StringIO
def get_challenge(s):
    return urllib.urlopen(s).read()
def get_image(s):
    return Image.open(StringIO.StringIO(get_challenge(s)))
if __name__=='__main__':
    image=get_image('http://www.pythonchallenge.com/pc/return/wire.png')#10000*1
    spiral=Image.new(image.mode,(100,100),0)
    lst=[(1,0),(0,1),(-1,0),(0,-1)]#right up left down
    stp=[[i,i-1,i-1,i-2]for i in range(100,0,-2)]#10000=100+99+99+98->right,up,left,down
    stp=reduce(lambda x,y:x+y,stp)
    x,y,z=-1,0,0
    '''for i in len(stp):
            direction=lst[i%4]
            for elements in stp:'''
         
    for i in range(200):# the length of the stp
        direction=lst[i%4]# the first 100 elements is the right direction 
        for j in range(100-(i+1)/2): #put the number of pixels stp in the spiral
            x+=direction[0]
            y+=direction[1]
            spiral.putpixel((x,y),image.getpixel((z,0)))
            z+=1
    spiral.show()
            
    
