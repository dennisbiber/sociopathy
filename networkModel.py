# dB Tech <Nov 2022 - ...>

class NeuralModel(object):

    def __init__(self):
        self._neuralTree = {}
        self._convergenceKey = None
        self._divergenceKey = None

    def nerualGrowth(self, key):
        if self.fetchNeuralTree() == {}:
            return {self.fetchPosiNewKey(): None, self.fetchNegaNewKey(): None}
        posiKey = self.convergePosiNega(self.fetchPosiNewKey() + key)
        posiKey = self.divergePosiNega(self.fetchPosiNewKey() + key)
        negaKey = self.convergePosiNega(self.fetchNegaNewKey() + key)
        negaKey = self.divergePosiNega(self.fetchNegaNewKey() + key)
        return {posiKey: None, negaKey: None}

    def triggerUndefinedSearch(self):
        self.findUndefined(self.fetchNeuralTree())

    def postConvergenceKey(self, key):
        self._convergenceKey = key

    def postDivergenceKey(self, key):
        self._divergenceKey = key

    def fetchPosiNewKey(self):
        return self._posiNewKey

    def fetchNegaNewKey(self):
        return self._negaNewKey

    def fetchConvergenceKey(self):
        return self._convergenceKey

    def fetchDivergenceKey(self):
        return self._divergenceKey

    def fetchNeuralTree(self):
        return self._neuralTree

    def convergePosiNega(self):
        pass

    def divergePosiNega(self):
        pass

    def postPosiNewKey(self):
        pass

    def postNegaNewKey(self):
        pass
