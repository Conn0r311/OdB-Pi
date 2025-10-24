# logo and splash screen display
import pygame
from config import *

def show_splash(screen, font):
    logo =  r"""


       ____      ______
      / __ \____/ / __ )
     / / / / __  / __  |
    / /_/ / /_/ / /_/ /
    \____/\__,_/_____/  
       ____  _      
      / __ \(_)    
     / /_/ / /      
    / ____/ /      
   /_/   /_/        
                   


    O B D - II  S C A N N E R
    """
    logo = pygame.transform.scale(logo, (200, 100))
    screen.fill(BLACK)
    screen.blit(logo, ((SCREEN_W - 200)//2, 50))
    text = font.render("Connecting to OBD...", True, WHITE)
    screen.blit(text, ((SCREEN_W - text.get_width())//2, 180))
    pygame.display.flip()
    pygame.time.wait(3000)
