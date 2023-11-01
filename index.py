import sys
import re
import json
import pprint

rawphrase = sys.argv[1]
wrd = sys.argv[1]
typesDefault = {
    "n.": "NOUN",
    "p.": "PRONOUN",
    "pron.": "PRONOUN",
    "v.": "VERB",
    "adj.": "ADJECTIVE",
    "adv.": "ADVERB",
    "prep.": "PREPOSITION",
    "conj.": "CONJUNCTION",
    "i.": "INTERJECTION"
}

def fetchWordFiltered(wrdprop):
    nlpdictionary = open("./resources/nlp_dictionary.json")
    data = json.load(nlpdictionary)
    filteredArray = [x for x in data if x['word'] == wrdprop]
    
    formattedWordHolder = wrdprop
    formattedWordObject = []
    
    for element in filteredArray:
        formattedWordHolder = element["word"]
        
        if element["type"] != "()":
            splitstring = element["type"].replace("(", "").replace(")", "").replace("&", "")
            splitstringarray = splitstring.split()
            
            for splits in splitstringarray:
                for key in typesDefault:
                    if splits == key:
                        if typesDefault[splits] not in formattedWordObject:
                            formattedWordObject.append(typesDefault[splits])
                    else:
                        refurbishedsplit = f"({splits})"
                        if splits not in typesDefault.keys():
                            if refurbishedsplit not in formattedWordObject:
                                formattedWordObject.append(refurbishedsplit)
    
    return {
        "word": formattedWordHolder,
        "type": formattedWordObject
    }

def tokenizeSentences(sentence):
    seekDefArray = []
    splitWords = re.split(' |\\,|\\"|\\(|\\)|\\”|\\“', sentence)
    splitWordsClean = list(filter(None, splitWords))
    splitWordsCapitalized = [cap.capitalize() for cap in splitWordsClean]
    for seekDefwrd in splitWordsCapitalized:
        checkArray = fetchWordFiltered(seekDefwrd)
        if(checkArray):
           if(len(checkArray) > 0):
                seekDefArray.append(checkArray)
    
    return seekDefArray

def tokenization(data):
    finalArray = []
    # cleanArray = []
    
    tokenizedToSentences = re.split('\\.|\\?|\\!', data)
    tokenizedToSentencesClean = list(filter(None, tokenizedToSentences))
    for stncs in tokenizedToSentencesClean:
        tokenSntcsHolder = tokenizeSentences(stncs)
        finalArray.append(tokenSntcsHolder)
      
    print(finalArray)
    
tokenization(rawphrase)
    
# fetchWordFiltered(wrd)

def getWordTypes():
    nlpdictionary = open("./resources/nlp_dictionary.json")
    data = json.load(nlpdictionary)
    filteredDuplicates = []
    typesArray = [typex["type"] for typex in data]
    [filteredDuplicates.append(x) for x in typesArray if x not in filteredDuplicates]
    
    print(filteredDuplicates)
    
# getWordTypes()