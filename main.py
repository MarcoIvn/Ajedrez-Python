#CapstoneProject.py
#07/10/2021
#A program that generate a valid chess board with a white king, a white queen, and the black king. The program will evaluate the possible movements for black king depending on the positions of the white queen and the black king, and show them, and then evaluate if black king is or not in check and checkmate, and show it. 
#Marco Ivan Pacheco Martinez
#Manuel Luciano Reyes Constantino

import random

def createBoard(): #Function to create the board
  board =[]
  shape = "@"
  for row in range(8):    #A for cicle to create rows and
    r =[]                 
    for col in range(8):  #another for cicle inside for columns
      r.append(shape)
      if col < 7:
        if shape == "@":
          shape ="#"
        else:
          shape ="@"
    board.append(r)
  return board

def printBoard(b): #Function that shows the board on the screen
  for r in range(8):
    for c in range(8):
      print(b[r][c], end=" ")
    print()

def find(piece,b): #Function to find the coordinates of a piece in the board, and returning them in a list
  cor =[]
  for r in range(8):
    for c in range(8):
      if b[r][c]==piece:
        cor.append(r)
        cor.append(c)
        return cor
  return None

def placek(b):               #Function to place the black king in the board
  rk = random.randint(0,7)
  rc = random.randint(0,7)
  b[rk][rc] = "k"

def placeK(b):                #Function to place the white king in the board
  bk = find("k",b)
  rk = bk[0]
  ck = bk[1]
  com = 0
  while com == 0:             #Com variable is to start the while cicle and keep having the same value if the condition evaluated is True 
    rK = random.randint(0,7)
    cK = random.randint(0,7)  
    if rk == rK and ck == cK: #If condition to evaluate if the postiions generated for white king are the same as the positions of 
      com = 0                 #the black king
    else:
      b[rK][cK] = "K"
      break

def placeQ(b):              #Function that places the queen on the board 
  bk = find("k",b)
  wk = find("K",b) 
  rk = bk[0]
  ck = bk[1]
  rK = wk[0]
  cK = wk[1]
  com = 0
  while com == 0:                 #Com variable is to start the while cicle and keep having the same value if the condition evaluated  is True
    rQ= random.randint(0,7)
    cQ= random.randint(0,7)
    if (rk == rQ and ck == cQ) or (rK == cQ and cK == cQ):  #If condintion to evaluate if the positions generated for queen are the same
      com = 0                                               #as the positions of the black king
    else:
      b[rQ][cQ] = "Q"
      break

def findPosition(piece,b):      #Function to find the posible movementes for black king or white king in the board
  posp = find(piece,b)
  r= posp[0]
  c= posp[1]
  neighbors=[[r,c+1],[r-1,c+1],[r-1,c],[r-1,c-1],[r,c-1],[r+1,c-1],[r+1,c],[r+1,c+1]]
  positions= []
  for i in neighbors:
    if (i[0] >= 0 and i[0] <= 7) and (i[1] >= 0 and i[1] <= 7):  
      positions.append(i)
  return positions

def findPositionsQ(b):          #Function to find the posible movements for queen in the board (Taking into consideration the position of black king and the white king)
  Qpos= find("Q",b)
  rQ = Qpos[0]
  cQ = Qpos[1]
  Qpositions = []

  #For Right
  for c in range(8): #This for cycle moves one block to the right
    cQ = cQ + 1
    if cQ > 7:
      break
    elif b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For up
  rQ = Qpos[0] 
  cQ = Qpos[1]
  for c in range(8): #This for cycle moves one block up
    rQ = rQ - 1
    if rQ < 0:
      break
    elif b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For left
  rQ = Qpos[0]
  cQ = Qpos[1]
  for c in range(8): #This for cycle moves one block to the left 
    cQ = cQ - 1
    if cQ < 0:
      break
    elif b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For down
  rQ = Qpos[0]
  cQ = Qpos[1]
  for c in range(8): #This for cycle moves one block down 
    rQ = rQ + 1
    if rQ > 7:
      break
    elif b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #While cycle up-right diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ > 0 and cQ < 7: #This while cycle moves diagonally one block up and one block to the right 
    rQ = rQ - 1
    cQ = cQ + 1 
    if b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)
    
  #While cycle up-left diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ > 0 and cQ > 0: #This while cycle moves diagonally one block up and one block to the left
    rQ = rQ - 1
    cQ = cQ - 1 
    if b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #While cycle down-left diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ < 7 and cQ > 0: #This while cycle moves diagonally one block down and one block to the left
    rQ = rQ + 1
    cQ = cQ - 1 
    if b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #While cycle down-right diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ < 7 and cQ < 7: #This while cycle moves diagonally one block down and one block to the right
    rQ = rQ + 1
    cQ = cQ + 1 
    if b[rQ][cQ] == "k" or b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)
  return Qpositions
