NAME=input('Please enter the name of the person who created this game:')
print("This game was made by amazing"+NAME+"! ")
print("Welcome to my guesssing game!")
print("In this game, you will try to guess a word that i chose")
print("Good luck!")

def start():
    Player_Name=input("what is the name of the player？")
    print("Greeting,"+Player_Name+"! It is time to guess!")

    Secret_Word="SAM".lower()
    Guesses="  "
    Turns_Left=3

    while Turns_Left >0:
        Wrong_Answers=0
        for Letter in Secret_Word:
            if Letter in Guesses:
                print(Letter)
            else:
                print("_")
                Wrong_Answers+=1
        if Wrong_Answers==0:
            print("You win the game!+ You guessed the secret word"+Secret_Word+"!")
            break
        
        Guess=input("Guess a letter here:").lower()
        Guesses+=Guess
    
        if Guess not in Secret_Word:
            Turns_Left-=1
            print("oops!This letter is not in my word. Please try again.")
            print("You have"+str(Turns_Left)+"more left. You can do it!")
        if Turns_Left==0:
            print("Game over")
        
    def Play_Again():
        Again=input("Would you like to play again?").lower()
        if Again=="NO".lower():
            quit()
        if Again=="YES".lower():
            start()
        else:
            print("Please enter Yes or NO, thank you!")
            Play_Again
    Play_Again()
        
start()
    
        
    
