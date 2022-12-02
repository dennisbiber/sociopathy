
__author__ = "Dennis Biber <decibelsTechnology>"

class Fussion:
    def __init__(self, fieldA, fieldB):
        # (++) and (--) cannot fuse without acceleration or another Field force acting on it
        self._fieldA = fieldA
        self._fieldB = fieldB
        self._length = len([*zip(self._fieldA, self._fieldB)])
        self._startingCount = 0
        self._poles = {
            "+-": "+-",
            "-+": "-+",
            "o+": "+",
            "o-": "-",
            "-o": "-",
            "+o": "+",
            "i+": "+",
            "i-": "-",
            "-i": "-",
            "+i": "+",
            "--": "--",
            "++": "++"
        }

    def startExistance(self):
        # print(self.__dir__())
        reconstructedA = []
        reconstructedB = []
        while self._startingCount < self._length:
            check = self.attchachBases()
            if check:
                web = check
            else:
                web = self.checkConnections()
            reconstructedA.append(web[0])
            reconstructedB.append(web[-1])
            self.moveExistance()
        self._fieldA = reconstructedA
        self._fieldB = reconstructedB

    def moveExistance(self):
        self._startingCount += 1

    def attchachBases(self):
        baseA = self._fieldA[self._startingCount][0]
        baseB = self._fieldB[self._startingCount][0]
        if baseA == baseB:
            if baseA[0]+baseA[-1] in self._poles.keys() and baseA[0] != baseA[-1]:
                return [None], [None]
            elif baseA[0] == "i" and baseA[-1] == "i" and baseA[2]+baseA[-3] in self._poles.keys():
                return [None], [None]
            elif baseA[0] == "o" and baseA[-1] == "o" and baseA[2]+baseA[-3] in self._poles.keys():
                return [None], [None]
        self._attachedField = self._fieldA[self._startingCount][0] + self._fieldB[self._startingCount][0]

    def checkConnections(self):
        fieldA = []
        fieldB = []
        fieldLength = self._length
        vector = self._attachedField
        idx = self.fetchIdx()
        if type(vector) != tuple:
            if vector[idx:idx + 2] in self._poles.keys():
                newDelimiter = self._poles[vector[idx:idx + 2]]
                if newDelimiter == vector[idx:idx + 2]:
                    return self._fieldA[self._startingCount], self._fieldB[self._startingCount]
            returnVector = self.processFusion()
            if "=" == vector[idx] and vector[idx + 1] == vector[idx] - 1:
                fields = self.processEquates("=")
            elif "=" in vector and vector[idx] == "-":
                fields = self.processEquates("-")
            elif "=" in vector and vector[idx] == "+":
                fields = self.processEquates("+")
            elif [x for x in range(len(vector) -1) if vector[x] == "+" and vector[x+1] == "-" or vector[x]\
                    == "-" and vector[x+1] == "+"]:
                fields = self.processEquates("=")
            elif "0+0" in vector:
                fields = self.negation()
            else:
                def findIdx(vector):
                    n = 0
                    while n < len(vector):
                        if vector[0:idx+n][0] == "i" and vector[0:idx+n][-1] == "i" or \
                            vector[0:idx+n][0] == "o" and vector[0:idx+n][-1] == "o":
                            return n
                        elif vector[0:idx+n][0] + vector[0:idx+n][-1] in self._poles.keys():
                            return n
                        n += 1
                n = findIdx(vector)
                fields = vector[0:idx+n], vector[idx+n::]
            if returnVector != vector:
                fields = returnVector
            if type(fields) == list or type(fields) == tuple:
                # fieldA = [fields[0]]
                # fieldB = [fields[-1]]
                if type(fields[0]) == list: 
                    if [None] in fields[0]: felidA = fields[0]
                elif  type(fields[-1]) == list:
                    if[None] in fields[-1]: fieldB = fields[-1]
                else: fieldB, fieldA = [fields[-1]], [fields[0]]
            else:
                fieldA = self._fieldA[self._startingCount]
                fieldB = self._fieldB[self._startingCount]

        return fieldA, fieldB


    def mergeNeighboringEquals(self):
        if x.isDigit() and y.isDigit() and x == y:
            return x

    def processEquates(self, equator):
        idx = self.fetchIdx()
        if len(equator) != 1:
            preDex = idx -1
            sufDex = idx + 1
        else:
            preDex = idx
            sufDex = idx
        attachedField = self._attachedField[0:preDex] + self._attachedField[sufDex + 1::]
        if attachedField != (None, None):
            attachedField = self.symetricalNegation(idx)
        if attachedField != (None, None):
            attachedField = self.pattern(idx)
        if len(attachedField) == 2:
            _fieldA = attachedField[0]
            _fieldB = attachedField[-1]
            return _fieldA, _fieldB
        else:
            return attachedField

    def checkForZero(self, vector):
        if vector != self.symetricalNegation(vector):
            return self.symetricalNegation(vector)
        return vector

    def processFusion(self):
        vector = check = self._attachedField
        idx = self._fetchIdx()
        if vector[idx:idx+2] in self._poles.keys():
            newDelimiter = self._poles[vector[idx:idx+2]]
            vector = vector[0:idx] + newDelimiter + vector[idx+2::]
            newIdx = int(len(vector)/2)
            center = vector[newIdx-2:newIdx+2]
            numbers = []
            for v in range(len(center)):
                if center[v].isdigit() and center[v-1] == "-" or center[v].isdigit() and center[v-1] == "+":
                    numbers.append(int(center[v-1:v+1]))
            newValue = sum(numbers)
            if newValue == 0:
                vector = vector[0:newIdx-2] + vector[newIdx+2::]
            else:
                vector = vector[0:newIdx-2] + f"{newValue}" + vector[newIdx+2::]
            newIdx = int(len(vector)/2)
            if not vector[newIdx].isdigit():
                check = self.checkForZero(vector)
            elif vector[newIdx].isdigit():
                newVector = vector[0:newIdx] + vector[newIdx+2::]
                vectorCheck = self.symetricalNegation(newVector)
                if vectorCheck == (None, None):
                    return vector[newIdx-1:newIdx+2], vector[newIdx-1:newIdx+2]
            if vector != self._attachedField:
                if check != vector:
                    return check
                return vector
            else:
                return self._attachedField

    def negation(self, vector = False):
        if vector == False:
            vector = self._attachedField
        if "0+0" in vector:
            self._attachedField = pattern(self._attachedField, "0+0")
        if self._attachedField == (None, None):
            return
        else:
            print("FUCK")

    def symetricalNegation(self, idx):
        if type(idx) == str:
            vector = idx
            self._fetchIdx(vector = vector)
            idx = self.fetchIdx()
            self.resetIdxFetch
        attachedField = self._attachedField
        leftSide = attachedField[0:idx]
        rightSide = attachedField[idx::]
        for l, r in zip(leftSide, rightSide[::-1]):
            if l == None and r == None:
                return attachedField
            if l == "+" and r == "-" or l == "-" and r == "+" or l == "o" and r == "-" or l=="-" and r=="o" or \
                l=="+" and r=="o" or l=="o" and r=="+":
                pass
            elif l != r:
                return attachedField
        return None, None

    def pattern(self, idx):
        idx = self.fetchIdx
        if self._attachedField[0:idx] == "".join(reversed(self._attachedField[idx::])):
            return None, None
        else:
            return self._attachedField

    @property
    def fetchIdx(self):
        return self._fetchIdx

    @property
    def fetchFieldA(self):
        return self._fieldA

    @property
    def fetchFieldB(self):
        return self._fieldB

    @property
    def resetIdxFetch(self):
        self._fetchIdx()

    def _fetchIdx(self, vector = False):
        if not vector:
            vector = self._attachedField
        if len(vector) % 2 == 0:
            return int(len(vector)/2)-1
        return int(len(vector)/2)