import keyboard
import time
import pyttsx3
import KeyBindsParsing

# Constants
tScanCode = 20
enterScanCode = 28
keybindsFileName = "KeyBinds.json" 

# Text to speech setup
tts = pyttsx3.init()
tts.setProperty("volume", 0)

# Write message with delay of aproximated message length
def WriteMessage(text):
    keyboard.press(tScanCode)
    keyboard.release(tScanCode)
    time.sleep(0.1)
    keyboard.write(text)
    keyboard.press(enterScanCode)
    keyboard.release(enterScanCode)
    tts.say(text)
    tts.runAndWait()

# The main loop of the program
def main():
    keyBinds = KeyBindsParsing.GetKeyBinds(keybindsFileName)
    print("Ready for use")

    while True:

        for keybind in keyBinds:
            if(keyboard.read_key() == keybind.keyCode):
                tts.setProperty("rate", keybind.ttsRate)
                for sentence in keybind.text:
                    WriteMessage(sentence)
            
        if(keyboard.read_key() == "esc"):
            break

main()