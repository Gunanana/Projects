#tell me how it goes~ Guna
print("Let's play a number counting game shall we??\n\n")
print("Okay so the game goes like this\n1. We both count numbers till 21 turn wise\n2. Whoever reaches 21 first, loses (hope its not me XD)\n3. We both get to say maximum of 3 numbers at a time but, in order from 1 to 21(ex:1 or 345 or 56)\n4. You would start from number 9 if i end my turn with 8\n\n ")
print("Now as for the format of YOUR input:\n1. Don't give any space or comma and type the numbers  together \n2. Dont't type any other numbers other than in your turn range (the program wont work otherwise ><)\n3. Thats all!! Let's get started!!\n\n")

while (1):
  x=int(input('\n\nEnter your number (remember to start with 1!) :) '))

  if x==1:
    y=int(input('\nMy numbers are 2,3,4\nNow your turn :) '))
  if x==12:
    y=int(input('\nMy numbers are 3,4\nNow your turn :) '))
  if x==123:
    y=int(input('\nMy number is 4\nNow your turn :) '))
  #else:
    #print('\nWhoops!! The number you have entered violates a rule. Please read the format of your input again\nAlso compile the program again to start from first :)')
    #quit(print('recompile'))

  if y==5:
    z=int(input('\nMy numbers are 6,7,8\nNow your turn :) '))
  if y==56:
    z=int(input('\nMy numbers are 7,8\nNow your turn :) '))
  if y==567:
    z=int(input('\nMy number is 8\nNow your turn :) '))
  #else:
    #print('\nWhoops!! The number you have entered violates a rule. Please read the format of your input again\nAlso compile the program again to start from first :)')
  
  if z==9:
    q=int(input('\nMy numbers are 10,11,12\nNow your turn :) '))
  if z==910:
    q=int(input('\nMy numbers are 11,12\nNow your turn :) '))
  if z==91011:
    q=int(input('\nMy number is 12\nNow your turn :) '))
  #else:
    #print('\nWhoops!! The number you have entered violates a rule. Please read the format of your input again\nAlso compile the program again to start from first :)')

  if q==13:
    h=int(input('\nMy numbers are 14,15,16\nNow your turn :) '))
  if q==1314:
    h=int(input('\nMy numbers are 15,16\nNow your turn :) '))
  if q==131415:
   h=int(input('\nMy number is 16\nNow your turn :) '))
  #else:
    #print('\nWhoops!! The number you have entered violates a rule. Please read the format of your input again\nAlso compile the program again to start from first :)')

  if h==17:
    t=int(input('\nMy numbers are 18,19,20\nNow your turn XD '))
  if h==1718:
    t=int(input('\nMy numbers are 19,20\nNow your turn XD '))
  if h==171819:
    t=int(input('\nMy number is 20\nNow your turn XD '))
  #else:
    #print('\nWhoops!! The number you have entered violates a rule. Please read the format of your input again\nAlso compile the program again to start from first :)')

  print('\nYou fell on 21! You LOSE XD!!\nBetter luck next time :D')
  r=input('\nDo you wanna play again?(Y/N): ')
  r=r.lower()
  if r=='n':
    break
