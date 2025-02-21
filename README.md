# CS 3090: An Encryption and Decryption Tool

## Feature
* **1. Encrypt password**: input password, the program will return a secret key and encrypt.
* **2. Decrypt encrypt**: input secret key and encrypt, the program will return the corresponding key.

## Dependency
* **Python 3.x**: developed based on Python 3.12.4

* **cryptography Library**: the only required library
* **run**: `python encryption_tool.py`

## Limitations
* **Educational Use Only**: This tool is designed for educational purposes and should not be used to secure sensitive information.
* **Management**: If the key is lost, the message cannot be decrypted.
* **Symmetric Encryption**: This toll uses symmetric encryption. it's not suitable for highly sensitive data protection.

## Potential Misuse
* **Malicious Modifications**: This program could be modified to create malicious tools, such as ransomware.
* **Unauthorized Access**: Do not use this tool to encrypt data without the owner's consent. Unauthorized encryption of data is illegal and unethical.
* **Data Privacy**: The program is designed to run entirely on the local device, ensuring that no data is transmitted over the network, and the tool does not save any files or retain any user data.
* **Encryption Algorithm**: The encryption algorithm utilized should be one-way, the encryption equation could be replaced or modified, rendering the encryption ineffective.

## AI Usage
* AI was used solely for learning about relevant libraries and as a translation tool to assist with understanding documentation and requirements.
* AI did not participate in the coding process.