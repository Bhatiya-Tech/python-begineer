#main
import random
import time
board=['1','2','3','4','5','6','7','8','9']
avail=[1,2,3,4,5,6,7,8,9]
ply_1=[]
counta=0
counte=0
comp=[]
z=0
countc=0
#input system
 
def prop1():
  global x
  x=int(input("player1 enter no for place="))
  if x in avail:
    ply_1.append(x)
    ply_1.sort()
    y=avail.remove(x)
  else:
    print("enter valid place")
    prop1()
 
#comp brain
 
def comp1():
  global x
  win=[[1,2,3],[1,4,7],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
  for i in win:
    global countc
    global zdef
    global z
    countc=0
    for j in i:
      zdef=0
      for k in ply_1:
        if k==j:
          countc+=1
        else:
          zdef+=1
        if zdef>=2:
          z=j
    if countc>=2:
      if z in avail:
        x=int(z)
        break
    else:
      x=random.choice(avail)
  comp.append(x)
  comp.sort()
  y=avail.remove(x)
  print()
#board
 
def boardlook():
  print(board[0],'|',board[1],'|',board[2])
  print('_','+','_','+','_')
  print(board[3],'|',board[4],'|',board[5])
  print('_','+','_','+','_')
  print(board[6],'|',board[7],'|',board[8])
 
#checking function
 
def check1():
  win=[[1,2,3],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[1,5,9],[3,5,7],[1,4,7]]
  for i in win:
    global counta
    counta=0
    for j in i:
      for k in ply_1:
        if j==k:
          counta+=1
    if counta>=3:
      print("player X won")
      break
 
 
def check2():
  win=[[1,2,3],[4,5,6],[7,8,9],[2,5,8],[3,6,9],[1,5,9],[3,5,7],[1,4,7]]
  for i in win:
    global counte
    counte=0
    for j in i:
      for k in comp:
        if j==k:
          counte+=1
    if counte>=3:
      print("player O won")
      break
 
#functioning 
boardlook()
turn=0
while turn<9:
  prop1()
  # here x is global for board
  board[x-1]='X'
  boardlook()
  check1()
  if counta==3:
    break
  turn+=1
  if turn==9:
    break  
  time.sleep(2)
  comp1() 
  board[x-1]='O'
  boardlook()
  check2()
  if counte==3:
   break
  turn+=1
if turn==9:
  print('tie')
