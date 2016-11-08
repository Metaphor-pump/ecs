import sys,os
from parse import vmparser
from codeWriter import writer

def translate(filename,parser,code):
    while parser.hasMoreCommands():
        parser.advance()
        while parser.current == '\n' or parser.current.startswith('//'):
            parser.advance()
        parser.Uncomment()
        commandType = parser.commandType()
        if commandType =='C_ARITHMETIC':
            code.writeArithmetic(parser.current.strip())
        elif commandType in ('C_PUSH','C_POP'):  
            code.writePushPop(commandType,parser)
        elif commandType == 'C_LABEL':
            code.writeLabel(parser.current)
        elif commandType == 'C_GOTO':
            code.writeGoto(parser.current)
        elif commandType == 'C_FUNCTION':
            funName = parser.current.split(' ')[1]
            LocalNum = int(parser.current.split(' ')[2])
            code.writeFun(funName,LocalNum)
        elif commandType == 'C_CALL':
            funName = parser.current.split(' ')[1]
            argNum = int(parser.current.split(' ')[2])
            code.writeCall(funName,argNum)
        elif commandType == 'C_RETURN':
            code.writeReturn()

filename = sys.argv[1]
if os.path.isdir(filename):
    os.chdir(filename)
    code = writer(filename)
    for i in os.walk(os.getcwd()):#get filelist
        filelist = i[2]
    if 'Sys.init' in filelist:
        code.init()
    for eachfile in filelist:
        if(eachfile.endswith('.vm')):
            parser = vmparser(eachfile)
            translate(filename,parser,code)
    code.close()
else :
    print 'do not have vm dir to tanslate'
    exit()