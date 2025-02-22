import sys
from itertools import product
from collections import Counter

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_comuns = 'ZQJXKVBPGYFMWCULDRHSNIOATE'   #da mais incomum à mais comum

def preproc(str):
    l = []
    for c in str:
        if c.isalpha():
            l.append(c.upper())
    return "".join(l)

def decrypt(keys, texto):
    resultado = ""
    for i  in range(len(texto)):
        index_key = i%len(keys)
        K = ALPHABET.index(keys[index_key])
        P = ALPHABET.index(texto[i])
        C = (P-K)%26
        resultado += ALPHABET[C]
    return resultado

#calcula uma pontuação baseada na frequência das letras
def letter_score(text):
    # Contar a frequência das letras no texto
    frequencia = Counter(text)
    score = 0
    for letter,frequency in frequencia.items():
        score += frequency*letras_comuns.index(letter)
    return score

def attack(key_length, cryptograma, words):
    best_score = -1
    best_key = ""
    best_plainText = ""
    for key in product(ALPHABET, repeat=key_length):   #tenta todas as combinações de chaves com tamanho 'key_length' contendo apenas caracteres do 'ALPHABET'
        possible_key = "".join(key)
        possible_plainText = decrypt(possible_key, cryptograma)
        for word in words:
            if word in possible_plainText:
                score = letter_score(possible_plainText)
                if score >= best_score:
                    best_score = score
                    best_key = possible_key
                    best_plainText = possible_plainText
    print(best_key)
    print(best_plainText)
    return


def main(args):
    key_length = int(args[1])
    cryptograma = args[2]
    words = args[3:]
    attack(key_length, preproc(cryptograma), words)
    return 0

if __name__ == "__main__":
    main(sys.argv)