import json
import markovify
import os
import pprint
import random
import time
from sociotransmitters import hyphinatedSplit, questionWords, testWordSplitter
from jsonStructTesting import valueSentence, makeJsonTestAvail
from botModel import Bot
from zeroDividerTests import divide

filePresent = False
HOME_DIR = os.path.expanduser("~")
filenameUno = HOME_DIR + "/data/sociopathy/socioBotUno.txt"
filenameDose = HOME_DIR + "/data/sociopathy/socioBotDose.txt"

def fetchText(contents):
    sentence = None
    random.shuffle(contents)
    model = markovify.Text(contents, state_size=2)
    # model = model.compile(inplace=True)
    while sentence == None or sentence == "None":
        sentence = model.make_short_sentence(200, tries=100)
        if sentence == None:
            print("Still nothing")
        elif len(sentence.split()) == 1:
            sentence = None
    return sentence

def writeFile(filename, sentence):
    with open(filename, "a") as f:
        f.write(sentence)

def getContents(filename, liveFilename):
    struct = fetchCurrentJson(liveFilename)
    contents = makeJsonTestAvail(struct)
    del struct
    with open(filename, "r") as f:
        for x in f.readlines():
            contents.append(x.replace(",", "").replace("\n", ""))
    return contents


def cycleRate():
    time.sleep(2)


def getDOB(startTime):
    return time.time() - startTime


def jsonStruct(speak, qualumValue, quantumValue, botName):
    timeStamp = time.time()
    struct = {timeStamp: {"sentence": speak,
                          "qualumValue": qualumValue,
                          "quantumValue": quantumValue,
                          "bot": botName}}
    speakValues = valueSentence(struct, timeStamp)
    if type(speakValues) == list:
        struct[timeStamp]["sentence"] = speakValues
    else:
        structp[timeStamp]["sentence"] = [speakValues]
    return struct


def fetchCurrentJson(filename):
    if os.path.exists(filename):
        return json.load(open(filename))
    else:
        return []


def writeLiveFile(liveFile, speak, qualumValue, quantumValue, botName):
    data = fetchCurrentJson(liveFile)
    with open(liveFile, "w") as f:
        struct = jsonStruct(speak, qualumValue, quantumValue, botName)
        data.append(struct)
        json.dump(data, f, indent=2)
    return struct


def unDefinite(undefinedValue):
    # print(undefinedValue, " This is the undefined variable")
    return undefinedValue

def valueOpinion(qualVal, quantVal, sentVol, logicVol, opinion, talkingBotName, divisonFilter = False):
    qualUndefinites = divide(int(qualVal), 0, zeroVariable = qualVal, exponentVariable = [quantVal] * int(qualVal))
    quantUndefinites = divide(int(quantVal), 0, zeroVariable = quantVal, exponentVariable = [qualVal] * int(quantVal))
    if divisonFilter:
        try:
            addonQual = unDefinite(qualUndefinites)
        except ZeroDivisionError:
            addonQaul = unDefinite(0)
        try:
            addonQuant = unDefinite(quantUndefinites)
        except ZeroDivisionError:
            addonQuant = unDefinite(0)
        qualVal = addonQual
        quantVal = addonQuant
    if sentVol == 1:
        opinion += qualVal/25
    elif sentVol == 2:
        opinion += 0
    elif sentVol >= 3:
        opinion -+ qualVal/25

    if logicVol == 1:
        opinion += quantVal/25
    elif logicVol == 2:
        opinion +=  0
    elif logicVol >= 3:
        opinion -= quantVal/25

    return opinion

def sensitizeJson(talkingBotName, botChangeValue, entity, struct, botPrint = False):
    timeStamp = [x for x in struct.keys()][0]
    botCurrentValue = entity.fetchOpinions(talkingBotName)
    struct = struct[timeStamp]
    qualumValue = struct["qualumValue"]
    quantumValue = struct["quantumValue"]
    sentimentVolume = len(struct["sentence"][0]["qualumSentence"])
    logimentVolume = len(struct["sentence"][-1]["quantumSentence"])
    opinion = valueOpinion(qualumValue, quantumValue, sentimentVolume, logimentVolume, botCurrentValue, talkingBotName, divisonFilter = True)
    botChangeValue(talkingBotName, opinion)

def main():
    startTime = time.time()
    botUno = Bot(getDOB(time.time() - startTime), "Truman Demiskil", 1, trainingFile = filenameUno)
    botDose = Bot(getDOB(time.time() - startTime), "Pauly ReMisdaree", 0, trainingFile = filenameDose)
    fileDir = "/home/dbiber/data/sociopathy"
    botNames = [botUno, botDose]

    cycleCount = 0
    while True:
        if cycleCount % 2 == botUno.fetchTimeMod():
            bot = botDose
            notBot = botUno
        elif cycleCount % 2 == botDose.fetchTimeMod():
            bot = botUno
            notBot = botDose
        contents = getContents(bot.fetchTrainingFile(), bot.fetchLiveFile(fileDir))
        if contents != None:
            botSpeech = fetchText(contents)
        qualumValue, quantumValue = testWordSplitter(sentence = botSpeech)
        botName = bot.fetchBotName()
        print(f"Bot: {botName} : {botSpeech}")
        for entity in botNames:
            struct = writeLiveFile(entity.fetchLiveFile(fileDir), botSpeech, qualumValue, quantumValue, bot.fetchBotName())
            if botName != entity.fetchBotName():
                sensitizeJson(botName, entity.opinionValue, entity, struct)
            print(entity.fetchBotInfo())
        cycleRate()
        cycleCount += 1

if __name__ == "__main__":
    main()