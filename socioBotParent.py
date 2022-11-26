import random
from jsonStructTesting import valueSentence


class SocioBot(object):

    def __init__(self, dob, name, timeMod, trainingFile = None):
        # value of dialog outputted when reporduction occurs
        self.reproductionValue = random.randint(80, 120)
        # value of bots the output at reproduction
        self.offspringValue = random.randint(1, 4)
        # value used for splitting sentiments of dialog into Blocks or Codons 
        self.codonModuloValue = random.randint(1, 4)
        # sentimental value (-1=Negative, 0=neutral, 1=positive)
        self.startingSentiment = 0
        self.opinions = {}
        self._dob = dob
        self._name = name
        self._timeMod = timeMod

    def SentimentalThought(self):
        self.sentiment = None

    def LogimentalThought(self):
        self.logiment = None

    def ThoughtSelector(self):
        changeDegreePercentages = {"-e": -0.001,
                                   "-r": -0.021,
                                   "-l": -0.136,
                                   "-c": -0.341,
                                   "p": 0,
                                   "+c": 0.341,
                                   "+l": 0.136,
                                   "+r": 0.21,
                                   "+e": 0.001}

    def opinionValue(self, botName, value):
        if botName not in self.opinions.keys():
            self.opinions[botName] = value
        elif botName in self.opinions.keys():
            self.opinions[botName] += value

    def jsonStruct(self, speak, qualumValue, quantumValue, botName):
        timeStamp = time.time()
        struct = {timeStamp: {"sentence": speak,
                            "qualumValue": qualumValue,
                            "quantumValue": quantumValue,
                            "bot": botName}}
        speakValues = valueSentence(struct)
        if type(speakValues) == list:
            struct[timeStamp]["sentence"] = speakValues
        else:
            structp[timeStamp]["sentence"] = [speakValues]
        return struct

    def fetchOpinions(self, botName):
        if botName not in self.opinions.keys():
            self.opinionValue(botName, 0.0)
        return self.opinions[botName]

    def fetchDOB(self):
        return self._dob

    def fetchBotName(self):
        return self._name

    def fetchTimeMod(self):
        return self._timeMod

    def fetchBotInfo(self):
        return {"botName": self.fetchBotName(),
                "dob": self.fetchDOB(),
                "opinion": self.opinions}    