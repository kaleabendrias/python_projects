import sys
import math
import random


def getNewBoard():
    board = []
    for x in range(60):  # The main list is a list of 60 lists.
        board.append([])
        for y in range(15):  # Each list in the main list has 15   single - character strings.
            # Use different characters for the ocean to make it more
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board


def drawBoard(board):
    # Draw the board data structure.
    tensDigitsLine = ' ' # Initial space for the numbers down the left

    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    print(tensDigitsLine)
    print('   '+('0123456789'*6))
    print()
    
    for row in range (15):
        if row < 10:
            extraSpace = ' '

        else:
            extraSpace = ''

            # Create the string for this row on the board.
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChests(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return 0 <= x <= 59 and 0 <= y <= 59

def makeMove(board, chests, x ,y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x)* (cx - x)+(cy - y)*(cy - y))

        if distance < smallestDistance:
            smallestDistance = distance
    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'

    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' %(smallestDistance)
        else:
            board [x][y] = 'X'
            return 'sonar did not detect anything. All treasure chests out of range.'
def enterPlayerMove(previousMoves):
    print('Where do you want to drop your next sonar device? (0-59 0-14) '
          '(or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('You already moved there')
                continue
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14')

def showInstructions():
    print('''Instructions:
     You are the captain of the Simon, a treasure-hunting ship. Your current
     mission
    Press enter to continue...''')
    input()


print('S O N A R !')
print()
print('Would you like to veiw the instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        print(' you have %s sonar devices left. %s treasure chests '
              'remaining.' %(sonarDevices, len(theChests)))
        x,y = enterPlayerMove(previousMoves)
        previousMoves.append([x,y])

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You have found a sunken treasure chest!':
                for x,y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('you have found all the sunken treasure chests! congratulations!')
            break
        sonarDevices -= 1

    if sonarDevices == 0:
        print('we \'ve run out of sonar devices! now we have to turn the '
              'ship around the head')
        print('fro home with treasure chests sti;; out there! Game Over')
        print('   The remaining chests were here:')
        for x,y in theChests:
            print('   %s, %s' %(x,y))













