# coding=utf8
import math
from PIL import Image
image=Image.open(r'F://beer2.png')
colors=image.getcolors()
print colors
data=image.getdata()
for i in range(65,-1,-2):
    stp=[] 
    tmp=[]
    for j in data:
        if j!=colors[i][1] and j!=colors[i-1][1]: 
            stp.append(j)
            tmp.append(0)
        else:
            if j==colors[i][1]:
                tmp.append(1)
            else:
                tmp.append(0)
    data=stp # wonderful to elimate elements every time
    n=int(math.sqrt(len(tmp)))
    new_image=Image.new('1',(n,n))
    new_image.putdata(tmp)
    new_image.save('F://out%d.png'%((i+1)/2))
    

