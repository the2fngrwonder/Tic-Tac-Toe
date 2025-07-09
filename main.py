player1 = input('Input player 1 name: ')
player2 = input('input player 2 name: ')

turn_count = 1
winner = ''
board = [
        ' ', '1', ' ', '2', ' ', '3',
        '1', ' ', '|', ' ', '|', ' ',
        ' ', '-', '-', '-', '-', '-',
        '2', ' ', '|', ' ', '|', ' ',
        ' ', '-', '-', '-', '-', '-',
        '3', ' ', '|', ' ', '|', ' ',
        'Turn Count: ', turn_count, '\n'
        ]
        
def draw_board(piece = ' '):
    count = 1
    for x in range(len(board)):
        if ((x + 1) % 6) != 0:
            print(board[x], end = '')
        else:
            print(board[x])
    
def get_x():
    print(f'It is your turn, {player1}')
    x = int(input('Enter X coord: '))
    y = int(input('Enter Y coord: '))
    board[37] = turn_count
    
    return(get_position(x,y), 'X')
    
def get_o():
    print(f'It is your turn, {player2}')
    x = int(input('Enter X coord: '))
    y = int(input('Enter Y coord: '))
    board[37] = turn_count
    
    return(get_position(x,y), 'O')
    
def get_position(x, y) -> int:
    if (x == 1) and (y == 1):
        return(7)
    
    elif (x == 2) and (y == 1):
        return(9)
        
    elif (x == 3) and (y == 1):
        return(11)
        
    elif (x == 1) and (y == 2):
        return(19)
        
    elif (x == 2) and (y == 2):
        return(21)
        
    elif (x == 3) and (y == 2):
        return(23)
        
    elif (x == 1) and (y == 3):
        return(31)
        
    elif (x == 2) and (y == 3):
        return(33)
        
    elif (x == 3) and (y == 3):
        return(35)
        
    else:
        print('That is not a valid placement.')
        return(0)
        
def win_game() -> bool:
    end_game = False
    
    if turn_count >= 3:
        if (board[7] != ' ') and (board[7] == board[9]) and (board[7] == board[11]):
            end_game = True
            
        if (board[19] != ' ') and (board[19] == board[21]) and (board[19] == board[23]):
            end_game = True    
        
        if (board[31] != ' ') and (board[31] == board[33]) and (board[31] == board[35]):
            end_game = True
            
        if (board[7] != ' ') and (board[7] == board[19]) and (board[7] == board[31]):
            end_game = True
            
        if (board[9] != ' ') and (board[9] == board[21]) and (board[9] == board[33]):
            end_game = True
            
        if (board[11] != ' ') and (board[11] == board[23]) and (board[11] == board[35]):
            end_game = True
            
        if (board[7] != ' ') and (board[7] == board[21]) and (board[7] == board[35]):
            end_game = True
            
        if (board[11] != ' ') and (board[11] == board[21]) and (board[11] == board[31]):
            end_game = True
            
    return(end_game)

while (win_game() != True) and (turn_count < 9) :
    draw_board()
    location, piece = get_x()
    turn_count += 1
    board[location] = piece
    if win_game() == True:
        print(f'{player1} Wins!')
        break
    
    draw_board()
    location, piece = get_o()
    turn_count += 1
    board[location] = piece
    if win_game() == True:
        print(f'{player2} Wins!')
        break
        
draw_board()