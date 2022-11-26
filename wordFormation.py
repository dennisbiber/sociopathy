from botModel import Bot
from wordModel import WordModel
import time
import pprint


def getDOB(startTime):
    return time.time() - startTime


class WordFormation(WordModel):

    def __init__(self, posiWord, negaWord):
        super(WordFormation, self).__init__()
        self._posiWord = posiWord
        self._negaWord = negaWord

    def generateNeuralTree(self):
        loop = 1
        while loop < 5:
            self.wordLoop(loop)
            loop += 1

    def wordLoop(self, loop):
        if loop == 1:
            self.postPosiNewKey(self._posiWord)
            self.postNegaNewKey(self._negaWord)
        if loop != 1:
            self.postPosiNewKey()
            self.postNegaNewKey()
        self.triggerUndefinedSearch()

    def synonomizeCheck(self):
        pass


def main():
    startTime = time.time()
    botUno = Bot(getDOB(time.time() - startTime), "Truman Demiskil", 1)
    botDose = Bot(getDOB(time.time() - startTime), "Pauly ReMisdaree", 0)
    botUnoWords = ["press", "lect", "fart"]
    botDoseWords = ["tense", "sense", "burp"]
    fileDir = "/home/dbiber/data/sociopathy"

    for cycleCount in range(len(botUnoWords)):
        formation = WordFormation(botUnoWords[cycleCount], botDoseWords[cycleCount])
        formation.generateNeuralTree()
        pprint.pprint(formation.fetchNeuralTree())



if __name__ == "__main__":
    main()