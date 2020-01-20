# Type your Final Code here
from random import randint
# Print Introduction For Game
print('This Is Intro:\n  Guessing Game, You Pick a Number,\n    We Check If It Is Correct,\n      Numbers Between 1:100.')
# Guess Random Number
rand_num = randint(1, 100)
print(rand_num)
# Creating List For Guesses and Put One Value So Length Will Be One 
lifes_list = [0]

# Type here the Big Loop
while True:
      # Taking Random Number From User.
      gues_num = int(input('Choose Your Random Number: '))
      # Check If Number Between (1 and 100)
      # If (No : Going To Else And Tell User To Guess Between 1:100)
      # If (Yes) Adding Guess To Guesses List.
      if 1 <= gues_num < 100:
            # Adding Guess To Guesses List.
            lifes_list.append(gues_num)
            # Check If Guessd Number Equal Random Number Or Not.
            # If (Yes.) Go TO Else And Tell User You Got Right Guess Also Tell Him How Many Guesses He Did (Guesses List Length)
            # If (No.) Enter If
            if gues_num != rand_num:
                  # Check If Random Number - Previous Guess Bigber Than Random Number - Last Guess.
                  if abs((rand_num - lifes_list[-2])) > abs((rand_num - lifes_list[-1])):
                        # User Getting Closer
                        print('Getting Closer.')
                  # Check If Random Number - Previous Guess Smaller Than Random Number - Last Guess.
                  elif abs((rand_num - lifes_list[-2])) < abs((rand_num - lifes_list[-1])):
                        # User Getting Further
                        print('Getting Further.')
                  else:
                        # If User Put Same Number More Than One
                        print('Try Again.')
            else:
                  # If User Guess Correct
                  print(f'Great Done. in Total {str(len(lifes_list))} Guesses.')
                  break
      else:
            print('Choose Number Between 1:100.')
