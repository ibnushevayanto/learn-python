alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
totalAlphabet = len(alphabet)

def getIndexOfAlphabet(charachter):
    theIndexOfAlphabet =  0
    while True:
        if alphabet[theIndexOfAlphabet] == charachter.lower():
            break
        theIndexOfAlphabet += 1
    return theIndexOfAlphabet
def getEncodeMessage(message, shiftNumber): 
    encodeMessage = ""
    
    for charachter in message:
        shiftNumberOverral = shiftNumber % len(alphabet)
        indexMessageAfterShift = (getIndexOfAlphabet(charachter) + shiftNumberOverral) % len(alphabet)
        encodeMessage += alphabet[indexMessageAfterShift]
        
    return encodeMessage


def getDecodeMessage(message, shiftNumber): 
    decodeMessage = ""
    
    for charachter in message:
        shiftNumberOverral = shiftNumber % len(alphabet)
        indexMessageAfterShift = (getIndexOfAlphabet(charachter) - shiftNumberOverral) % len(alphabet)
        decodeMessage += alphabet[indexMessageAfterShift]
        
    return decodeMessage

while True:
    mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n")
    shiftNumber = int(input("Type the shift number:\n"))
    messageList = message.split()
    
    if mode == "encode":
        for idx in range(0, len(messageList)):
            messageList[idx] = getEncodeMessage(messageList[idx], shiftNumber)
        print(f'Here\'s the encode result: {" ".join(messageList)}')
    elif mode == 'decode':
        for idx in range(0, len(messageList)):
            messageList[idx] = getDecodeMessage(messageList[idx], shiftNumber)
        print(f'Here\'s the encode result: {" ".join(messageList)}')
    else:
        print("Your command not found, Exit!")
        break 

    wannaPlayAgain = input("Type 'yes' if you want to go again:\n").lower()
    if wannaPlayAgain != "yes":
        print("Exit!")
        break
    