from networkModel import NeuralModel
from sociotransmitters import openLanguageStruct

# dB Tech <Nov 2022 - ...>

class WordModel(NeuralModel):

    def __init__(self):
        super(WordModel, self).__init__()
        self._prefixes = {"-c": "-de",
                          "+c": "+re",
                          "c": "com",
                          "-l": "-mis",
                          "+l": "pro"}

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
                                neuron[key] = self.nerualGrowth(key)
                            if "-" in x:
                                neuron[key] = self.nerualGrowth(key)
                    else:
                        neuron[key] = self.nerualGrowth(key)
                elif neuron[key] != None:
                    self.findUndefined(neuron[key])
        else:
            self.fetchNeuralTree().update(self.nerualGrowth(""))

    def convergePosiNega(self, key):
        convergedKey = key
        if key[0:3] == self._prefixes["-c"] and key[3:6] == self._prefixes["+c"] or key[0:3] == self._prefixes["+c"] and key[3:6] == self._prefixes["-c"]:
            if key[6] == "m" or key[6] == "p":
                addon = "com"
            else:
                addon = "con"
            convergedKey = addon + key[6::]
        return convergedKey

    def divergePosiNega(self, key):
        divergedKey = key
        if key[0:3] == key[3:6]:
            if key[0:3] == self._prefixes["-c"]:
                addon = "mis"
                divergedKey = addon + key[6::]
            if key[0:3] == self._prefixes["+c"]:
                addon = "pro"
                divergedKey = addon + key[6::]
        return divergedKey

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
    import time
    filename = "/home/dbiber/data/sociopathy/languageStruct.json"
    words, _, _ = openLanguageStruct(filename = filename)
    count = 4
    for word in words.keys():
        model = WordModel()
        x = 0
        while x < 4:
            for x in range(1, 5):
                if x == 1:
                    model.postPosiNewKey(newKey = word)
                    model.postNegaNewKey(newKey = "kill")
                else:
                    model.postPosiNewKey()
                    model.postNegaNewKey()
                model.triggerUndefinedSearch()
        tree = model.fetchNeuralTree()
        for key in tree:
            if key != "kill":
                print(tree[key])
                print(" ")

    def matrix():
        matrixList = [       
                        "    /\/\/\/\ . /\/\/\/\ \n",
                        "   /  \ \ \ \_/  \ \ \ \ \n",
                        "  / /\ \ \ \_/ /\ \ \ \ \ \n",
                        " / /  \ \ \_/ /  \ \_\_\_\ \n",
                        "/ / /\ \ \_/ / /\ \ \    /\   \n",
                        "\ \ \/ / / \ \ \/ / /___/ /   \n",
                        " \ \  / /  |\ \  / /\ \ \/\n",
                        "  \ \/ /  /  \ \/ /\ \ \/\n",
                        "   \  /  /    \  /\ \ \/\n",
                        "    \/__/      \/__\_\/\n"]
        return matrixList

if __name__ == "__main__":
    main()