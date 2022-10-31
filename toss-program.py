import random

coin = ["Heads","Tails"]
toss = random.choice(coin)

selection = input("Heads or Tails: ")

if selection == toss:
	print("You won! coin landed on " + toss)
else:
	print("You lose! coin landed on " + toss)
