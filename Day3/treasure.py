#show welcome message 
print("Welcome to my island!")
#ask the user to chose color form red or blue
print("There are two doors in front of you. a red door and a blue door")
firstcolor = input("which door do you want to open? ").lower() 
if firstcolor == "blue" :
  print("Ooops! You chose the crocodile door.")
  print("Game over!")
elif firstcolor == "red" :
  print("you found three boxes: white, black, green.")
  secondcolor = input("Which box do you open? ").lower()
  if secondcolor == "white":
    print("Ooops! You chose a box filled with snakes.")
  elif secondcolor == "black":
    print("Ooops! You chose a box filled with spiders.")
  elif secondcolor == "green":
    print("Congratulatiions! You found the treasure!")
  else:
    print("Invalid choice")  
else:
  print("Invalid choice")
