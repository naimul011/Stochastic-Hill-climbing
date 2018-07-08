
# coding: utf-8

# In[131]:


import random

n = int(input('Enter the number of queens to solve for: '))

class problem():
    
    board = list()
    neighbor = list()
    
    h = 0
    neighborh = 0
    
    def attacking(self,board,i,j):
        
        if i == j:
            return True
        elif i!=j :
            return i != j and (board[i] == board[j] or abs(board[i] - board[j])) == abs(i-j)
    
    def __init__(self):
        self.board = random.sample(range(n), n)
        self.neighbor = list(self.board) 
        
    def calValue(self,board):
        h = 0
        for i in range(len(board)):
            
            for j in range(len(board)):
                
                if self.attacking(board,i,j):
                        h += 1
                        #print('abs(board[',i,'] - board[',j,'])) == abs(',i,'-',j,')')
        self.h = h//2
            

        return int(h//2)
    
    
    def selectNeighbor(self,q):
        
        self.neighbor = list(self.board)
        board = list(self.board)
        

        for pos in range(len(self.board)):
            self.neighbor = list(board)
            
            if (pos != board[q]):
                self.neighbor[q] = pos
                
                print('c ',board,' ',self.calValue(board),'  ',self.neighbor,' ',self.calValue(self.neighbor))
                if self.calValue(board) > self.calValue(self.neighbor):
                    print(self.calValue(board),' >= ',self.calValue(self.neighbor))
                    board = list(self.neighbor)
                    
                    
                    
                
                
        return list(board)
               
    def hillclimbing(self):
        
        while 1:
            
            for q in range(len(self.board)):
                self.neighbor = self.selectNeighbor(q)
                
                print(self.calValue(self.board),' ',self.calValue(self.neighbor))
                if self.calValue(self.board) <= self.calValue(self.neighbor):
                    
                    print ('Optimal solution value ',problem.calValue(self.board))
                    return list(self.board)
                
                
                self.board = list(self.neighbor)

                    
problem = problem()


print ('Current ',problem.board)
print ('H value ',problem.calValue(problem.board))
print ('Result ',problem.hillclimbing())


def hillclimbing (problem):
    current = problem.intial_state()
    neighbor = problem.height()
    while neighbor.calValue() > current.calValue :
        neighbor = problem.height()
        
        if neighbor.calValue() <= current.calValue() :
            return current.board

