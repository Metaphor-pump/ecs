class compile:
    def __init__(self,parser,filename):
        self.parser = parser
        self.wfile = open(filename.strip('.jack')+'.xml','w')  
        self.nested = 0
        self.op = ('+','-','*','/','&','|','<','>','=')
        self.unaryOp = ('-','~')
        self.keywordConst = ('true','false','null','this')

    def indentedWrite(self,Str):
        self.wfile.write('  '*self.nested)
        self.wfile.write(Str)

    def nest(self,function,tag):
        self.indentedWrite('<'+tag+'>\n')
        self.nested+=1
        function()
        self.nested-=1
        self.indentedWrite('</'+tag+'>\n')

    def writeTk_Advance(self,x):
        for i in range(x):
            self.indentedWrite(self.parser.tagedToken())
            self.parser.advance()

    def compileClass(self):
        def a():
            self.writeTk_Advance(3)#'class' className '{'
            self.compileClassVarDec()
            self.compileSubroutine()
            self.writeTk_Advance(1) #'}'
        self.parser.advance()
        while self.parser.token == 'class':
            self.nest(a,'class')
        
    def compileClassVarDec(self):
        
        def a():
            self.writeTk_Advance(3)#static or field type varName
            while self.parser.token != ';':
                self.writeTk_Advance(2)#',' varName
            self.writeTk_Advance(1)#';'
        while self.parser.token in ('static','field'):#varDec part existd?
            self.nest(a,'classVarDec')
        
    def compileSubroutine(self):
        def a():
            self.writeTk_Advance(4)#'constructor','function','method' type subroutineName '('
            self.compileParameterList()
            self.writeTk_Advance(1)#')'
            self.compileSubroutineBody()
        while self.parser.token in ('constructor','function','method'):
            self.nest(a,'subroutineDec')

    def compileSubroutineBody(self):
        def a():
            self.writeTk_Advance(1)#'{'
            self.compileVarDec()
            self.compileStatements()
            self.writeTk_Advance(1)#'}'
        self.nest(a,'subroutineBody')

    def compileParameterList(self):
        def a():
            if self.parser.token != ')':
                self.writeTk_Advance(2)#type varName
                while self.parser.token == ',':
                    self.writeTk_Advance(3)#','' type varname
        self.nest(a,'parameterList')

    def compileVarDec(self):#similar to compileClassVarDec      
        def a():
            self.writeTk_Advance(3)#'var' type name
            while self.parser.token != ';':
                self.writeTk_Advance(2)#',' varName
            self.writeTk_Advance(1)#';'
        while self.parser.token == 'var':
            self.nest(a,'varDec')

    def compileStatements(self):
        def a():
            while self.parser.token in ('let','if','while','do','return'):
                if self.parser.token == 'let':
                    self.compileLet()
                elif self.parser.token == 'if':
                    self.compileIf()
                elif self.parser.token == 'do':
                    self.compileDo()
                elif self.parser.token == 'while':
                    self.compileWhile()
                elif self.parser.token == 'return':
                    self.compileReturn()
        self.nest(a,'statements')

    def compileLet(self):
        def a():
            self.writeTk_Advance(2)#'let'' varname
            self.compileIndex()
            self.writeTk_Advance(1)#'='
            self.compileExp()
            self.writeTk_Advance(1)#';'
        self.nest(a,'letStatement')

    def compileIndex(self):
        if self.parser.token == '[':
            self.writeTk_Advance(1)#'['
            self.compileExp()
            self.writeTk_Advance(1)#']'

    def compileDo(self):
        def a():
            self.writeTk_Advance(1)#'do'
            self.compileSubCall()
            self.writeTk_Advance(1)#';'
        self.nest(a,'doStatement')

    def compileSubCall(self):
        self.writeTk_Advance(1)
        if self.parser.token == '.':
            self.writeTk_Advance(2)#'.' subroutineName 
        self.writeTk_Advance(1)#'('
        self.compileExpList()
        self.writeTk_Advance(1)#')'

    def compileIf(self):
        def a():
            self.writeTk_Advance(2)#'if' '('
            self.compileExp()
            self.writeTk_Advance(2)#')''{'
            self.compileStatements()
            self.writeTk_Advance(1)#'}'
        self.nest(a,'ifStatement')

    def compileWhile(self):#similar to compile if
        def a():
            self.writeTk_Advance(2)#'while' '('
            self.compileExp()
            self.writeTk_Advance(2)#'(''{'
            self.compileStatements()
            self.writeTk_Advance(1)#'}'
        self.nest(a,'whileStatement')

    def compileReturn(self):
        def a():
            self.writeTk_Advance(1)#'return'
            if self.parser.token != ';':
                self.compileExp()
            self.writeTk_Advance(1)#';'
        self.nest(a,'returnStatement')

    def compileExpList(self):
        def a():
            if self.parser.token != ')':
                self.compileExp()
                while self.parser.token == ',':
                    self.writeTk_Advance(1)#','
                    self.compileExp()
        self.nest(a,'expressionList')

    def compileExp(self):
        def a():
            self.compileTerm()
            if self.parser.token in self.op:
                self.writeTk_Advance(1)#op
                self.compileTerm()
        self.nest(a,'expression')

    def compileTerm(self):
        def a():
            if self.parser.tokenType in ('integerConstant','stringConstant'):
                self.writeTk_Advance(1)
            elif self.parser.token in self.keywordConst:
                self.writeTk_Advance(1)
            elif self.parser.token in self.unaryOp:
                self.writeTk_Advance(1)
                self.compileTerm()#unaryop term
            elif self.parser.token == '(':
                self.writeTk_Advance(1)
                self.compileExp()
                self.writeTk_Advance(1)#'('exp')'
            else:#varname|varname[index]|subroutineCall
                self.writeTk_Advance(1)#term is a varname
                if self.parser.token == '[':#term is an varname[index]
                    self.writeTk_Advance(1)
                    self.compileExp()
                    self.writeTk_Advance(1)#'['exp']'
                elif self.parser.token == '.':#trem is a subroutineCall
                    self.writeTk_Advance(3)#'.'subroutineName '('
                    self.compileExpList()
                    self.writeTk_Advance(1)#')'
                elif self.parser.token == '(':
                    self.writeTk_Advance(1)#subroutineName '('
                    self.compileExpList()
                    self.writeTk_Advance(1)#')'
        self.nest(a,'term')