# MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#
# This is part of the crypto_keys_package
# 
# 
# The possibility to generate an encrypted file with your credentials
# You should delete this file from port after execution
#

import os
from crypto_keys import fn_crypto as crypt
 
#
fn = open("credentials.dat", "wb")
c = crypt()
c.fn_write_encrypt(fn, "SSID:YourWiFi")
c.fn_write_encrypt(fn, "WIFIPW:YourWIFIPassword")
c.fn_write_encrypt(fn, "MQTT:YourBroker")
c.fn_write_encrypt(fn, "UN:YourMQTTUser")
c.fn_write_encrypt(fn, "UPW:YourUserPassword")
c.fn_write_eof_encrypt(fn)
fn.close()
