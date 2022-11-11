# MIT License
#
# Copyright (c) 2022  Dr. Magnus Christ (mc0110)
#
# This is part of the crypto_keys_package
# 
# 
# After reboot the port starts with boot.py and main.py
# If you bind this code-segment with
#
# import set_credentials
#
# then after the boot-process the port checks for an encrypted credential.dat file
# If this file isn't found, the user will be asked for input of credentials.
# After the procedure the data will be stored encrypted.
#
#
# You can use this short snippet for decrypt your encrypted credentials
#

from crypto_keys import fn_crypto as crypt


c = crypt()
server   = c.get_decrypt_key("credentials.dat", "MQTT")
ssid     = c.get_decrypt_key("credentials.dat", "SSID") 
wifi_pw  = c.get_decrypt_key("credentials.dat", "WIFIPW") 
user     = c.get_decrypt_key("credentials.dat", "UN") 
password = c.get_decrypt_key("credentials.dat", "UPW")

