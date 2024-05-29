#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:15:21 2024
@author: SuperElephant
"""

def set_up_game():
    '''set_up_game() -> (list, list)
    returns a list of players' names and a list
    of whether the player is a computer'''

    playerList = []  # initialize list of players
    print('Let\'s start the game! (two player mode and player X starts)')
    name1 = input("Player X, enter your name: ")
    playerList.append(name1)
    name2 = input("Player O, enter your name: ")
    playerList.append(name2)
    return playerList

def winner_list(row_size, column_size):
    '''is_winner() -> None
    determine if there is a winner
    '''
    winnerList = []
    
    #... horizontal
    for row in range(row_size):
        for column in range(column_size - 3):
            winnerList.append([[row, column], [row, column + 1], [row, column + 2], [row, column + 3]])
    
    #... vertical
    for row in range(row_size - 3):
        for column in range(column_size):
            winnerList.append([[row, column], [row + 1, column], [row + 2, column], [row + 3, column]])
    
    #... right diagonal
    for row in range(3, row_size):
        for column in range(column_size - 3):
            winnerList.append([[row, column], [row - 1, column + 1], [row - 2, column + 2], [row - 3, column + 3]])

    #... left diagonal
    for row in range(row_size - 3):
        for column in range(column_size - 3):
            winnerList.append([[row, column], [row + 1, column + 1], [row + 2, column + 2], [row + 3, column + 3]])
 
    return winnerList

def print_board(dotList, xList, oList, row_size, column_size):
    '''
    print_board() -> None
    print a Connect Four board in the standard size, 
    i.e., 7 columns numbered from left to right and 6 rows from top to bottom
    . -> empty posiiton
    X -> player 1
    O -> player 2
    '''
    print('\n' + "This is the board right now!")
    
    #... first line of 
    for column in range(column_size):
        hcolumn = column + 1    #... add one to the column for humans
        if column == column_size - 1:
            print(hcolumn)
        else:
            print(hcolumn, end=' ')
    
    #... other lines based on oList and xList
    for row in range(row_size):
        for column in range(column_size):
            checkerPos = [row, column]
            if column == column_size - 1:
                if checkerPos in xList:
                    print('X')
                elif checkerPos in oList:
                    print('O')
                else:
                    print('.')
            else:
                if checkerPos in xList:
                    print('X', end=' ')
                elif checkerPos in oList:
                    print('O', end=' ')
                else:
                    print('.', end=' ')


#... check if there is a winner
def is_winner(playerList, winList):
    #... loop over all items in the winner_list
    for item in winList:
        checkerMatch = 0
        #... loop over all checkers in each item which has four checkers
        for checker in item:
            if checker in playerList:
                checkerMatch += 1
        #... four checkers are in the playerList, win!
        if checkerMatch == 4:    
            return True

    return False


#... This is the main program
def play_ConnectFour(row_size, column_size):
    '''
    play_ConnectFour() -> int, int
    plays a game of Connect Four
    '''
    
    playerList = set_up_game()    #... get players' names
    winList = winner_list(row_size, column_size)    #... create the winner list
    
    winner = False
    
    dotList = []    #... set up dotList to store the postions of the dots
    xList = []    #... set up xList to store the postions of the X's
    oList = []    #... set up oList to store the postions of the O's
    
    #... initialize the board with all dots
    for row in range(row_size):
        for column in range(column_size):
            dotList.append([row, column])
    print_board(dotList, xList, oList, row_size, column_size)
    
    turns = 0    #... track the number of plays

    while not winner:    #... take a turn
        
        #... check if take turns from one player to the other
        nextPlayer = False
        
        #... Player X
        if turns % 2 == 0:
            print('\n' + playerList[0] + ", your're X. Now is your turn!")
        #... Player O
        if turns % 2 == 1:
            print('\n' + playerList[1] + ", your're O. Now is your turn!")
        
        #... the column has to be [1,7]
        choice = int(input("Pick a column between 1 to " + str(column_size) + " to go: ")) - 1
        while choice > column_size - 1 or choice < 0:   
            choice = int(input("Warning: The column has to be between 1 to " + str(column_size) + ": ")) - 1
            
        #... determine position for the current checker based on player's choice
        currentPos = []
        for row in range(row_size):
            currentRow = row_size - 1 - row    #... get row from bottom to top
            currentPos = [currentRow, choice]
            
            if currentPos in dotList:    #... the pick is available
                dotList.remove(currentPos)    #... remove the pick from dotList
                if turns % 2 == 0:
                    xList.append(currentPos)    #... add the pick into xList
                if turns % 2 == 1:
                    oList.append(currentPos)    #... add the pick into oList
                
                turns += 1    #... take turns only when the checker is placed
                nextPlayer = True

                break    #... break when player place the checker
            
            else:    #... the pick is not available, move to the position above it
                if row == row_size - 1:    #... when the top position is filled
                    print("Warning: The position is not available! Pick again.")

        if nextPlayer == True:
            
            #... check win for playerX
            if turns % 2 == 1:
                if is_winner(xList, winList) == True:
                    winner = True
                    print("\nCongrats, " + playerList[0] + " (player X)" + ", you won!" )
                    
            #... check win for playerO
            if turns % 2 == 0:
                if is_winner(oList, winList) == True:
                    winner = True
                    print("\nCongrats, " + playerList[1] + " (player O)" + ", you won!" )
                    
            if (winner == False):
                print_board(dotList, xList, oList, row_size, column_size)

#... set up the size for the game board (standard size is 6 * 7)
row_size = 6
column_size = 7

#... start to play
play_ConnectFour(row_size, column_size)















    
