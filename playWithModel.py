import json
from sociotransmitters import openLanguageStruct, consonantList
import pprint
import english_words
import nltk
import random
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

filename = "/home/dbiber/data/sociopathy/languageStruct.json"
wordsList = []
words, prefix, suffix = openLanguageStruct(filename = filename)
# for x in words:
#     for y in suffix:
#         if x[-1] not in consonantList and y[0] not in consonantList:
#             word = f"{x}{y}"
#         elif x[-1] in consonantList and y[0] not in consonantList:
#             word = f"{x}{y}"
#         elif x[-1] not in consonantList and y[0] in consonantList:
#             word = f"{x}{y}"
#         if word in english_words.english_words_lower_set:
#             if word not in wordsList:
#                 wordsList.append(word)
#         for z in prefix:
#             word = f"{z}{x}"
#             if word in english_words.english_words_lower_set:
#                 if word not in wordsList:
#                     wordsList.append(word)
#             word2 = f"{z}{y}"
#             if word2 in english_words.english_words_lower_set:
#                 if word not in wordsList:
#                     wordsList.append(word)
#             word3 = f"{z}{x}{y}"
#             if word3 in english_words.english_words_lower_set:
#                 print(word2)
#                 if word not in wordsList:
#                     wordsList.append(word)

# pprint.pprint(wordsList)
wordDict = {}
for x in words:
    prefixList = []
    for w in words:
        for y in prefix:
            for z in prefix:
                for t in suffix:
                    word = f"{y}{x}"
                    word2 = f"{z}{y}{x}"
                    word3 = f"{y}{z}{x}"
                    word4 = f"{x}{w}"
                    word5 = f"{y}{x}{w}"
                    word6 = f"{x}{t}"
                    word7 = f"{y}{x}{t}"
                    if word in english_words.english_words_lower_set:
                        if f"{y}-{x}" not in prefixList:
                            prefixList.append(f"{y}-{x}")
                    if word2 in english_words.english_words_lower_set:
                        if f"{z}-{y}-{x}" not in prefixList:
                            prefixList.append(f"{z}-{y}-{x}")
                    if word3 in english_words.english_words_lower_set:
                        if f"{y}-{z}-{x}" not in prefixList:
                            prefixList.append(f"{y}-{z}-{x}")
                    if word4 in english_words.english_words_lower_set:
                        if f"{x}-{w}" not in prefixList:
                            prefixList.append(f"{x}-{w}")
                    if word5 in english_words.english_words_lower_set:
                        if f"{y}-{x}-{w}" not in prefixList:
                            prefixList.append(f"{y}-{x}-{w}")
                    if word6 in english_words.english_words_lower_set:
                        if f"{x}-{t}" not in prefixList:
                            prefixList.append(f"{x}-{t}")
                    if word7 in english_words.english_words_lower_set:
                        if f"{y}-{x}-{t}" not in prefixList:
                            prefixList.append(f"{y}-{x}-{t}")

    if prefixList != []:
        wordDict[x] = prefixList

pprint.pprint(wordDict)
