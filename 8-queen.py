import numpy as np

class node:
    def __init__(self,childs, y=None, x=None, par=None):
        self.row = y
        self.col = x
        self.parent = par
        self.child = [None for i in range(childs)]

class queens:
    def __init__(self, chess_size=4):
        self.size = chess_size
        self.root = None
        self.chess = None
        self.is_fined = False

    def conflict(self,cur_node):
        if cur_node.row == 0:
            return False
        self.chess = np.zeros((self.size,self.size),dtype=int)
        temp = cur_node
        #make chess matrix
        while temp.parent:      
            self.chess[temp.row,temp.col] = 1
            temp = temp.parent
        self.show()
        #check up 
        y = cur_node.row - 1
        while y >= 0:
            if self.chess[y,cur_node.col] == 1:
                return True
            y -= 1

        #check diameter up-left
        y = cur_node.row - 1    
        x = cur_node.col - 1
        while y >= 0 and x >= 0:
            if self.chess[y,x] == 1:
                return True
            y -= 1
            x -= 1
        #check diameter up-right
        y = cur_node.row - 1    
        x = cur_node.col + 1
        while y >= 0 and x < self.size:
            if self.chess[y,x] == 1:
                return True
            y -= 1
            x += 1

        return False
        
    def Find_DFS(self,cur_node):
        if self.is_fined == True:
            return  True
        else:
            if self.root == None:
                self.root = node(self.size)
                row = 0
                for colum in range (self.size):
                    self.root.child[colum] = node(childs=self.size, y=row, x=colum, par=self.root)
                    self.Find_DFS(self.root.child[colum])
                    if self.is_fined == True:
                        return True
                    self.root.child[colum] = None
            else:
                if self.conflict(cur_node) == True:
                    return False
                else:
                    if cur_node.row == self.size-1:
                        self.is_fined = True
                        return True
                    else:
                        row = cur_node.row + 1
                        for colum in range (self.size):
                            cur_node.child[colum] = node(childs=self.size, y=row, x=colum, par=cur_node)
                            self.Find_DFS(cur_node.child[colum])
                            if self.is_fined == True:
                                return True
                            cur_node.child[colum] = None
    
    def Find(self):
        self.Find_DFS(self.root)
        if self.is_fined == False:
            print('There is no way to arrange queens :(')
        else:
            print('Arrange Found :) ==>\n')
            self.show()
         
    def show(self):
        for i in self.chess:
            for j in i:
                if j == 1:
                    print('Q  ',end='')
                else:
                    print('-  ',end='')
            print()
        print('\n----------------------------\n')

size = 0
while size < 2:
    size = int(input('Enter size of Chess:  '))

chess = queens(chess_size=size)
chess.Find()