import random
import tkinter
import os
bank = 1000 # global variable

def slots():
  game = 0
  betRole = 1
  bank = 1000 
  print('bank: $',bank)
  numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
  bet = int(input('bet:'))
  if bet > bank:
    print('you do not have enough money in your bank')
    game += 2
  while game <= 1:
    print('bank: $',bank)
    if betRole > 1:
      bet = int(input('bet:'))
    if bet > bank:
      print('you do not have enough money in your bank')
      game += 2
      bet = 0
    #slot values 
    A = random.choice(numbers)
    B = random.choice(numbers)
    C = random.choice(numbers)
    print('=================')
    print('-----------------')
    print('[|',A,'||',B,'||',C,'|]')
    print('-----------------')
    print('=================')
    if(A == B == C):
      if(B == 1):
        print('winnings:',bet*2.50)
        bank += bet*2.50
      
      if(B == 2):
        print('winnings:',bet*3)
        bank += bet*3
      
      if(B == 3):
        print('winnings:',bet*4)
        bank += bet*4
      
      if(B == 4):
        print('winnings:',bet*7)
        bank += bet*7
      
      if(B == 5):
        print('winnings:',bet*15)
        bank += bet*15
        print('jackpot!')
  
  
    elif (A == B):
      if(B == 1):
        print('losses:',bet*.5)
        bank -= bet*.5
      
      if(B == 2):
        print('winnings:',bet*2)
        bank += bet*2
        
      if(B == 3):
        print('winnings:',bet*2)
        bank += bet*2
      
      if(B == 4):
        print('winnings:',bet*3.5)
        bank += bet*3.5
      
      if(B == 5):
        print('winnings:',bet*7)
        bank += bet*7
      
  
    elif(B == C):
      if(B == 1):
        print('losses:',bet*.5)
        bank -= bet*.5
      
      if(B == 2):
        print('winnings:',bet*2)
        bank += bet*2
      
      if(B == 3):
        print('winnings:',bet*2)
        bank += bet*2
      
      if(B == 4):
        print('winnings:',bet*3.5)
        bank += bet*3.5
      
      if(B == 5):
        print('winnings:',bet*7)
        bank += bet*7
      
    else:
      print('losses:',bet)
      bank -= bet
    betRole += 2
    print('bank:',bank)
    game = int(input('please select one of the following: [1.continue slots] [2.end slots] :'))

def war():
  numbers = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
  numbers1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
  game = 0
  money = 1000
  while game <= 1:
    print("bank: $",money)
    bet = int(input('bet: $'))
    if bet > money:
      print("error you do not have engough money")
    else:
      computer = random.choice(numbers1)
      user = random.choice(numbers)
      if user == computer:
        print("The computer drew",computer,". You drew",user)
        print("it was a draw")
        print("bank: $",money)
      elif user > computer:
        print("The computer drew",computer,". You drew",user)
        print("you won: $",bet)
        money = money + bet
        print("bank: $",money)
      else:
        print("The computer drew",computer,". You drew",user)
        print("you loss:", bet)
        money = money - bet
        print("bank: $",money)
    game = int(input('please select one of the fallowing: [1.continue war] [2.end war] :'))
    
    


  





  



