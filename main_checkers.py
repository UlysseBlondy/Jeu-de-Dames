import pygame
import sys

# Initialisation de Pygame
pygame.init()


# Initialisation des constantes

width, height = 1000, 800 # les dimensions de ma fenetre
Rows, Cols = 8,8 # Nombre de lignes e colonnes sur la grille
size_case = 100 # taille de case en pixels

# Definir les palettes de couleurs
white = (255, 255, 255)
color_1 = '#582615' # couleurs des cases
color_2= '#F9CE78'
red = (255, 0, 0) # couleurs de pions
black = (0, 0, 0)


# Creation de la grille du damier
'''Ici les 1 et 2 font references aux deux joueurs
case foncée = 1 ou 2 
case blanche = 0 '''
grid = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2]]


# Initialisation de la fenêtre
win= pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de Dames")



def display_grid():
    ''' Cette fonction permet dans un premier temps de parcourir la grille et de la colorer, 
    en prenant le reste de la division. si le reste est 0 alors on met color_1 sinon color_2
    
    Puis via une fonction d'affichage de pion, on place les pions de manière à ce les conditions soient vraies
    si board[row][col] == 1 ou 2 alors on depose un pion
    '''
    for row in range(Rows):
        for col in range(Cols):
            if (row + col) % 2 == 0:
                color_case = color_1
            else :
                color_case = color_2
            pygame.draw.rect(win, color_case, (col * size_case, row * size_case, size_case, size_case))


            # Placer les pions en utilisant la fonction dessiner_pion
            if grid[row][col] == 1:
                display_pawn(win, row, col, red)
            elif grid[row][col] == 2:
                display_pawn(win, row, col, black)


# Fonction pour dessiner un pion
def display_pawn(win, Rows, Cols, color):
    ''' Cette fonction permet de dessiner le pion sur une case donnée. 
    Pour cela, on cherche d'abord à localiser le centre de la case
    '''
    horizo_pos = Cols * size_case + size_case // 2  # calcul la position horizontale du centre d'une case donnée
    verti_pos = Rows * size_case + size_case // 2   # calcul la position verticale du centre d'une case donnée


    pygame.draw.circle(win, color, (horizo_pos, verti_pos), size_case // 2-3)



# Fonction deplacement des pions
def move_pawn():
    '''Cette fonction permet le deplacement des pions selon les règles
    par exemple un pion peut deplacer seulement sur les diagonales( en avant ou en arriere s'il peut prendre un autre pion)
    en sautant par dessus le pion adverse.

    '''
    pass

def promoted_pawn():
    ''' Cette fonction permet de promouvoir un pion en Dame s'il arrive sur la derniere rangée adverse
    '''
    pass

def check_mate():
    '''' Cette fonction d'arreter le jeu et meme si le joueur adverse reste des pions
    c'est le cas où on caputure tous ses pions ou le joueur ne peut plus bouger
    '''
    pass


def captured_pawn():
    '''Cette fonction affiche dans la fenetre le nombre de pions capturés par les joueurs et le score
    '''
    pass



# Cette boucle consiste à afficher la grille et tient à ce que la fenetre reste ouverte.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner le plateau de jeu
    win.fill(white)
    display_grid()


    # Rafraîchir l'affichage
    pygame.display.flip()
