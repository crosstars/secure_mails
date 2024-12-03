In this project a prototype of an email service has
been built in which the user's password will be stored in form of an md5 hash in the
server(Firebase realtime database (NoSQL) used as a server), user's public key will be stored
in a byte format in the database and the private key of the user will be stored in the user’s
machine in byte format. Elliptic Curve Diffie Hellman Key Exchange is used to generate
public, and private key pairs and ensure secure key exchange so that the final 256-bit
symmetric key for encryption/decryption is only available to the sender and the receiver, the
message will be encrypted with widely used symmetric encryption algorithm AES(In this
project we have used AES-256). For GUI implementation we used PyQt. It is a Python
interface for Qt, one of the most powerful, and popular cross-platform GUI libraries. PyQt5 is
a blend of the Python programming language and the Qt library.
