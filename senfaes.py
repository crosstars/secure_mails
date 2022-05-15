from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
import recfaes

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(file_name):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext,key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    os.remove(file_name)
    
key = os.urandom(32)
print(key)
files=[]
body = []
print("Enter body of your mail,if any\n")
print("Press 1 to enter body of mail or 0 if you dont have any body- \n")
choice = int(input())
if(choice==1):
    print("Enter body of mail.\n")
    temp = input().splitlines()
    for i in temp:
        body.append(encrypt(i.encode('utf-8'),key))
    
n = int(input("Enter no of files you want to encrypt:- "))
for i in range(0,n):
    file_name=str(input("Enter the file name- "))
    files.append(file_name)
    encrypt_file(file_name)
    


if(recfaes.permission()):
    recfaes.keydec(key,body,files)
        

