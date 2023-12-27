import random
from game_data import data
from art import logo, vs
import os
clear = lambda: os.system('cls')

print(logo)


# format the account data 
def format_account(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_description}, {account_country}"


def check_answer(guess, follower_1, follower_2):
    if follower_1 > follower_2:
        return guess == "A"
    else:
        return guess == "B"


score = 0
end_of_game = False
account_2 = random.choice(data)

while not end_of_game:
    # Generate random accounts 
    account_1 = account_2
    account_2 = random.choice(data)
    while account_1 == account_2:
        account_2 = random.choice(data)

    # format account
    print(f"Compare A: {format_account(account_1)}")
    print(vs)
    print(f"Against B: {format_account(account_2)}")

    # Ask the user for a guess
    guess = input("Who has more followers? Type A or B: ").upper()

    follower_1 = account_1["follower_count"]
    follower_2 = account_2["follower_count"]

    is_correct = check_answer(guess, follower_1, follower_2)

    clear()
    print(logo)
    if is_correct == True:
        score += 1

    if is_correct == True:
        print(f"You're right: Current Score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = True
        


    # def question():
    #     print(logo)
    #  print(data[country[2]])

    # print(data[2]["country"])
    # followers = random.choice(data)
    # print(followers["country"])
