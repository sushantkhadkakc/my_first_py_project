b_sc=0
a_sc=0
import random
print("Dragon, Knight, Wizard game\n")
while True:
  
  print("please choice one of three\n")
  a=input("enter choice of player 1\n")
  v=["dragon","knight","wizard"]
  b=random.choice(v) 
  print(f"compter choices {b}")
  if a=="quit":
    print(f"thank for playing : ps:{a_sc} cs:{b_sc}")
    break
  if a == "dragon" and b == "wizard":
        a_sc += 1
        print("Dragon roasts Wizard")
  elif a == "wizard" and b == "knight":
        a_sc += 1
        print("Wizard charms Knight")
  elif a == "knight" and b == "dragon":
        a_sc += 1
        print("Knight defeats Dragon")
  elif a == "wizard" and b == "dragon":
        b_sc += 1
        print("Dragon roasts Wizard")
  elif a == "knight" and b == "wizard":
        b_sc += 1
        print("Wizard charms Knight")
  elif a == "dragon" and b == "knight":
    b_sc += 1
    print("Knight defeats Dragon")
  elif a == b:
        print("draw")
  else:
        print("something is wrong")
        print(f"sorce of player:{a_sc} and com:{b_sc}")
    
        
  
 