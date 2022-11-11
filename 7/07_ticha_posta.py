class Speaker:
    def __init__(self,name):
        self.name = name

    def say(self,message):
        return f"{self.name}: {message}"

class LoudSpeaker(Speaker):
    def say(self,message):
        return f"{self.name}: {message.upper()}"

class SilentSpeaker(Speaker):
    def say(self,message):
        return f"{self.name}: {message.lower()}"


def inputHandler(stringInput):
    splitIndex = stringInput.index(";")
    message = stringInput[:splitIndex]
    peopleDict = eval(stringInput[splitIndex+1:])

    people = []

    sortedKeys = sorted(peopleDict.keys())

    for key in sortedKeys:
        if peopleDict[key] == 'normální':
            people.append(Speaker(key))
        elif peopleDict[key] == 'tichošlápek':
            people.append(SilentSpeaker(key))
        else:
            people.append(LoudSpeaker(key))

    for human in people:
        print(human.say(message))


inputHandler(input())