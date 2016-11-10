class parser:
    def __init__(self,filename):
        self.symbol=('{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~')  
        self.keyword=('class','constructor','function','method','field','static','var','int','char','boolean', 'void','true','false','null','this','let','do','if','else','while','return')  
        self.rfile = open(filename,'r')  
        self.token = ''
        self.filename = filename
        self.tokenType = ''

    def advance(self):
        self.token = ''
        char = self.rfile.read(1)
        while char == ' ' or char == '\n' or char == '\t':
            char = self.rfile.read(1)
        if not char:#end of file
            return
        elif char == '"':#string
            char = self.rfile.read(1)
            while char != '"':
                self.token += char
                char = self.rfile.read(1)
            self.tokenType = 'stringConstant'
            return
        elif char in self.symbol:#symbol
            self.token = char
            self.tokenType = 'symbol'
            return
        elif char.isdigit():#integer
            self.token += char
            char = self.rfile.read(1)
            while char.isdigit():
                self.token += char
                char = self.rfile.read(1)
            self.rfile.seek(-1,1)
            self.tokenType = 'integerConstant'
            return
        elif char.isalpha() or char == '_' or char.isdigit():#indentifier or keyword
            while char.isalpha() or char == '_' or char.isdigit():
                self.token += char
                char = self.rfile.read(1)
            self.rfile.seek(-1,1)
            if self.token in self.keyword:
                self.tokenType = 'keyword'
            else:
                self.tokenType = 'identifier'

    def uncomment(self):
        def write(line):
            if line != '\n':
                wfile.write(line)
                
        line = self.rfile.readline()
        wfile = open(self.filename.split('.')[0]+'.un','w')
        while line:
            if '//' in line:
                line = line.split('//')[0]
                write(line+'\n')
            elif '/*' in line:
                aline = line.split('/*')[0]
                write(aline+'\n')
                while line.find('*/')<0:
                    line = self.rfile.readline()
                bline = line.split('*/')[1]
                write(bline)
            else:
                wfile.write(line)
            line = self.rfile.readline()
        wfile.close()
        self.rfile = open(self.filename.strip('jack')+'un','r')

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
        elif self.token =='&':
            self.token = '&amp;'
        return '<'+self.tokenType+'> '+self.token+' </'+self.tokenType+'>\n'