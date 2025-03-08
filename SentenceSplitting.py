# Constants
CharacterLimit = 49

# Split text by the spesified sentence ending
def SepperateTextByGrammerRule(text: str, splitCharacter: str) -> list:
    sepperatedSentences = text.split(splitCharacter + ' ')
    return sepperatedSentences

# Split a list of sentences by the spesified sentence ending
def SepperateListOfSentencesByGrammerRule(sentenceList: list, splitCharacter: str) -> list:
    result = []
    
    for sentence in sentenceList:
        sepperatedSentences = SepperateTextByGrammerRule(sentence, splitCharacter)
        for sepperatedSentence in sepperatedSentences:
            result.append(sepperatedSentence)

    return result

# Apply english grammer rules for sentences to the provided text
def SepperateByGrammerRules(text: str) -> list:
    sepperatedText = SepperateTextByGrammerRule(text, '.')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, '!')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, '?')
    sepperatedText = SepperateListOfSentencesByGrammerRule(sepperatedText, ',')
    return sepperatedText

# Splits up the provided sentence into sentences that abide by the R.E.P.O character limit
def ApplyCharacterLimit(sentence: str) -> list:
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

# Sepperates all sentences into sentences that abide by the R.E.P.O character limit
def SepperateByCharacterCount(sentences: list) -> list:
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
def TextToSentences(text: str) -> list:
    sentences = SepperateByGrammerRules(text)
    sentences = SepperateByCharacterCount(sentences)
    return sentences