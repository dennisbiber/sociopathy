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
    def __init__(self, field):
        self._msg = "Howdy World"
        self._field = field
        self._unitsList = []

    def getSocioGraph(self):
        if len(self._field) == 3:
            return f"{self._field[0]}\n{self._field[1]}\n{self._field[-1]}"
        elif len(self._field) == 2 and type(self._field[0][0]) == list:
            return f"{self._field[0][0]} | {self._field[-1][0]}\n{self._field[0][1]} | {self._field[-1][1]}\n{self._field[0][-1]} | {self._field[-1][-1]}"

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

def depict(field):
    depiction = Depiction(field)
    print(depiction.fetchSocioGraph)
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
    
    for thing in x:
        fieldType = RealField(1, size, timeValue, thing[0])
        fieldType2 = RealField(1, size, timeValue, thing[-1])
        field1 = fieldType.fetchField
        field2 = fieldType2.fetchField
        depict([field1, field2])

        fussionField = Fussion(field1, field2)
        fussionField.startExistance()
        field1 = fussionField.fetchFieldA
        field2 = fussionField.fetchFieldB
        print(thing)
        depict([field1, field2])
        print("  _-_-_-_-_-_-_")
        print("_-_-_-_-_-_-_-_-_")
        print(" -_-_-_-_-_-_-_- ")
        print("   - - - - - - ")