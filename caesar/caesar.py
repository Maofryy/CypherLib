 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
import os
import traceback
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

def crack(cyphertext):
    most_freq = collections.Counter(cyphertext.replace(" ", "")).most_common(1)
    key = ord(most_freq[0][0]) - ord('e')
    
    plaintext = decode(cyphertext, key)

    return (plaintext, key)

def encode_letter(p, *args):
    # Encoding method
    c = rot(p, int(args[0]))
    return (c)

def decode_letter(c, *args):
    # Decoding method
    p = rot(c, -int(args[0]))
    return (p)

def encode(plaintext, *args):
    cyphertext = ""
    for p in plaintext:
        cyphertext += encode_letter(p, *args)
    return (cyphertext)

def decode(cyphertext, *args):
    plaintext = ""
    for c in cyphertext:
        plaintext += decode_letter(c, *args)
    return (plaintext)

def print_usage(msg=None):
    print("\nusage: prog.py -e plaintext [<cypher_arg1> <cypher_arg2> ... <cypher_argn>]")
    print("usage: prog.py -d cyphertext [<cypher_arg1> <cypher_arg2> ... <cypher_argn>]")
    print("usage: prog.py -c [<cypher_arg1> <cypher_arg2> ... <cypher_argn>]")
    print("usage: prog.py [-h, --help]\n")
    print("Arguments descriptions")
    print("     -e, --encode :      Encoding plaintext to cyphertext using the program selected")
    print("     -d, --decode :      Decoding cyphertext to plaintext using the program selected")
    print("     -c, --crack :       Cracking cyphertext to plaintext using statistical attack")
    print("     <cypher_arg> :      Args passed to cypher program, key or passphrase, etc...")
    print("     -h, --help:         Printing this usage message")
    if not isinstance(msg, type(None)):
       print(msg) 
    exit()

if __name__ == "__main__":
    #Check for incorrect number of args
    if (len(sys.argv) < 3):
        print_usage("Error: not enough arguments were passed.\nPlease refer to the usage printed.")
    
    #* Check for method used and passing arguments from main to encoding or decoding functions
    #Checking if text file exists or can be opened ? without the command
    if not (os.path.exists(sys.argv[2]) and os.access(sys.argv[2], os.R_OK)):
        print_usage("Error: plaintext of cyphertext file is inaccessible.")
    
    #Checking for args
    function = print
    text = None
    args = list()
    for i, arg in enumerate(sys.argv[1:]):
        if (arg == '-h' or arg =='--help'):
            print_usage()
        if (arg == '-e' or arg == '--encode') and i == 0:
            #open plaintext file to string 
            with open(sys.argv[i+2], 'r') as f:
                plaintext = f.read()
            #Choose encoder
            function = encode
            text = plaintext
        if (arg == '-d' or arg == '--decode') and i == 0:
            with open(sys.argv[i+2], 'r') as f:
                cyphertext = f.read()
            function = decode
            text = cyphertext
        if (arg == '-c' or arg == '--crack') and i == 0:
            with open(sys.argv[i+2], 'r') as f:
                cyphertext = f.read()
            function = crack
            text = cyphertext
        elif i>1:
            args.append(arg)
    try:
        output_text = function(text, *args)
    except (TypeError, IndexError):
        traceback.print_exc()
        print_usage("Wrong number of arguments.")
    
    if function == encode:
        print(output_text)
        with open("cypher_caesar.txt", 'w') as f:
            f.write(output_text)
    elif function == decode:
        print(output_text)
        with open("plain_caesar.txt", 'w') as f:
            f.write(output_text)
    elif function == crack:
        print(output_text)
        with open("crack_caesar.txt", 'w') as f:
            f.write(output_text[0])