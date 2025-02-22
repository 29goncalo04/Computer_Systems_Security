import sys
import os

def setup(nBytes, file_path):
    bytes = os.urandom(nBytes)
    correct_file_path = "./OTP/" + (file_path)
    with open(correct_file_path, "wb") as file:
        file.write(bytes)

def encrypt(file_text, file_key):
    with open("./OTP/" + file_text, "r") as file:
        plainText = file.read()
    with open("./OTP/" + file_key, "rb") as file:
        keys = file.read()
    bin_plainText = "".join(format(ord(c), '08b') for c in plainText)  #mensagem em binário
    bin_keys = "".join(format(byte, '08b') for byte in keys)  # chave em binário
    bin_textEncrypted = ""
    for i in range(len(bin_plainText)):
        if bin_plainText[i] == bin_keys[i]:
            bin_textEncrypted += "0"
        else:
            bin_textEncrypted += "1"
    with open("./OTP/" + file_text + ".enc", "w") as file:
        file.write(bin_textEncrypted)

def decrypt(file_text, file_key):
    with open("./OTP/" + file_text, "r") as file:
        bin_textEncrypted = file.read()
    with open("./OTP/" + file_key, "rb") as file:
        keys = file.read()
    bin_keys = "".join(format(byte, '08b') for byte in keys)  # chave em binário
    bin_plainText = ""
    for i in range(len(bin_textEncrypted)):
        if bin_textEncrypted[i] == bin_keys[i]:
            bin_plainText += "0"
        else: 
            bin_plainText += "1"
    plainText = ""
    for i in range(0, len(bin_plainText), 8):    #converte os bits numa string
        plainText += chr(int(bin_plainText[i:i+8], 2))
    with open("./OTP/" + file_text + ".dec", "w") as file:
        file.write(plainText)

def main(args):
    operacao = args[1]
    if operacao == "setup":
        nBytes = int(args[2])
        file_path = args[3]
        setup(nBytes, file_path)
    elif operacao == "enc":
        file_text = args[2]
        file_key = args[3]
        encrypt(file_text, file_key)
    elif operacao == "dec":
        file_text = args[2]
        file_key = args[3]
        decrypt(file_text, file_key)


if __name__ == "__main__":
    main(sys.argv)