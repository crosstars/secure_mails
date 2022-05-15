import socket
import pickle#using pickle to convert objects into bytes so that we can easily transfer object information through socket.
from tinyec import registry
import secrets
from Crypto.Cipher import AES
import os
import os.path


def compress(pubKey):# to convert the keys into a 256 bit keys as the private keys and public keys are in the form of point objects.
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g

def decrypt(ciphertext, key):#decryption function
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(file_name,key):# storing encrypted file in to string and sending it to decrypt function to get the original file.
    with open(file_name, 'rb') as fo:#storing encrypted file in a string and sending it decrypt function
        ciphertext = fo.read()
    dec = decrypt(ciphertext,key)
    with open(file_name[:-4], 'wb') as fo:#storing the decrypted file with the original file name and storing it.
        fo.write(dec)
    os.remove(file_name)#removing the encrypted file
    
def keydec(temp,body,fi):
    print("Message Body\n")#decrypting message body
    for i in body:
        print(str(decrypt(i,temp))[2:-1]+"\n")
    print("\n")
    
    for i in fi:#decrypting files
        decrypt_file(i+".enc",temp)
        
def server():
    
    host = socket.gethostname()
    port = 5000
    print("->" + host)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))
    
    alicePub = conn.recv(4096)
    alicePub = pickle.loads(alicePub)#recieving senders public key
    
    bobPub =  pickle.dumps(bobPubKey)#sending sender recievers public key
     
    conn.send(bobPub)
    
    deckey = alicePub * bobPrivKey 
    
    deckey = compress(deckey) # getting the decryption key
    deckey = int(deckey,16)
    deckey = bin(deckey)[:256] 
    deckey = int(deckey, 2).to_bytes((len(deckey) + 7) // 8, byteorder='big') # the final key which will be use for decryption (256 bits)    
    body = conn.recv(4096)
    body = pickle.loads(body)
    files = conn.recv(4096).decode('utf-8')
    files = files.split('+')
    keydec(deckey,body,files)
    
    conn.close()

if __name__ == '__main__':
    server()



