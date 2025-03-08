import keyboard
import pyttsx3
from KeyBindsParsing import GetKeyBinds
from KeyboardInteraction import SimulateKeyPress, SuspendGameplayInputs, UnSuspendGameplayInputs, T, ENTER, ESCAPE

# Constants
keybindsFileName = "KeyBinds.json" 

# Variables
pressedKey = ""
closing = False

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

def OnKeyPressed(keyboardEvent: keyboard.KeyboardEvent):
    # Access global variables
    global closing
    global pressedKey

    # Close application if escape is pressed
    if(keyboardEvent.scan_code == ESCAPE):
        closing = True
    
    # Process keybind
    stringScanCode = str(keyboardEvent.scan_code)
    if((not pressedKey) and (not closing)):
        pressedKey = stringScanCode
        

# The main loop of the program
def main():
    # Access global varibles
    global pressedKey
    global closing

    # Initialize application
    keyBinds = GetKeyBinds(keybindsFileName)
    keyboard.hook(OnKeyPressed)
    print("Ready for use")

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
        if(closing):
            break

main()