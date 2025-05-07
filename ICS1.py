from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import binascii


def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return binascii.hexlify(iv).decode('utf-8'),binascii.hexlify(ciphertext).decode('utf-8')

def decrypt_data(iv, ciphertext, key):
    iv = binascii.unhexlify(iv)
    ciphertext = binascii.unhexlify(ciphertext)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode()

if __name__ == "__main__":
    key = os.urandom(32)
    data = "This is a secret message"
    print("Original data : ", data)
    iv, ciphertext = encrypt_data(data, key)
    print("IV:", iv)
    print("ciphertext : ", ciphertext)

    decrypt_data = decrypt_data(iv, ciphertext, key)
    print("decrypted Data : ", decrypt_data)