from socioBotParent import SocioBot
from networkModel import NeuralModel

# dB Tech <Nov2022 - ... >


class Bot(SocioBot, NeuralModel):

    def __init__(self, dob, name, timeMod, trainingFile = None):
        super(Bot, self).__init__(dob, name, timeMod, trainingFile = None)
        self._liveFileName = f"{name}_{dob}.json"
        if trainingFile != None:
            self._trainingFile = trainingFile
        else:
            self._trainingFile = None
        
    def fetchLiveFile(self, rootDir):
        return rootDir + "/" + self._liveFileName

    def fetchTrainingFile(self):
        if self._trainingFile != None:
            return self._trainingFile
        return None