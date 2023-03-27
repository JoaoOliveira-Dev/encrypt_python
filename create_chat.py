import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Original: {chars}")
# print(f"Key: {key}")  

def encrypt(text):
    encrypted = ""
    key_env = "".join(key)
    print(f"Key: {key_env}")
    
    for char in text:
        index = chars.index(char)
        encrypted += key[index]
    return encrypted

def decrypt(text):
    decrypted = ""
    for char in text:
        index = key.index(char)
        decrypted += chars[index]
    return decrypted

text = input("Type a message: ")
encrypted = encrypt(text)
decrypted = decrypt(encrypted)

print(f"Original: {text}")
print(f"Encrypted: {encrypted}")