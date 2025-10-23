# Display management for ODB-Pi
import pygame
from config import *

def init_display():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("OdB Pi Scanner")
    font = pygame.font.SysFont(FONT_NAME, 22)
    return screen, font
def draw_main_screen(screen, font, dtcs, status_text):
    screen.fill(BLACK)
    title = font.render("OdB Pi Scanner", True, WHITE)
    screen.blit(title, (SCREEN_W// - title.get_width()//2, 20))

    status = font.render(status_text, True, VIOLET)
    screen.blit(status, (20,60))

    y = 100
    if dtcs:
        for code in dtcs:
            line = font.render(code, True, RED)
            screen.blit(line, (40, y))
            y += 30

        else:
            none = font.render("NO DTCs FOUND",True, RED)
            screen.blit(none, (40, y))

        pygame.display.flip()