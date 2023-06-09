# caesar cipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you want to encrypt or decrypt or bruteforce a message?')
        mode = input().lower()
        if mode in ['encrypt','e','decrypt','d','bruteforce', 'b']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "bruteforce" or "b".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)'%(MAX_KEY_SIZE))
        key = int(input())
        if 1 <= key <= MAX_KEY_SIZE:
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated



mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated message is:')
if mode[0] != 'b':
    getTranslatedMessage(mode, message, key)
else:
    for key in range(1, MAX_KEY_SIZE+1):
        print(key, getTranslatedMessage('d', message, key))


