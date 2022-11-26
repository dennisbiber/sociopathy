import json
import numpy
import os
import pprint
import random
import statistics
import sys
import time

HOME_DIR = os.path.expanduser("~")
filename = HOME_DIR + "/data/sociopathy/languageStruct.json"
consonantList = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q",
                  "r", "s", "t", "v", "w", "x", "y", "z"]

phonetic2ConsonantDict = {"ph": "f",
                          "th": "t",
                          "cs": "x"}

vowelsList = ["a", "e", "i", "o", "u", "y"]
questionWords = ["who", "what", "when", "where", "why", "how"]


def openLanguageStruct(filename = filename):
    lingualStructs = None
    with open(filename, "r") as f:
        lingualStructs = json.load(f)
    return lingualStructs["words"], lingualStructs["prefix"], lingualStructs["suffix"]


def hyphinatedSplit(word):
    return word.split("-")


def changeDegree():
    return [-4, -3, -2, -1, 0, 1, 2, 3, 4]


def stdDev(qualities):
    # direction: Positive = True, Negative = False
    direction = None
    average = sum(qualities)/len(qualities)
    averageDigitLength = len(f"{average}".replace("-", "").replace(".", ""))
    if "-" in f"{average}":
        direction = False
    elif "-" not in f"{average}":
        direction = True
    factor = 10**averageDigitLength
    return [((((x-average)*factor)/factor)**2)/len(qualities) for x in qualities], direction


def unpackNestedList(listylist):
    masterList = []
    for listeroo in listylist:
        lenCount = 0
        listLen = len(listeroo)
        while lenCount < listLen:
            masterList.append(listeroo[lenCount])
            lenCount += 1
    return masterList


def wordPointAwarder(textSegment, words):
    if textSegment in words.keys():
        if words[textSegment.lower()]["state"] == 2:
            return 1
        elif words[textSegment.lower()]["state"] == 3:
            return 2
        elif words[textSegment.lower()]["state"] == 1:
            return 0
        elif words[textSegment.lower()]["state"] == -1:
            return -2
    else:
        if 2 in [words[x.lower()]["state"] for x in words.keys() if textSegment in words[x]["define"]]:
            return 1
        elif 3 in [words[x.lower()]["state"] for x in words.keys() if textSegment in words[x]["define"]]:
            return 2
        elif 1 in [words[x.lower()]["state"] for x in words.keys() if textSegment in words[x]["define"]]:
            return 0
        elif -1 in [words[x.lower()]["state"] for x in words.keys() if textSegment in words[x]["define"]]:
            return -2


def wordValuation(textSegment, words):
    if type(textSegment) == str:
        if textSegment.lower() in words.keys():
            return textSegment, wordPointAwarder(textSegment, words)
        elif textSegment.lower() in unpackNestedList([words[x]["define"] for x in words.keys()]):
            return textSegment, wordPointAwarder(textSegment, words)
        else:
            return textSegment, wordPointAwarder(textSegment, words)

def wordListOrganize(wordList, textList):
    textStruct = {}
    for variable in wordList:
        word = variable[0]
        value = variable[-1]
        if word.lower() in textList:
            textStruct[word] = {"value": value,
                                "index": textList.index(word)}
            if value >= 0:
                value = 1
            elif value < 0:
                value = -1
            textList[textStruct[word]["index"]] = value
        elif word.capitalize() in textList:
            textStruct[word] = {"value": value,
                                "index": textList.index(word.capitalize())}
            if value >= 0:
                value = 2
            elif value < 0:
                value = -2
            textList[textStruct[word]["index"]] = value
        elif word.lower() in questionWords:
            textStruct[word] = {"value": value,
                                "index": textList.index(word.capitalize())}
            if value >= 0:
                value = 2
            elif value < 0:
                value = -2
            textList[textStruct[word]["index"]] = value
        else:
            textList[textStruct[word]["index"]] = 0
    return textList, textStruct


def prefixValuation(textSegment, prefix):
    if type(textSegment) == str:
        if textSegment in prefix.keys():
            return prefixCondition(textSegment, prefix)
            
        elif [x for x in prefix.values() if textSegment in x["logic"]]:
            textSegmentRoot = [x for x in prefix.keys() if textSegment in prefix[x]["logic"]][0]
            return prefixCondition(textSegmentRoot, prefix, textSegmentOption=textSegment)


        elif textSegment[0:-1] in prefix.keys():
            print(textSegment)

    # return 0, textSegment, textSegment
            

