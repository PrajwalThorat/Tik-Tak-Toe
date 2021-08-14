board = [' ' for x in range(10)]

def insertletter(letter,pos):
     board[pos] = letter

def spaceIsfree(pos):
    return board[pos] == ' '


 
def printboard(board):
     print('   |   |   ')
     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
     print('   |   |   ')
     print('-------------')
     print('   |   |   ')
     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
     print('   |   |   ')
     print('-------------')
     print('   |   |   ')
     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
     print('   |   |   ')
    

def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def iswinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
           (b[4] == l and b[5] == l and b[6] == l) or
           (b[7] == l and b[8] == l and b[9] == l) or
           (b[1] == l and b[4] == l and b[7] == l) or
           (b[2] == l and b[5] == l and b[8] == l) or
           (b[3] == l and b[6] == l and b[9] == l) or
           (b[1] == l and b[5] == l and b[9] == l) or
           (b[3] == l and b[5] == l and b[7] == l))
           
           
def playermove():
    run = True
    while run:
        move = input("please select the poosition to enter the X in between 0 to 9 :")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsfree(move):
                    run = False
                    insertletter('X' , move)
                else:
                    print("sorry! , the space os occupied")
            else:
                print('please type the number netween 1 to 9 ')
        except:
            print('please type a number ')


                    
def computermove():
    possiblemove = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O' , 'X']:
        for i in possiblemove:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(boardcopy , let):
                move = i
                return move 
            


    corneropen = []
    for i in possiblemove:
         if i in [1 , 3 , 7 , 9]:
              corneropen.append(i)

    if len(corneropen) > 0:
         move = selectRandom(corneropen)
         return move

    if 5 in possiblemove:
         move = 5
         return move


    edgeopen = []
    for i in possiblemove:
         if i in [2 , 4 , 6 , 8]: 
              edgeopen.append(i)

    if len(edgeopen) > 0:
         move = selectRamdom(edgeopen)
         return move

def selectRandom(li):
     import random
     ln = len(li)
     r = random.randrange(0,ln)
     return li[r]



def main():
     print("Welcome to the game !")
     printboard(board)


     while not(isboardfull(board)):
          if not(iswinner(board , 'O')):
               playermove()
               printboard(board)
          else:
               print("sorry , you loose!")
               break

          if not(iswinner(board , 'X')):
               move = computermove()
               if move == 0:
                    print("tie game!")
               else:
                    insertletter('O' , move)
                    print('compuetr placed an o on position ', move ,':')
                    printboard(board)
          else:
               print("You win !")
               break
     

     if isboardfull(board):
          print("Tie game")





while True:
     x = input("Do you want play TicTacToe game ? (y/n) :")
     if x.lower() == 'y':
          board = [' ' for x in range(10)]
          print('----------------------')
          main()
     else:
          break






