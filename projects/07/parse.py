class vmparser:
    def __init__(self,filename):
        self.input = open(filename,'r')
        self.current = 1
        self.arithList=['add','sub','neg','eq','gt','lt','and','or','not']

    def hasMoreCommands(self):
        if self.current:
            return 1
        else:
            return 0
    
    def advance(self):
        self.current = self.input.readline()
    
    def commandType(self):
        if self.current.strip() in self.arithList:
            return 'C_ARITHMETIC'
        elif self.current.find('push')>=0:
            return 'C_PUSH'
        elif self.current.find('pop')>=0:
            return 'C_POP'
        elif self.current.find('label')>=0:
            return 'C_PUSH'
        elif self.current.find('goto')>=0:
            return 'C_GOTO'
        elif self.current.find('fuction')>=0:
            return 'C_FUCTION'
        elif self.current.find('return')>=0:
            return 'C_RETURN'
        elif self.current.find('call')>=0:
            return 'C_CALL'
        else:
            return 'None'

    def arg1(self):
        commandtype = self.commandType()
        if commandtype == 'C_ARITHMETIC':
            return self.current.strip()
        elif commandtype == 'C_RETURN':
            return
        else:
            return self.current.split(' ')[1].strip()
    
    def arg2(self):
        commandtype = self.commandType()
        if commandtype in ('C_POP','C_PUSH','C_FUNCTION','C_CALL'):
            return self.current.split(' ')[2].strip()
    
    def Uncomment(self):
        self.current = self.current.split('//')[0]