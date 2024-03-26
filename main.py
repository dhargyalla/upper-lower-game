#steps involved in the project
#1. import modules
from art import logo, vs
from game_data import data
import random
from replit import clear

#3. generate random items from game_data
def random_item():
  return random.choice(data)
#4. compare two items based on the follower count
def compare(item1, item2):
  if item1['follower_count'] > item2['follower_count']:
    return 'A'
  else:
    return 'B'

#update score 
def update_score(score):
  return score + 1
    
#6. main game
def game():
  print(logo)
  score = 0
  game_over = False
  item1 = random_item()
  item2 = random_item()
  
  while not game_over:
    
    print(f"compare A: {item1['name']}, a {item1['description']}, from {item1['country']}, {item1['follower_count']}")
    print(vs)
    print(f"compare B: {item2['name']}, a {item2['description']}, from {item2['country']}, {item2['follower_count']}")
    user_choice = input("who has more followers? Type 'A' or 'B': ")
    if user_choice == compare(item1, item2):
      score = update_score(score)
      item1 = item2
      item2 = random_item()
      clear()
     
      print(f"you're right! Current score: {score}")
      
  
    else:
      game_over = True
      print(f"sorry, that's wrong. Final score: {score}")

game()
#7. end game
#PROJECT FOR HIGHER-LOWER GAME
