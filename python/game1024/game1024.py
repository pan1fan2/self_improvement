# coding:utf-8

# Steps
# 1. Create a temporary matrix that consists of a list of lists 
# 2. Carry out functions that join data , which requires to reverse and transpose the list of lists
# 3. Set up the start of the game by creating an empty matrix filled with two 2s randomly
# 4. Set up the rounds of the game, where a user determines the direction of movement
# 5. Add a new value
# 6. Check if a user has won the game (reach 1024)

import numpy as np
import random
import copy

def show():
    """
    Display the result
    """
    for row in matrix:
        # each row starts with a '|'
        row_ = '|'
        # format the output based on the numbers of digit
        for num in row:
            if num == 0:
               row_ += '____|' 
            elif len(str(num)) <= 2:
                row_ +=  '_' + str(num).zfill(2) + '_' + '|'
            elif len(str(num)) == 3:
                row_ +=  str(num) + '_' + '|'
            elif len(str(num)) == 4:
                row_ +=  str(num) + '|'
        print(row_)

def moveJoinLeft(row):
    
    """
    Single row operation, move and join the number to the left 

    Args:
        row (list): one row in the matrix, a list of number
    """
    # need to operate 'matrixSize - 1' times
    for _ in range(matrixSize - 1):
        for i in range(matrixSize - 1, 0, -1):
            # check if there is an empty spot to its left, then move over
            if row[i - 1] == 0: 
                row[i - 1] = row[i]
                row[i] = 0

    # join numbers
    for i in range(matrixSize -1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    # move to its left one more time , i.g.[2,2,2,2] -> [4,0,4,0] -> [4,4,0,0]
    for i in range(matrixSize - 1, 0, -1):
            if row[i - 1] == 0: 
                row[i - 1] = row[i]
                row[i] = 0
    return row

def join_left(matrix_now):
    """
    Operate on all rows of the matrix,  move and join the number to the left 

    Args:
        matrix_now ([list]): a list of lists

    Returns:
        [list]: An updated matrix after join_left 
    """
    for i in range(matrixSize):
        matrix_now[i] = moveJoinLeft(matrix_now[i])

    return matrix_now

def reverse(row):
    """
    Reverse the numbers of a single row 

    Args:
        row ([list]): a list of numbers to represent one row in the matrix

    Returns:
        [list]: reversed row
    """
    return row[::-1]

def transpose(matrix_now):
    """
    Transpoed matrix of the current matrix

    Args:
        matrix_now ([list]): A list of lists

    Returns:
        [list]: Transpoe of the current matrix 
    """
    matrix_now_T = np.transpose(np.array(matrix_now, dtype = np.int32))
    return matrix_now_T.tolist()


def join_right(matrix_now):
    """
    Operate on all rows of the matrix,  move and join the number to the right

    Args:
        matrix_now ([list]): a list of lists

    Returns:
        [list]: An updated matrix after join_right 
    """
    for i in range(matrixSize):
        matrix_now[i] = reverse(matrix_now[i])
        matrix_now[i] = moveJoinLeft(matrix_now[i])
        matrix_now[i] = reverse(matrix_now[i])
    return matrix_now

def join_up(matrix_now):
    """
    Operate on all rows of the matrix,  move and join the number to the top

    Args:
        matrix_now ([list]): a list of lists

    Returns:
        [list]: An updated matrix after join_up
    """
    matrix_now = transpose(matrix_now)
    matrix_now = join_left(matrix_now)
    matrix_now = transpose(matrix_now)
    return matrix_now

def join_down(matrix_now):
    """
    Operate on all rows of the matrix,  move and join the number to the bottom

    Args:
        matrix_now ([list]): a list of lists

    Returns:
        [list]: An updated matrix after join_down
    """
    matrix_now = transpose(matrix_now)
    matrix_now = join_right(matrix_now)
    matrix_now = transpose(matrix_now)
    return matrix_now

def isWin():
    """
    Check if any number in the matrix is equal or greater than 1024

    Returns:
        [Boolean]: 
    """
    return np.any(np.array(matrix) >= 1024)

def addTwo():
    """
    After each move, randomly pick an empty spot and fill in the spot with number two

    """
    rowNum = random.randint(0,matrixSize - 1)
    rowNum = random.randint(0,matrixSize - 1)
    # find an empty spot within 1000 trials
    count = 0
    while not matrix[rowNum][rowNum] == 0:
        count += 1
        rowNum = random.randint(0,matrixSize - 1)
        rowNum = random.randint(0,matrixSize - 1)
        if count > 5000:
            return "Game Over"
    matrix[rowNum][rowNum] = 2

def moveAvailability():
    """
    Check if there is any available move in the matrix
    """
    cp_matrix1 = copy.deepcopy(matrix)
    cp_matrix2 = copy.deepcopy(matrix)
    cp_matrix1 = join_up(cp_matrix1)
    if cp_matrix1 == cp_matrix2:
        cp_matrix1 = join_down(cp_matrix1)
        if cp_matrix1 == cp_matrix2:
            cp_matrix1 = join_left(cp_matrix1)
            if cp_matrix1 == cp_matrix2:
                cp_matrix1 = join_right(cp_matrix1)
                if cp_matrix1 == cp_matrix2:
                    return True
    return False

if __name__ == '__main__':
    # size of of the matrix (4 * 4)
    matrixSize = 4 
    # Initialize a matrix with zeros
    matrix = [[0]*matrixSize for _ in range(matrixSize)]
    # pick up two random spots to populate with number 2
    spotNum = 2
    while spotNum > 0:
        rowNum = random.randint(0,matrixSize - 1)
        rowNum = random.randint(0,matrixSize - 1)
        if matrix[rowNum][rowNum] == 0 :
            matrix[rowNum][rowNum] = 2
            spotNum -= 1
    
    print(" Have fun with playing game 1024, try to join the numbers and get to the 1024 tiles\n")
    print(""" You can join the numbers in 4 directions, please use the keyboard and enter w to join up,a to join left, s to join down and d to join right\n""")
    # Display the initial matrix 
    show()
    # Create a flag to determin the status
    gameFlag = True
    while gameFlag:

        direction = input("What direction do you choose to join the number?")
        if direction.lower() not in ['a','d','s','w']:
            print("Wrong input, please try again and enter w to join up, a to join left, s to join down and d to join right\n")
            continue
        # Create a copy of the matrix
        matrix_cp = copy.deepcopy(matrix) 

        if direction.lower() == 'a':
            matrix = join_left(matrix)
        elif direction.lower() == 'd':
            matrix = join_right(matrix)
        elif direction.lower() == 's':
            matrix = join_down(matrix)
        else:
            matrix = join_up(matrix)

        # the updated matrix is identical to the matrix before the move, then ask to try a different direction
        if matrix == matrix_cp:
            print("Same as before, please try a new direction!")
        else:
            # check if win
            if isWin():
                show()
                print("Congradulations, you get the 1024 tile!")
                gameFlag = False
            # Add a number two to the matrix
            addTwo()
            if addTwo() == 'Game Over':
                print("Can not add a new value, game over!")
                gameFlag = False
            # display the new matrix
            show()
            # check if there is any available moves
            if moveAvailability():
                print("No more available moves, game over!")
                gameFlag = False
