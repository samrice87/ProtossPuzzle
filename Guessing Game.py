import random
while True:  

    random_number = random.randint(1, 100)

    print("Welcome! Would You Like to Play a Game?")

    user_input = input("Yes or No: ").lower()


    if user_input == "yes":
        print("NOW GUESS THE NUMBER!")



        user_guess = int(input("Enter Your Number "))

        if user_guess == random_number:
            print("u guessed right!")
        else:
            print("you suck at guessing! " + str(random_number) )

        play_again = input("Woud You Like to Try Again? Yes or No")

        if play_again != "yes":
            print("Thanks for Playing You Lil BIEECH")
            break
        else:
            print("RUN AWAY LITTLE GIRL! RUN AWAY!")
            break
       

    