########################################

def findUpositionsQ(b):       #Function to find the posible movements for queen in the board (Taking into consideration only the position of white king)
  Qpos= find("Q",b)
  rQ = Qpos[0]
  cQ = Qpos[1]
  Qpositions = []

  #For Right
  for c in range(8): #This for cycle moves one block to the right
    cQ = cQ + 1
    if cQ > 7:
      break
    elif b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For up
  rQ = Qpos[0]
  cQ = Qpos[1]
  for c in range(8): #This for cycle moves one block up
    rQ = rQ - 1
    if rQ < 0:
      break
    elif b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For left
  rQ = Qpos[0]
  cQ = Qpos[1]
  for c in range(8): #This for cycle moves one block to the left
    cQ = cQ - 1
    if cQ < 0:
      break
    elif b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #For down
  rQ = Qpos[0]
  cQ = Qpos[1]
  for c in range(8): #Thus for cycle moves one block down
    rQ = rQ + 1
    if rQ > 7:
      break
    elif b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    else:
      n = [rQ,cQ]
      Qpositions.append(n)

  #While cycle up-right diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ > 0 and cQ < 7: #This while cycle moves one block up and one block to the right
    rQ = rQ - 1
    cQ = cQ + 1 
    if b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    n = [rQ,cQ]
    Qpositions.append(n)
    
  #While cycle up-left diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ > 0 and cQ > 0: #This while cycle moves one block up and one block to the left
    rQ = rQ - 1
    cQ = cQ - 1 
    if b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    n = [rQ,cQ]
    Qpositions.append(n)

  #While cycle down-left diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ < 7 and cQ > 0: #This while cycle moves one block down and one block to the left
    rQ = rQ + 1
    cQ = cQ - 1
    if b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break 
    n = [rQ,cQ]
    Qpositions.append(n)

  #While cycle down-right diagonal
  rQ = Qpos[0]
  cQ = Qpos[1]
  while rQ < 7 and cQ < 7: #This while cycle moves one block down and one block to the right
    rQ = rQ + 1
    cQ = cQ + 1 
    if b[rQ][cQ] == "K":
      n = [rQ,cQ]
      Qpositions.append(n)
      break
    n = [rQ,cQ]
    Qpositions.append(n)
  return Qpositions

########################################

def findpositionsk(b):          #Function that finds the possible movementes of the black king taking into consideration the positions of the white king and the white queen
  kpos = findPosition("k",b)
  Kpos = findPosition("K",b)
  Qpos = findUpositionsQ(b)
  fpositions = kpos
  for n in Kpos:
    if n in kpos:
      fpositions.remove(n)
  for l in Qpos:
    if l in kpos:
      fpositions.remove(l)
  return fpositions

def checkCheck(b):              #Function that evaluates if the black king in the board is in check
  Qpos = findPositionsQ(b)
  Kpos = findPosition("K",b)
  #Check for White King
  for i in Kpos:
    ri=i[0]
    ci=i[1]
    if b[ri][ci] == "k":
      check = True
      break
    else:
      check = False
  #Check for White Queen
  if check == False:
    for l in Qpos:
      rl=l[0]
      cl=l[1]
      if b[rl][cl] == "k":
        check = True
        break
      else:
        check = False
  return check

def checkCheckmate(b):        #Function that evaluates if the black king in the board is in checkmate
  kposi = findpositionsk(b)
  check = checkCheck(b)
  if kposi == []:
    if check == False:
      return False
    else:  
      return True
  else:
    return False
######################################
choice= int(input("Enter your choice: "))

if choice == 1:
  board = createBoard()
  placek(board)
  placeK(board)
  placeQ(board)
else:
  board=[]
  for r in range(8): 
    line= input("Enter line of your board: ")
    line = line.strip()
    row = line.split(" ")
    board.append(row)
print()
printBoard(board)
print()

kpositions = findpositionsk(board)
print("Black king moves:",kpositions)

check = checkCheck(board)
print("Check:",check)

checkmate = checkCheckmate(board)
print("Checkmate:",checkmate)

