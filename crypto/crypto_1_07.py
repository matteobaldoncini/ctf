#!/usr/bin/python3

import string
import base64
import itertools
import numpy as np


def encrypt(clear, key):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
        enc.append(enc_c)
    return str(base64.urlsafe_b64encode("".join(enc).encode("ascii")), "ascii")


def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode("ascii")), "ascii")
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)


m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="
d1_dict = {}
d2 = ""


if __name__ == "__main__":
    print("Bruteforcing k1 by encrypting m with several keys... ", end="", flush=True)
    for k1 in itertools.product(string.ascii_lowercase, repeat=4):
        k1 = "".join(k1)
        d1_dict[encrypt(m, k1)] = k1
    print("done")

    print("Bruteforcing k2 by decrypting c with several keys... ", end="", flush=True)
    for k2 in itertools.product(string.ascii_lowercase, repeat=4):
        k2 = "".join(k2)
        d2 = decrypt(c, k2)
        if d2 in d1_dict:
            print(f"done\n\nflag: CCIT{{{d1_dict[d2]}{k2}}}")


"""
se cripto m con le prime 4 cifre di K e decripto c con le ultime 4 cifre di K, e ottengo lo stesso d, allora è la chiave giusta
"""
