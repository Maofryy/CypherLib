


import sys
import os
import collections

def rot(c, nb):
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = "abcdefghijklmnopqrstuvwxyz"
    ALPHA_rot = ALPHA[nb:] + ALPHA[:nb]
    alpha_rot = alpha[nb:] + alpha[:nb]
    for i in range(len(alpha)):
       if c == ALPHA[i]:
           return ALPHA_rot[i]
       if c == alpha[i]:
           return alpha_rot[i]
    return (c)

def decode_letter(c, key):
    # Decoding method
    p = rot(c, -int(key))
    return (p)

def decode(cyphertext, key):
    plaintext = ""
    for c in cyphertext:
        plaintext += decode_letter(c, key)
    return (plaintext)

if __name__ == "__main__":
    
    if not (os.path.exists(sys.argv[1]) and os.access(sys.argv[1], os.R_OK)):
        print("Error: plaintext of cyphertext file is inaccessible.")
        exit()

    with open(sys.argv[1], 'r') as f:
        cyphertext = f.read()
    
    most_freq = collections.Counter(cyphertext.replace(" ", "")).most_common(1)
    key = ord(most_freq[0][0]) - ord('e')
    
    plaintext = decode(cyphertext, key)

    print(plaintext)
    print("Key = %d\n"%key)



