import socket
import pickle

from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g


def client():
    host = socket.gethostname()
    port = 5000
    
    alicePub = pickle.dumps(alicePubKey)
  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    client_socket.send(alicePub)
    
    bobPub = client_socket.recv(1024)
    bobPub = pickle.loads(bobPub)
    
    enckey = bobPub * alicePrivKey
    enckey = compress(enckey)
    enckey = int(enckey,16)
    enckey = bin(enckey)[:256]
    enckey = int(enckey, 2).to_bytes((len(enckey) + 7) // 8, byteorder='big')
    print(enckey)
    client_socket.close()

if __name__ == '__main__':
    client()