import sys
import random

def bad_prng_with_seed(nBytes, seed):
    random.seed(seed)
    return random.randbytes(nBytes)

def attack(cryptogram_file, words):
    with open("./OTP/" + cryptogram_file, "r") as file:
        encrypted_text = file.read()
    for seed in range(65536):
        #with open("./OTP/bad_otp.key", "rb") as file:
        #    possible_key = file.read()
        possible_key = bad_prng_with_seed(30, seed)
        bin_possible_key = "".join(format(byte, '08b') for byte in possible_key)  # chave em binário
        bin_possible_plainText = ""
        for i in range(len(encrypted_text)):
            if encrypted_text[i] == bin_possible_key[i]:
                bin_possible_plainText += "0"
            else:
                bin_possible_plainText += "1"
        possible_plainText = ""
        for k in range(0, len(bin_possible_plainText), 8):    #converte os bits numa string
            possible_plainText += chr(int(bin_possible_plainText[k:k+8], 2))
        for word in words:
            if word in possible_plainText:
                print(possible_plainText)
                return 

def main(args):
    cryptogram_file = args[1]
    words = args[2:]
    attack(cryptogram_file, words)

if __name__ == "__main__":
    main(sys.argv)