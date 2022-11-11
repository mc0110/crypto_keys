# microPython crypto_keys
encrypt / decrypt credentials with a chip specific key - unreadable and individual

The library is tested on the ESP32, but should also be usable for other microPython ports.

## Functionality
The aim of this library is not to leave the necessary credentials for contacting the WiFi network or the MQTT broker unencrypted in the chip's file system. Therefore, an AES encryption was used via the standard crypto library. The crucial point here is that the key is generated using the chip's own unique ID. This means that the encryption is bound to the chip and the data file itself is useless outside the chip's own file system.


