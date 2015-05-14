import re
from PIL import Image

f = open(r'F://yankeedoodle.csv','r').read()  
  
data = re.findall(r'(0.\d*)',f)  
new = Image.new('F',(53,139))  
new.putdata(map(float,data))  
new = new.transpose(Image.ROTATE_90)  
new = new.transpose(Image.FLIP_TOP_BOTTOM)  
new.save(r'F:\out30.tiff')  
  
s = [chr(int(data[i][5]+data[i+1][5]+data[i+2][6])) for i in range(0,len(data)-2,3)]  
print ''.join(s)  
