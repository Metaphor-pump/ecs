from symbolTable import Table
from asmparser import parser
import code
import sys

filename = sys.argv[1].split('.')[0]
output = open(filename+'.hack','w')
onepass = parser(filename)
twopass = parser(filename)
table = Table()

labelCnt = 0
while onepass.hasMoreCommands():
    onepass.advance()
    while onepass.current == '\n' or onepass.current.startswith('//'):
        onepass.advance()
    Type = onepass.commandType()
    if Type == 'L_COMMAND':
        symbol = onepass.symbol()
        if not table.contains(symbol):
            table.addEntry(symbol,labelCnt)
    else:
        labelCnt += 1

varCnt = 16
while twopass.hasMoreCommands():
    twopass.advance()
    while twopass.current == '\n' or twopass.current.startswith('//'):
        twopass.advance()
    twopass.Uncomment()
    Type = twopass.commandType()
    if Type == 'A_COMMAND':
        symbol = twopass.symbol()
        if symbol.isdigit():
            result = code.tenTobin(symbol)
        else:
            if table.contains(symbol):
                result = code.tenTobin(table.getAddress(symbol))
            else:
                table.addEntry(symbol,varCnt)
                result = code.tenTobin(varCnt)
                varCnt += 1
        output.write(result+'\n')
    elif Type ==  'C_COMMAND':  
        dest = code.dest(twopass)
        comp = code.comp(twopass)
        jump = code.jump(twopass)
        output.write('111'+comp+dest+jump+'\n')
output.close()
                