def prefixCondition(textSegment, prefix, textSegmentOption = False):
    logicSense = None
    randLogic = None
    senticValue = 0
    randLogic = random.randint(0, len(prefix[textSegment]["logic"]))-1
    sentic = prefix[textSegment]["sentic"]
    if textSegment in prefix.keys():
        if sentic.lower() == "negative":
            senticValue -= 1
        elif sentic.lower() == "positive":
            senticValue += 1
        elif sentic.lower() == "neutral":
            senticValue = senticValue
        if randLogic != None:
            logicSense = prefix[textSegment]["logic"][randLogic]
        
        if textSegmentOption != False:
            return senticValue, logicSense, textSegmentOption
        else:
            if logicSense != None:
                return senticValue, logicSense, textSegment



def prefixListOrganize(prefixList, textList, textStruct):
    for x in prefixList:
        if x != None:
            value = x[0]
            prefixObject = x[-1]

            if prefixObject in textList:
                textList, textStruct = Conditon(textList, prefixObject, textStruct, value)
            
            elif prefixObject[-1] in vowelsList:
                prefixObject = prefixObject[0:-1]
                textList, textStruct = Conditon(textList, prefixObject, textStruct, value)

    return textList, textStruct


def Conditon(textList, Object, textStruct, value):
    textStruct[Object] = {"value": value,
                          "index": textList.index(Object)}
    textList[textStruct[Object]["index"]] = value
    
    return textList, textStruct


def suffixValuation(textSegment, textStruct, suffix):
    value = None
    if textSegment.lower() in suffix.keys():
        former = suffix[textSegment.lower()]["former"]
        latter = suffix[textSegment.lower()]["latter"]
        state = suffix[textSegment.lower()]["state"]
        if former not in latter:
            if state == "present":
                value = 1
            elif state == "future":
                value = 2
            elif state == "past":
                value = 0
            else:
                sys.exit()
        elif former in latter:
            if former == "adjective":
                value = 2
            if former == "verb":
                value = 3
            if former == "noun":
                value = 4

    elif textSegment.lower() in vowelsList:
        value = 0

    return textSegment, value


def suffixListOrganize(suffixList, textList, textStruct):
    for x in suffixList:
        suffixObject = x[0]
        value = x[-1]

        if suffixObject in textList:
            textList, textStruct = Conditon(textList, suffixObject, textStruct, value)
    
        elif suffixObject[0] in vowelsList:
            suffixObject = suffixObject[0]
            textList, textStruct = Conditon(textList, suffixObject, textStruct, value)

    return textList, textStruct


def Energize(qualities):
    if type(qualities) == list:
        stdev, direction = stdDev(qualities)
        std = statistics.stdev(stdev)
        if direction == True:
            std = 0 + std
        elif direction == False:
            std = 0 - std
        else:
            return 0
        return std
    elif type(qualities) == str:
        bla = True
    else:
        return 0


def Dopamine(qualities):
        # qualitites = List()
        # sentiment reward system
        # motivations
        # memory and postivity/negativity toward sentiment
    value = Energize(qualities)
    if type(value) == float:
        variant = value
        return variant
    elif type(value) == str:
        speech = value
        return speech
    else:
        return 0


def Histamine(quantites):
    # attention ability
    # endocrine function (Hormones)
    return time.sleep(abs(Socialize(quantites)))


class Serotonin():
    # desire 
    # imagination
    def __init__(self, qualities, _sC=False, _iC=False, _sR=False):
        self._inert_model = {}
        self._sC = _sC
        self._iC = _iC
        self._sR = _sR
        self._qualities = qualities

    def socioComfortAlters(self):
        confidenceDegree = statistics.median(self._qualities)
        relaxedDegree = statistics.mode(self._qualities)
        return relaxedDegree, confidenceDegree

    def isoComfortAlters(self):
        bookInputDegree = 0
        artInputDegree = 0
        return bookInputDegree, artInputDegree

    def socioRadicalAlters(self):
        phonicInputDegree = 0
        verbalInputDegree = 0
        return phonicInputDegree, verbalInputDegree

    def modelReturn(self):
        if self._sC:
            return sum(self.socioComfortAlters())/len(dir(self.socioComfortAlters()))
        elif self._iC:
            return sum(self.isoComfortAlters())/len(dir(self.isoComfortAlters()))
        elif self._sR:
            return sum(self.socioRadicalAlters())/len(dir(self.socioRadicalAlters()))


def Socialize(qualities):
    if type(qualities) == list:
        summation = sum(qualities)
        if summation > 4:
            return 4
        elif summation < -4:
            return -4
        return summation


def GABA(qualities):
    # social reward system
    # nuerotics
    seroLevels = Serotonin(qualities, _sC=True).modelReturn()
    return Socialize(qualities)
    

def Neuradrenline():
    # Norepinephrine (Neural Adrenaline)
    # attention desire
    # affects time of responding
    attentionDegrees = changeDegree()

def Glutamate():
    # Learning (Reinforcement Learning)
    attentionDegrees = changeDegree()

