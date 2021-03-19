from random import randint # randint gives random whole numbers

pls = 0 # Player's score board
comps = 0 # Computer's score board
rounds = int(input("Enter the number of rounds you want to play: ")) # How many rouds the game shall last
game = 0 # Number of rounds completed

while True:
    pl = int(input("1.Stone 2.Paper 3.Scissor: ")) # Taking input in int for choosing stone, paper or scissor
    comp = randint(1,3) # random number generated for the computer

    if pl == comp: # If the player and computer have the same number/object then output is given as it is a tie
        print("Tie")
        game = game + 1 # this increase rounds
    
    elif pl == 1:
        if comp == 2:
            print("You lose", comp , "beats" , pl)#IDK how does paper manage to do that.
            pls = pls - 1 # adds point to player's leaderboard
            comps = comps + 1 # adds point to player's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)
        else:
            print("You Win")
            pls = pls + 1 # adds point to player's leaderboard
            comps = comps - 1 # subtracts point to computer's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)
    
    elif pl == 2:
        if comp == 3:
            print("You Lose", pl , "beats" , comp)
            pls = pls - 1 # adds point to player's leaderboard
            comps = comps + 1 # adds point to player's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)
        else:
            print("You Win")
            pls = pls + 1 # adds point to player's leaderboard
            comps = comps - 1 # subtracts point to computer's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)
    
    elif pl == 3:
        if comp == '1':
            print("You Lose", comp , "beats" , pl)
            pls = pls - 1 # adds point to player's leaderboard
            comps = comps + 1 # adds point to player's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)
        else:
            print("You Win")
            pls = pls + 1 # adds point to player's leaderboard
            comps = comps - 1 # subtracts point to computer's leaderboard
            game = game + 1 # this increase rounds
            print("Scores are ", "Player: ",pls, "Computer: ",comps)        
    
    if game == rounds:
        print("Gamer over")
        print("Final scores are:", "Player :",pls, " Computer: ",comps)
        if pls > comps: # if player has more score than computer then this will excecute
            print("You Win")
            break
        elif pls == comps: # if player has equal score than computer then this will excecute
            print("Tie")
            break # it breaks the while loop and ends the program
        else: # if player has less score than computer then this will excecute
            print("Try Again next time.")
            break # it breaks the while loop and ends the program
    else:
        print("Enter a number from 1 to 3")
        
    
