import sys
import re
import json

rawphrase = sys.argv[1]
wrd = sys.argv[1]

def fetchWordFiltered(wrdprop):
    nlpdictionary = open("./resources/nlp_dictionary.json")
    data = json.load(nlpdictionary)
    filteredArray = [x for x in data if x['word'] == wrdprop]
    
    return [{
        "word": element["word"],
        "type": element["type"]
    } for element in filteredArray]

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
    
    tokenizedToSentences = re.split('\\.|\\?|\\!', data)
    tokenizedToSentencesClean = list(filter(None, tokenizedToSentences))
    for stncs in tokenizedToSentencesClean:
        tokenSntcsHolder = tokenizeSentences(stncs)
        finalArray.append(tokenSntcsHolder)
        
    print(finalArray)
    
tokenization(rawphrase)
    
# fetchWordFiltered(wrd)