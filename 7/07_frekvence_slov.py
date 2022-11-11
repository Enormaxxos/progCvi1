import string

def wordFrequency(inputString):
    strList = inputString.split()

    wordLibrary = dict()

    for word in strList:
        newWord = ""
        hasVowel = False
        for char in word:
            if char in string.punctuation:
                continue
            elif char.lower() in "aáeěéiíyýoóuůú":
                hasVowel = True

            newWord += char.lower()

        try:
            wordLibrary[newWord]['number'] += 1
        except KeyError:
            wordLibrary[newWord] = {
                'number': 1,
                'hasVowel': hasVowel
            }

    for word in wordLibrary.keys():
        if wordLibrary[word]['hasVowel'] and wordLibrary[word]['number'] % 2 == 0:
            print(word)
                
wordFrequency(input())

    
