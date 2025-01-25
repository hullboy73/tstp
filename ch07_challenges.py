series = ["The Walking Dead","Entourage","The Sopranos","The Vampire Diaries"]
##for show in series:
##    print(show)
##for i in range(25,51):
##  print(i)

numbers = [23,21,67,9,18,4]

while True:
   guess = input("Guess a number or type q to quit. ")
   if guess == "q":
       break
   try:
       guess = int(guess)
   except ValueError:
       print("Please type a number or q to quit.")
   if guess in numbers:
       print("You guessed correctly! ")
   else:
       print("You guessed wrong this time. ")
