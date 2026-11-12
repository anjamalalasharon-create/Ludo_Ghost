import pygame
pygame.init()

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

from ici.code.pions import Ghost
from ici.code.logique import Tours
from ici.code.temps import Temps
from ici.code.logique import BLUE_PATH
from ici.code.logique import GREEN_PATH
from ici.code.logique import WHITE_PATH
from ici.code.logique import PURPLE_PATH
from ici.code.des import lancer_de, dessiner_de


WIDTH, HEIGHT= 900, 700
CASE_SIZE = 40
X = 100
Y = 20

GHOST_WHITE = (240, 240, 240)
DARK_GREY = (30, 30, 30)
PURPLE = (128, 0, 128)
GREEN = (50, 205, 50)
BLUE = (0, 100, 255)
BLEU_PROFOND_HAUT = (20, 30, 60)
GRIS_2 = (60, 70, 90, 160)
GRIS_3 = (100, 200, 255)
BLACK = (5, 5, 5)
BLUE_CYAN = (100, 200, 255)

GHOST_SIZE = int(CASE_SIZE * 0.8)

COULEURS_RGB = {
    "Green": (50, 205, 50),
    "White": (200, 200, 200),
    "Purple": (128, 0, 128),
    "Blue": (0, 100, 255)
}


def degrade(win):
    degrade = pygame.Surface((1, 2))
    degrade.set_at((0, 0), GHOST_WHITE)
    degrade.set_at((0, 1), BLUE_CYAN)
    degrade = pygame.transform.smoothscale(degrade, (WIDTH, HEIGHT))
    win.blit(degrade, (0, 0))


def draw_plateau(win):
    for row in range(15):
        for col in range(15):
            x = X + col * CASE_SIZE
            y = Y + row * CASE_SIZE
            rect = pygame.Rect(x, y, CASE_SIZE, CASE_SIZE)

            if (row < 6 and col < 6): 
                color = GREEN             
            elif (row < 6 and col > 8): 
                color = GHOST_WHITE     
            elif (row > 8 and col < 6): 
                color = BLUE            
            elif (row > 8 and col > 8): 
                color = PURPLE          
            elif 6 <= row <= 8 and 6 <= col <= 8:
                color = (60, 60, 60)
            else:
                color = DARK_GREY  
            
            if col == 7 and 0 < row < 7: 
                color = GHOST_WHITE
            elif row == 7 and 7 < col < 14: 
                color = PURPLE
            elif col == 7 and 7 < row < 14: 
                color = BLUE
            elif row == 7 and 0 < col < 7: 
                color = GREEN

            if (row==6 and col==1):
                color = GREEN
            if (row==1 and col==8): 
                color = GHOST_WHITE
            if (row==8 and col==13): 
                color = PURPLE
            if (row==13 and col==6): 
                color = BLUE

            pygame.draw.rect(win, color, rect)
            pygame.draw.rect(win, (50, 50, 50), rect, 1)



def draw_home_circles(win, x_start, y_start, color):
    positions = [
        (1.5, 1.5), (4.5, 1.5),
        (1.5, 4.5), (4.5, 4.5)
    ]
    for px, py in positions:
        center_x = x_start + px * CASE_SIZE
        center_y = y_start + py * CASE_SIZE
        pygame.draw.circle(win, (255, 255, 255), (int(center_x), int(center_y)), int(CASE_SIZE * 0.6))
        pygame.draw.circle(win, (0, 0, 0), (int(center_x), int(center_y)), int(CASE_SIZE * 0.6), 2)



