from symbolTable import Table
from asmparser import parser
import code
import sys

filename = sys.argv[1].split('.')[0]

onepass = parser(filename)
table = Table()
lineCnt = 0
while onepass.hasMoreCommands():
    onepass.advance()
    onepass.Uncomment()
    Type = onepass.commandType()
    if Type == 'L_COMMAND':
        symbol = onepass.symbol()
        if not table.contains(symbol):
            table.addEntry(symbol,lineCnt)
    else:
        lineCnt += 1

twopass = parser(filename)
output = open(filename+'.hack','w')
varCnt = 16
while twopass.hasMoreCommands():
    twopass.advance()
    onepass.Uncomment()
    Type = twopass.commandType()
    if Type == 'A_COMMAND':
        symbol = twopass.symbol()
        if symbol.isdigit():
            result = code.A_command(symbol)
        else:
            if table.contains(symbol):
                value = table.valueOf(symbol)
                result = code.A_command(value)
            else:
                table.addEntry(symbol,varCnt)
                result = code.A_command(varCnt)
                varCnt += 1
        output.write(result+'\n')
    elif Type ==  'C_COMMAND':  
        binary = code.C_command(twopass)
        output.write('111'+ binary +'\n')
output.close()
                