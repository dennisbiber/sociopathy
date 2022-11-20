from networkModel import NeuralModel

class WordModel(NeuralModel):

    def __init__(self):
        super(WordModel, self).__init__()
        self._prefixes = {"-c": "-de",
                          "+c": "+re"}

    def findUndefined(self, neuron):
        posiKey = False
        negaKey = False
        if neuron != {}:
            for key in neuron:
                if neuron[key] == None:
                    if self._prefixes["+c"] in key:
                        posiKey = key
                    elif self._prefixes["-c"] in key:
                        negaKey = key
                    if posiKey and negaKey:
                        for x in [posiKey, negaKey]:
                            if "+" in x:
                                neuron[key] = self.nerualGrowth(self.fetchPosiNewKey() + key, self.fetchNegaNewKey() + key)
                            if "-" in x:
                                neuron[key] = self.nerualGrowth(self.fetchPosiNewKey() + key, self.fetchNegaNewKey() + key)
                    else:
                        neuron[key] = self.nerualGrowth(self.fetchPosiNewKey() + key, self.fetchNegaNewKey() + key)
                elif neuron[key] != None:
                    self.findUndefined(neuron[key])
        else:
            self._neuralTree.update(self.nerualGrowth(self.fetchPosiNewKey(), self.fetchNegaNewKey()))

    def convergePosiNega(self, key):
        convergedKey = key
        if key[0:3] == self._prefixes["-c"] and key[3:6] == self._prefixes["+c"] or key[0:3] == self._prefixes["+c"] and key[3:6] == self._prefixes["-c"]:
            if key[6] == "m":
                addon = "com"
            else:
                addon = "con"
            convergedKey = addon + key[6::]
        return convergedKey

    def divergePosiNega(self, key):
        divergedKey = key
        if key[0:3] == key[3:6]:
            pass

    def postPosiNewKey(self, newKey = None):
        if newKey == None:
            self._posiNewKey = self._prefixes["+c"]
        else:
            self._posiNewKey = newKey

    def postNegaNewKey(self, newKey = None):
        if newKey == None:
            self._negaNewKey = self._prefixes["-c"]
        else:
            self._negaNewKey = newKey

def main():
    model = WordModel()
    model.postPosiNewKey("cept") # knowing
    model.postNegaNewKey("ment") # thinking
    model.triggerUndefinedSearch()
    print("1st")
    model.postPosiNewKey()
    model.postNegaNewKey()
    model.triggerUndefinedSearch()
    print("2nd")
    model.postPosiNewKey()
    model.postNegaNewKey()
    model.triggerUndefinedSearch()
    print("3rd")
    print(model.fetchNeuralTree())


if __name__ == "__main__":
    main()