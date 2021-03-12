 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import sys
import os

def encode_letter(p):
    # Encoding method
    c = p
    return (c)

def decode_letter(c):
    # Decoding method
    p = c
    return (p)

def encode(plaintext, *args):
    cyphertext = ""
    for p in plaintext:
        cyphertext += encode_letter(p)
    return (cyphertext)

def decode(cyphertext, *args):
    plaintext = ""
    for p in cyphertext:
        plaintext += decode_letter(p)
    return (plaintext)

def print_usage(msg=None):
    print("\nusage: prog.py -e plaintext [<cypher_arg1> <cypher_arg2> ... <cypher_argn>]")
    print("usage: prog.py -d cyphertext [<cypher_arg1> <cypher_arg2> ... <cypher_argn>]")
    print("usage: prog.py [-h, --help]\n")
    print("Arguments descriptions")
    print("     -e, --encode :      Encoding plaintext to cyphertext using the program selected")
    print("     -d, --decode :      Decoding cyphertext to plaintext using the program selected")
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
    #Checking if text file exists or can be opened ?
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
        elif i>2:
            args.append(arg)
    try:
        print(function(text, *args))
    except TypeError:
        print_usage("Wrong number of arguments.")