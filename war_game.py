import random

choices = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

tie = "It is a tie."
lost = "You lost!"
won = "You won!"

outcomes = [[tie, lost, lost, lost, lost, lost, lost, lost, lost, lost, lost, lost, lost],
            [won, tie, lost, lost, lost, lost, lost, lost, lost, lost, lost, lost, lost],
            [won, won, tie,  lost, lost, lost, lost, lost, lost, lost, lost, lost, lost],
            [won, won, won, tie,  lost, lost, lost, lost, lost, lost, lost, lost, lost],
            [won, won, won, won, tie,  lost, lost, lost, lost, lost, lost, lost, lost],
            [won, won, won, won, won, tie, lost, lost, lost, lost, lost, lost, lost],
            [won, won, won, won, won, won, tie, lost, lost, lost, lost, lost, lost],
            [won, won, won, won, won, won, won, tie, lost, lost, lost, lost, lost],
            [won, won, won, won, won, won, won, won, tie, lost, lost, lost, lost],
            [won, won, won, won, won, won, won, won, won, tie, lost, lost, lost],
            [won, won, won, won, won, won, won, won, won, won, tie, lost, lost],
            [won, won, won, won, won, won, won, won, won, won, won, tie, lost],
            [won, won, won, won, won, won, won, won, won, won, won, won, tie]]


human_score = 0
comp_score = 0

while True:

    user_card = random.randint(1, 13)
    comp_card = random.randint(1, 13)

    int(input("\nPress 1 to start "))
    print("You drew:", choices[user_card - 1], "   Computer drew:", choices[comp_card - 1])

    outcome = outcomes[user_card - 1][comp_card - 1]
    print(outcome)

    if outcome == won:
        human_score += 1
    elif outcome == lost:
        comp_score += 1

    print("Score: ")
    print("Human:", human_score, "   Computer:", comp_score)

    if human_score == 5 or comp_score == 5:
        break

if human_score == 5:
    print("\nYou won the game of WAR!")
elif comp_score == 5:
    print("\nYou lost the game of WAR. Better luck next time!")

print("Thanks for playing!")






