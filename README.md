# microPython crypto_keys

## encrypt / decrypt credentials with a chip specific key

The library is tested on the ESP32, but should also be usable for other microPython ports.

## Functionality
The aim of this library is not to leave the necessary credentials for contacting the WiFi network or the MQTT broker unencrypted in the chip's file system. Therefore, an AES encryption was used via the standard crypto library. The crucial point here is that the key is generated using the chip's own unique ID. This means that the encryption is bound to the chip and the data file itself is useless outside the chip's own file system.

These routines make it possible to store critical data on the chip in such a way that it cannot be easily read. The effort required to spy out and illegally use the data is exorbitantly greater than when using unencrypted data, and this with really little additional effort when using these routines.

The library we use is ucryptolib, which is already available in the microPython kernel. The main advantage of our library is 
- the encryption / decryption of standard strings 
- the possibility to access them via a keyword in the encrypted data file

## Generating the encrypted file
The data file can be created either by user input e.g. in ***set_credentials.py*** or by executing a prepared ***gen_credentials_dat.py***. Both examples can be found in the examples section.

## Use-Case
This small code snippet makes the simplicity, but also the potential of the library wonderfully clear. The encrypted credential data in the data file ***credential.dat*** can easily be passed on to further routines without them appearing in plain text.

    from crypto_keys import fn_crypto as crypt


    c = crypt()
    server   = c.get_decrypt_key("credentials.dat", "MQTT")
    ssid     = c.get_decrypt_key("credentials.dat", "SSID") 
    wifi_pw  = c.get_decrypt_key("credentials.dat", "WIFIPW") 
    user     = c.get_decrypt_key("credentials.dat", "UN") 
    password = c.get_decrypt_key("credentials.dat", "UPW")


## Acknowledgement
 The creation of this library was motivated by the discussions with [7wells](https://github.com/7wells) on the project-issue [inetbox2mqtt-credentials-encryption](https://github.com/mc0110/inetbox2mqtt/issues/3). I would like to thank him for his engagement.