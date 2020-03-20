def display_board(b):
    
    for i in range(3):
        for j in range(0,3):
            print(b[i][j], ' ', end='')
        print('\n')
        
def check(b, currPlayer):
    
    for i in range(3):
        flag=0
        for j in range(3):
            if b[i][j]==currPlayer:
                flag += 1
        if flag==3:    
            print("Winner: ", currPlayer)
            return 1
    
    for i in range(3):
        flag=0
        for j in range(3):
            if b[j][i]==currPlayer:
                flag += 1
        if flag==3:    
            print("Winner: ", currPlayer)
            return 1
    
    
    return 0
    
    
board = [] # = {}

for i in range(3): # add 3 rows
    row = []
    for j in range(3): # for each row, add 3 elements
        row.append('_')
        
    # row = ['_', '_', '_']
    board.append(row)

display_board(board)

currPlayer = "x"

while(check(board, currPlayer)==0):
    if (currPlayer == "o"):
        currPlayer = "x"
    else:
        currPlayer = "o"
    # print('Player1')    
    posx = int(input('Enter x: '))
    posy = int(input('Enter y: '))
    # p1sym = "o"
    print()
    
    board[posx][posy] = currPlayer
    display_board(board)
    
    

