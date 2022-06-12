import random

print("Welcome to the Rock Paper Scissors Game!")
print("---------------------------------------")
print("RULES OF THE GAME")
print("Pick a letter: R - Rock, P - Paper, S - Scissors")
print("Use UPPER CASE letters")
print("---------------------------------------")
print("WINNER IS CHOSEN AS FOLLOWS:")
print("Rock beats Scissors")
print("Paper beats Rock")
print("Scissors beats Paper")
print("---------------------------------------")

### Set up variables
Score = 1
possibleOptions = ["R","P","S"]

def checkForWinner(player, computer):
  if(player == "R" and computer == "P"):
    return "CPU"
  elif(player == "R" and computer == "S"):
    return "Player"
  elif(player == "S" and computer == "P"):
    return "Player"
  elif(player == "S" and computer == "R"):
    return "CPU"
  elif(player == "P" and computer == "R"):
    return "Player"
  elif(player == "P" and computer == "S"):
    return "CPU"
  else:
    return "Tie"

### Start game loop
while(Score >= 1):
  ### Validate input
  while True:
    player = input("\nStart the game! Go ahead and pick a letter: ")
    if(player == "R" or player == "P" or player == "S"):
      break
    else:
      print("That's an Invalid input. Please try again.")
  
  ### Generate computer pick
  computer = random.choice(possibleOptions)
  optResult = {
    'R': "Rock",
    'S': "Scissors",
    'P': "Paper"
}

  print(f"Player ({optResult.get(player)}) : CPU ({optResult.get(computer)})")

  result = checkForWinner(player, computer)
  if(result == "Player"):
    print("Player wins")
    break
  elif(result == "CPU"):
    print("Computer wins")
    break
  else:
    (result == "Tie")
    print("It's a tie! Please play again")