def Acetylcholine():
    # cooridnation 
    # timing synchricity
    attentionDegrees = changeDegree()


def isWord(textSegment, words):
    if textSegment in words.keys():
        return True
    elif textSegment in unpackNestedList([words[x]["define"] for x in words.keys()]):
        return True
    return False


def doubleSylabulValidator(word):

    stringPatternCheck = getPattern(word)

    words, prefix, suffix = openLanguageStruct()
    wordLogic = []
    for key in words.keys():
        wordLogic += words[key]["define"]
    wordLogic += [*words.keys()]
    wordLogic = set(wordLogic)

    prefixLogic = []
    for key in prefix.keys():
        prefixLogic[-1:] = prefix[key]["logic"]
    prefixLogic += [*prefix.keys()]
    prefixLogic = set(prefixLogic)

    suffixLogic = [*suffix.keys()]
    suffixFound = False

    wordLen = len(word)
    loopLen = 0
    def findWords(loopLen, wordLen, word, wordLogic):
        while loopLen != wordLen:
            if word[0:loopLen] in wordLogic and word[loopLen::] in wordLogic:
                word = [word[0:loopLen], word[loopLen::]]
                break
            loopLen += 1
    item = findWords(loopLen, wordLen, word, wordLogic)
    if item != None:
        word = item 
    if not suffixFound:
        result = checkForSuffix(word, suffixLogic)
        suffixFound = True
    else:
        result = word
    if result != word and type(result) == list:
        blob = repeatCheckForStruct(result[0], prefixLogic, wordLogic)
        if type(blob) == list:
            result[:-1] = blob
        elif type(blob) == str:
            result[0] = blob
    else:
        blob = repeatCheckForStruct(word, prefixLogic, wordLogic)
        return blob
    if result != None:
        return result

def checkForSuffix(word, suffixKeys):
    pattern = getPattern(word)
    lenCheck = 0
    for suf in suffixKeys:
        def checker(word, suf):
            if suf == word[-len(suf)::]:
                return len(suf)
            return 0
        if len(suf) >= lenCheck:
            new = checker(word, suf)
            if new > lenCheck:
                lenCheck = new
    if lenCheck != 0:
        return [word[0:-lenCheck], word[-lenCheck::]]
    else:
        return None


def getPattern(word):
    stringPatternCheck = ""
    for x in range(len(word)):
        if x != len(word):
            letter = word[x]
            if letter in vowelsList:
                if [0, "y"] == [x, letter.lower()]:
                    stringPatternCheck += "C"
                elif [not 0, "y"] == [x, letter.lower()]:
                    stringPatternCheck += "V"
                else:
                    stringPatternCheck += "V"
            elif letter in consonantList:
                stringPatternCheck += "C"
    return stringPatternCheck


def validateWords(startsegment, endSegment, prefixKeys, wordsKeys):
    nonWordLetters = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]
    if startsegment in prefixKeys and endSegment in prefixKeys:
        return True
    elif startsegment in prefixKeys and endSegment in wordsKeys:
        return True
    elif startsegment in wordsKeys and endSegment in wordsKeys:
        return True
    elif startsegment in wordsKeys and endSegment in prefixKeys:
        return True
    elif startsegment in wordsKeys and len(endSegment) == 1 and endSegment not in nonWordLetters:
        return True
    elif startsegment in prefixKeys and len(endSegment) == 1 and endSegment not in nonWordLetters:
        return True
    return False


def repeatCheckForStruct(word, prefixKeys, wordsKeys, final = None):
    if type(word) == list:
        word = word[0]
    rootFound = False
    lenValue = 0
    newStuff = None
    for root in wordsKeys:
        if len(root) >= lenValue:
            if len(root) > 1:
                if root == word:
                    rootFound = True
                    lenValue = len(root)
                elif root in word and root == word[0:len(root)]:
                    lenValue = len(root)
                    theIndex = len(root)
                    if validateWords(word[0:theIndex], word[theIndex::], prefixKeys, wordsKeys):
                        newStuff = [word[0:theIndex], word[theIndex::]]
                    rootFound = True
                elif root in word and root == word[-len(root)::]:
                    lenValue = len(root)
                    theIndex = lenValue
                    if validateWords(word[0:-theIndex], word[-theIndex::], prefixKeys, wordsKeys):
                        newStuff = [word[0:-theIndex], word[-theIndex::]]
                    rootFound = True
    if rootFound and newStuff != None:
        if final != None and newStuff != None:
            final[-1:] = newStuff
        elif newStuff != None:
            final = newStuff
    if rootFound == False:
        result = checkForStruct(word, prefixKeys)
        if result != None:
            if len(result) >= 2:
                if final == None:
                    final = result
                else:
                    final[-1:] = result
            repeatCheckForStruct(result[-1], prefixKeys, wordsKeys, final=final)

    if final != None:
        return final
    elif final == None:
        return word


