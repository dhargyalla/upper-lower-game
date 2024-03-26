#steps involved in the project
#1. import modules
from art import logo, vs
from game_data import data
import random
#2. print logo
print(logo)
#3. generate random items from game_data
def random_item():
  item = random.choice(data)
  print(item)
#4. compare two items based on the follower count
#5. update the current score
#6. main game
#7. end game
#PROJECT FOR HIGHER-LOWER GAME
