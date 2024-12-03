from tinyec import registry 
import secrets
import pickle
from Crypto import Random
from Crypto.Cipher import AES
import os

curve = registry.get_curve('brainpoolP256r1')

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]



def generate(uname):#insert.py line 39 40
    #save(private,uname)
    private_key = secrets.randbelow(curve.field.n)
  
    public_key = private_key * curve.g
    private_key = pickle.dumps(private_key)
    save(private_key,uname)
    #return public
    return str(pickle.dumps(public_key))
    #print(type(q))
    
    pass


def save(private,uname):
    #dump the private key in a file
    
    with open(os.path.join(os.path.join(os.path.dirname(__file__)),uname + ".key"),"wb") as priv:
        priv.write(private)
    
    pass

def generate_secret(public,uname):
    #get the private key from file with get key 
    # private = getkey(uname)
    private_key = get_key(uname)
    private_key = pickle.loads(private_key)
    print(public)
    public_key = public[2:-1].encode("utf-8").decode('unicode_escape').encode("raw_unicode_escape")
    print(public_key)
    public_key = pickle.loads(public_key)
    print(type(public_key))
    secret = private_key * public_key
    secret = compress(secret)
    secret = int(secret,16)
    secret = bin(secret)[:256]
    secret = int(secret, 2).to_bytes((len(secret) + 7) // 8, byteorder='big')
    return secret
    secret = public
    pass


def get_key(uname):
    #openfile and return private key
    with open(os.path.join(os.path.join(os.path.dirname(__file__)),uname + ".key"),"rb") as f:
        k = f.read()
        return k
        f.close()
    pass

def encrypt(secret,message): #send.py line 10 11
    #return chypher
    message = message.encode('utf-8')
    print(message)
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    return str(iv + cipher.encrypt(message))

    pass

def decrypt(secret,ciphertext): 
    #return message 
    ciphertext = ciphertext[2:-1].encode("utf-8").decode('unicode_escape').encode("raw_unicode_escape")
    print(ciphertext)
    print(type(ciphertext))
    #.decode('unicode_escape').encode("raw_unicode_escape")
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
     
    return str(plaintext.rstrip(b"\0"))[2:-1]+"\n"
    pass

def get_pub_key(uname,ref):
    key = ref.child("User").child(uname).child("gen_pubkey").get()
    return key
