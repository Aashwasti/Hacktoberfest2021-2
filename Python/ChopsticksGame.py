p1_l=1
p1_r=1
p2_l=1
p2_r=1

def display(p1_l,p1_r,p2_l,p2_r):
    print("Current Status")
    print("Player1 - ",p1_l,p1_r)
    print("Player2 - ",p2_l,p2_r)


while True:
    p1_move= input("Enter move for Player 1 - ")
    if p1_move=="A":
        x,y= input("Enter the move combination - ").split()
        if x=="L" and y=="L":
            p2_l+=p1_l
        elif x=="L" and y=="R":
            p2_r+=p1_l
        elif x=="R" and y=="L":
            p2_l+=p1_r
        else:
            p2_r+=p1_r 

        if p2_l>=5:
            p2_l=0
        if p2_r>=5:
            p2_r=0
        display(p1_l,p1_r,p2_l,p2_r)
        if p2_l==0 and p2_r==0:
            print("Player1 is the winner")
            exit()
        
    else:
        x,y,z=input("Enter the move combination - ").split()
        y=int(y)
        z=int(z)
        p1_l=y
        p1_r=z
        display(p1_l,p1_r,p2_l,p2_r)

    p2_move= input("Enter move for Player 2 - ")
    if p2_move=="A":
        x,y= input("Enter the move combination - ").split()
        if x=="L" and y=="L":
            p1_l+=p2_l
        elif x=="L" and y=="R":
            p1_r+=p2_l
        elif x=="R" and y=="L":
            p1_l+=p2_r
        else:
            p1_r+=p2_r 

        if p1_l>=5:
            p1_l=0
        if p1_r>=5:
            p1_r=0
        display(p1_l,p1_r,p2_l,p2_r)
        if p1_l==0 and p1_r==0:
            print("Player2 is the winner")
            exit()
        
    else:
        x,y,z=input("Enter the move combination - ").split()
        y=int(y)
        z=int(z)
        p2_l=y
        p2_r=z
        display(p1_l,p1_r,p2_l,p2_r)

    
