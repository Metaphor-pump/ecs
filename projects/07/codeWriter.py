from parse import vmparser

class writer:
    def __init__(self,filename):
        self.filename = filename.split('.')[0]
        self.output = open(filename.split('.')[0]+'.asm','w')
        self.CODEFLAG1=0
        self.CODEFLAG2=0
    def writeArithmetic(self,command):
        if command == 'add':
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n')
        elif command == 'sub':
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n')  
        elif command == 'neg':  
            self.output.write('@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n')  
        elif command == 'and':  
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n')  
        elif command == 'or':  
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n')  
        elif command == 'not':  
            self.output.write('@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n')  
        elif command == 'eq':  
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\n@RET_TRUE'+str(self.CODEFLAG1)+'\nD;JEQ\nD=0\n@CONTINUE'+str(self.CODEFLAG2)+'\n0;JMP\n(RET_TRUE'+str(self.CODEFLAG1)+')\nD=-1\n(CONTINUE'+str(self.CODEFLAG2)+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')  
            self.CODEFLAG1+=1  
            self.CODEFLAG2+=1  
        elif command == 'gt':  
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@RET_TRUE'+str(self.CODEFLAG1)+'\nD;JGT\nD=0\n@CONTINUE'+str(self.CODEFLAG2)+'\n0;JMP\n(RET_TRUE'+str(self.CODEFLAG1)+')\nD=-1\n(CONTINUE'+str(self.CODEFLAG2)+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')  
            self.CODEFLAG1+=1  
            self.CODEFLAG2+=1  
        elif command == 'lt':  
            self.output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@RET_TRUE'+str(self.CODEFLAG1)+'\nD;JLT\nD=0\n@CONTINUE'+str(self.CODEFLAG2)+'\n0;JMP\n(RET_TRUE'+str(self.CODEFLAG1)+')\nD=-1\n(CONTINUE'+str(self.CODEFLAG2)+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')  
            self.CODEFLAG1+=1  
            self.CODEFLAG2+=1  
        self.output.write('//'+command+'\n')
    def writePushPop(self,command,segment,index):
        if command == 'C_PUSH':
            if segment == 'constant':
                self.output.write('@'+index+'\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'local':
                self.output.write('@LCL\nD=M\n@'+index+'\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'argument':
                self.output.write('@ARG\nD=M\n@'+index+'\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'this':
                self.output.write('@THIS\nD=M\n@'+index+'\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'that':
                self.output.write('@THAT\nD=M\n@'+index+'\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'pointer':  
                if index == '0':  
                    self.output.write('@3\n')  
                elif index == '1':  
                    self.output.write('@4\n')  
                self.output.write('D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')  
            elif segment == 'temp':
                self.output.write('@'+str(5+int(index))+'\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
            elif segment == 'static':
                self.output.write('@'+self.filename+'.'+index+'\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')
        elif command =='C_POP':   
            if segment == 'local':  
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@LCL\nA=M\n')  
                for i in range (int(index)):  
                    self.output.write('A=A+1\n')  
                self.output.write('M=D\n')  
            elif segment =='argument':  
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\n')  
                for i in range (int(index)):  
                    self.output.write('A=A+1\n')  
                self.output.write('M=D\n')  
            elif segment == 'this':  
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@THIS\nA=M\n')  
                for i in range (int(index)):  
                    self.output.write('A=A+1\n')  
                self.output.write('M=D\n')  
            elif segment == 'that':  
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@THAT\nA=M\n')  
                for i in range (int(index)):  
                    self.output.write('A=A+1\n')  
                self.output.write('M=D\n')  
            elif segment == 'pointer':  
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n')  
                if index == '0':  
                    self.output.write('@3\n')  
                else:  
                    self.output.write('@4\n')  
                self.output.write('M=D\n')  
            elif segment == 'temp':
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@'+str(5+int(index))+'\nM=D\n')
            elif segment == 'static':
                self.output.write('@SP\nM=M-1\nA=M\nD=M\n@'+self.filename+'.'+index+'\nM=D\n')
        self.output.write('//'+command+' '+segment+' '+index+'\n')
    def close(self):
        self.output.close()