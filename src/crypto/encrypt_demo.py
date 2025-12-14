from Crypto.Cipher import AES
import os

def encrypt_message(message: str):
    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())

    print("Key:", key.hex())
    print("Ciphertext:", ciphertext.hex())
    print("Tag:", tag.hex())

    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
    plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)
    print("Decrypted:", plaintext.decode())

if __name__ == "__main__":
    encrypt_message("Hello Cyber World")