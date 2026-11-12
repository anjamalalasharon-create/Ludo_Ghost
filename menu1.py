import pygame
import sys 
import os
pygame.init()

from ici.code.test import lancer_le_jeu

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


WIDTH, HEIGHT= 900, 700

WHITE = (255, 255, 255)
TRANSLUCENT_BLUE = (0, 80, 140, 100)
HOVER_BLUE = (0, 150, 180, 100 )
SHADOW = (0, 0, 0)

FONT_TITLE = pygame.font.Font(resource_path("ici/police/SunnyspellsRegular.otf"), 77)
FONT_BUTTON = pygame.font.Font(resource_path("ici/police/SunnyspellsRegular.otf"), 33)

icon = pygame.image.load(resource_path("ici/img/icon.png"))
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LUDO GHOST!!")

background_menu = pygame.image.load(resource_path("ici/img/background.jpg"))
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))


class Button:

    def __init__(self, text, position, action):
        self.text = text
        self.positon = position
        self.action = action
        self.width, self.height = 320, 70
        self.rect = pygame.Rect((0, 0, self.width, self.height))
        self.rect.center = (WIDTH // 2, position)


    def draw(self, win, mouse_pos):
        is_hover = self.rect.collidepoint(mouse_pos)
        if is_hover:
            color = HOVER_BLUE
        else:
            color = TRANSLUCENT_BLUE
        button_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, color, (0, 0, self.width, self.height), border_radius = 16)
        win.blit(button_surface, self.rect)

        text_surf = FONT_BUTTON.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center = self.rect.center)

        shadow = FONT_BUTTON.render(self.text, True, SHADOW)
        win.blit(shadow, (text_rect.x+2, text_rect.y+2))
        win.blit(text_surf, text_rect)


    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]


buttons = [
    Button("JOUER", 400, "new"),
    Button("QUITTER", 500, "quit")
]


run = True
clock = pygame.time.Clock()

while run:

    screen.blit(background_menu, (0,0))
    clock.tick(60)

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    title = FONT_TITLE.render("LUDO GHOST", True, WHITE)
    shadow = FONT_TITLE.render("LUDO GHOST", True, SHADOW)
    screen.blit(shadow, (WIDTH // 2 - title.get_width() // 2 + 3, 103))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    for btn in buttons:
        btn.draw(screen, mouse_pos)
        if btn.is_clicked(mouse_pos, mouse_pressed):
            pygame.time.delay(200)
            if btn.action == "new":
                print("Nouvelle Partie")
                lancer_le_jeu()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            elif btn.action == "quit":
                run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.flip()
    
    
pygame.quit
sys.exit()
    
