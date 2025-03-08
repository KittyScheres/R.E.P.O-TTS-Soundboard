import keyboard
import time
import pyttsx3

# Constants
TScanCode = 20
EnterScanCode = 28
CharacterLimit = 50
TestText = "Welcome to the internet. Have a look around. Anything, that brain of yours can think off can be found"

# Text to speech setup
tts = pyttsx3.init()
tts.setProperty("volume", 0)
tts.setProperty("rate", 170)

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

# Split text by the spesified sentence ending
def SepperateTextByGrammerRule(text, splitCharacter):
    sepperatedSentences = text.split(splitCharacter + " ")
    return sepperatedSentences

# Split a list of sentences by the spesified sentence ending
def SepperateListOfSentencesByGrammerRule(sentenceList, splitCharacter):
    result = []
    for sentence in sentenceList:
        sepperatedSentences = SepperateTextByGrammerRule(sentence, splitCharacter)
        for sepperatedSentence in sepperatedSentences:
            result.append(sepperatedSentence)
    return result

# Apply english grammer rules for sentences to the provided text
def SepperateByGrammerRules(text):
    sepperatedText = SepperateTextByGrammerRule(text, ".")
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, "!")
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, "?")
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, ",")
    return sepperatedText

# Split up the text to make it possible to write out in R.E.P.O
def SplitUpText(text):
    sentencesSepperatedByGrammer = SepperateByGrammerRules(text)
    return sentencesSepperatedByGrammer

textToSay = SplitUpText(TestText)

print("Ready for use")

while True:
    
    if(keyboard.read_key() == "home"):
        for sentence in textToSay:
            WriteMessage(sentence)
        
    if(keyboard.read_key() == "esc"):
        break