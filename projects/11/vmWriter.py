class writer:
    def __init__(self,filename):
        self.vmfile = open(filename.split('.')[0]+'.vm','w')

    def writePush(self,segment,index):
        self.vmfile.write('push '+segment+' '+str(index)+'\n')

    def writePop(self,segment,index):
        self.vmfile.write('pop '+segment+' '+str(index)+'\n')

    def writeOp(self,op):
        if op == '+':
            self.writeArith('add')
        elif op == '~':
            self.writeArith('not')
        elif op == '-':
            self.writeArith('sub')
        elif op == '*':
            self.writeCall('Math.multiply',2)
        elif op == '/':
            self.writeCall('Math.divide',2)
        elif op == '&':  
            self.writeArith('and')  
        elif op == '|':  
            self.writeArith('or')  
        elif op == '<':  
            self.writeArith('lt')  
        elif op == '>':  
            self.writeArith('gt')  
        elif op == '=':  
            self.writeArith('eq')  

    def writeArith(self,command):
        self.vmfile.write(command+'\n')

    def writeLabel(self,label):
        self.vmfile.write('label '+label+'\n')

    def writeGoto(self,label):
        self.vmfile.write('goto '+label+'\n')

    def writeIfgoto(self,label):
        self.vmfile.write('if-goto '+label+'\n')

    def writeCall(self,funName,nArgs):
        self.vmfile.write('call '+funName+' '+str(nArgs)+'\n')

    def writeFun(self,funName,nArgs):
        self.vmfile.write('function '+funName+' '+str(nArgs)+'\n')

    def writeReturn(self):
        self.vmfile.write('return\n')

    def close(self):
        self.vmfile.close()
