

class NeuralModel(object):

    def __init__(self):
        self._neuralTree = {}

    def nerualGrowth(self, posiKey, negaKey):
        posiKey = self.convergePosiNega(posiKey)
        negaKey = self.convergePosiNega(negaKey)
        return {posiKey: None, negaKey: None}

    def triggerUndefinedSearch(self):
        self.findUndefined(self._neuralTree)

    def postConvergenceKey(self, key):
        self._convergenceKey = key

    def fetchPosiNewKey(self):
        return self._posiNewKey

    def fetchNegaNewKey(self):
        return self._negaNewKey

    def fetchConvergenceKey(self):
        return self._convergenceKey

    def fetchNeuralTree(self):
        return self._neuralTree