import re
from collections import Counter
a=[1,11,21,1211,111221,]#the after is the each number of the before
cnt=Counter()
word=''
def func():
    while (1):
        word=''
        for char in str(a[-1]):
            cnt[char]+=1
        lst=list(cnt)
  
        for x in range(0,len(lst)):
            word+=str(cnt[lst[x]])+lst[x]       
        a.append(word)
        word=''
        cnt=Counter()
        if len(a)>31:
            break
    print a
    print len(a[30])
def fun():
    a=[1,11,21,1211,111221,]
    while(1):
        length=len(str(a[-1]))
        temp=str(a[-1])[0]
        word=''
        cur=1
        for x in range(1,length): 
            char=str(a[-1])[x]
            if temp==char:
                cur+=1
                if(x==length-1): 
                    word+=str(cur)+temp
                else:
                    continue
            else:
                word+=str(cur)+temp
                if(x==length-1):  
                    word+='1'+char
                else:
                    temp=char
                    cur=1
        a.append(word)
        cur=1
        word=''
        if len(a)>31:
            break
    print len(a[30])     
if __name__=='__main__':
    fun()
        
                       
                    
                       
            
