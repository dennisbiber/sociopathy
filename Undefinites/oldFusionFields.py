
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
                newField.append(col)
            if type(col) == list or type(col) == tuple:
                reconstructedA.append([col[0]])
                reconstructedB.append([col[-1]])
            if type(col) == str:
                pass
            self.moveExistance()
        if newField != []:
            newFieldReturn = False
            for x in newField:
                if len(x) != 1:
                    self._newField.append(x)
                elif len(x) == 1:
                    self._newField.append(x)
                    newFieldReturn = True
            if newFieldReturn:
                return
            else:
                self._newField = []
        else:
            if col == [[None], [None], [None]]:
                self._fieldA = [None]
                self._fieldB = [None]
            elif col[0] == [None] and col[-1] == [None]:
                self._fieldA = reconstructedA[1]
                self._fieldB = reconstructedB[1]
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
                return [None], [None]
            elif baseA[0] == "i" and baseA[-1] == "i" and baseA[2]+baseA[-3] in self._poles.keys():
                return [None], [None]
            elif baseA[0] == "o" and baseA[-1] == "o" and baseA[2]+baseA[-3] in self._poles.keys():
                return [None], [None]
        self._attachedField = self._fieldA[self._startingCount][0] + self._fieldB[self._startingCount][0]

    # def checkConnections(self):
    #     print(self._startingCount)
    #     fieldA = []
    #     fieldB = []
    #     fieldLength = self._length
    #     vector = self._attachedField
    #     idx = self.fetchIdx()
    #     if type(vector) != tuple:
    #         if vector[idx:idx + 2] in self._poles.keys():
    #             newDelimiter = self._poles[vector[idx:idx + 2]]
    #             if newDelimiter == vector[idx:idx + 2]:
    #                 return self._fieldA[self._startingCount], self._fieldB[self._startingCount]
    #         returnVector = self.processFusion()
    #         # if "=" == vector[idx] and vector[idx + 1] == vector[idx] - 1:
    #         #     fields = self.processEquates("=")
    #         # elif "=" in vector and vector[idx] == "-":
    #         #     fields = self.processEquates("-")
    #         # elif "=" in vector and vector[idx] == "+":
    #         #     fields = self.processEquates("+")
    #         # elif [x for x in range(len(vector) -1) if vector[x] == "+" and vector[x+1] == "-" or vector[x]\
    #         #         == "-" and vector[x+1] == "+"]:
    #         #     fields = self.processEquates("=")
    #         # elif "0+0" in vector:
    #         #     fields = self.negation()
    #         # else:
    #         def findIdx(vector):
    #             n = 0
    #             while n < len(vector):
    #                 if vector[0:idx+n][0] == "i" and vector[0:idx+n][-1] == "i" or \
    #                     vector[0:idx+n][0] == "o" and vector[0:idx+n][-1] == "o":
    #                     return n
    #                 elif vector[0:idx+n][0] + vector[0:idx+n][-1] in self._poles.keys():
    #                     return n
    #                 n += 1
    #             else: return 0
    #         n = findIdx(vector)
    #         fields = vector[0:idx+n], vector[idx+n::]
    #         if returnVector != vector:
    #             fields = returnVector
    #         if type(fields) == list or type(fields) == tuple:
    #             if type(fields[0]) == list: 
    #                 if [None] in fields[0]: felidA = fields[0]
    #             elif  type(fields[-1]) == list:
    #                 if[None] in fields[-1]: fieldB = fields[-1]
    #             else: fieldB, fieldA = [fields[-1]], [fields[0]]
    #         else:
    #             fieldA = self._fieldA[self._startingCount]
    #             fieldB = self._fieldB[self._startingCount]

    #     return fieldA, fieldB

    def checkConnections(self):
        fieldA = []
        fieldB = []
        fieldLength = self._length
        vector = checkVector = self._attachedField
        idx = self.fetchIdx()
        newVector = self.checkSymetry(vector)
        if newVector != checkVector:
            return newVector, len(newVector)
        elif newVector != None:
            return newVector, len(newVector)
        else:
            return None, None

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
        return None


    def mergeNeighboringEquals(self):
        if x.isDigit() and y.isDigit() and x == y:
            return x

    # def processEquates(self, equator):
    #     idx = self.fetchIdx()
    #     if len(equator) != 1:
    #         preDex = idx -1
    #         sufDex = idx + 1
    #     else:
    #         preDex = idx
    #         sufDex = idx
    #     attachedField = self._attachedField[0:preDex] + self._attachedField[sufDex + 1::]
    #     if attachedField != (None, None):
    #         attachedField = self.symetricalNegation(idx)
    #     if attachedField != (None, None):
    #         attachedField = self.pattern(idx)
    #     if len(attachedField) == 2:
    #         _fieldA = attachedField[0]
    #         _fieldB = attachedField[-1]
    #         return _fieldA, _fieldB
    #     else:
    #         return attachedField

    def checkForZero(self, vector):
        if vector != self.symetricalPosition(vector):
            return self.symetricalPosition(vector)
        if vector != self.symetricalNegation(vector):
            return self.symetricalNegation(vector)
        return vector

    def getSection(self, vector: str):
        return vector[0:3], vector[3:6], vector[6::]

    def checkPairs(self, pairs: list):
        f1, s1, t1 = pairs[0][0], pairs[0][1], pairs[0][-1]
        f2, s2, t2 = pairs[-1][0], pairs[-1][1], pairs[-1][-1]
        if s1.isdigit() and s2.isdigit() and t1 == t2 and t1 != "-" and t1 != "+" and f1 != "i" and f1 != "o":
            if f1 == "+" and f1 == "-" or f1 == "-" or f1 == "+":
                if f1 == "i" or f1 == "o":
                    f1 = ""
                    f2 = ""
                fInt = int("".join([f1, s1]))
                lInt = int("".join([f2, s2]))
                newInt = sum([fInt, lInt])
                newInt = "".join([f"{newInt}", t1])
        elif f1 == f2 and s1.isdigit() and s2.isdigit() and f1 != "-" and f1 != "+" and t1 != "i" and t1 != "o":
            if t1 == "+" and t1 == "-" or t1 == "-" and t1 == "+":
                if t1 == "i" or t1 == "o":
                    t1 = ""
                    t2 = ""
                fInt = int("".join([t1, s1]))
                lInt = int("".join([t2, s2]))
                newInt = sum([fInt, lInt]) 
                newInt = "".join([f1, f"{newInt}"[-1], f"{newInt}"[0]])
        else:
            newInt = pairs
        return newInt

    def checkForMultiHoles(self, vector):
        originVector = vector
        whiteHole = "o0o"
        if vector.count(whiteHole) > 1:
            vector = vector.split(whiteHole)
            newVector = []
            if len(vector) == 3:
                print(vector)
                for x in vector:
                    if len(x) > 3:
                        position = self.symetricalPosition(x)
                        if type(position) == tuple:
                            return originVector
                        else:
                            newVector.append(position)
                    else:
                        newVector.append(x)
            vector = self.getSection("".join(newVector))
            print("PRE PAIR CHECK ", vector)
            fPair = self.checkPairs(vector[0:-1])
            print("HERE ", fPair)
            if fPair != vector[0:-1]:
                nextVector = [fPair, vector[-1]]
                fResult = fPair
            else:
                nextVector = vector[1::]
                fResult = vector[0]
            result = self.checkPairs(nextVector)
            newResult = self.checkForZero(result)
            print(newResult)
            if result != newResult:
                result = newResult
            if result != nextVector:
                if type(result) != str:
                    pass
                else:
                    if len(result) == 2:
                        result = "".join(["+", result])
                print(result)
                lResult = result
            else:
                lResult = vector[-1]
            
            if fResult != vector[0] and type(result) == str:
                returnVector = result
            elif lResult != vector[-1] and type(result) == str:
                returnVector = result
            else:
                returnVector = vector
            print("PAIR: ", returnVector)
            return returnVector

    def processFusion(self):
        vector = check = self._attachedField
        idx = self._fetchIdx()
        if vector[idx:idx+2] in self._poles.keys():
            newDelimiter = self._poles[vector[idx:idx+2]]
            vector = vector[0:idx] + newDelimiter + vector[idx+2::]
            newIdx = int(len(vector)/2)
            center = vector[newIdx-2:newIdx+3]
            numbers = []
            for v in range(len(center)):
                # if center[v].isdigit: print(center)
                # if center[v].isdigit() and center[v-1] == "-" or center[v].isdigit() and center[v-1] == "+":
                #     numbers.append(int(center[v-1:v+1]))
                if v < len(center) - 3:
                    if center[v].isdigit() and center[v-1] == "i" and center[v+3] == "i" or \
                        center[v].isdigit() and center[v-1] == "o" and center[v+3] == "o" or \
                        center[v].isdigit() and center[v-1] == "+" and center[v+3] == "-" or \
                        center[v].isdigit() and center[v-1] == "-" and center[v+3] == "+":
                        if "i" in center:
                            symbol = "i"
                        elif "o" in center:
                            symbol = "o"
                        elif "+" in center:
                            symbol = "+"
                        elif "-" in center:
                            symobl = "-"
                        numbers.append(sum([int("".join(["-", center[v]])), int(center[v+1:v+3])]))
            newValue = sum(numbers)
            if newValue > 0:
                newValue = symbol + f"{newValue}"
            elif newValue < 0:
                newValue = f"{newValue}" + symbol
            else:
                newValue = f"{newValue}"
            if newValue == 0:
                vector = vector[0:newIdx-2] + vector[newIdx+2::]
            else:
                if newValue[-1] == "+" and newValue[0] == "i" or newValue[-1] and newValue[0] == "o" or \
                    newValue[-1] == "+" and newValue[0] == "-":
                    vector = vector.replace(center, "") + newValue + vector.replace(center,"")[newIdx+3::]
                elif newValue[0] == "-" and newValue[-1] == "i" or newValue[0] and newValue[-1] == "o" or \
                    newValue[0] == "-" and newValue[-1] == "+":
                    vector = vector[0:newIdx-2] + newValue + vector[newIdx+3::]
            self.checkForMultiHoles(vector)
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
    
    def symetricalPosition(self, idx):
        attachedField = None
        if type(idx) == tuple:
            idx = list(idx)
        if type(idx) == str:
            vector = idx
            idx = self._fetchIdx(vector = vector)
            fV = vector[0]
            lV = vector[-1]
            attachedField = vector
            leftSide = vector[0:idx]
            rightSide = vector[idx+1::]
            self.resetIdxFetch
        elif type(idx) == list and len(idx) == 2 :
            leftSide = idx[0]
            rightSide = idx[-1]
            fV = leftSide[0]
            lV = rightSide[-1]
            if leftSide[0] == leftSide[-1] or rightSide[0] == rightSide[-1]:
                return idx
            attachedField = idx
        elif type(idx) == int:
            idx = idx
        if attachedField == None:
            attachedField = self._attachedField
            leftSide = attachedField[0:idx]
            rightSide = attachedField[idx::]
        for l, r in zip(leftSide, rightSide[::-1]):
            if l == None and r == None:
                return attachedField
            if l == "+" and r == "-" or l == "-" and r == "+" or l == "o" and r == "-" or l=="-" and r=="o" or \
                l=="+" and r=="o" or l=="o" and r=="+":
                pass
            elif l != r and l.isdigit() and r.isdigit():
                if leftSide[-1] == rightSide[0]:
                    newValue = sum([int(leftSide[0:-1]), int("".join([rightSide[-1], rightSide[1]]))])
                else:
                    newValue = sum([int(leftSide), int("".join([rightSide[-1], rightSide[0]]))])
                if newValue > 0:
                    newValue = fV[-1] + f"{newValue}" + "+"
                elif newValue < 0:
                    newValue = "-" + f"{newValue}"[-1] + lV[0]
                return newValue
        return attachedField

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
        if idx() >= len(self._attachedField):
            return self._attachedField
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

    @property
    def fetchNewField(self):
        return self._newField

    def _fetchIdx(self, vector = False):
        if vector == False:
            vector = self._attachedField
        if len(vector) % 2 == 0:
            return int(len(vector)/2)-1
        return int(len(vector)/2)