print('Welcome to Tic Tac Toe!')

while True:
    def display_board(b):
        
        print(f"\nPlease note the positions on the board...")
        
        print(f'     |     |     ')
        print(f'  {b[1]}  |  {b[2]}  |  {b[3]}   ')
        print(f'_____|_____|_____')
        print(f'     |     |     ')
        print(f'  {b[4]}  |  {b[5]}  |  {b[6]}   ')
        print(f'_____|_____|_____')
        print(f'     |     |     ')
        print(f'  {b[7]}  |  {b[8]}  |  {b[9]}   ')
        print(f'     |     |     ')

    test_board = ['#','1','2','3','4','5','6','7','8','9']
    display_board(test_board)
    
    import random

    def choose_first():
        
        mynum = randint(0,2)
            if mynum == 1:
                print("Player 1 to start....")
            else:
                print("Player 2 to start....")

    choose_first()   
    
     # get player input
    
    nums = ['#',1,2,3,4,5,6,7,8,9]

        
    while game_on:
        
        
        def player_input():
            marker = input("Pick a marker 'x' or 'o'? (x/o)")
            position = int(input("Enter your position on the board(1-9)?"))

            return(marker,position)               


        (marker,position) = player_input()

        if position in nums:
            nums.pop(position)
            break
        else:
            print(f"Invalid choice/Number already entered...Please try again!")

    def place_marker(b,a,c):
        if a == 'x':
            mark = 'x'
        else:
            mark = 'o'
        b[c] = mark

        print(f'     |     |     ')
        print(f'  {b[1]}  |  {b[2]}  |  {b[3]}   ')
        print(f'_____|_____|_____')
        print(f'     |     |     ')
        print(f'  {b[4]}  |  {b[5]}  |  {b[6]}   ')
        print(f'_____|_____|_____')
        print(f'     |     |     ')
        print(f'  {b[7]}  |  {b[8]}  |  {b[9]}   ')
        print(f'     |     |     ')

        return b

    latest = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    latest = place_marker(latest,'x',3)

    print(f"\nthis is the latest board values = {latest} ")
    
    def win_check(board, mark):
        
        return ((board[1] and board[2] and board[3] == mark) or 
        (board[4] and board[5] and board[6] == mark) or 
        (board[7] and board[8] and board[9] == mark) or 
        (board[1] and board[4] and board[7] == mark) or
        (board[2] and board[5] and board[8] == mark) or 
        (board[3] and board[6] and board[9] == mark) or 
        (board[1] and board[5] and board[9] == mark) or 
        (board[3] and board[5] and board[7] == mark))

    win_check(latest, mark1)
    
    
    
    def space_check(board, position):
        return board[position] == ' '


    space_check(latest,3)
    
    
    
    def full_board_check(board):
        return ' ' not in board

    full_board_check(latest)
    
    
    
