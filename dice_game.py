import random

player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")


def roll_dice():
    """simulates dice roll by 
    generating a random number between one and six twice and then adding these

    Returns:
        _int_: _the two simulated dice rolls_
    """
    rolls_dice = random.randint(1, 6) + random.randint(1, 6)

    return rolls_dice


roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1)
print(player2, 'rolled', roll2)

if roll1 > roll2:
    print(player1, "Has won!")

elif roll1 == roll2:
    print("TIE")

else:
    print(player2, "Has Won!")
