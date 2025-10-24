import RPi.GPIO as GPIO
import time

# Button pin layout
BUTTONS = {
    "select": 5,
    "next": 6,
    "prev": 13,
    "reset": 19
}

def setup_buttons():
    GPIO.setmode(GPIO.BCM)
    
    for pin in BUTTONS.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_pressed_button():
    """Check which button is pressed"""
    for name, pin in BUTTONS.items():
        if GPIO.input(pin) == GPIO.LOW:
            time.sleep(0.2)
            return name
    return None