import sys
import re
import json
import pprint

rawphrase = sys.argv[1]
wrd = sys.argv[1]
typesDefault = {
    "NOUN": "n.",
    "PRONOUN": "p.",
    "VERB": "v.",
    "ADJECTIVE": "adj.",
    "ADVERB": "adv.",
    "PREPOSITION": "prep.",
    "CONJUNCTION": "conj.",
    "INTERJECTION": "i."
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
            if element["type"] not in formattedWordObject:
                formattedWordObject.append(element["type"])
    
    # return [{
    #     "word": element["word"],
    #     "type": element["type"]
    # } for element in filteredArray]
    
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
    cleanArray = []
    
    tokenizedToSentences = re.split('\\.|\\?|\\!', data)
    tokenizedToSentencesClean = list(filter(None, tokenizedToSentences))
    for stncs in tokenizedToSentencesClean:
        tokenSntcsHolder = tokenizeSentences(stncs)
        finalArray.append(tokenSntcsHolder)
        
    for fnlarr in finalArray:
        print(fnlarr)
        # cleanArray.append()
        
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