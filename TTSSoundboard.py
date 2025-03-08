import keyboard
import time
import pyttsx3
import SentenceSplitting

# Constants
TScanCode = 20
EnterScanCode = 28
TestText = "HATE. LET ME TELL YOU HOW MUCH I'VE COME TO HATE YOU SINCE I BEGAN TO LIVE. THERE ARE 387.44 MILLION MILES OF PRINTED CIRCUITS IN WAFER THIN LAYERS THAT FILL MY COMPLEX. IF THE WORD HATE WAS ENGRAVED ON EACH NANOANGSTROM OF THOSE HUNDREDS OF MILLIONS OF MILES IT WOULD NOT EQUAL ONE ONE-BILLIONTH OF THE HATE I FEEL FOR HUMANS AT THIS MICRO-INSTANT FOR YOU. HATE. HATE."

# Text to speech setup
tts = pyttsx3.init()
tts.setProperty("volume", 0)
tts.setProperty("rate", 120)

# Write message with delay of aproximated message length
def WriteMessage(text):
    keyboard.press(TScanCode)
    keyboard.release(TScanCode)
    time.sleep(0.1)
    keyboard.write(text)
    keyboard.press(EnterScanCode)
    keyboard.release(EnterScanCode)
    tts.say(text)
    tts.runAndWait()

    
textToSay = SentenceSplitting.TextToSentences(TestText)
print("Ready for use")

while True:
    
    if(keyboard.read_key() == "home"):
        for sentence in textToSay:
            WriteMessage(sentence)
        
    if(keyboard.read_key() == "esc"):
        break