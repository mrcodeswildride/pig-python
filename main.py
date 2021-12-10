import os
import random

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  print("Two player game. Each turn, roll the die as many times as you like. If you roll a 1, your turn is over, and you earn no points. If you pass, your turn is over, and you add the points to your total. First player to reach 100 or more wins.\n")

  print("--------------------")
  print(f"Player one: {scores[1]}")
  print(f"Player two: {scores[2]}")
  print(f"Score this turn: {turn_score}")
  print("--------------------\n")

scores = {1: 0, 2: 0}
turn_score = 0
game_over = False
player = 1

while not game_over:
  print_game_state()
  print(f"Player {player}:")

  command = input("Roll [enter] or [p]ass? ").lower()

  if command in ["p", "pass"]:
    scores[player] += turn_score
    turn_score = 0

    if scores[player] >= 100:
      game_over = True
      print_game_state()
      print(f"Player {player} wins!")
    else:
      player = 2 if player == 1 else 1
  else:
    roll = random.randint(1, 6)

    if roll == 1:
      turn_score = 0
      player = 2 if player == 1 else 1
      input(f"\nYou rolled a 1. Press enter to switch turns. ")
    else:
      turn_score += roll
      input(f"\nYou rolled a {roll}. Press enter to continue. ")
