import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def preproc(str):
    l = []
    for c in str:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)

def encrypt(key, plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        K = ALPHABET.index(key)
        P = ALPHABET.index(plaintext[i])
        C = (P+K)%26
        ciphertext += ALPHABET[C]
    return ciphertext

def decrypt(key, plainext):
    text = ""
    for i in range(len(plainext)):
        K = ALPHABET.index(key)
        P = ALPHABET.index(plainext[i])
        C = (P-K)%26
        text += ALPHABET[C]
    return text

def main(args):
    if len(args)!=4:
        print("Argumentos incorretos")
        return -1
    operacao = args[1]
    key = args[2]
    plaintext = args[3]
    if operacao == "enc":
        print(encrypt(key, preproc(plaintext)))
    elif operacao == "dec":
        print(decrypt(key, preproc(plaintext)))
    else:
        return -1
    return 0


if __name__ == "__main__":
    main(sys.argv)