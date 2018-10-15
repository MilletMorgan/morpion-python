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

def IA_jouer(int jeu, int profondeur):
    int max = -1000
    int tmp, maxi, maxj
    int i, j

    for(i=0; i<3; i++):
        for(j=0; j<3 j++):
            if(jeu[i][j] == 0):
                jeu[i][j] = 1
                tmp = Min(jeu, profondeur-1)

                if(tmp > max):
                    max = tmp;
                    maxi = i
                    maxj = j

                jeu[i][j] = 0

    jeu[maxi][maxj] = 1

def Max(int jeu, int profondeur):
    if(profondeur ==0 | gagnant(jeu) != 0):
        return eval(jeu)

    int max = -1000
    int i, j, tmp

    for(i=0; i<3; i++):
        for(j=0;j<3;j++):
            if(jeu[i][j] == 0):
                jeu[i][j] = 2
                tmp = Min(jeu, profondeur-1)

                if(tmp > max | ((tmp == max) && (rand()%2 == 0))):
                    max = tmp

                jeu[i][j] = 0

    return max

def Min(int jeu, int profondeur):
    if(profondeur == 0 | gagnant(jeu)!=0)
        return eval(jeu);
    int min = 10000
    int i, j, tmp

    for(i=0; i<3; i++):
        for(j=0; j<3; j++):
            if(jeu[i][j] == 0):
                eu[i][j] = 1;
                tmp = Max(jeu, profondeur-1);

                if(tmp < min | ((tmp == min) & (rand()%2 == 0))):
                    min = tmp
                
                jeu[i][j] = 0

    return min

def nb_series(int jeu, int series_j1, int series_j2, int n):
    int compteur1, compteur2, i, j

    series_j1 = 0
    series_j2 = 0

    compteur1 = 0
    compteur2 = 0

    for(i=0; i<3; i++):
        if(jeu[i][j] == 1):
            compteur1++
            compteur2 = 0

            if(compteur1 == n):
                series_j1++

        elif (jeu[i][i] == 2):
            compteur2++
            compteur1 = 0

            if(compteur2 == n):
                series_j2++
    
    compteur1 = 0
    compteur2 = 0

    for(i=0; i<3; i++):
        if(jeu[i][2-i] == 1):
            compteur1++
            compteur2 = 0

            if(compteur1 == n):
                series_j1++

        elif(jeu[i][2-i] == 2):
            compteur2++
            compteur1 = 0

            if(compteur2 == n):
                series_j2++

    for(i=0; i<3; i++):
        compteur1 = 0
        compteur2 = 0

        for(j=0; j<3; j++):
            if(jeu[i][j] == 1):
                compteur1++
                compteur2 = 0

                if(compteur1 == n):
                    series_j1++
            
            elif(jeu[i][j] == 2):
                compteur2++
                compteur1 = 0

                if(compteur2 == n):
                    series_j2++

        compteur1 = 0
        compteur2 = 0

        for(j=0; j<3; j++):
            if(jeu[j][i] == 1):
                compteur1++
                compteur2 =0

                if(compteur1 == n):
                    series_j1++
            
            elif(jeu[j][i] == 2):
                compteur2++
                compteur1 = 0

                if(compteur2 == n):
                    series_j2++

def eval(int jeu):
    int vainqueur, nb_de_pions = 0
    int i, j

    for(i=0; i<3; i++):
        for(j=0; j<3; j++):
            if(jeu[i][j] != 0):
                nb_de_pions++

    if((vainqueur = gagnant(jeu)) != 0):
        if(vainqueur == 1):
            return 1000 - nb_de_pions
        elif(vainqueur == 2):
            return -1000 + nb_de_pions
        else:
            return 0
    
    int series_j1 = 0, series_j2 = 0

    nb_series(jeu,series_j1, series_j2, 2)

    return series_j1 - series_j2

def gagnant(int jeu):
    int i, j
    int j1, j2

    nb_series(jeu, j1, j2, 3)

    if(j1):
        return 1
    elif(j2):
        return 2
    else:
        for(i=0; i<3, i++):
            if(jeu[i][j] == 0):
                return 0

    return 3



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