import zipfile
import re
def zip_file():
    comments=[]
    zpf=zipfile.ZipFile('D://channel.zip')
    text=zpf.read('90052.txt')
    for x in range(len(zpf.namelist())):
        mat=re.match('Next nothing is ([0-9]+)',text)
        if mat:
          number=mat.group(1)
          text=zpf.read('%s.txt'%number)
          comments.append(zpf.getinfo('%s.txt'%number).comment)
        else:
            print text
            break
    return comments
print ''.join(zip_file())
