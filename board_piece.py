import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
width, height = 760, 760

# Initialisation de la fenêtre
win= pygame.display.set_mode((width, height))
pygame.display.set_caption("Jeu de Dames")

# Taille du carré de jeu
square = width // 8

# Définition des pièces
black_pawn = 1
red_pawn = 2

Rows, Cols = 8,8 # Nombre de lignes e colonnes sur la grille
size_case = 100 # taille de case en pixels
square = width//Rows

# Definir les palettes de couleurs
white = (255, 255, 255)
color_1 = '#582615' # couleurs des cases
color_2= '#F9CE78'
red = (255, 0, 0) # couleurs de pions
black = (0, 0, 0)


# Classe pour le jeu de dames
class CheckerGame:
    def __init__(self):
        self.grid = [['-' for _ in range(8)] for _ in range(8)]
        self.begin = black_pawn
        self.selected_piece = None
        self.moves = []
        self.moves_promoted = []
        


    def display_grid(self):
        ''' Cette fonction permet de placer les pions sur la grille.
        Puis via une fonction d'affichage de pion, on place les pions de manière à ce les conditions soient vraies
        si grid[row][col] == 1 ou 2 (red_pawn and black_pawn) alors on depose un pion
        '''
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = red_pawn
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = black_pawn

    def draw_grid(self, win):
        ''' Cette fonction permet dans un premier temps de parcourir la grille et de la colorer, 
    en prenant le reste de la division. si le reste est 0 alors on met color_1 sinon color_2
    '''
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color_case = color_1
                else :
                    color_case = color_2
                pygame.draw.rect(win, color_case, (col * square, row * square, square, square))

    def draw_pawn(self, win):
        ''' Cette fonction de dessiner la piece, elle parcours la grille, si la case n'est pas vide c'est-à-dire grid[row][col] = 0,
        alors on regarde si grid[row][col = 1 ou 2 puis on colorie la piece
        '''
        for row in range(8):
            for col in range(8):
                if self.grid[row][col] != '-':
                    if (row, col) == self.selected_piece:
                        color = red
                    else:
                        color = black
                    
                    pygame.draw.circle(win, red if self.grid[row][col] == black_pawn 
                                       else black, (col * square + square // 2, row * square + square // 2), square // 2 - 3)
                    
                    horizo_pos = Cols * size_case + size_case // 2 
                    verti_pos = Rows * size_case + size_case // 2 
                    pygame.draw.circle(win, color, (horizo_pos, verti_pos), square // 3)
                    

    def get_piece_at_position(self, pos):
        ''' Cette fonction renvoie la position du piece sur la grille, c'est-à-dire les coordonnées en x ligne et y colonne.
        Elle verifie egalement si une piece n'est pas hors de la grille.
        '''
        row, col = pos[1] // square, pos[0] // square
        if 0 <= row < 8 and 0 <= col < 8:
            return row, col
        return None
    

    def is_valid_move(self, player, debut, fin):
        '''Cette fonction permet d'etablir les regles du jeu, les deplacement si c'est envisageable.
        '''
        # la position d'une pièce de la grille
        pawn = self.grid[debut[0]][debut[1]]

        # Si la case de fin est hors de  la grille alors on arrete
        if fin[0] < 0 or fin[0] > 7 or fin[1] < 0 or fin[1] > 7:
            return False

        '''# Vérifier si la case de fin est occupée
        if self.grid[fin[0]][fin[1]] != '-':
            return False'''

        if fin[0] < 0 or fin[0] > 7 or fin[1] < 0 or fin[1] > 7:
            return False

        if player == 1:
        # Le premier joueur ne peut se déplacer que vers le haut, en bas (si la pièce est promue)
            if fin[0] <= debut[0]:
                return False
        # Deplacement en diagonale
            if fin[0] == debut[0] + 1 and (fin[1] == debut[1] + 1 or fin[1] == debut[1] - 1):
                return True
        # Capture des pions de l'adversaire
            if fin[0] == debut[0] + 2 and (fin[1] == debut[1] + 2 or fin[1] == debut[1] - 2):
            # Si la case suivante est capable de capture
                if self.grid[debut[0] + 1][(debut[1] + fin[1]) // 2] == 2:
                    return True
        
        elif player == 2:
        # Le jouueur adverse (pièce noire) ne peut se diriger que en bas contrairement au joueur (rouge)
            if fin[0] >= debut[0]:
                return False
        # Le joueur adverse ne peut se deplacer qu'en diagonale vers le haut ou bas si une pièce est promue
            if fin[0] == debut[0] - 1 and (fin[1] == debut[1] + 1 or fin[1] == debut[1] - 1):
                return True

        # Vérifier si la case de départ contient une pièce du joueur, cela permet a un joueur de deplacer que ses pièces pas celles de l'adversaire
        if (player == 1 and pawn != 1) or (player == 2 and pawn != 2):
            return False
        else:
            return True
         
        
    def promote_piece(self, fin):
        ''' Cette fonction permet de promouvoir une pièce.
        Si la pièce atteint la dernière rangée adverse, elle est promue en dame 
        Elle est est donc capable de se deplacer vers le haut, vers le bas en diagonale. 
        Cela signie qu'elle peut capture tous le pions dans sa zone de mouvement
        '''
        if (self.grid[fin[0]][fin[1]] == 1 and fin[0] == 8 - 1) or (self.grid[fin[0]][fin[1]] == 2 and fin[0] == 0):
            self.grid[fin[0]][fin[1]] = 'D'  
            print("piece promue en Dame")
            return True
        else:
            return False


    def move_pawn(self, debut, fin):
        ''' Cette fonction effectue les deplacements du joueur dans la grille.
        Si le deplace est possible alors le joueur peut atteindre une autre case
        '''
        if self.is_valid_move(self,debut, fin):

            self.promote_piece(fin)
            self.grid[fin[0]][fin[1]] = self.grid[debut[0]][debut[1]]
            self.grid[debut[0]][debut[1]] = '-'
            self.selected_piece = None
            return True
        return False
    
    def check_mate(self, player):
        ''' Cette fonction permet d'arreter le jeu si:
    le joueur ne peut plus deplacer ses pieces (bloqué) et meme s'il lui reste des pions ou si on caputure tous ses pions
    '''
        for self.row in range(8):
            for self.col in range(8):
                if self.grid[self.row][self.col] == player:
                    return False


