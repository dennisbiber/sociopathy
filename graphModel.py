# this is an expirement in new ways to Enummerate pixels in an image.
# the pixelModel2 example seems to work the best as it creates 4 parallel fibonnaci spirals of the data in the image
import pprint

pixelModel = [
[6],
[6, 5, 6],
[6, 5, 4, 5, 6],
[6, 5, 4, 3, 4, 5, 6],
[6, 5, 4, 3, 2, 3, 4, 5, 6],
[6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
[6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
[6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
[6, 5, 4, 3, 2, 3, 4, 5, 6],
[6, 5, 4, 3, 4, 5, 6],
[6, 5, 4, 5, 6],
[6, 5, 6],
[6]]

pixelModel2 = [
    ["+050"],
    ["+05", "+040", "+50"],
    ["+05", "+04", "+030", "+40", "+50"],
    ["+05", "+04", "+03", "+020", "+30", "+40", "+50"],
    ["+05", "+04", "+03", "+02", "+010", "+20", "+30", "+40", "+50"],
    ["o05", "o04", "o03", "o02", "o01", "000", "o10", "o20", "o30", "o40", "o50"],
    ["-05", "-04", "-03", "-02", "-010", "-20", "-30", "-40", "-50"],
    ["-05", "-04", "-03", "-020", "-30", "-40", "-50"],
    ["-05", "-04", "-030", "-40", "-50"],
    ["-05", "-040", "-50"],
    ["-050"]
]

def addToPixelModel2(pixelModel2):
    def find_limits(model):
        upper_limit = model[0]
        newUpper_limit = upper_limit[0][0:-2] + str(int(upper_limit[0][-2]) + 1) + upper_limit[0][-1]
        lower_limit = model[-1]
        newLower_limit = lower_limit[0][0:-2] + str(int(lower_limit[0][-2]) + 1) + lower_limit[0][-1]
        return [newUpper_limit, newLower_limit]

    def find_boundary(row):
        rowOrigin = row
        first_limit = row[0]
        last_limit = row[-1]
        if first_limit == last_limit:
            theInt = int(first_limit[-2])
            theSign = first_limit[0]
            outL = theSign + str(0) + str(theInt + 1)
            outR = theSign + str(theInt + 1) + str(0)
            inner = theSign + str(0) + str(theInt) + str(0)
            row = [outL, inner, outR]
        elif int(first_limit[-1]) != 0:
            theInt = int(first_limit[-1])
        elif int(first_limit[-1]) == 0:
            theInt = int(first_limit[-2])
        if rowOrigin == row:
            print(row)
            row = [first_limit[0:-1] + f"{((theInt) + 1)}", *row]
            row = [*row, last_limit[0] + f"{((theInt) + 1)}" + str(0)]

        return row

    limits = find_limits(pixelModel2)
    new_model = [[limits[0]]]
    for row in pixelModel2:
        new_model.append(find_boundary(row))
    new_model.append([limits[-1]])
    return new_model

fibonnaciModel = [
    [11],
    [11, 7, 11],
    [11, 7, 5, 7, 11],
    [11, 7, 5, 3, 5, 7, 11],
    [11, 7, 5, 3, 2, 3, 5, 7, 11],
    [11, 7, 5, 3, 2, 0, 2, 3, 5, 7, 11],
    [11, 7, 5, 3, 2, 3, 5, 7, 11],
    [11, 7, 5, 3, 5, 7, 11],
    [11, 7, 5, 7, 11],
    [11, 7, 11],
    [11]
]

pattern1 = ["000", "+010", "+20", "o20", "-30", "-030", "-04", "o04"]
pattern2 = ["000", "o10", "-20", "-020", "-03", "o03", "+04", "+040"]
pattern3 = ["000", "-010", "-02", "o02", "+03", "+030", "+40", "o40"]
pattern4 = ["000", "o01", "+02", "+020", "+30", "o30", "-40", "-040"]
patterns = [pattern1, pattern2, pattern3, pattern4]

def find_indices(list_to_check, item_to_find, model_row):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append([model_row, idx])
    return indices



def findZeroIndex(model, targetNumber):
    modelRow = 0
    zeroIndex = []
    while modelRow < len(model):
        if targetNumber in model[modelRow]:
            if type(targetNumber) == int:
                zeroIndex = [modelRow, model[modelRow].index(targetNumber)]
                if len(zeroIndex) != 0:
                    return zeroIndex

            elif type(targetNumber) == str:
                zeroIndex = [modelRow, model[modelRow].index(targetNumber)]
                if len(zeroIndex) != 0:
                    return zeroIndex
            else:
                returnedPair = find_indices(model[modelRow], targetNumber, modelRow)
                if len(returnedPair) == 1:
                    zeroIndex.append(returnedPair[0])
                elif len(returnedPair) == 2:
                    zeroIndex.append(returnedPair[0])
                    zeroIndex.append(returnedPair[-1])
                elif len(returnedPair) == 3:
                    zeroIndex.append(returnedPair[0])
                    zeroIndex.append(returnedPair[1])
                    zeroIndex.append(returnedPair[-1])
                if len(zeroIndex) >= targetNumber*4:
                    return zeroIndex
        modelRow += 1
    return None


def makePattern(length):
    root = "000"
    # p1 = [root, "-010"]
    def patterns(n):
        p1 = []
        negaPostive = "+0" + n
        positive = "+0" + n + "0"
        
        p1.append(negaPostive)
        p1.append(positive)

        p2 = []
        posiNegative = "-" + n + "0"
        negative = "-0" + n + "0"
        p2.append(posiNegative)
        p2.append(negative)

        p3 = []
        posiPositive = "+" + n + "0"
        posiNeutral = "o" +n + "0"
        p3.append(posiPositive)
        p3.append(posiNeutral)

        p4 = []
        negaNegative = "-0" + n
        negaNeutral = "o0" + n
        p4.append(negaNegative)
        p4.append(negaNeutral)

        if int(n) % 4 == 0:
            return p1, p2, p3, p4
        if int(n) % 4 == 1:
            return p2, p3, p4, p1
        if int(n) % 4 == 2:
            return p3, p4, p1, p2
        elif int(n) % 4 == 3:
            return p4, p1, p2, p3
    
    patternList = []
    for x in range(1, length):
        if x == 1:
            patternList.append((["000", "o01"], ["000", "o10"], ["000", "-010"], ["000", "+010"]))
        elif x > 1:
            patternList.append(patterns(str(x)))
        
    return patternList


def reorganizePatterns(patterns):
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    for x in range(len(patterns)):
        for y in range(len(patterns[x])):
            if y == 0:
                p1.append(patterns[x][y][0])
                p1.append(patterns[x][y][-1])
            elif y == 1:
                p2.append(patterns[x][y][0])
                p2.append(patterns[x][y][-1])
            elif y == 2:
                p3.append(patterns[x][y][0])
                p3.append(patterns[x][y][-1])
            elif y == 3:
                p4.append(patterns[x][y][0])
                p4.append(patterns[x][y][-1])

    return p1, p2, p3, p4
            

def main():
    import pprint
    blaflooful = False
    if blaflooful:
        pixelMap = []
        pixelMap.append([findZeroIndex(pixelModel, 0)])
        pixelMap.append(findZeroIndex(pixelModel, 1))
        pixelMap.append(findZeroIndex(pixelModel, 2))
        pixelMap.append(findZeroIndex(pixelModel, 3))
        pixelMap.append(findZeroIndex(pixelModel, 4))
        pixelMap.append(findZeroIndex(pixelModel, 5))
        pixelMap.append(findZeroIndex(pixelModel, 6))

        pprint.pprint(pixelMap)

        for x in range(len(pixelMap)):
            for y in pixelMap[x]:
                print(pixelModel[y[0]][y[-1]])
    thePattern = makePattern(int(len(pixelModel2)/2) + 1)
    patternList = []
    patterns = reorganizePatterns(thePattern)
    for x in range(len(patterns)):
        theList = []
        for y in patterns[x]:
            theList.append(findZeroIndex(pixelModel2, y))
        patternList.append(theList)
    totalValue = 0
    pprint.pprint(patternList)
    for row in range(len(patternList)):
        sumValue = 0
        multiValue = 1
        valueList = []
        for coordinate in patternList[row]:
            value = fibonnaciModel[coordinate[0]][coordinate[-1]]
            sumValue += value 
            valueList.append(value)
            if value > 0:
                multiValue *= value
        totalValue = sum(set(valueList))*4
    print(totalValue)
    print(totalValue/144)

    print((7/9)*144)

    newModel = pixelModel2
    for x in range(1,5):
        newModel = addToPixelModel2(newModel)
        print(newModel)

    pprint.pprint(newModel)

if __name__ == "__main__":
    main()