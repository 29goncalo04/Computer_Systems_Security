import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt(key, plainext):
    text = ""
    for i in range(len(plainext)):
        K = ALPHABET.index(key)
        P = ALPHABET.index(plainext[i])
        C = (P-K)%26
        text += ALPHABET[C]
    return text

def attack(cryptograma, words):
    for character in ALPHABET:
        text = decrypt(character, cryptograma)
        for word in words:
            if word in text:
                print (character)
                print (text)
                return
    return

def main(args):
    cryptograma = args[1]
    words = args[2:]
    attack(cryptograma, words)
    return 0

if __name__ == "__main__":
    main(sys.argv)