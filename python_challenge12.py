# coding=utf-8
f=open('F://evil2.gfx','rb')
contents=f.read()
f.close()

for i in xrange(5):
    f=open('F://%d.png'%i,'wb')
    f.write(contents[i::5])
    f.close()

    
