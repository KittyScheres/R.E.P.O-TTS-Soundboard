import keyboard
import pyttsx3
import subprocess
from KeyBindsParsing import GetKeyBinds
from KeyboardInteraction import SimulateKeyPress, SuspendGameplayInputs, UnSuspendGameplayInputs, T, ENTER, ESCAPE, ALT

# Constants
keybindsFileName = "KeyBinds.json"

# Variables
pressedKey = ""
overrideTtsSoundboard = False

# Text to speech setup
tts = pyttsx3.init()
tts.setProperty("volume", 0)

# Write message with delay of aproximated message length
def WriteMessage(text: str):
    SuspendGameplayInputs()
    SimulateKeyPress(T)
    keyboard.write(text)
    SimulateKeyPress(ENTER)
    UnSuspendGameplayInputs()
    tts.say(text)
    tts.runAndWait()

# Event for when a key has been pressed
def OnEscapePressed(keyboardEvent: keyboard.KeyboardEvent):
    # Access global variables
    global overrideTtsSoundboard

    # Close application if escape is pressed
    if(keyboardEvent.event_type == keyboard.KEY_DOWN):
        overrideTtsSoundboard = True
        

# The main loop of the program
def main():
    # Access global varibles
    global pressedKey
    global overrideTtsSoundboard

    # Initialize application
    keyBinds = GetKeyBinds(keybindsFileName)
    keyboard.hook_key(ESCAPE, OnEscapePressed)

    # Check for closing button press
    while True:

        # Try to run keybind
        pressedKey = str(keyboard.key_to_scan_codes(keyboard.read_key())[0])
        if(pressedKey in keyBinds):
            keybind = keyBinds[pressedKey]
            tts.setProperty("rate", keybind.ttsRate)
            for sentence in keybind.text:
                WriteMessage(sentence)
                if(overrideTtsSoundboard):
                    overrideTtsSoundboard = False
                    break

main()