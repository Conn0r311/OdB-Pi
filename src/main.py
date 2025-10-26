from display import init_display, draw_main_screen
from obd_reader import connect_obd, get_dtc_codes, clear_codes 
from buttons import setup_buttons, get_pressed_button 
#from splash import show_splash
from config import *
try:
    import obd  # real OBD library (on Raspberry Pi)
except (ImportError, RuntimeError):
    import fake_obd as obd  # use the fake module on PC
import pygame
import time 


def main():
    screen, font = init_display()
    #show_splash(screen, font)
    setup_buttons()

    connection = connect_obd()
    dtcs = []
    status = "Ready"

    running = True
    while running:
        button = get_pressed_button()

        match button:
            case "select":
                dtcs = get_dtc_codes(connection)
                status = f"{len(dtcs)} Codes Found" if dtcs else "No Codes"
                
            case "reset":
                clear_codes(connection)
                status = "Codes Cleared"
                dtcs = []
                
            case "next":
                status = "Next → (Feature Coming)"
                
            case "prev":
                status = "Prev ← (Feature Coming)"
                
            case _:
                pass
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_main_screen(screen, font, dtcs, status)
        time.sleep(0.1)

    pygame.quit()

if __name__ == "__main__":
    main()
