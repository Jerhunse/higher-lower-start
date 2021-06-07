from art import logo
from art import vs
from game_data import data
import random

print(logo)
#Randomly generate a cleb
def selector():
    choice = random.choice(data)
    return choice 

print(selector())

def find_follower_count(celebrity):
  followers = celebrity["follower_count"]
  return followers


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

