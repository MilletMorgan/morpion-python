# A FAIRE :
#
# - CREER IA


# import pour pouvoir nettoyer le terminal
import os 

#Nettoie le terminal
os.system('clear')

#Déclaration des variables
horiBar = "----------"
vertBar = "|"
space = " "

circle = "O"
cross = "X"

scoreJoueur1 = 0
scoreJoueur2 = 0

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

#Déclaration des fonctions.

#Fonction d'affichage pour afficher le cadrillage.
def affichage():
    global case1, case2, case3, case4, case5, case6, case7, case8, case9

    print('\n')
    print(case1, vertBar, case2, vertBar, case3)
    print(horiBar)
    print(case4, vertBar, case5, vertBar, case6)
    print(horiBar)
    print(case7, vertBar, case8, vertBar, case9, '\n')     

#Fonction qui fait jouer le joueur 1 et vérifie si il a entré un nombre valide.
def turn_player1():
    #Appel des variables précédemment déclaré.
    global a, case1, case2, case3, case4, case5, case6, case7, case8, case9

    #Demande au joueur 1 ou il veut placer sa croix.
    player1 = int(input("Joueur 1 : "))

    #Si le joueur insère un nombre supérieur à 9, il redemande au joueur ou placer son symbole.
    if (player1 > 9):
        print("\033[31mVeuillez choisir une case entre 1 et 9 !\033[0m")
        turn_player1()
    else:
        if(player1 == 7): #Met une croix à la case 1.
            if(case1 != space): #Vérifie si la case n'est pas déjà utiliser
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:
                case1 = cross
                a+=1
        elif(player1 == 8):
            if(case2 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case2 = cross
                a+=1
        elif(player1 == 9):
            if(case3 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case3 = cross
                a+=1
        elif(player1 == 4):
            if(case4 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case4 = cross
                a+=1
        elif(player1 == 5):
            if(case5 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case5 = cross
                a+=1
        elif(player1 == 6):
            if(case6 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case6 = cross
                a+=1
        elif(player1 == 1):
            if(case7 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case7 = cross
                a+=1
        elif(player1 == 2):
            if(case8 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case8 = cross
                a+=1
        elif(player1 == 3):
            if(case9 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player1()
            else:        
                case9 = cross
                a+=1

#Fonction qui fait jouer le joueur 2 et vérifie si il a entré un nombre valide.
def turn_player2():
    global a, case1, case2, case3, case4, case5, case6, case7, case8, case9

    player2 = int(input("Joueur 2 :"))

    if (player2 > 9):
        print("\033[31mVeuillez choisir une case entre 1 et 9 !\033[0m")
        turn_player2()
    else:
        if(player2 == 7):
            if(case1 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case1 = circle
                a+=1
        elif(player2 == 8):
            if(case2 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case2 = circle
                a+=1
        elif(player2 == 9):
            if(case3 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case3 = circle
                a+=1
        elif(player2 == 4):
            if(case4 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case4 = circle
                a+=1
        elif(player2 == 5):
            if(case5 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case5 = circle
                a+=1
        elif(player2 == 6):
            if(case6 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case6 = circle
                a+=1
        elif(player2 == 1):
            if(case7 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case7 = circle
                a+=1
        elif(player2 == 2):
            if(case8 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case8 = circle
                a+=1
        elif(player2 == 3):
            if(case9 != space):
                print("\033[31mCase déjà utilisé !\033[0m")
                turn_player2()
            else:
                case9 = circle
                a+=1 

#Fonction pour vérifier si le joueur 1 à alligner 3 croix.
def player1_win():
    global scoreJoueur1, a, case1, case2, case3, case4, case5, case6, case7, case8, case9

    if ((case1 == cross) &
        (case2 == cross) & 
        (case3 == cross) |

        (case4 == cross) &
        (case5 == cross) &
        (case6 == cross) |

        (case7 == cross) &
        (case8 == cross) &
        (case9 == cross) |

        (case1 == cross) & 
        (case4 == cross) & 
        (case7 == cross) |

        (case2 == cross) & 
        (case5 == cross) & 
        (case8 == cross) |
        
        (case3 == cross) & 
        (case6 == cross) & 
        (case9 == cross) |

        (case1 == cross) & 
        (case5 == cross) & 
        (case9 == cross) |

        (case3 == cross) & 
        (case5 == cross) & 
        (case7 == cross)):

        print("\033[32mJoueur 1 gagne !\033[0m")
        print("\nScore : ")
        scoreJoueur1+=1
        print("Joueur 1 : ", scoreJoueur1)
        print("Joueur 2 : ", scoreJoueur2)
        replay = str(input("\nRejouer ? o/n \n"))
        if(replay == 'n'):
            exit()
        else:
            print("\n")
            a = 0
            case1 = space
            case2 = space
            case3 = space
            case4 = space
            case5 = space
            case6 = space
            case7 = space
            case8 = space
            case9 = space
            whileGame()

#Fonction pour vérifier si le joueur 2 à alligner 3 cercle.
def player2_win():
    global scoreJoueur2, a, case1, case2, case3, case4, case5, case6, case7, case8, case9

    if ((case1 == circle) &
        (case2 == circle) & 
        (case3 == circle) |

        (case4 == circle) &
        (case5 == circle) &
        (case6 == circle) |

        (case7 == circle) &
        (case8 == circle) &
        (case9 == circle) |

        (case1 == circle) & 
        (case4 == circle) & 
        (case7 == circle) |

        (case2 == circle) & 
        (case5 == circle) & 
        (case8 == circle) |
        
        (case3 == circle) & 
        (case6 == circle) & 
        (case9 == circle) |

        (case1 == circle) & 
        (case5 == circle) & 
        (case9 == circle) |

        (case3 == circle) & 
        (case5 == circle) & 
        (case7 == circle)):

        print("\033[32mJoueur 2 gagne !\033[0m")
        print("\nScore : ")
        scoreJoueur2+=1
        print("Joueur 1 : ", scoreJoueur1)
        print("Joueur 2 : ", scoreJoueur2)
        replay = str(input("\nRejouer ? o/n \n"))
        if(replay == 'n'):
            exit()
        else:
            print("\n")
            a = 0
            case1 = space
            case2 = space
            case3 = space
            case4 = space
            case5 = space
            case6 = space
            case7 = space
            case8 = space
            case9 = space
            whileGame()

def whileGame():
    global scoreJoueur1, scoreJoueur2, a, case1, case2, case3, case4, case5, case6, case7, case8, case9

    #Boucle qui appelle les fonctions jusqu'a la fin du jeu.
    while (a <= 9):

        #Appel des fonctions pour le joueur 1.
        turn_player1()
        affichage()
        player1_win()

        #Si toute les cases sont rempli sans qu'il y ait 3 symboles alligné, il y a match nul
        if(a == 9):
            print("\033[34mMatch nul !\033[0m")
            print("\nScore : ")
            print("Joueur 1 : ", scoreJoueur1)
            print("Joueur 2 : ", scoreJoueur2)
            replay = str(input("\nRejouer ? o/n \n"))
            if(replay == 'n'):
                break
            else:
                print("\n")
                a = 0
                case1 = space
                case2 = space
                case3 = space
                case4 = space
                case5 = space
                case6 = space
                case7 = space
                case8 = space
                case9 = space
                whileGame()
        
        #Appel des fonctions pour le joueur 2.
        turn_player2()
        affichage()
        player2_win()

        if(a == 9):
            print("\033[34mMatch nul !\033[0m")
            print("\nScore : ")
            print("Joueur 1 : ", scoreJoueur1)
            print("Joueur 2 : ", scoreJoueur2)
            replay = str(input("\nRejouer ? o/n \n"))
            if(replay == 'n'):
                break
            else:
                print("\n")
                a = 0
                case1 = space
                case2 = space
                case3 = space
                case4 = space
                case5 = space
                case6 = space
                case7 = space
                case8 = space
                case9 = space
                whileGame()

print("Bienvenue dans le jeu du Morpion !\n")
print("Pour jouer, les joueurs doivent chacun leur tour inséré un numéro de 0 à 9")
print("correspondant à la case où il souhaite mettre leur symbole, à savoir, 7 étant")
print("la première case en haut à gauche, 3 la dernière case en bas à droite, etc..")
print("Le but du jeu est d'aligner, verticalement, horizontalement ou diagonalement")
print("3 de vos symboles avant votre adversaire. Si aucun des deux joueurs n'a réussi") 
print("à aligner 3 symboles il y a match nul. \n \n")
print(" 7 | 8 | 9 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 1 | 2 | 3 ")
print("\n \n \n")

whileGame()