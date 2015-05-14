from PIL import Image,ImageDraw,ImageSequence


image=Image.open(r'F://white.gif')
path =[im.getbbox()[0:2] for im in ImageSequence.Iterator(image)]
letter=0
pos=(30,30)
joy=Image.new(image.mode,(200,200),0)
for p in path:
    if p==(100,100):
        letter+=1
        pos=(letter*30,)*2
    else:
        pos=(pos[0]+p[0]-100,pos[1]+p[1]-100)
            
    joy.putpixel(pos,255)
joy.save('joy.gif')
joy.show()
