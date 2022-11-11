# MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#
# Crypto-Class for Strings with bonding the key with the machine.unique_id
#
#
# This modules are using the machine_unique_number to generate the key for encrypt / decrypt
# with the consequence, that the data are only on the target-system are usable and readable
# 
# Based on an ESP32 Micropython implementation of cryptographic but should also be useable on other hw-implementations (ports)
#
# reference:
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
# https://docs.micropython.org/en/latest/library/ucryptolib.html
#
 
import os
from ucryptolib import aes
import machine


# Cryptomodule: keys are generated with the chip_unique_id and with the random generator
class crypto:
    def encrypt(text):
        BLOCK_SIZE = 32
        IV_SIZE = 16
        MODE_CBC = 2
        # Padding plain text with space
        
        pad = BLOCK_SIZE - len(text) % BLOCK_SIZE
        text = text + " "*pad
        key1 = machine.unique_id()
        key = bytearray(b'I_am_32bytes=256bits_key_padding')
        for i in range(len(key1)-1):
            key[i] = key1[i]
            key[len(key)-i-1] = key1[i]
        # Generate iv with HW random generator 
        iv = os.urandom(IV_SIZE)
        cipher = aes(key, MODE_CBC, iv)
        ct_bytes = iv + cipher.encrypt(text)
        return ct_bytes

    def decrypt(enc_bytes):
        BLOCK_SIZE = 32
        IV_SIZE = 16
        MODE_CBC = 2
        key1 = machine.unique_id()
        key = bytearray(b'I_am_32bytes=256bits_key_padding')
        for i in range(len(key1)-1):
            key[i] = key1[i]
            key[len(key)-i-1] = key1[i]
        # Generate iv with HW random generator 
        iv = enc_bytes[:IV_SIZE]
        cipher = aes(key, MODE_CBC, iv)
        return cipher.decrypt(enc_bytes)[IV_SIZE:].strip()


# Here an entry will be written to an file, prepared open for binary write (wb / rb)
class fn_crypto:
    def __init__(self):
        pass

# Encrypt string x and write it encrypted
# Format is no. of bytes (2 bytes long) and then the bytes     
    def fn_write_encrypt(self, f, x):
        cip = crypto
        x = cip.encrypt(x)
        f.write(len(x).to_bytes(2, 'little'))
        f.write(x)

# Write eof-indicator with 0x00 0x00
    def fn_write_eof_encrypt(self, f):
        x=0
        f.write(x.to_bytes(2, 'little'))
        
        
# Read encrypted entry and decrypt it as string
# Format is no. of bytes (2 bytes long) and then the bytes     
    def fn_read_decrypt(self, f):
        cip = crypto
        x = int.from_bytes(f.read(2), "little")
        if x > 0:
            return str(cip.decrypt(f.read(x)), 'utf-8')
        else: return ""


# Read x bytes encrypted entry and decrypt it as string
# No. of bytes are given     
    def fn_read_str_decrypt(self, f, x):
        cip = crypto()
        return str(cip.decrypt(f.read(x)), 'utf-8')


# Search a message for a given key in an encrypted file
# String-format is KEY:MESSAGE
# Returns Message or 0, if Key not found
    def get_decrypt_key(self, fn, key):
        f = open(fn, "rb")
        s = self.fn_read_decrypt(f)
        while s != "":
            if s.find(key) > -1:
                f.close()
                return str(s[s.find(":")+1:], 'utf-8')
            s = self.fn_read_decrypt(f)
        f.close()    
        return 0    
