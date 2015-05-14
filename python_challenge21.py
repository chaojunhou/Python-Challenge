#__author__ = 'Houcj'
#coding=utf-8
'''
import bz2
import zlib
fp=open("F://package.pack",'rb')
data=fp.read()
fp.close()
print data
out=[]
while True:
    if data.startswith('BZh'):
        data=bz2.decompress(data)
        out.append('#')
    elif data.startswith('x\x9c'):
        data=zlib.decompress(data)
        out.append(' ')
    elif data.endswith('\x9cx'):
        data=data[::-1]
        out.append('\n')
    else:
        raise ValueError
f=open('F://hou.txt','wb')
f.writelines(data)
f.close()
print ''.join(data)
'''
import zlib,bz2  
 
f = open(r'F://package.pack','rb').read()
print list(f)
log = ''  
s = [' ','*','\n']  
decom = [zlib.decompress, bz2.decompress]  
revers = False  
while True:  
    index = -1  
    for decompress in decom:  
        index+=1  
        try:  
            f = decompress(f)  
            revers = False  
            break  
        except:  
            continue  
    else:  
        if not revers:  
            f = f[::-1]  
            index +=1  
            revers = True  
        else:  
            print f  
            break     
    log+=s[index]
print log 

