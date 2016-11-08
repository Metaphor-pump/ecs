class table:
    def __init__(self):
        self.table = []

    def find(self,name):
        for i in range(len(self.table)):
            if self.table[i][0] == name:
                return True
        return False
    
    def define(self,kind,Type,name):
        index = self.varCount(kind)
        self.table.append([name,kind,Type,index])

    def varCount(self,kind):
        cnt = 0
        for i in range(len(self.table)):
            if self.table[i][1] == kind:
                cnt+=1
        return cnt

    def kindOf(self,name):
        for i in range(len(self.table)):
            if self.table[i][0] == name:
                return self.table[i][1]
        return 'none'

    def typeOf(self,name):
        for i in range(len(self.table)):
            if self.table[i][0] == name:
                return self.table[i][2]
        return 'none'

    def indexOf(self,name):
        for i in range(len(self.table)):
            if self.table[i][0] == name:
                return self.table[i][3]
        return 'none'

    def init(self):
        self.table = []