import json

def jsonValuation(fileContents):
    for item in fileContents:
        print(valueSentence(item))

def valueSentence(item, timeStamp):
    writeList = []
    qualityValue = item[timeStamp]["qualumValue"]
    quauntityValue = item[timeStamp]["quantumValue"]
    sentence = item[timeStamp]["sentence"]
    values = [qualityValue, quauntityValue]
    listAssign = 0
    for value in values:
        if value > 0 and value <= 1:
            value = 1
        elif value > 1 and value <= 2:
            value = 2
        elif value > 2 and value <= 3:
            value = 3
        elif value > 3:
            value = 4
        elif value < 0 and value >= -1:
            value = -1
        elif value < -1 and value >= -2:
            value = -2
        elif value < -2 and value >= -3:
            value = -3
        elif value < -3:
            value = -4
        value = [sentence] * int(value)
        if listAssign == 0 and value != "":
            writeList.append({"qualumSentence": value})
        elif listAssign == 1 and value != "":
            writeList.append({"quantumSentence": value})
        listAssign += 1

    return writeList


def unpackNestedList(listylist):
    masterList = []
    for listeroo in listylist:
        lenCount = 0
        listLen = len(listeroo)
        while lenCount < listLen:
            masterList.append(listeroo[lenCount])
            lenCount += 1
    return masterList


def makeJsonTestAvail(struct):
    content = []
    for key in range(len(struct)):
        timeStamp = [x for x in struct[key].keys()][0]
        sentences = struct[key][timeStamp]["sentence"]
        if len(sentences[0]["qualumSentence"]) != 0:
            content.append(sentences[0]["qualumSentence"])
        if len(sentences[-1]["quantumSentence"]) != 0:
            content.append(sentences[-1]["quantumSentence"])
    return unpackNestedList(content)

def main():
    filename = "/home/dbiber/data/sociopathy/botdose_1668609245.0857794.json"
    struct = []
    with open(filename, "r") as f:
        struct = json.load(f)
    print(makeJsonTestAvail(struct))

if __name__ == "__main__":
    main()