def checkForStruct(word, prefixKeys):
    if type(word) == list:
        word = word[0]
    pattern = getPattern(word)
    if pattern[0:3] == "VCV" and word[0:2] in prefixKeys:
        return [word[0:2], word[2::]]
    elif pattern[0:3] == "VCC" and word[1] == word[2]:
        return [word[0:2], word[2::]]
    elif pattern[0:3] == "VCC" and word[0:2] in prefixKeys:
        return [word[0:2], word[2::]]
    elif pattern[0:4] == "CVCC" and word[2] == word[3] and word[2::] != word[-2::]:
        return [word[0:3], word[3::]]
    elif pattern[0:3] == "CVV" and word[0:2]in prefixKeys:
        return [word[0:2], word[2::]]
    elif pattern[0:3] == "CVC" and word[0:2]in prefixKeys and word[0:3] not in prefixKeys:
        return [word[0:2], word[2::]]
    elif pattern[0:3] == "CVC" and word[0:3]in prefixKeys:
        return [word[0:3], word[3::]]
    elif pattern[0:2] == "CVC" and word[0:3]in prefixKeys:
        return [word[0:3], word[3::]]
    elif pattern[0:4] == "CVCC" and len(word) > 4:
        return [word[0:4], word[4::]]
    elif pattern[0:4] == "CVCC" and word[2] == word[3] and len(word) != len(pattern):
        return [word[0:3], word[3::]]


def checkIfFix(word, fix):
    for fixer in fix.keys():
        if fixer == word:
            return word


def testFunction(text, printHelp=False):
    if printHelp:
        print("TEST FUNCTION START:  ", text)
    quantifiedValue = []
    words, prefix, suffix = openLanguageStruct()
    textList = []
    for word in text.split():
        if "-" in word:
            textList += hyphinatedSplit(word)
        else:
            textList.append(word)
    if printHelp:
        print(f"Step1 : ", textList)
    wordScores = [wordValuation(x.lower(), words) for x in textList if type(x) != int and isWord(x.lower(), words)]
    if printHelp:
        print("Step1.5 : ", wordScores)
    textList, textStruct = wordListOrganize(wordScores, textList)
    if printHelp:
        print(f"Step2 : ", textList)
    prefixScores = [prefixValuation(x, prefix) for x in textList if x not in suffix.keys() and type(x) != int]

    textList, textStruct = prefixListOrganize(prefixScores, textList, textStruct)
    if printHelp:
        print(f"Step3 : ", textList)
    suffixScores = [suffixValuation(x, textStruct, suffix)for x in textList if type(x) != int]
    quantifiedValue, textStruct = suffixListOrganize(suffixScores, textList, textStruct)
    if printHelp:
        print("Step4 : ", quantifiedValue)
    
    qualifiedValue = [textStruct[x]["value"] for x in textStruct.keys()]

    stimulusDegree = Dopamine(quantifiedValue)
    socialDegree = GABA(quantifiedValue)

    Histamine(quantifiedValue)
    # print("Quantum (Dynamics) Degree: ", stimulusDegree*socialDegree)
    qualV = stimulusDegree*socialDegree

    # print("Qualum (Sentiments) Degree: ", Dopamine(qualifiedValue)*GABA(qualifiedValue))
    quantV = Dopamine(qualifiedValue)*GABA(qualifiedValue)
    return qualV, quantV


def doctorSentence(word):
    if len(word) > 1:
        if word[-1] != word[-2]:
            if word[-1] == "s" and word[-2] not in vowelsList or word[-1] == "s" and len(word) > 2:
                word = word[0:-1]
    return word


def testWordSplitter(sentence = None, printWords = None):
    if sentence == None:
        sentence = sys.argv[-1].lower().replace("'", "").split()
    else:
        sentence = sentence.lower().replace("'", "").split()
    correctedSentence = []
    for word in sentence:
        if "-" in word:
            word = "".join(hyphinatedSplit(word)).replace(".", "")
        correctedSentence.append(doctorSentence(word))
    text = ""
    for word in correctedSentence:
        if len(word) == 1 or len(word) == 2 or len(word) == 3 or word == "some":
            text += word
        elif word in questionWords:
            text += word
        elif doubleSylabulValidator(word) != "":
            x = doubleSylabulValidator(word)
            if type(x) == str:
                text += "".join(x)
            else:
                text += "-".join(x)
        text += " "

    return testFunction(text, printHelp = printWords)

if __name__ == "__main__":
    # qualum is the sentimental value of the words
    # quantum is the numberical value of the frequency of sylabuls
    testWordSplitter(printWords = True)