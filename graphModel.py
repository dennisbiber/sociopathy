# this is an expirement in new ways to Enummerate pixels in an image.
# the pixelModel2 example seems to work the best as it creates 4 parallel fibonnaci spirals of the data in the image


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
    ["+040"],
    ["+04", "+030", "+40"],
    ["+04", "+03", "+020", "+30", "+40"],
    ["+04", "+03", "+02", "+010", "+20", "+30", "+40"],
    ["o04", "o03", "o02", "o01", "000", "o10" "o20", "o30", "o40"],
    ["-04", "-03", "-02", "-010", "-20", "-30", "-40"],
    ["-04", "-03", "-020", "-30", "-40"],
    ["-04", "-030", "-40"],
    ["-040"]
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


def getNextCorridante(model, zeroIndex):
    pass


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

    patternList = []
    for x in range(len(patterns)):
        theList = []
        for y in patterns[x]:
            theList.append(findZeroIndex(pixelModel2, y))
        patternList.append(theList)

    pprint.pprint(patternList)

if __name__ == "__main__":
    main()