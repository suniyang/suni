def start():
    print("This is my Elephant Cat Mouse Game!")
    Player_One="Kenna"
    Player_Two="Sam"
    def choices(Player_One_Choice,Player_Two_Choice):
        if Player_One_Choice=="elephant" and Player_Two_Choice=="mouse":
            return("mouse kills elephant "+ Player_Two+" wins!")
        elif Player_One_Choice=='mouse'and Player_Two_Choice=="elephant":
            return("mouse kills elephant "+ Player_Two +" wins!")
        elif Player_One_Choice=="cat" and Player_Two_Choice=="mouse":
            return("cat kills mouse "+ Player_Two+" wins!")
        elif Player_One_Choice=="elephant" and Player_Two_Choice=="cat":
            return("elephant kills cat "+ Player_One+" wins!")
        elif Player_One_Choice=="mouse"and Player_Two_Choice=="cat":
            return("cat kills mouse "+ Player_Two+" wins!")
        elif Player_One_Choice=="cat"and Player_Two_Choice=="elephant":
            return("elephant kills cat "+ Player_Two+" wins!")
        elif Player_One_Choice==Player_Two_Choice:
            return("Kenna and Sam tied!")
        else:
            return("Please type elephant,cat or mouse!")

    Player_One_Choose=input("Does "+Player_One+" choose elephant ,cat or mouse?").lower()
    Player_Two_Choose=input("Does "+Player_Two+' choose elephant, cat or mouse?').lower()
    print(choices(Player_One_Choose, Player_Two_Choose))

    def Play_Again():
        Again=input("Would you like to play the game again?").lower()
        if Again=="No".lower():
            quit()
        if Again=="Yes".lower():
            start()
        else:
            print("Please enter Yes or No. Thank you!")
            Play_Again()
    Play_Again ()    
start()

