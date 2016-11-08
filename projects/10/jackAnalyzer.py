from jackTokenizer import parser
from compilationEngine import compile
import sys,os
import pdb
pdb.set_trace()
filename = sys.argv[1]
jackParser = parser(filename)
jackParser.uncomment()
jackParser = parser('uncommentFile')
compiler = compile(jackParser,filename)
compiler.compileClass()  
#os.remove('uncommentFile') 