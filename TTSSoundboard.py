import keyboard
import pyttsx3
from KeyBindsParsing import GetKeyBinds
from KeyboardInteraction import SimulateKeyPress, SuspendGameplayInputs, UnSuspendGameplayInputs, T, ENTER, ESCAPE, ALT

# Constants
keybindsFileName = "KeyBinds.json"

# Variables
pressedKey = ""
escapePressed = False
altPressed = False

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
def OnKeyPressed(keyboardEvent: keyboard.KeyboardEvent):
    # Access global variables
    global escapePressed
    global altPressed
    global pressedKey

    # Close application if escape is pressed
    if(keyboardEvent.scan_code == ESCAPE):
        escapePressed = keyboardEvent.event_type == keyboard.KEY_DOWN

    # Close application if escape is pressed
    if(keyboardEvent.scan_code == ALT):
        altPressed = keyboardEvent.event_type == keyboard.KEY_DOWN
    
    # Process keybind
    stringScanCode = str(keyboardEvent.scan_code)
    if((not pressedKey) and (not escapePressed and not altPressed)):
        pressedKey = stringScanCode
        

# The main loop of the program
def main():
    # Access global varibles
    global pressedKey
    global escapePressed
    global altPressed

    # Initialize application
    keyBinds = GetKeyBinds(keybindsFileName)
    keyboard.hook(OnKeyPressed)

    # Check for closing button press
    while True:

        # Try to run keybind
        if(pressedKey):
            if(pressedKey in keyBinds):
                keybind = keyBinds[pressedKey]
                tts.setProperty("rate", keybind.ttsRate)
                for sentence in keybind.text:
                    WriteMessage(sentence)
            pressedKey = ""

        # Stop application
        if(escapePressed and altPressed):
            break

main()