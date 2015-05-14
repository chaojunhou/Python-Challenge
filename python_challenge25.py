import urllib
import urllib2
from PIL import Image
import wave
def get_wave(i):
    return urllib.urlopen('http://www.pythonchallenge.com/pc/hex/lake%d.wav'%i)
waves=[wave.open(get_wave(i)) for i in range(1,26)]
print 'Hello world!'
jigsaw=Image.new('RGB',(300,300),0)
def jig(w):
    return Image.fromstring('RGB',(60,60),w.readframes(w.getnframes()))
for i in range(len(waves)):
    jigsaw.paste(jig(waves[i]),(60*(i%5),60*(i/5)))
jigsaw.save('F://lake.png')
