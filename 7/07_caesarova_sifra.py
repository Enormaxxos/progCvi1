alphabet = "aábcčdďeéěfghiíjklmnňoópqrřsštťuúůvwxyýzž"
alphabetCharCount = len(alphabet)

def caesarCipher(text,shiftNum):

    encipheredText = ""

    for char in text:
        if not char.isalpha():
            encipheredText += char
            continue

        charIndex = alphabet.index(char)
        newIndex = (charIndex + shiftNum) % alphabetCharCount
        encipheredText += alphabet[newIndex]

    return encipheredText

def inputHandler(inputString):
    inputString = inputString.lower()
    splitIndex = inputString.index(';')
    shiftNum = int(inputString[:splitIndex])
    text = inputString[splitIndex+1:]

    return caesarCipher(text,shiftNum)

print(inputHandler(input()))