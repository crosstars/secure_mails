import socket
import pickle#using pickle to convert objects into bytes so that we can easily transfer object information through socket.
from tinyec import registry#tinyec used to preform elliptic curve diffie hellman key exchange
import secrets
from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path

files = []# storing file names in a list
body = []# splitting message body into parts and putting it into a list and then encrypting it.
def compress(pubKey):# to convert the keys into a 256 bit keys as the private keys and public keys are in the form of point objects.
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)#private key of sender
alicePubKey = alicePrivKey * curve.g#public key of sender

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):#to encrypt the message
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(file_name,key):#to store file data into a string and then sending it to encrypt function to encrypt.
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()#storing file contents in a string
    enc = encrypt(plaintext,key)#storing encrypted file in a string
    with open(file_name + ".enc", 'wb') as fo:#generating encrypted file
        fo.write(enc)
    os.remove(file_name)#removing original file
    

def client():
    host = socket.gethostname()
    port = 5000
    
    alicePub = pickle.dumps(alicePubKey)#public key of sender which will be uploaded in the database
  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    client_socket.send(alicePub)
    
    bobPub = client_socket.recv(4096)
    bobPub = pickle.loads(bobPub)
    
    enckey = bobPub * alicePrivKey
    enckey = compress(enckey)
    enckey = int(enckey,16)
    enckey = bin(enckey)[:256]
    enckey = int(enckey, 2).to_bytes((len(enckey) + 7) // 8, byteorder='big')
    
    print("Enter body of your mail,if any\n")
    print("Press 1 to enter body of mail or 0 if you dont have any body- \n")
    choice = int(input())
    if(choice==1):
        print("Enter body of mail.\n")
        temp = input().splitlines()
        for i in temp:
            body.append(encrypt(i.encode('utf-8'),enckey))
            
    n = int(input("Enter no of files you want to encrypt:- "))
    for i in range(0,n):
        file_name=str(input("Enter the file name- "))
        files.append(file_name)
        encrypt_file(file_name,enckey)
        
    tempb = pickle.dumps(body)
    tempf = "+".join([i for i in files])
    
    client_socket.send(tempb)
    client_socket.send(tempf.encode('utf-8'))
    
    client_socket.close()

if __name__ == '__main__':
    client()