TicTacToeBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in TicTacToeBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(TicTacToeBoard)
        print("It's your turn " + turn + ". Move to which place?")

        move = input()        

        if TicTacToeBoard[move] == ' ':
            TicTacToeBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
 
        if count >= 5:
            if TicTacToeBoard['7'] == TicTacToeBoard['8'] == TicTacToeBoard['9'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif TicTacToeBoard['4'] == TicTacToeBoard['5'] == TicTacToeBoard['6'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif TicTacToeBoard['1'] == TicTacToeBoard['2'] == TicTacToeBoard['3'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif TicTacToeBoard['1'] == TicTacToeBoard['4'] == TicTacToeBoard['7'] != ' ':
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif TicTacToeBoard['2'] == TicTacToeBoard['5'] == TicTacToeBoard['8'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif TicTacToeBoard['3'] == TicTacToeBoard['6'] == TicTacToeBoard['9'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif TicTacToeBoard['7'] == TicTacToeBoard['5'] == TicTacToeBoard['3'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif TicTacToeBoard['1'] == TicTacToeBoard['5'] == TicTacToeBoard['9'] != ' ': 
                printBoard(TicTacToeBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            TicTacToeBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
