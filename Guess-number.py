# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 06:13:43 2021

@author: hp
"""
import random

game_start ="True"


print("Hello and welcome in my program")

#Ask user to enter a number between 1 and 10

user_guess= input("Please am thinking about a number between 1 and 10, can you geuess it? : " )

print ("You think my number is " + user_guess + " Ok let's check")
  
#After asking user to enter his guess number we will generate a random from 1 to 10

my_number = random.randint(0 , 10) 
# Ok we have now a code which will generate a random btw 1 and 10
  
#Convert user_guess to an integer

user_guess = int(user_guess)


#Now we will create a loop to continue running our program

#while(user_guess != my_number):
    ##print("This not my number try again")
    #user_guess
number =str(my_number)
if user_guess == my_number:

    print("You have guessed my number , congratulations !!!")
else:
    print("my number was " + number)
    
print("Bye see you soon, thank you")




    


