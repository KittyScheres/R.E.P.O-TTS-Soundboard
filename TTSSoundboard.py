import keyboard
import time
import pyttsx3

# Constants
TScanCode = 20
EnterScanCode = 28
CharacterLimit = 49
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

# Split text by the spesified sentence ending
def SepperateTextByGrammerRule(text, splitCharacter):
    sepperatedSentences = text.split(splitCharacter + ' ')
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
    sepperatedText = SepperateTextByGrammerRule(text, '.')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, '!')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, '?')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, ',')
    return sepperatedText

def ApplyCharacterLimit(sentence):
    result = []
    wordsInSentence = sentence.split(' ')
    newSentence = ""

    for word in wordsInSentence:
        if((len(newSentence) + len(word)) > CharacterLimit):
            result.append(newSentence[:-1])
            newSentence = ""
        newSentence += word + ' '

    result.append(newSentence[:-1])
    return result

def SepperateByCharacterCount(sentences):
    result = []

    for sentence in sentences:
        if(len(sentence) > CharacterLimit):
            sepperatedSentence = ApplyCharacterLimit(sentence)
            for sentencePart in sepperatedSentence:
                result.append(sentencePart)
        else:
            result.append(sentence)

    return result

# Split up the text to make it possible to write out in R.E.P.O
def TextToSentences(text):
    sentences = SepperateByGrammerRules(text)
    sentences = SepperateByCharacterCount(sentences)
    return sentences

textToSay = TextToSentences(TestText)

print("Ready for use")

while True:
    
    if(keyboard.read_key() == "home"):
        for sentence in textToSay:
            WriteMessage(sentence)
        
    if(keyboard.read_key() == "esc"):
        break