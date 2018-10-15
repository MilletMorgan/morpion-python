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