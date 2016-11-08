import sys
from parse import vmparser
from codeWriter import writer


filename = sys.argv[1]
parser = vmparser(filename)
code = writer(filename)

while parser.hasMoreCommands():
    parser.advance()
    while parser.current == '\n' or parser.current.startswith('//'):
        parser.advance()
    parser.Uncomment()
    commandType = parser.commandType()
    if commandType =='C_ARITHMETIC':
        code.writeArithmetic(parser.current.strip())
    elif commandType in ('C_PUSH','C_POP'):  
        code.writePushPop(commandType,parser.arg1(),parser.arg2())

code.close()
