
__author__ = "Dennis Biber <decibelsTechnology>"

class Fussion:
    def __init__(self, fieldA, fieldB):
        # (++) and (--) cannot fuse without acceleration or another Field force acting on it
        self._fieldA = fieldA
        self._fieldB = fieldB
        self._newField = []
        self._length = len([*zip(self._fieldA, self._fieldB)])
        self._startingCount = 0
        self._attachedField = ""
        self._poles = {
            "+-": "-",
            "-+": "+"
        }

    def startExistance(self):
        # print(self.__dir__())
        lenCheck = 0
        reconstructedA = []
        reconstructedB = []
        newField = []
        constructedNew = []
        while self._startingCount < self._length:
            check = self.attchachBases()
            if check:
                col = check
            else:
                web, lenCheck = self.checkConnections()
                if lenCheck == 2:
                    col1 = web[0]
                    col2 = web[-1]
                    col = [col1, col2]
                elif lenCheck == 1:
                    col = web
                if len(col) == 1:
                    newField.append(col)
            if type(col) == list or type(col) == tuple:
                reconstructedA.append([col[0]])
                reconstructedB.append([col[-1]])
            if newField != []:
                constructedNew.append(col)
            self.moveExistance()
        if newField != []:
            newFieldReturn = False
            for x in constructedNew:
                if len(x) != 1:
                    self._newField.append(x)
                elif len(x) == 1:
                    self._newField.append(x)
                    newFieldReturn = True
            if newFieldReturn:
                pass
            else:
                self._newField = []
        else:
            if reconstructedA == [[None], [None], [None]]:
                self._fieldA = [None]
                self._fieldB = [None]
            elif reconstructedA[0] == [None] and reconstructedA[-1] == [None] and reconstructedA[1] != [None]:
                self._fieldA = reconstructedA[1]
                self._fieldB = reconstructedA[1]
            elif reconstructedA[0] == [None] and reconstructedA[1] == [None] and reconstructedA[-1] != [None]:
                self._fieldA = reconstructedA[-1]
                self._fieldB = reconstructedB[-1]
            elif reconstructedA[0] != [None] and reconstructedA[1] == [None] and reconstructedA[-1] == [None]:
                self._fieldA = reconstructedA[0]
                self._fieldB = reconstructedB[0]
            else:
                self._fieldA = reconstructedA
                self._fieldB = reconstructedB

    def moveExistance(self):
        self._startingCount += 1

    def attchachBases(self):
        baseA = self._fieldA[self._startingCount][0]
        baseB = self._fieldB[self._startingCount][0]
        if baseA == baseB:
            if baseA[0]+baseA[-1] in self._poles.keys() and baseA[0] != baseA[-1]:
                return None, None
            elif baseA[0] == "i" and baseA[-1] == "i" and baseA[2]+baseA[-3] in self._poles.keys():
                return None, None
            elif baseA[0] == "o" and baseA[-1] == "o" and baseA[2]+baseA[-3] in self._poles.keys():
                return None, None
        self._attachedField = self._fieldA[self._startingCount][0] + self._fieldB[self._startingCount][0]

    def checkConnections(self):
        fieldA = []
        fieldB = []
        fieldLength = self._length
        vector = checkVector = self._attachedField
        idx = self.fetchIdx()
        newVector = self.checkSymetry(vector)
        print("NEW", newVector)
        if newVector != checkVector and newVector != None:
            self.check0s(newVector)
            return newVector, len(newVector)
        elif newVector != None:
            return newVector, len(newVector)
        elif newVector == None:
            return newVector, 0
        else:
            return None, None

    def check0s(self, vector):
        zeroSymbol = "o0o"
        if zeroSymbol in vector:
            newVector = "".join(vector.split(zeroSymbol))
            print(newVector)

    def checkSymetry(self, vector):
        nonRationalablePairs = ["--", "++", "io", "oi", "-i", "+i", "i-", "i+", "-o", "+o", "o-", "o+"]
        rationalablePairs = ["-+", "+-", "ii", "oo"]
        if len(vector) % 2 == 0:
            idx = int(len(vector)/2)
        else:
            idx = int(len(vector)/2)
        for x in range(0, idx):
            if "".join([vector[idx-1-x], vector[idx+x]]) in nonRationalablePairs:
                return vector[0:idx], vector[idx::]
            if x == 2 and "".join([vector[idx-1], vector[idx]]) in rationalablePairs and \
                "".join([vector[idx-1-x], vector[idx+x]]) in rationalablePairs:
                if vector[idx-1-x] == "-" and vector[idx+x] == "+":
                    print("HELLO")
                    newValue = -int(vector[idx-x]) - int(vector[idx+1])
                    newVector = vector[0:idx-1-x] + f"{newValue}+" + vector[idx+1+x::]
                    exVector = "".join(newVector.split("o0o"))
                    checker = [x for x in nonRationalablePairs if x in exVector]
                    if checker != []:
                        return [newVector]
                elif vector[idx-1-x] == "+" and vector[idx+x] == "-":
                    newValue = int(vector[idx-x]) + int(vector[idx+1])
                    newVector = vector[0:idx-x] + f"{newValue}" + vector[idx+x::]
                    return [newVector]
                elif vector[idx-1-x] == "i" and vector[idx+x] == "i":
                    newValue = int(vector[idx-x]) + int(vector[idx+1])
                    newVector = vector[0:idx-x] + f"{newValue}" + vector[idx+x::]
                    return [newVector]
        return None

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

    @property
    def fetchNewField(self):
        return self._newField

    def _fetchIdx(self, vector = False):
        if vector == False:
            vector = self._attachedField
        if len(vector) % 2 == 0:
            return int(len(vector)/2)-1
        return int(len(vector)/2)