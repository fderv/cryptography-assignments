#!/usr/bin/python

import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def get_key(ciphertexts):
    key = [0] * 1024
    for ct1 in ciphertexts:
        possible_spaces = [0] * 1024
        ct1string = ct1.decode('hex')
        for ct2 in ciphertexts:
            if (ct1 == ct2): continue
            ct2string = ct2.decode('hex')
            xored_cts = strxor(ct1string, ct2string)
            for i in range(len(xored_cts)):
                if (xored_cts[i].isalpha()):
                    possible_spaces[i] += 1

            for s in range(len(ct1string)):
                if possible_spaces[s] > len(ciphertexts)/2:
                    key[s] = chr(ord(ct1string[s]) ^ ord(" "))
    return "".join(map(str, key))
def main():

    with open("ciphers.txt") as file:
        ciphertexts = [ciphertext.rstrip('\n') for ciphertext in file]

    key = get_key(ciphertexts)

    cipher_to_be_decrypted = ciphertexts[10]

    print(strxor(cipher_to_be_decrypted.decode('hex'), key))

main()