import socket
import pickle

from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g

def server():
    
    host = socket.gethostname()
    port = 5000
    print("->" + host)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))
    
    alicePub = conn.recv(1024)
    alicePub = pickle.loads(alicePub)
    
    bobPub =  pickle.dumps(bobPubKey)
     
    conn.send(bobPub)
    
    deckey = alicePub * bobPrivKey
    
    deckey = compress(deckey)
    deckey = int(deckey,16)
    deckey = bin(deckey)[:256]
    deckey = int(deckey, 2).to_bytes((len(deckey) + 7) // 8, byteorder='big')
    print(deckey)
    conn.close()

if __name__ == '__main__':
    server()



