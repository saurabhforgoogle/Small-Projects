def printgame(matrix):
    print('  {}  |  {}  |  {}  \n--------------------\n  {}  |  {}  |  {}  \n--------------------\n  {}  |  {}  |  {}  '
    .format(matrix[0][0],matrix[0][1],matrix[0][2],matrix[1][0],matrix[1][1],matrix[1][2],matrix[2][0],matrix[2][1],matrix[2][2]))

    if matrix[0][0]==matrix[0][1] and matrix[0][1]==matrix[0][2]:
        return 1
    elif matrix[1][0]==matrix[1][1] and matrix[1][1]==matrix[1][2]:
        return 1
    elif matrix[2][0]==matrix[2][1] and matrix[2][1]==matrix[2][2]:
        return 1
    elif matrix[0][0]==matrix[1][0] and matrix[1][0]==matrix[2][0]:
        return 1
    elif matrix[0][1]==matrix[1][1] and matrix[1][1]==matrix[2][1]:
        return 1
    elif matrix[0][2]==matrix[1][2] and matrix[1][2]==matrix[2][2]:
        return 1
    elif matrix[0][0]==matrix[1][1] and matrix[1][1]==matrix[2][2]:
        return 1
    elif matrix[0][2]==matrix[1][1] and matrix[1][1]==matrix[2][0]:
        return 1
    else:
        return 0

import random
print('*******TIC*******TAC*******TOE*******\n')
turn=random.randint(0,1)
result=0
data=[[0,1,2],[3,4,5],[6,7,8]]
result=printgame(data)
times=1
while(result==0 and times<=9):
    if turn==0:
        print('\nTurn: O\n\t')
    else:
        print('\nTurn: X\n\t')
    print('Enter Desired Number from Choices')
    try:
        value=int(input())
    except ValueError:
        value=10
    temp=1
    for i in range(3):
        for j in range(3):
            if data[i][j]==value and turn==0:
                data[i][j]='O'
                temp=0
                break
            elif data[i][j]==value and turn==1:
                data[i][j]='X'
                temp=0
                break
            else:
                temp=1
        if temp==0:
            break
    result=printgame(data)
    if result==1:
        if turn==0:
            print('O Won|O Won|O Won')
        elif turn==1:
            print('X Won|X Won|X Won')
    
    if temp==1:
        print('Not Possible! Try Again.')
    else:
        turn=1-turn
        times+=1
if times==10:
    print('MATCH DRAWN')
    
