import keyboard
import time

# Simulate pin states: 1 = HIGH (not pressed), 0 = LOW (pressed)
pin_states = {}

# GPIO constants
BOARD = "BOARD"
BCM = "BCM"
IN = "IN"
OUT = "OUT"
PUD_UP = "PUD_UP"
LOW = 0
HIGH = 1

# Map pins to keys
pin_keys = {
    5: 'w',   # select
    6: 'x',   # next
    13: 's',  # prev
    19: 'r'   # reset
}

def setmode(mode):
    print(f"[MOCK GPIO] Set mode: {mode}")

def setup(pin, mode, pull_up_down=None):
    pin_states[pin] = HIGH  # pull-up: default state is HIGH
    print(f"[MOCK GPIO] Setup pin {pin} as {mode}, pull_up_down={pull_up_down}")

def input(pin):
    key = pin_keys.get(pin)
    if key and keyboard.is_pressed(key):
        pin_states[pin] = LOW
    else:
        pin_states[pin] = HIGH
    return pin_states[pin]

def cleanup():
    print("[MOCK GPIO] Cleanup called")
    pin_states.clear()
