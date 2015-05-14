import urllib2
import re
import difflib
from PIL import Image
import gzip
import StringIO
gfp=gzip.open("F://deltas.gz")
p1,p2=[],[]
file1,file2,file3=[],[],[]
for line in gfp:
    p1.append(line[0:53])
    p2.append(line[56:-1])
for line in list(difflib.ndiff(p1,p2)):
    if line[0]=='+':
        file1.append(line[2:])
    elif line[0]=='-':
        file2.append(line[2:])
    else:
        file3.append(line[2:])

for n,data in enumerate((file1,file2,file3)):
    temp=[]
    count=0
    for line in data:
        temp.extend([chr(int(ch,16)) for ch in line.strip().split(' ')if ch])
    f=open("%d.png"%n,'wb')
    print 'is writing'
    f.writelines(temp)
    f.close()
  
'''
import gzip, difflib  
    
h = gzip.open("F://deltas.gz")  
d = difflib.Differ()  
   
part_1, part_2 = [], []  
file_1, file_2, file_3 = [], [], []  
   
for line in h:  
    part_1.append(line[0:53])  
    part_2.append(line[56:-1])  
   
h.close()  
   
for line in list(d.compare(part_1, part_2)):  
    if line[0] == "+":  
        file_1.append(line[2:])  
    elif line[0] == "-":  
        file_2.append(line[2:])  
    else:  
        file_3.append(line[2:])  
   
for n, data in enumerate((file_1, file_2, file_3)):  
    temp = []  
   
    for line in data:  
        temp.extend([chr(int(o, 16)) for o in line.strip().split(" ") if o])  
   
    h = open("%s.png" % (n + 1), "wb")  
    h.writelines(temp)  
    h.close()  
'''    
    
