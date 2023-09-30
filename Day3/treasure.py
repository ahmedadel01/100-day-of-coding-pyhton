#show welcome message 
print("Welcome to my island!")
#ask the user to chose color form red or blue
print("There are two doors in front of you. a red door and a blue door")
first-color = input("which door do you want to open? ").lower() 
if first-color == blue :
  print("Ooops! You chose the crocodile door.")
  print("Game over!")
elif first-color == red :
  print("you found three boxes: white, black, green.")
  second-color = input("Which box do you open? ").lower()
  if second-color == white:
    print("Ooops! You chose a box filled with snakes.")
  elif second-color == black:
    print("Ooops! You chose a box filled with spiders.")
  elif second-color == green:
    print("Congratulatiions! You found the treasure!")
  else:
    print("Invalid choice")  
else:
  print("Invalid choice")
