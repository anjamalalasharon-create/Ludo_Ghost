import pygame

pygame.init()

BLACK = (0, 0, 0)
def Temps():
    temps_de_jeu = pygame.time.get_ticks()
    secondes_totale = temps_de_jeu // 1000
    minutes = secondes_totale //60
    secondes = secondes_totale % 60

    police_temps = pygame.font.Font("ici/police/SunnyspellsRegular.otf", 21)
    format_texte = f"TEMPS: {minutes:02d}:{secondes:02d}"
    texte_temps = police_temps.render(format_texte, True, BLACK)
    return texte_temps
