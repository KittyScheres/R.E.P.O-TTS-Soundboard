import json
from SentenceSplitting import TextToSentences

# Constants
keybindsLable = "Keybinds"
keyCodeLable = "KeyCode"
ttsRateLable = "TtsRate"
textLable = "Text"

# Structure for storing keybinds
class Keybind:
    ttsRate: int = 120
    text: list = []
    
    def __init__(self, ttsRate, text):
        self.ttsRate = ttsRate
        self.text = text

    def __str__(self):
        return f"({self.ttsRate},{self.text})"

# Read the provided json file
def ReadJsonFile(fileName: str) -> list:
    fileContent = {}
    with open(fileName) as file:
        fileContent = json.load(file)
    return fileContent

# Parse and store all keybinds in the json data
def ParseJsonData(jsonData: json) -> dict:
    result = {}
    keyBinds = jsonData[keybindsLable]

    for keyBind in keyBinds:
        keyCode = keyBind[keyCodeLable]
        ttsRate = keyBind[ttsRateLable]
        text = TextToSentences(keyBind[textLable])
        result[str(keyCode)] = Keybind(ttsRate, text)
    
    return result

# Read keybinds from the provided json file
def GetKeyBinds(fileName: str) -> dict:
    jsonData = ReadJsonFile(fileName)
    keyBinds = ParseJsonData(jsonData)
    return keyBinds