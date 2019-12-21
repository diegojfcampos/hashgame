#HASH GAME

"Globals"

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
position = 0
game = True
player = 1


"""IMPORT´s"""


"""Def's"""

def DesignBoard(tabuleiro):
    print("  GAME BOARD  ")
    tab = ""
    for i in range(0, 9):
        mark = " "
        if board[i] == 1:
            mark = "X"
        elif board[i] == -1:
            mark = "0"
        tab += " | " + mark

        if i == 2 or i == 5 or i == 8:
            print(tab + " | ")
            tab = ""
    print("---------------")

def Restart(restart):
    global board
    global position
    global game
    global player

    board[0:9] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    position = 0
    game = True
    player = 1
    print(f"===============\n GAME RESTARTED\n===============")
    DesignBoard(board)

def Test(test):
    test1 = board[0] + board[1] + board[2]
    test2 = board[3] + board[4] + board[5]
    test3 = board[6] + board[7] + board[8]
    test4 = board[0] + board[4] + board[8]
    test5 = board[2] + board[4] + board[6]
    test6 = board[0] + board[3] + board[6]
    test7 = board[1] + board[4] + board[7]
    test8 = board[2] + board[5] + board[8]

    if test1 == 3 or test2 == 3 or test3 == 3 or test4 == 3 or test5 == 3 or test6 == 3 or test7 == 3 or test8 == 3:
        print("PLAYER 1 WIN")
        ScoreBoard(1)
        Restart(board)




    elif test1 == -3 or test2 == -3 or test3 == -3 or test4 == -3 or test5 == -3 or test6 == -3 or test7 == -3 or test8 == -3:
        print("PLAYER 2 WIN")
        ScoreBoard(2)
        Restart(board)




def Drawn(drawn):
    test1 = board[0] + board[1] + board[2]
    test2 = board[3] + board[4] + board[5]
    test3 = board[6] + board[7] + board[8]
    test4 = board[0] + board[4] + board[8]
    test5 = board[2] + board[4] + board[6]
    test6 = board[0] + board[3] + board[6]
    test7 = board[1] + board[4] + board[7]
    test8 = board[2] + board[5] + board[8]
    if test1 != 0 and test1 > -3 and test1 < 3:
        if test2 != 0 and test2 > -3 and test2 < 3:
            if test3 != 0 and test3 > -3 and test3 < 3:
                if test4 != 0 and test4 > -3 and test4 < 3:
                    if test5 != 0 and test5 > -3 and test5 < 3:
                        if test6 != 0 and test6 > -3 and test6 < 3:
                            if test7 != 0 and test7 > -3 and test7 < 3:
                                if test8 != 0 and test8 > -3 and test8 < 3:
                                    print("     DRAWN     ")
                                    ScoreBoard(3)
                                    Restart(board)





def ScoreBoard(scoreboard):
    player1 = []
    player2 = []
    drawn = []
    if scoreboard == 3:
        drawn.extend('3')
    else:
        if scoreboard == 1:
            player1.extend('1')
        else:
            player2.extend('2')
    print(f"SCOREBOARD\n\nPLAYER 1: {len(player1)}\nPlAYER 2: {len(player2)}\nDRAWN: {len(drawn)}")


#JOGO

while game == True:
        Test(board)
        if player == 1:
            print("PLAYER 1")
        else:
            print("PLAYER 2")
        position = int(input("Choose Position 0 to 8: "))
        if position < 0 or position > 8:
            print("Invalid Position, type: 1 to 8.")
        elif board[position] == 1 or board[position] == -1:
            print("Unavailable Position, try another position: 0 to 8.")
        else:
            if player == 1 and board[position] == 0:
                board[position] = 1
                DesignBoard(board)
                player = -1
                Test(board)
                Drawn(board)

            if player == -1 and board[position] == 0:
                board[position] = -1
                DesignBoard(board)
                player = 1
                Test(board)
                Drawn(board)