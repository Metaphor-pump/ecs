class parser:
    def __init__(self,filename):
        self.symbol=('{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~')  
        self.keyword=('class','constructor','function','method','field','static','var','int','char','boolean', 'void','true','false','null','this','let','do','if','else','while','return')  
        self.rfile = open(filename,'r')  
        self.token = ''
        self.tokenType = ''

    def advance(self):
        self.token = ''
        temp = self.rfile.read(1)
        while temp == ' ' or temp == '\n' or temp == '\t':
            temp = self.rfile.read(1)
        if not temp:#end of file
            return
        elif temp == '"':
            temp = self.rfile.read(1)
            while temp != '"':
                self.token += temp
                temp = self.rfile.read(1)
            self.tokenType = 'stringConstant'
            return#string
        elif temp in self.symbol:
            self.token = temp
            self.tokenType = 'symbol'
            return#symbol
        elif temp.isdigit():
            self.token+=temp
            temp = self.rfile.read(1)
            while temp.isdigit():
                self.token+=temp
                temp = self.rfile.read(1)
            self.rfile.seek(-1,1)
            self.tokenType = 'integerConstant'
            return#integer
        elif temp.isalpha() or temp == '_' or temp.isdigit():
            while temp.isalpha() or temp == '_' or temp.isdigit():
                self.token += temp
                temp = self.rfile.read(1)
                if self.token in self.keyword:
                    self.tokenType = 'keyword'
                    self.rfile.seek(-1,1)
                    return#keyword
            self.rfile.seek(-1,1)
            self.tokenType = 'identifier'
            return#indentifier

    def uncomment(self):
        line = self.rfile.readline()
        wfile = open('uncommentFile','w')
        while line:
            while line == '\n' or line.startswith('//'):
                line = self.rfile.readline()
            if '//' in line:
                line = line.split('//')[0]
                wfile.write(line+'\n')
            elif '/*' in line:
                aline = line.split('/*')[0]
                wfile.write(aline+'\n')
                while line.find('*/')<0:
                    line = self.rfile.readline()
                line = line.split('*/')[1]
                wfile.write(line+'\n')
            else:
                wfile.write(line)
            line = self.rfile.readline()
        wfile.close()

    def hasMoreTokens(self):
        if self.token:
            return True
        else:
            return false

    def tagedToken(self):
        if self.token == '<':
            self.token = '&lt;'
        elif self.token == '>':
            self.token = '&gt;'
        return '<'+self.tokenType+'> '+self.token+' </'+self.tokenType+'>\n'