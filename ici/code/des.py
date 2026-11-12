import pygame
import random

def lancer_de():
    return random.randint(1, 6)

def dessiner_de(screen, valeur, x, y, couleur): 
    rect = pygame.Rect(x, y, 60, 60)
    pygame.draw.rect(screen, (255, 255, 255), rect, border_radius=10)
    
    pygame.draw.rect(screen, couleur, rect, 4, border_radius=10) 
    
    font = pygame.font.SysFont("Arial", 40, bold=True)
    texte = font.render(str(valeur), True, (0, 0, 0))
    text_rect = texte.get_rect(center=rect.center)
    screen.blit(texte, text_rect)
