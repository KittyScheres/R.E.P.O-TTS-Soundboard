import json
import SentenceSplitting

# Constants
keybindsLable = "Keybinds"
keyCodeLable = "KeyCode"
ttsRateLable = "TtsRate"
textLable = "Text"

# Structure for storing keybinds
class Keybind:
    keyCode = ""
    ttsRate = 120
    text = []
    
    def __init__(self, keyCode, ttsRate, text):
        self.keyCode = keyCode
        self.ttsRate = ttsRate
        self.text = text

    def __str__(self):
        return f"({self.keyCode},{self.ttsRate},{self.text})"

# Read the provided json file
def ReadJsonFile(fileName):
    fileContent = {}
    with open(fileName) as file:
        fileContent = json.load(file)
    return fileContent

# Parse and store all keybinds in the json data
def ParseJsonData(jsonData):
    result = []
    keyBinds = jsonData[keybindsLable]

    for keyBind in keyBinds:
        keyCode = keyBind[keyCodeLable]
        ttsRate = keyBind[ttsRateLable]
        text = SentenceSplitting.TextToSentences(keyBind[textLable])
        result.append(Keybind(keyCode, ttsRate, text))
    
    return result

# Read keybinds from the provided json file
def GetKeyBinds(fileName):
    jsonData = ReadJsonFile(fileName)
    keyBinds = ParseJsonData(jsonData)
    return keyBinds