from .realFields import RealField
from .fusionFields import Fussion

class negationMap:
    negationMap ={
        "o": "i",
        "i": "o",
        "+": "-",
        "-": "+"
    }

def spinField(field, spin, size, timeValue):
    # 1 = 90 degrees
    # 2 = 180 degrees
    # 3 = 270 degrees
    # print("Type: ", field.fetchFieldType, " spin: ", spin)
    if "integral" == field.fetchFieldType:
        return integerField(spin, size, timeValue)
    elif "integer" == field.fetchFieldType:
        return posineutralField(spin, size, timeValue)
    elif "posineutral" == field.fetchFieldType:
        return integralField(spin, size, timeValue)


def readNumeralMap(size = "1"):
    numeralReaderMap = {
        "o": "0",
        "+": size,
        "-": f"{-int(size)}",
        size: size,
        "i": f"{complex(0, 1)}",
        "0": "0"
    }

    return numeralReaderMap


def rationalizeNumeral(numeral):
    if type(numeral) == list:
        numeral = numeral[0]
    elif type(numeral) == str:
        pass
    if len(numeral) > 2:
        if negationMap().negationMap[numeral[0]] == numeral[-1]:
            return numeral[1]
    elif len(numeral) == 2:
        if numeral[0] in negationMap().negationMap.keys():
            return numeral[-1]
        elif numeral[-1] in negationMap().negationMap.keys():
            return numeral[0]


class Depiction:
    def __init__(self, field, spins, fieldType):
        self._spins = spins
        self._type = fieldType
        self._msg = "Howdy World"
        self._field = field
        self._unitsList = []

    def getSocioGraph(self):
        if len(self._field) == 3:
            return f"{self._field[0]}\n{self._field[1]}\n{self._field[-1]}"
        elif len(self._field) == 2 and type(self._field[0][0]) == list:
            if len(self._field[0]) == 3:
                f = self._field[0][0][0]
                s = self._field[0][1][0]
                t = self._field[0][-1][0]
            elif len(self._field[0]) == 1:
                f = self._field[0]
                s = self._field[0]
                t = self._field[0]
                return f"{self._field[0]} | {self._field[-1]}"

            # get field lengths
            if f != None: fLen = len(f) - 2
            elif f == None: fLen = 2
            if s != None: sLen = len(s) - 2
            elif s == None: sLen = 2
            if t != None: tLen = len(t) - 2
            elif t == None: tLen = 2
            maxLen = max(fLen, sLen, tLen)
            if maxLen % 2 == 1: b = 0 # find space buffer
            elif maxLen % 1 == 0: b = 1
            if fLen == maxLen: f = ""
            else: f = str.ljust(" ", int((maxLen - fLen +b)+2))
            if sLen == maxLen: s = ""
            else: s = str.ljust(" ", int((maxLen - sLen +b)+2))
            if tLen == maxLen: t =""
            else: t = str.ljust(" ", int((maxLen - tLen +b)+2))
                        
            return f"{f}{self._field[0][0]} | {self._field[-1][0]}\n{s}{self._field[0][1]} | {self._field[-1][1]}\n{t}{self._field[0][-1]} | {self._field[-1][-1]}"
        elif len(self._field) == 2 and len(self._field[0]) == 1:
            return f"{self._field[0]} | {self._field[-1]}"

    def writeFile(self, filename):
        if filename[-3::] == "txt":
            with open(filename, "a") as f:
                print(self._spins[0])
                f.write(self._spins + "\n")
                f.write(f"{self._type[0]} | {self._type[-1]}")
                f.write("\n")
                f.write(self.fetchSocioGraph)
                f.write("\n_____________________\n")

    def analyzeUnit(self, row):
        unitList = []
        if row[0] == None and row[1] == None and row[-1] == None:
            return None
        for unit in row:
            if unit[0] == None:
                continue
            unitList.append(unit)
        return unitList

    @property
    def fetchSocioGraph(self):
        return self.getSocioGraph()


def loopsCaluclate(loops, timeValue):
    if timeValue > 1:
        loops += 100
    elif timeValue > 0.01 and timeValue <= 1:
        loops += 10
    elif timeValue >0.000000001 and timeValue <= 0.01:
        loops += 1
    return loops


