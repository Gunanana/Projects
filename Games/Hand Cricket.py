print("\n\nWelcome to hand cricket.\n")
print("Rules are simple.")
print("You get to play the game exactly like a normal hand cricket but with plays between 1 and 6 only.\n")
print("Try entering only the expected values.")
print("Well I have tried my best at making this code a fool proof to any circumstance even remotely possible and hence the bloat.")
print("So lets see if you can break it.\n")
print("I am open to any suggestions on the script plus on making it more interactive with the users.")
print("Well if its about using functions, then yes, i did try using it but i had to 'break' and 'return' values simultaneously (in toss evaluation block) which was not possible. Hence i removed it entirely.")
print("\nWith that out of the way, lets get started then :)\n")

playagain='y'
while playagain=="y":
#toss begins
  import random
  while True:

#odd or even block
    oe=input("\n\nOdd or Even? [odd/even]: ") 
    oe=oe.lower()
    if oe not in ["odd","even"]:
      print("\nSpelling error. Enter odd or even (case independent)\n")
      continue

#toss number block
    try:
      un=int(input("Enter your number (1 to 6): "))
    except:
      print("\nUnexpected value. Try entering Integer value only\n")
      continue
    if un not in range(1,7):
      print("\nEnter numbers between 1 and 6 only\n")
      continue
    cn=random.randint(1,6)
    print(f'The Computer chose {cn}\n')

#toss evaluation block 
    s=2  
    if oe=="even":
      if (un+cn)%2==0:
        print("You won the toss!")  
        s=1
        break
      else:
        print("You lost the toss!")
        s=0
        break
    elif oe=="odd":
      if (un+cn)%2==0:
        print("You lost the toss!")
        s=0
        break
      else:
        print("You won the toss!") 
        s=1
        break
  
#bat or bowl block
  uchoice=0
  cchoice=0
  if s==1:
    while True:
      uchoice=input("What do you choose? [bat/bowl]: ")
      uchoice=uchoice.lower()
      if uchoice in ["bat","bowl"]:
        break
      else:
        print("\nSpelling error (case independent),try again \n")
        continue
  elif s==0:
    cchoice=random.choice(["bat","bowl"])
    print(f"And the Computer chose to {cchoice}\n")
#toss ends

#play begins 
  
  uplay=0
  score=0
  cplay=0
  target=0

#player won
  if s==1:
#player chose to bat
    if uchoice=='bat':
      score=0
      target=0
      print("\nFirst innings begin:")
      print("You are batting first!!\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nYou are out!!")
            break
          else:
            score=score+uplay
            print("Your score: ",score)
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue

#computer chasing    
      target=score+1
      score=0
      print(f"\nYour score is {target-1} hence Computer's target is {target}. Good luck defending it\n")
      print("Second innings begin:\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nComputer is out!\n")
            if score==target:
              print("The game ended in a draw!!")
              break
            else:
              print(f"You won by {target-score} runs")
              break
          else:
            score=score+cplay
          if score>=target:
            print("\nComputer won!!\n")
            break
          elif score<target:
            print(f"Computer's score is {score}.\nIt needs {target-score} more runs to win!")
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue


#player chose to bowl
    
    elif uchoice=="bowl":
      score=0
      target=0
      print("\nFirst innings begin:")
      print("The Computer bats first\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nComputer is out!\n")
            break
          else:
            score=score+cplay
            print(f"Computer's score is {score}")
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue

#player chases
      target=score+1
      score=0
      print("Second innings begin:")
      print(f"Your target is {target}")
      while True:
          try:
            uplay=int(input("\nYour play [1 to 6]: "))
            if uplay not in range(1,7):
              print("\nEnter numbers between 1 and 6 only\n")
              continue
            cplay=random.randint(1,6)
            print("The Computer played ",cplay)
            if uplay==cplay:
              print("\nYou are out!")
              if score==target:
                print("The game ended in a draw!!")
                break
              else:
                print(f"Computer won by {target-score} runs")
                break
            else:
              score=score+uplay
            if target<=score:
              print("\nYou won!!\n")
              break
            elif score<target:
              print(f"Your score is {score}.\nYou need {target-score} more runs to win!")
              continue
            
          except:
            print("\nUnexpected value. Try entering Integer value only\n")
            continue

#player loses toss
  elif s==0:

#computer chose to bat
    score=0
    target=0
    if cchoice=="bat":
      print("\nFirst innings begin:")
      print("The Computer bats first\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nComputer is out!\n")
            break
          else:
            score=score+cplay
            print(f"Computer's score is {score}")
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue

#player chases
      target=score+1
      score=0
      print("Second innings begin:")
      print(f"Your target is {target}")
      while True:
          try:
            uplay=int(input("\nYour play [1 to 6]: "))
            if uplay not in range(1,7):
              print("\nEnter numbers between 1 and 6 only\n")
              continue
            cplay=random.randint(1,6)
            print("The Computer played ",cplay)
            if uplay==cplay:
              print("\nYou are out!")
              if score==target:
                print("The game ended in a draw!!")
                break
              else:
                print(f"Computer won by {target-score} runs")
                break
            else:
              score=score+uplay
            if target<=score:
              print("\nYou won!!\n")
              break
            elif score<target:
              print(f"Your score is {score}.\nYou need {target-score} more runs to win!")
              continue
          except:
            print("\nUnexpected value. Try entering Integer value only\n")
            continue

#computer chose to bowl
    elif cchoice=='bowl':
      score=0
      target=0
      print("\nFirst innings begin:")
      print("You are batting first!!\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nYou are out!!\n")
            break
          else:
            score=score+uplay
            print("Your score: ",score)
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue

#computer chases
      target=score+1
      score=0
      print(f"\nYour score is {target-1} hence Computer's target is {target}. Good luck defending it\n")
      print("Second innings begin:\n")
      while True:
        try:
          uplay=int(input("\nYour play [1 to 6]: "))
          if uplay not in range(1,7):
            print("\nEnter numbers between 1 and 6 only\n")
            continue
          cplay=random.randint(1,6)
          print("The Computer played ",cplay)
          if uplay==cplay:
            print("\nComputer is out!")
            if score==target:
              print("The game ended in a draw!!")
              break
            else:
              print(f"You won by {target-score} runs")
              break
          else:
            score=score+cplay
          if target<=score:
            print("\nComputer won!!\n")
            break
          elif score<target:
            print(f"Computer's score is {score}.\nIt needs {target-score} more runs to win!")
            continue
        except:
          print("\nUnexpected value. Try entering Integer value only\n")
          continue
#play again?
  while True:
    playagain=input("\nDo you wanna play again?[Y/N]")
    playagain=playagain.lower()
    if playagain not in ['y','n']:
      print("Unexpected input. Enter 'Y' or 'N' only")
      continue
    else:
      break