import sys

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def preproc(str):
    l = []
    for c in str:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)

def encrypt(keys, texto):
    resultado = ""
    for i  in range(len(texto)):
        index_key = i%len(keys)
        K = ALPHABET.index(keys[index_key])
        P = ALPHABET.index(texto[i])
        C = (P+K)%26
        resultado += ALPHABET[C]
    return resultado

def decrypt(keys, texto):
    resultado = ""
    for i  in range(len(texto)):
        index_key = i%len(keys)
        K = ALPHABET.index(keys[index_key])
        P = ALPHABET.index(texto[i])
        C = (P-K)%26
        resultado += ALPHABET[C]
    return resultado

def main(args):
    operacao = args[1]
    keys = args[2]
    texto = args[3]
    if operacao=="enc":
        print(encrypt(keys, preproc(texto)))
    elif operacao=="dec":
        print(decrypt(keys, preproc(texto)))
    else: 
        return -1
    return 0

if __name__ == "__main__":
    main(sys.argv)