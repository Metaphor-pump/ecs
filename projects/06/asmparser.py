
class parser(object):
    
    def __init__(self,filename):
        self.current = 1
        self.input = open(filename+'.asm','r')

    def advance(self):
        self.current = self.input.readline()

    def hasMoreCommands(self):
        return self.current


    def commandType(self):
        if self.current.find('@')>=0:
            return 'A_COMMAND'  
        elif self.current.find('=')>=0 or self.current.find(';')>=0:  
            return 'C_COMMAND'  
        elif self.current.find('(')>=0:  
            return 'L_COMMAND'  
        else:
            return 'None'

    def symbol(self):
        return self.current.strip(' @()\n')
    
    def dest(self):
        if self.current.find('=')>=0:  
            destlist=self.current.split('=')
            return destlist[0].strip(' \n') 
        elif self.current.find(';')>=0:
            return 'null'

    def comp(self):
        if self.current.find('=')>=0:
            if self.current.find(';')>=0:
                complist=self.current.split('=')
                complist=complist[1].split(';')
                return complist[0].strip(' \n')
            else:
                complist=self.current.split('=')
                return complist[1].strip(' \n')
        else:
            complist=self.current.split(';')
            return complist[0].strip(' \n')

    def jump(self):
        if self.current.find(';')>=0:
            complist=self.current.split(';')
            return complist[1].strip(' \n')
        else:
            return 'null'

    def Uncomment(self):
        while self.current == '\n' or self.current.startswith('//'):      
            self.advance()