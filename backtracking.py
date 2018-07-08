board = {}
n = int(input('Enter the number of queens to solve for: '))


def minConflict(k, i):
    if (i in board.values()):
        return False
    j = 1
    while(j < k):
        if abs(board[j]-i) == abs(j-k):
            return False
        j+=1
    return True

def clear_future_blocks(k):
    
    for i in range(k,n+1):
       board[i] = None
      
def backtrack(k):
    
    for pos in range(1, n + 1):
        clear_future_blocks(k)
        
        if minConflict(k, pos):
            board[k] = pos
            if (k==n):
                for j in board:
                    
                    print (board[j],end="")
                print ()
            else:
                backtrack(k+1)


def backtrackingSearch () :
    backtrack(1)

backtrackingSearch()