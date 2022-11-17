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
        self._liveFileName = f"{name}_{dob}.json"
        self._dob = dob
        self._name = name
        self._timeMod = timeMod
        if trainingFile != None:
            self._trainingFile = trainingFile
        else:
            self._trainingFile = None

    def SentimentalThought(self):
        self.sentiment = None

    def LogimentalThought(self):
        self.logiment = None

    def ThoughtSelector(self):
        changeDegreePercentages = {"negextremal": -0.001,
                                   "negaradical": -0.021,
                                   "negaliberal": -0.136,
                                   "negaconservative": -0.341,
                                   "preservative": 0,
                                   "posiconservative": 0.341,
                                   "posiliberal": 0.136,
                                   "posiradical": 0.21,
                                   "posiextremal": 0.001}

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

    def fetchLiveFile(self, rootDir):
        return rootDir + "/" + self._liveFileName

    def fetchDOB(self):
        return self._dob

    def fetchBotName(self):
        return self._name

    def fetchTimeMod(self):
        return self._timeMod

    def fetchTrainingFile(self):
        if self._trainingFile != None:
            return self._trainingFile
        return None

    def fetchBotInfo(self):
        botInfo = {"botName": self.fetchBotName(),
                   "dob": self.fetchDOB(),
                   "opinion": self.opinions}
        return botInfo

    