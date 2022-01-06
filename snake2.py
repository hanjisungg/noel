#importation du modue random pour générer aléatoirement les pommes et la tete du serpent
from random import*


############################################################################################################

#creation du double tableau
g = [0]*12
for i in range(12):
    g[i] = [" "]*12

#creation des lignes
#ligne du haut 
for i in range(12):
    g[0][i] = "X"

#ligne du bas 
for i in range(12):
    g[11][i] = "X"

#creation des colonnes
#creation colonne gauche
for j in range(1, 12):
    g[j][0] = "X"

#creation colonne droite
for i in range(1, 12):
    g[i][11] = "X"
    
##############################################################################################################################
    
#création de la tete du serpent

def tete_du_serpent(g):
    yserpent = randint(1, 10)
    xserpent = randint(1, 10)
    g[yserpent][xserpent] = "O"

tete_du_serpent(g)
##################################################################################################################################

#creation d'une pomme
def pomme(g):
    global xserpent
    global yserpent
    ypomme = randint(1, 10)
    xpomme = randint(1, 10)
    if xpomme == xserpent and ypomme == yserpent:
        pomme(g)
    else:
        g[ypomme][xpomme] = "."
        
#appel de la fonction de la pomme
pomme(g)


##############################################################################################################################

#creation de la fonction deplacement
def deplacement():
    global xserpent
    global yserpent
    if keyCode == 37:
        xserpent -= 1
    elif keyCode == 39:
        xserpent += 1
    elif keyCode == 38:
        yserpent -= 1
    elif keyCode == 40:
        yserpent += 1
        
        
########################################################################################################################################################
        
#creation de la fonction qui dit que si le serpent mange la pomme, il gagne 1 bout de corps

def corps():
    global xserpent
    global yserpent
    global xpomme
    global ypomme
    xserpent == xpomme and yserpent == ypomme

##############################################################################################################################
        
#afficher le tableau 
def affiche(g):
    for i in range(12):
        for j in range(12):
            print(g[i][j], end = "")
        print()
        
#################################################################################################################################
        
#creation d'une boucle while qui marche tant que l'on joue et qui s'arrete quand l'on meurt
        
while True:
    
    if xserpent == 0 or xserpent == 11 or yserpent == 0 or yserpent == 11 : break




        