#NAME: ERIC AMOH ADJEI
#DATE: 10/19/2023
#ASSIGNMENT: Loops and Decision-Making in Python


#creating a conditional Python programming with while, for, break, if, elif, and else loops.
while True:
    
    #\n represents a newline
    print(  "    \n \n \n\t\t\t   @AMOHERIC GAMING CORPORATION  \n \n      \t\t\t   CC: ALL RIGHTS RESERVED  2023\n\n ")


    #\t represents a tab
    print( "\t\t\t\t    CHOOSE YOUR SAGA  \n \n ")


    #Creating a description as an introduction to Python sim game for my users.
    print( "\t\t\t     WELCOME TO PYTHON INTERACTIVE SIM GAME   \n \n ")


    # Adding the print Python command
    print("To begin this exciting  journey \n\n  You will need to save your progress \n \n ")
    
    
    #getting the user ready to interact with the application
    print("\n And therefore we ask all new players to register basic information first\n ")


    # print() is a function that prints a line of text.
    print("\t\t\t Please Register Here... \n\n ")

    # Adding at least two variables holding different data types for my application as a user input
    name = input("What is your name?\n :")
    phone = int( input("What is your best phone number? (Int(). only) \n :"))

    #this prints user input data with my set string
    print(name + " your phone number is " + str(phone) + " right?  \n \n ")
    
    
    #user input
    Fun = input(name + " are you excited to Play the game? (yes/no) \n \n: ")
    print( Fun + " because Python is still Python, \n nothing changed still a reptile in this game \n\n ")
    
    
    #getting user ready for main sim game
    print(" Are you ready " + name + "  for your first try then? \n\n ")
    

    #adding a descriptive text of the first sim
    print(" Now will you run or Walk away from a stranger in black? \n\n ")
    print("A weird looking men in black with a hat on sitting at the back of a strange house calling your full name\n \n ")
    print("1 - Run")
    print("2- Walk away")


    #getting user input or answer and converting it into a variable
    action1 = input("Choose your action (1 or 2 )\n \n:")
    
    #start our if statement to match or loop user input
    if action1 == "1":
        
        #determing the outcome of user action taken
        print(" So you run and got to a point where there is no way but 3 tall walls and the way you coming from\n")
        print(" You looked back to see this stranger coming towards you")
        print(" 1 - Scream for help")
        print(" 2 - Ask stranger what he wants?")
        
        action2 = input("Choose your action (1 or 2 )\n \n:")
        
        
        
        if action2 == "1":
            
            #determing the outcome of user action taken
            print(" So you Scream for help\n")
            print(" You looked back to see who was coming to help but another men in black stranger coming towards you")
            print(" 1 - Get ready to fight")
            print(" 2 - Beg strangers to let you go and not harm you")
            
            action3 = input("Choose your action (1 or 2 )\n \n:")            
            
            
            
            if action3 == "1":
                    
                    #determing the outcome of user action taken
                    print(" So you are ready to fight\n")
                    print(" The strangers looked at each other and laugh")
                    print(" 1 - Attack first")
                    print(" 2 - Ask why they are laughing at you")
                    
                    action4 = input("Choose your action (1 or 2 )\n \n:")
                
                
                
                    if action4 == "1":
                        #determing the outcome of user action taken
                        print(" So you decided to resolve with violence,\n sorry but you lose, \n that was your parents playing prank on you.\n")
                    
                    
                    # else if is used to make other options possible for the user    
                    elif action4 == "2":
                        #    
                        print(" The strangers looked at each other and laugh because you won, \n its just your parents in prank")
                        
                        #else to ask the user to stay according to the code
                    else:
                        print("Please choose from only 1 or 2 for you action, thank you")   


    # else if is used to make other options possible for the user
    elif action1 == "2":
        
        print(" So you decided to walk away but the stranger follows you") 
        print(" You asked stranger what he wants") 
        print(" The stranger just looked at you and laugh")
        
        
        #determing the outcome of user action taken
        print(" 1 - Attack the stranger first")
        print(" 2 - Ask the stranger what is the sense in all this?")
                        
        action2 = input("Choose your action (1 or 2 )\n \n:")
        
        
    # If statement to determine user result   
    if action2 == "1":
        print(" So you decided to resolve with violence,\n sorry but you lose, \n that was your parents playing prank on you.\n")
    
    
    # else if is used to make other options possible    
    elif action2 == "2":
                    
        print(" The strangers looked at each other and laugh because you won, \n its just your parents in prank")  
    
    
    #else to ask the user to stay according to the code
    else:
                        
        print("Please choose from only 1 or 2 for you action, thank you")
    
    
                        
    # asking users whether they want to continue the game                    
    replay = input("Do you want to try again? (Yes/No) :  ")
    
    
    #if the user types yes the game starts over
    if replay.upper() != "YES" :
        print(" Thank You - Game Over!!!")
        break
