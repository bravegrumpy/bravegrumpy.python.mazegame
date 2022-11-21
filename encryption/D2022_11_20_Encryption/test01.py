import cryptography
from cryptography.fernet import Fernet

message = input("Input string here:\n")

key = Fernet.generate_key()
fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("Original message: {message}\nEncrypted message: {enc}".format(message=message, enc=encMessage))

decMessage = fernet.decrypt(encMessage).decode()

print("Decrypted message: {dec}".format(dec=decMessage))