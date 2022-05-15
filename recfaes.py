from Crypto.Cipher import AES
import os
import os.path



def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(file_name):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext,keydec.key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
    os.remove(file_name)
    
def keydec(temp,body,fi):
    keydec.key = temp
    print("Message Body\n")
    for i in body:
        print(str(decrypt(i,keydec.key))[2:-1]+"\n")
    print("\n")
    
    for i in fi:
        decrypt_file(i+".enc")

def permission():
    print("Do want to decrypt the files,press 1 for yes,0 for no")
    k =  int(input())
    return k