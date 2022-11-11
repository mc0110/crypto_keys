# MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#
# This is part of the crypto_keys_package
# 
# 
# Make your encrypted file with your credentials visible
# You shouldn't hold this file in your port-filesystem
#


import os
from crypto_keys import fn_crypto as crypt



def find(name, path):
    x = False
    for files in os.listdir():
        x = x or (name in files)
    return x

if (find("credentials.dat", "/")):
    print("Read credentials.dat ....")     
    fn = open("credentials.dat", "rb")
    c = crypt()
    print(c.fn_read_decrypt(fn))
    print(c.fn_read_decrypt(fn))
    print(c.fn_read_decrypt(fn))
    print(c.fn_read_decrypt(fn))
    print(c.fn_read_decrypt(fn))
    print(c.fn_read_decrypt(fn))
    fn.close()
