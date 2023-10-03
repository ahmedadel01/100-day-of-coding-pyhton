import random

pin_code = random.randint(1000, 9999)

user_input = int(input("Enter a 4-digit PIN code: "))

if user_input < 1000 or user_input > 9999:
  print("Please enter 4 digits")
elif user_input == pin_code:
  print("Success! PIN code matched")
else:
  print("Failure! PIN code did not match")
  print(f"The computer generatedthis PIN: {pin_code}")
