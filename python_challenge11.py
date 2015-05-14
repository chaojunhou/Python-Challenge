from PIL import Image
image=Image.open('F://cave.jpg')
w,h=image.size
print w,h
for x in range(0,w):
    for y in range(0,h):
        if(x+y)%2==1:
            image.putpixel((x,y),0)
image.show()
            
        
