horiBar = "-"
vertBar = "|"
space = " "

circle = "O"
cross = "X"

case1 = space
case2 = space
case3 = space
case4 = space
case5 = space
case6 = space
case7 = space
case8 = space
case9 = space

a = 0

def affichage():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9

    print(case1, vertBar, case2, vertBar, case3)
    print(horiBar, horiBar, horiBar, horiBar, horiBar)
    print(case4, vertBar, case5, vertBar, case6)
    print(horiBar, horiBar, horiBar, horiBar, horiBar)
    print(case7, vertBar, case8, vertBar, case9, '\n')     


def turn_player1():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9

    player1 = int(input("Joueur 1 : "))

    if(player1 == 1):
        if(case1 == circle):
            print("Case déjà utilisé! \n")
            turn_player1()
        else:
            case1 = cross
    elif(player1 == 2):
        if(case2 == circle):
            print("Case déjà utilisé! \n")
            turn_player1()
        else:        
            case2 = cross
    elif(player1 == 3):
        if(case3 == circle):
            print("Case déjà utilisé! \n")
            turn_player1()
        else:        
            case3 = cross
    elif(player1 == 4):
        if(case4 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case4 = cross
    elif(player1 == 5):
        if(case5 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case5 = cross
    elif(player1 == 6):
        if(case6 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case6 = cross
    elif(player1 == 7):
        if(case7 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case7 = cross
    elif(player1 == 8):
        if(case8 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case8 = cross
    elif(player1 == 9):
        if(case9 == circle):
            print("Case déjà utilisé! \n")
            player1 = int(input("Joueur 1 : "))
        else:        
            case9 = cross

def turn_player2():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9

    player2 = int(input("Joueur 2 :"))

    if(player2 == 1):
        if(case1 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case1 = circle
    elif(player2 == 2):
        if(case2 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case2 = circle
    elif(player2 == 3):
        if(case3 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case3 = circle
    elif(player2 == 4):
        if(case4 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case4 = circle
    elif(player2 == 5):
        if(case5 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case5 = circle
    elif(player2 == 6):
        if(case6 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case6 = circle
    elif(player2 == 7):
        if(case7 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case7 = circle
    elif(player2 == 8):
        if(case8 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case8 = circle
    elif(player2 == 9):
        if(case9 == cross):
            print("Case déjà utilisé! \n")
            player2 = int(input("Joueur 2 : "))
        else:
            case9 = circle    

def player1_win():
    if ((case1 == cross) &
        (case2 == cross) & 
        (case3 == cross) | 
        (case1 == cross) & 
        (case4 == cross) & 
        (case7 == cross) | 
        (case1 == cross) & 
        (case5 == cross) & 
        (case9 == cross)):

        print("Joueur 1 gagne \n")
        exit()

def player2_win():
    if ((case1 == circle) & 
        (case2 == circle) & 
        (case3 == circle) | 
        (case1 == circle) & 
        (case4 == circle) & 
        (case7 == circle) | 
        (case1 == circle) & 
        (case5 == circle) & 
        (case9 == circle)):

        print("Joueur 2 gagne \n")
        exit()

while (a <= 8):
    turn_player1()
    affichage()
    player1_win()
    
    a+=1

    turn_player2()
    affichage()
    player2_win()

    a+=1
    
    if(a>=8):
        print("match nul")
        break