from jackTokenizer import parser
from compilationEngine import compiler
import sys,os

def compile(filename):
    jackParser = parser(filename)
    jackParser.uncomment()
    compile  = compiler(jackParser,filename)
    compile.compileClass()

filename = sys.argv[1]
if os.path.isdir(filename):
    filelist = os.listdir(filename)
    os.chdir(filename)
    filelist = filter(lambda(x):x.find('.jack')>0,filelist)
    for each in filelist:
        compile(each)
elif os.path.isfile(filename):
    compile(filename)
else:
    print 'not found '+ filename