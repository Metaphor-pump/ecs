from jackTokenizer import parser
from compilationEngine import compile
import sys,os

def main(filename):
    jackParser = parser(filename)
    jackParser.uncomment()
    compiler = compile(jackParser,filename)
    compiler.compileClass()  

filename = sys.argv[1]
if os.path.isdir(filename):
    filelist = os.listdir(filename)
    os.chdir(filename)
    filelist = filter(lambda(x):x.find('.jack')>0,filelist)
    for each in filelist:
        main(each)
elif os.path.isfile(filename):
    main(filename)
else:
    print 'not found '+ filename