def B4NG(spinAlteration = [0, 1, 2, 3], timeValue = 0.25, size = 1, accelerate = False, accelRate = 0.9):
    import pprint
    totalCycles = 0
    if type(spinAlteration) != list:
        spinAlteration = list(spinAlteration)

    fieldType = integerField(0, size, timeValue)
    position = 0
    spinPattern = spinAlteration
    loops = 0

    # while True:

    loops = loopsCaluclate(loops, timeValue)
    field = fieldType.fetchField
    depiction = Depiction(field)
    isFieldFull = False
    if len(field) == 3:
        isFieldFull = True
    if isFieldFull and loops == 100:
        print(depiction.fetchSocioGraph)
        loops = 0
    # field2 = spinField(fieldType, position, size, timeValue)
    # if field == field2:
    #     break
    # elif field != field2:
    totalCycles += 1

    if totalCycles == 100000:
        print("100K")
    if totalCycles == 10000000:
        print("10M")

def depict(field, spins, fT, write = False):
    depiction = Depiction(field, spins, fT)
    x = depiction.fetchSocioGraph
    if write:
        depiction.writeFile("models.txt")
    elif not write:
        print(x)
    print("-----------------------")


def SpinParticle(fieldType):
    field = fieldType.fetchField
    depict(field)
    fieldType.spinForward()

def ParticlePlay(spinAlteration = [0, 1, 2, 3], timeValue = 0.25, size = 1, accelerate = False, accelRate = 0.9):
    fieldType = RealField(0, size, timeValue, "posineutral")
    for x in range(0, 10):
        SpinParticle(fieldType)

def FusionParticles(spinAlteration = [0, 1, 2, 3], timeValue = 0.25, size = 1, accelerate = False, accelRate = 0.9):
    # data type collision outcomes are:
    #     integer/integer === empty top/bottom & left/right recation (both position 0)
    #     integral/integral === destructive (both position 0)
    #     neganeutral/neganeutral === destructive (both position 0)
    #     posineutral/posineutral === destructive (both position 0)
    #     integer/neganeutral === empty left/right recation (both position 0)
    #     integral/posineutral === non-reactive (both postion 0)
    #     integer/posineutral === empty top/bottom & back/front & left/right Additive (both position 0)
    #     integral/neganeutral === non-reactive (both position 0)
    #     neganeutral/integer === empty left/right (both position 0)
    #     posineutral/integral === non-reactive (both position 0)
    #     posineutral/integer === empty left/right & back/front & top/bottom Additive (both position 0) 
    #     neganeutral/integral === non-reactive (both position 0)
    #     integer/integral === Repulsive reaction (both position 0)
    #     posineutral/neganeutral === Repulsive reaction (both position 0)

    x = [["integer", "integer"], ["integral", "integral"], ["neganeutral", "neganeutral"], \
         ["posineutral", "posineutral"], ["integer", "neganeutral"], ["integral", "posineutral"], \
         ["integer", "posineutral"], ["integral", "neganeutral"], ["neganeutral", "integer"], \
         ["posineutral", "integral"], ["posineutral", "integer"], ["neganeutral", "integral"], \
         ["integer", "integral"], ["posineutral", "neganeutral"]]
    
    pos1 = 0
    pos2 = 0
    # while pos1 <= 3:
    for thing in x:
        fieldType = RealField(pos1, 3, timeValue, thing[0])
        fieldType2 = RealField(pos2, 2, timeValue, thing[-1])
        field1 = fieldType.fetchField
        field2 = fieldType2.fetchField
        print("______________________________")
        print(thing)
        print(f"-------Spin: {pos1} | {pos2} :Spin-------")
        print("------------------------------")
        depict([field1, field2], f"-------Spin: {pos1} | {pos2} :Spin-------", thing)

        fussionField = Fussion(field1, field2)
        fussionField.startExistance()
        field1 = fussionField.fetchFieldA
        field2 = fussionField.fetchFieldB
        newField = fussionField.fetchNewField
        if newField != []:
            theField = newField
        else:
            theField = [field1, field2]
        depict(theField, f"-------Spin: {pos1} | {pos2} :Spin-------", thing)
        print("  _-_-_-_-_-_-_")
        print("_-_-_-_-_-_-_-_-_")
        print(" -_-_-_-_-_-_-_- ")
        print("   - - - - - - ")
        # if pos2 == 3:
        #     pos1 += 1
        # if pos1 == 3:
        #     pos2 += 1
        #     pos1 = 0
        # pos1 += 1