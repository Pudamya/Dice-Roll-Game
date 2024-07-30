import random
roll_die=lambda : random.randint(1,6)

def dice_game(rounds):
    player01=input("Enter the name: ")
    player02=input("Enter the name: ")
    print()
    p1win=0
    p2win=0
    rn=1
    
    while rn<=rounds:
        print("..........Round Number {}...........".format(rn))
        
        p1=roll_die()
        p2=roll_die()
        
        print("{} roll: {} and {} roll: {}".format(player01,p1,player02,p2))
        
        if p1==p2:
            print("The round was drawn")
        elif p1>p2:
            print("The round was won by {}".format(player01))
            p1win+=1
        else:
        
            print("The round was won by {}".format(player02))
            p2win+=1
        print()  
        rn+=1
        

    if p1win==p2win:
        print()
        print("The game was drawn")
    elif p1win>p2win:
        print()
        print("The game was won by {}".format(player01))
    else:
        print()
        print("The game was won by {}".format(player02))
      
        
dice_game(5)        
    
