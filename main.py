from art import logo
from art import vs
from game_data import data
import random
import replit

#Randomly generate a cleb
def selector():
    choice = random.choice(data)
    return choice 
selected = selector()


#compares current selectors and returns the winner 

play_again = True
current_points = 0

while play_again == True:
  #define currrent things being compared 
  current_a = selector()
  current_b = selector()
  #set point system
  

  #print logo
  print(logo)

  #print comparison block and get user guess
  print("Compare "+current_a["name"]+ " a "+ current_a["description"] +", from "+current_a["country"])
  print(vs)
  print("Against "+current_b["name"]+ " a "+ current_b["description"]+ ", from "+current_b["country"])
  user_guess = input("Who has more followers? 'A' of 'B': ")

  if user_guess == "a":
    c1 = current_a["follower_count"]
    c2 = current_b["follower_count"]
    if c1 > c2:
      replit.clear()
      current_points += 1
      print(f"You're Right! Your current score is:{current_points}")
    elif c1 <= c2:
      replit.clear()
      play_again = False
      print(f"Thats Wrong, Game Over. Your final score is:{current_points}")

  elif user_guess == "b":
    c1 = current_a["follower_count"]
    c2 = current_b["follower_count"]
    if c2 > c1:
      current_points += 1
      replit.clear()
      print(f"You're Right! Your current score is: {current_points}")
    elif c2 <= c1:
      replit.clear()
      play_again = False
      print(f"Thats Wrong, Game Over. Your final score is: {current_points}")




      





# #assign their followers to a variable 
# choice1_followers = (choice1["follower_count"],choice1["name"])
# choice2_followers = (choice2["follower_count"],choice2["name"])

# def compare_items(first_info, first_follower, sec_info, sec_follower):
#   winner = []
#   points = 0
#   next_starter = []
#   if first_follower > sec_follower:
#     winner = "a"
#     next_starter = first_info
#   elif first_follower < sec_follower:
#     winner = "b"
#     next_starter = sec_info

#   print(f"Compare{first_info}")
#   print(vs)
#   print(f"Against{sec_info}")

#   guess = input("Select A or B: ")
#   if guess == winner:
#     points += 1
#     return (f"You got it! Current score {points} \n")
#   else:
#     print(f"Wrong answer, your final score was {points}")
#   return next_starter