def lancer_le_jeu():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LUDO GHOST!!")
    plateau = pygame.image.load(resource_path("ici/img/plateaux.png"))
    plateau = pygame.transform.scale(plateau,(600, 600))

    icon = pygame.image.load(resource_path("ici/img/icon.png"))
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("LUDO GHOST!!")

    ghost_green = pygame.image.load(resource_path("ici/img/agreen.png"))
    ghost_green = pygame.transform.scale(ghost_green, (GHOST_SIZE, GHOST_SIZE))

    ghost_white = pygame.image.load(resource_path("ici/img/awhite.png"))
    ghost_white = pygame.transform.scale(ghost_white, (GHOST_SIZE, GHOST_SIZE))

    ghost_blue = pygame.image.load(resource_path("ici/img/ablue.png"))
    ghost_blue = pygame.transform.scale(ghost_blue, (GHOST_SIZE, GHOST_SIZE))

    ghost_purple = pygame.image.load(resource_path("ici/img/apurple.png"))
    ghost_purple = pygame.transform.scale(ghost_purple, (GHOST_SIZE, GHOST_SIZE))


    pion_vert1 = Ghost("Green1", "Green",ghost_green, (4, 1))
    pion_vert2 = Ghost("Green2", "Green",ghost_green, (4, 4))
    pion_vert3 = Ghost("Green3", "Green",ghost_green, (1, 1))
    pion_vert4 = Ghost("Green4", "Green",ghost_green, (1, 4))

    pion_bleu1 = Ghost("Blue1", "Blue",ghost_blue, (13, 4))
    pion_bleu2 = Ghost("Blue2", "Blue",ghost_blue, (10, 4))
    pion_bleu3 = Ghost("Blue3", "Blue",ghost_blue, (13, 1))
    pion_bleu4 = Ghost("Blue4", "Blue",ghost_blue, (10, 1))

    pion_violet1 = Ghost("Purple1", "Purple", ghost_purple, (10, 13))
    pion_violet2 = Ghost("Purple2", "Purple", ghost_purple, (13, 13))
    pion_violet3 = Ghost("Purple3", "Purple", ghost_purple, (10, 10))
    pion_violet4 = Ghost("Purple4", "Purple", ghost_purple, (13, 10))

    pion_blanc1 = Ghost("White1", "White", ghost_white, (1, 10) )
    pion_blanc2 = Ghost("White2", "White", ghost_white, (1, 13) )
    pion_blanc3 = Ghost("White3", "White", ghost_white, (4, 10) )
    pion_blanc4 = Ghost("White4", "White", ghost_white, (4, 13) )

    tous_les_pions = [
        pion_vert1, pion_vert2, pion_vert3, pion_vert4,
        pion_bleu1, pion_bleu2, pion_bleu3, pion_bleu4,
        pion_violet1, pion_violet2, pion_violet3, pion_violet4,
        pion_blanc1, pion_blanc2, pion_blanc3, pion_blanc4
    ]


    gestionnaire = Tours()
    valeur_de = 0
    attend_choix_pion = False


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not attend_choix_pion:
                    valeur_de = lancer_de()
                    couleur_actuelle = gestionnaire.joueur_actuel()
                    print(f"Dé : {valeur_de} pour {couleur_actuelle}")
                    
                    peut_bouger = False
                    for p in tous_les_pions:
                        if p.color_type == couleur_actuelle:
                            if not p.is_home or valeur_de == 6:
                                peut_bouger = True
                                break
                    
                    if peut_bouger:
                        attend_choix_pion = True
                    else:
                        print(f"Aucun mouvement possible pour {couleur_actuelle}, tour suivant !")
                        gestionnaire.passer_au_suivant()
                        attend_choix_pion = False

            if event.type == pygame.MOUSEBUTTONDOWN and attend_choix_pion:
                pos_souris = pygame.mouse.get_pos()
                pion_a_effectivement_bouge = False
                
                for pion in tous_les_pions:
                    if pion.color_type == gestionnaire.joueur_actuel():
                        pion_rect = pygame.Rect(X + pion.grid_pos[1]*CASE_SIZE, Y + pion.grid_pos[0]*CASE_SIZE, CASE_SIZE, CASE_SIZE)
                        
                        if pion_rect.collidepoint(pos_souris):
                            if not pion.is_home or valeur_de == 6:
                                chemins = {"Green": GREEN_PATH, "Blue": BLUE_PATH, "Purple": PURPLE_PATH, "White": WHITE_PATH}
                                pion.move(valeur_de, chemins[pion.color_type])
                                pion_a_effectivement_bouge = True
                                
                                for autre in tous_les_pions:
                                    if autre != pion and autre.grid_pos == pion.grid_pos and not autre.is_home:
                                        if autre.color_type != pion.color_type:
                                            autre.grid_pos = autre.start_pos
                                            autre.is_home = True
                                            autre.path_index = -1
                                            print(f"MANGÉ ! {pion.color_name} a renvoyé {autre.color_name}")
                                break 

                if pion_a_effectivement_bouge:
                    gestionnaire.passer_au_suivant()
                    attend_choix_pion = False
                pions_finis = [p for p in tous_les_pions if p.color_type == couleur_actuelle and p.path_index == len(chemins[p.color_type]) - 1]
                if len(pions_finis) == 4:
                    print(f"Le joueur {couleur_actuelle} a gagné !")

        degrade(screen)
        draw_plateau(screen)
        screen.blit(plateau, (100,20))
        texte_chrono = Temps()
        screen.blit(texte_chrono, (720, 220)) 
        
        for pion in tous_les_pions:
            pion.draw(screen, CASE_SIZE, X, Y)

        if valeur_de > 0:
            c_rgb = COULEURS_RGB.get(gestionnaire.joueur_actuel(), (0,0,0))
            dessiner_de(screen, valeur_de, 720, 100, c_rgb)

        font_tour = pygame.font.SysFont("Arial", 25, bold=True)
        couleur_txt = COULEURS_RGB.get(gestionnaire.joueur_actuel(), BLACK)
        txt_tour = font_tour.render(f"Tour : {gestionnaire.joueur_actuel()}", True, couleur_txt)
        screen.blit(txt_tour, (720, 180))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
