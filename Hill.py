import math
import numpy as np
import random


def input_board(board):
    for row in range(4):
        for column in range(4):
            board[row][column]=int(input())
    return board

def calculate_cost(queens):
    return (math.factorial(queens))/(2*math.factorial(queens-2))

def heuristic_cost(tboard):
    h_cost=0
    #Traverse Row
    for row in range(len(tboard)):
        queens=0

        for col in range(len(tboard)):
            if tboard[row][col]==1:
                queens+=1

        if queens>1:
            h_cost+=calculate_cost(queens)


    # Traverse Column

    for col in range(len(tboard)):
        queens=0
        for row in range(len(tboard)):
            if tboard[row][col]==1:
                queens+=1

        if queens>1:
            h_cost+=calculate_cost(queens)

    
    # Traverse Diagonals South-West to North-East

    for i in range(1,len(tboard)):
        row = i
        queens = 0
        for j in range(i+1):
            if tboard[row][j]==1:
                queens+=1
            row-=1

        if queens>1:
            h_cost+=calculate_cost(queens)

    for i in range(len(tboard)):
        row = 3
        queens=0
        for j in range(i,4-i):
            if tboard[row][j]==1:
                queens+=1
            row-=1

        if queens>1:
            h_cost+=calculate_cost(queens)

    # Traverse Diagonals South-East to North-West

    for i in range(2,-1,-1):
        row = i
        queens=0
        for j in range(4-i):
            if tboard[row][j]==1:
                queens+=1
            row+=1

        if queens>1:
            h_cost+=calculate_cost(queens)

    for i in range(len(tboard)):
        row = 0
        queens=0
        for j in range(i, 4-i):
            if tboard[row][j]==1:
                queens+=1
            row+=1
        if queens>1:
            h_cost+=calculate_cost(queens)


    return h_cost

def hill_climb(board,prev_cost):
    # We jump up and down in the column only
    # For a single queen, we check if the jump up or down is lowest hcost
    # if for that particular move h cost is minimum we take the jump

    # Row is constant, only column changes
    moves=[]
    for col in range(len(board)):
        found=False
        options=[0,1,2,3]
        for row in range(len(board)):
            print(row,col)
            if board[row][col]==1:
                options.remove(row)
                found=True
                break
        print(found)
        
        if found:
            temp_board=board.copy()
            for i in range(3):
                choice=random.choice(options)
                options.remove(choice)
                temp_board[row][col]=0
                temp_board[choice][col]=1

                new_cost=heuristic_cost(temp_board)
                print(new_cost)
                if prev_cost>=new_cost:
                    prev_cost=new_cost
                    print(prev_cost)

                    moves=moves+[row,col,choice,col]

        if moves:
            board[moves[0]][moves[1]]=0
            board[moves[2]][moves[3]]=1
            print(board)
            moves.clear()

    return board,prev_cost



if __name__=="__main__":
    board = np.zeros((4,4))
    board=input_board(board)
    cost=heuristic_cost(board)
    print("Cost of the Board is",cost)
    print("Let us See")
    iterations=0
    while (iterations!=10 and cost!=0):
        new_board, cost = hill_climb(board,cost)
        print("Board No:",iterations,"Cost:",cost)
        print()
        print(new_board)
        iterations+=1





















            


        





            




