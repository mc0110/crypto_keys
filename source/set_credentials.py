import os
from crypto_keys import fn_crypto as crypt



def find(name, path):
    x = False
    for files in os.listdir():
        x = x or (name in files)
    return x

print("Check for credentials.dat")
if not(find("credentials.dat", "/")):
    a = ""
    while a != "yes":
        print("Fill in your credentials:")
        SSID = input("SSID: ")
        print()
        Wifi_PW = input("Wifi-password: ")
        print()
        MQTT = input("MQTT-Server - IP or hostname: ")
        print()
        UName = input("Username: ")
        print()
        UPW = input("User-Password: ")
        print()
        print("Your inputs are:")
        print()
        print(f"SSID       : {SSID}")
        print(f"Wifi-PW    : {Wifi_PW}")
        print(f"MQTT-Server: {MQTT}")
        print(f"Username   : {UName}")
        print(f"User-PW    : {UPW}")
        print()
        a = input("ok for you (yes/no): ")
        
    print("Write credentials encrypted to disk")
    fn = open("credentials.dat", "wb")
    c = crypt()
    c.fn_write_encrypt(fn, "SSID:" + SSID)
    c.fn_write_encrypt(fn, "WIFIPW:" + Wifi_PW)
    c.fn_write_encrypt(fn, "MQTT:" + MQTT)
    c.fn_write_encrypt(fn, "UN:" + UName)
    c.fn_write_encrypt(fn, "USW:" + UPW)
    c.fn_write_eof_encrypt(fn)
    fn.close()
else:
    print("credentials.dat file exists -> pass the ask for credentials")
        
        
