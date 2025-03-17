from art import logo, vs
from game_data import data
import random

end_of_game = False
score = 0

print(logo)
while not end_of_game:
    data_1 = random.choice(data)
    data_2 = random.choice(data)

    print(f"1. {data_1["name"]} a {data_1["description"]} from {data_1["country"]}")
    print(vs)
    print(f"2. {data_2["name"]} a {data_2["description"]} from {data_2["country"]}")
    winner = 0
    if data_1["follower_count"] > data_2["follower_count"]:
        winner = 1
    else:
        winner = 2
    
    guess = int(input("Guess who has more follower? 1 or 2 ; "))
    if guess != winner:
        end_of_game = True
        print(f"You lose! Your score is {score}")
    else:
        score += 1
        print(f"You gussed correctly. Your score is {score}")