


def inputHandler(stringInput):
    splitIndex = stringInput.index(";")
    message = stringInput[:splitIndex]
    remainder = stringInput[splitIndex+1:]

    print(f"message = {message}")
    print(f"remainder = {remainder}")
    return True


print(inputHandler("Někdo Klepe!;{'Anna': 'normální', 'Petr': 'tichošlápek', 'Marie': 'řvoun'}"))