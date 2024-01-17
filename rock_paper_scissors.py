npc = "scissors"

player = input("Choose either rock, paper or scissors\n")

outcomes = {
    ("scissors", "rock"): "Player wins!",
    ("paper", "scissors"): "Player wins!",
    ("rock", "paper"): "Player wins!",
    (npc, player): "Tie"
}

result = outcomes.get((npc, player), "NPC wins!")
print(result)



