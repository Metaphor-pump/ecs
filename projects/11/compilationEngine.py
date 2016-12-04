from vmWriter import writer
from symbolTable import table
class compiler:
    def __init__(self,parser,filename):
        self.parser = parser
        self.vm = writer(filename)
        self.className = []
        self.classScope = table()
        self.subScope = table()
        self.op = ('+','-','*','/','&','|','<','>','=')
        self.keywordConst = ('true','false','null','this')
        self.unaryOp = ('-','~')
        self.whileCnt = -1
        self.ifCnt = -1

    def returnTk_advance(self,x):
        for i in range(x):
            temp = self.nextToken()
            self.parser.advance()
        return temp

    def nextToken(self):
        return self.parser.token

    def compileClass(self):
        self.parser.advance()#'class'  the only preread to force the whole compiler
        while self.nextToken() == 'class':
            self.className = self.returnTk_advance(2)# 'class'className 
            self.returnTk_advance(1)#'{'
            self.compileClassVarDec()#classvar decalaration
            self.compileSubroutine()#subroutine decalaration
            self.returnTk_advance(1)#'}'
        
    def compileClassVarDec(self):
        while self.nextToken() in ('static','field'):
            kind = self.returnTk_advance(1)#kind
            Type = self.returnTk_advance(1)#type
            name = self.returnTk_advance(1)#varName
            self.classScope.define(kind,Type,name)
            while self.nextToken() == ',':
                name = self.returnTk_advance(2)#',' varName
                self.classScope.define(kind,Type,name)
            self.returnTk_advance(1)#';'
        
    def compileSubroutine(self):
        while self.nextToken() in ('method','function','constructor'):
            self.subScope.init()
            self.whileCnt = -1
            self.ifCnt = -1
            kind = self.nextToken()
            Type = self.returnTk_advance(2)#kind type
            self.funName = self.returnTk_advance(1)#funName
            self.compileParameterList(kind)#'('paraList')'
            self.returnTk_advance(1)#'{'
            self.compileSubroutineBody(kind)
            self.returnTk_advance(1)#'}'

    def compileParameterList(self,kind):
        def compileParameter():
            kind = 'argument'
            Type = self.returnTk_advance(1)#type
            name = self.returnTk_advance(1)#varName
            self.subScope.define(kind,Type,name)
        if kind == 'method':
            self.subScope.define('argument','class','Objname')
        self.returnTk_advance(1)#'('
        if self.nextToken() != ')':#first parameter's name
            compileParameter()#type varName
            while self.nextToken() == ',':
                self.returnTk_advance(1)#','
                compileParameter()#type varName
        self.returnTk_advance(1)#')'

    def compileSubroutineBody(self,kind):
        self.compileVarDec()
        if kind == 'constructor':
            n = self.classScope.varCount('field')
            self.vm.writePush('constant',n)
            self.vm.writeCall('Memory.alloc',1)
            self.vm.writePop('pointer',0)
        elif kind == 'method':
            self.vm.writePush('argument',0)
            self.vm.writePop('pointer',0)
        self.compileStatements()

    def compileVarDec(self):#similar to compileClassVarDec    
        varCnt = 0 
        while self.nextToken() =='var':#var or ('let','if','while','do','return')
            varCnt+=1
            kind = 'local'
            Type = self.returnTk_advance(2)#'var' type
            name = self.returnTk_advance(1)#varName
            self.subScope.define(kind,Type,name)
            while self.returnTk_advance(1) == ',':#','or';'
                varCnt += 1
                name = self.returnTk_advance(1)#varName
                self.subScope.define(kind,Type,name)
        funName = self.className +'.'+ self.funName
        self.vm.writeFun(funName,varCnt)

    def compileStatements(self):
         while self.nextToken() in ('let','if','do','while','return'):
            if self.nextToken() == 'let':
                self.compileLet()
            elif self.nextToken() == 'if':
                self.compileIf()
            elif self.nextToken() == 'do':
                self.compileDo()
            elif self.nextToken() == 'while':
                self.compileWhile()
            elif self.nextToken() == 'return':
                self.compileReturn()

    def compileLet(self):
        name = self.returnTk_advance(2)#'let'varName
        if self.nextToken() == '[':#array[index]
            self.returnTk_advance(1)
            self.compileExp()
            self.returnTk_advance(1)#'['exp']'
            segment,index = self.findVarInScope(name)
            self.vm.writePush(segment,index)
            self.vm.writeOp('+')
            self.returnTk_advance(1)#'='
            self.compileExp()
            self.vm.writePop('temp',0)
            self.vm.writePop('pointer',1)
            self.vm.writePush('temp',0)
            self.vm.writePop('that',0)
            self.returnTk_advance(1)#';'
        else:#varName
            segment,index = self.findVarInScope(name)
            self.returnTk_advance(1)#'=' 
            self.compileExp()#exp
            self.vm.writePop(segment,index)
            self.returnTk_advance(1)#';'

    def compileDo(self):
        self.returnTk_advance(1)#'do'
        self.compileExp()#function call
        self.vm.writePop('temp',0) #when do statement calling function must dispose the return value
        self.returnTk_advance(1)#';'

    def compileIf(self):
        self.ifCnt+=1
        cnt = self.ifCnt
        self.returnTk_advance(2)#'if''('
        self.compileExp()#exp
        self.returnTk_advance(2)#')''{'
        self.vm.writeIfgoto('IF_TRUE'+str(cnt))
        self.vm.writeGoto('IF_FALSE'+str(cnt))
        self.vm.writeLabel('IF_TRUE'+str(cnt))
        self.compileStatements()
        self.returnTk_advance(1)#'}'
        if self.nextToken() == 'else':
            self.vm.writeGoto('IF_END'+str(cnt))
            self.vm.writeLabel('IF_FALSE'+str(cnt))
            self.returnTk_advance(2)#'else {'
            self.compileStatements()
            self.returnTk_advance(1)#'}'
            self.vm.writeLabel('IF_END'+str(cnt))
        else:
            self.vm.writeLabel('IF_FALSE'+str(cnt))

    def compileWhile(self):#similar to compile if
        self.whileCnt+=1
        cnt = self.whileCnt
        self.vm.writeLabel('WHILE_EXP'+str(cnt))
        self.returnTk_advance(2)#'while''('
        self.compileExp()#exp
        self.vm.writeArith('not')
        self.vm.writeIfgoto('WHILE_END'+str(cnt))
        self.returnTk_advance(2)#')''{'
        self.compileStatements()
        self.returnTk_advance(1)#'}'
        self.vm.writeGoto('WHILE_EXP'+str(cnt))
        self.vm.writeLabel('WHILE_END'+str(cnt))

    def compileReturn(self):
        self.returnTk_advance(1)#'return'
        if self.nextToken() != ';':
            self.compileExp()
        else:
            self.vm.writePush('constant',0)
        self.returnTk_advance(1)#';'
        self.vm.writeReturn()

    def compileExpList(self):
        expCnt = 0
        self.returnTk_advance(1)#'('
        if self.nextToken() != ')':#exp
            expCnt += 1
            self.compileExp()
            while self.nextToken() == ',':
                expCnt += 1
                self.returnTk_advance(1)#','
                self.compileExp()
        self.returnTk_advance(1)#')'
        return expCnt

    def compileExp(self):
        self.compileTerm()
        while self.nextToken() in self.op:
            op = self.nextToken()
            self.returnTk_advance(1)#op
            self.compileTerm()
            self.vm.writeOp(op)

    def compileTerm(self):
        if self.parser.tokenType == 'integerConstant':#integer
            num = self.returnTk_advance(1)
            self.vm.writePush('constant',num)
        elif self.parser.tokenType =='stringConstant':#string
            string = self.returnTk_advance(1)
            lenth = len(string)
            self.vm.writePush('constant',lenth)
            self.vm.writeCall('String.new',1)
            for char in string:
                self.vm.writePush('constant',ord(char))
                self.vm.writeCall('String.appendChar',2)
        elif self.nextToken() in self.keywordConst:#keyword
            keyword = self.returnTk_advance(1)
            self.writeKeywordConst(keyword)
        elif self.nextToken() in self.unaryOp:#unaryop term
            op = self.nextToken()
            self.returnTk_advance(1)#unaryop
            self.compileTerm()#term
            if op == '~':
                self.vm.writeArith('not')
            elif op =='-':
                self.vm.writeArith('neg')
        elif self.nextToken() == '(':#'('exp')'
            self.returnTk_advance(1)#'('
            self.compileExp()#exp
            self.returnTk_advance(1)#')'
        elif self.nextToken() == '[':
            self.returnTk_advance(1)
            self.compileExp()
            self.returnTk_advance(1)#'['exp']'
        else:#varname|varname[index]|subroutineCall
            temp = self.returnTk_advance(1)
            if self.nextToken() == '.':#term is a subroutineCall aaa.bbb()
                Objname = temp
                funName = self.returnTk_advance(2)#'.' subroutineName
                if  self.subScope.find(Objname):#call function of an object which in subScope
                    className = self.subScope.typeOf(Objname)
                    name = className + '.' + funName
                    nArgs = 1
                    index = self.subScope.indexOf(Objname)
                    self.vm.writePush('local',index)            
                elif  self.classScope.find(Objname):#call function of an object which in classScope
                    className = self.classScope.typeOf(Objname)
                    name = className + '.' + funName
                    nArgs = 1
                    index = self.classScope.indexOf(Objname)
                    self.vm.writePush('this',index)
                else :#call system function or class 'function' or constuctor
                    name = Objname + '.' + funName
                    nArgs = 0
                nArgs += self.compileExpList()#'('expList')'
                self.vm.writeCall(name,nArgs)
            elif self.nextToken() == '(':#term is a subroutineCall bbb()
                nArgs = 1
                name = self.className + '.' + temp
                self.vm.writePush('pointer',0)
                nArgs += self.compileExpList()#'('expList')'
                self.vm.writeCall(name,nArgs)
            elif self.nextToken() == '[':#term is a array[index]
                array = temp
                self.returnTk_advance(1)#'['
                self.compileExp()
                self.returnTk_advance(1)#']'
                segment,index = self.findVarInScope(array)
                self.vm.writePush(segment,index)
                self.vm.writeOp('+')
                self.vm.writePop('pointer',1)
                self.vm.writePush('that',0)
            else:#term is a varname
                segment,index = self.findVarInScope(temp)
                self.vm.writePush(segment,index)

    def writeKeywordConst(self,keyword):
        if keyword == 'true':
            self.vm.writePush('constant',0)
            self.vm.writeArith('not')
        elif keyword == 'false':
            self.vm.writePush('constant',0)
        elif keyword == 'this':
            self.vm.writePush('pointer',0)
        elif keyword == 'null':
            self.vm.writePush('constant',0)

    def findVarInScope(self,varName):
        kind,index = 'not found','n'
        if self.classScope.find(varName):
            for var in self.classScope.table:
                if varName == var[0]:
                    kind,index = var[1],var[3]
        else:
            for var in self.subScope.table:
                if varName == var[0]:
                    kind,index = var[1],var[3]
        if kind == 'field':
            segment = 'this'
        else:
            segment = kind
        return segment,index