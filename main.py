import random 

def gameWin(comp,you):  #gamefuntion 
    if comp==you:
        return None
    elif comp=='s':
      if you=='w':
          return False
      elif you=='g':
          return True
    elif comp=='w':
      if you=='s':
          return True
      elif you=='g':
          return False
    elif comp=='g':
      if you=='s':
          return False
      elif you=='w':
          return True

print("Comp turn: Snake(s) Water(w) or Gun(g)?")
randno=random.randint(1,3)

if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("your Turn: Snake(s) Water(w) Gun(g)?")
a=gameWin(comp,you) 

print(f"Computer choose {comp}")
print(f"you choose {you}")
if a==None:
    print("The game is tie")
elif a:
    print("Hurray! you win")
else:
    print("you lose!")