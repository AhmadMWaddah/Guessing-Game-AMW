#!/usr/bin/env python
# coding: utf-8

# # Guessing Game Challenge
# 
# Let's use `while` loops to create a guessing game.
# 
# The Challenge:
# 
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 
# 2. On all turns, if a guess is 
#  * closer to the number than the previous guess return "Closer!"
#  * farther from the number than the previous guess, return "Farther!"
# 3. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!
# 
# Now Lets o fro the Steps!

# #### First, Build a Line of Code that can Return arandom integer from 1 to 100 and store this number in object called Actual

# In[6]:


#Type Your Code Here  - Replace None with Correct  Function  


# #### Next, build a Code to display an introduction to the Game to tell the user the Boundaries from 1 to 100 and what is his target.

# In[4]:


#Type Your Code here 


# ### Next, Build a Code that takes an integer input from the user 

# In[5]:


#Type Your Code Here - Replace None With Correct Function 


# ### Next, Put the Upper Cell in A Loop that keeps checking if the Number is Out of Bounds or Not  

# In[3]:


#Replace None Values with correct conditions or Booleans


# ### Next, Build a Code that Check if the Guess is equal to the Actual Random Number3

# In[2]:


# Put function that calculate the Real Number of Guesses 
      


# ### Next, Build a Code that Check on Each Guess whether its closer than the Previous Guess or not.

# In[ ]:





# #### Write a `while` loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're Closer or Farer , and continue asking for guesses.
# 
# **Try to Collect All the cells you 've made above and use it here**
# 
# Hint:
# 
# 
# * you can use the `abs()` function to find the positive difference between two numbers
# 
# 
# # Decomposition 
# 
# *   Choosing Random Number
# *   Game Intro for the User
# *   Checking on the Inserted Guess if its in boundary or not
# *   Checking on the Inserted Guess if its equal to the Random Number or Not
# *   Checking on the Inserted Guess if its Far or Close from the Previous Guess.
# 
# 
# 
# 

# In[1]:


# Type your Final Code here
from random import randint

print('This Is Intro:\n  Guessing Game, You Pick a Number,\n    We Check If It Is Correct,\n      Numbers Between 1:100.')
rand_num = randint(1, 100)
print(rand_num)
lifes_list = [0]

        


# In[2]:


# Type here the Big Loop
while True:
    gues_num = int(input('Choose Your Random Number: '))
    if 1 <= gues_num < 100:
        lifes_list.append(gues_num)
        if gues_num != rand_num:
            if abs((rand_num - lifes_list[-2])) > abs((rand_num - lifes_list[-1])):
                print('Getting Closer.')
            elif abs((rand_num - lifes_list[-2])) < abs((rand_num - lifes_list[-1])):
                print('Getting Further.')
            else:
                print('Try Again.')
        else:
            print(f'Great Done. in Total {str(len(lifes_list))} Guesses.')
            break
    else:
        print('Choose Number Between 1:100.')

        


# That's it! You've just programmed your first game!
# 
# In the next section we'll learn how to turn some of these repetitive actions into *functions* that can be called whenever we need them.

# ### Good Job!
