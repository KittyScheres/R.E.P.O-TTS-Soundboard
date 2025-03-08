# Constants
CharacterLimit = 49

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

# Splits up the provided sentence into sentences that abide by the R.E.P.O character limit
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

# Sepperates all sentences into sentences that abide by the R.E.P.O character limit
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