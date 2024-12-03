import datetime
from Crypt.secret import *
def send( contents, reciver, sub , login_info , ref):
    
    timestamp = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    u_ref = ref.child("Users")
    s_ref = ref.child("Sent").child(login_info["name"])
    r_ref = ref.child("Recived").child(reciver)
    
    secret = generate_secret(get_pub_key(reciver,ref),login_info["name"])
    enc_content = encrypt(secret,contents)
    sender_dir = {
        "sender" : login_info["name"],
        "subject" : sub,
        "contents" : enc_content,
        "TimeStamp" : timestamp ,
        "read" : 0
    }

    reciver_dir = {
        "reciver" : reciver,
        "subject" : sub,
        "contents" : enc_content,
        "TimeStamp" : timestamp

    }
    

    r_ref.child(timestamp).set(sender_dir)
    s_ref.child(timestamp).set(reciver_dir)

    return timestamp,s_ref,r_ref


def read_unread():
    pass





    # print("TO:" , reciver) 
    
    # print("subject : ", sub)

    # print("contents :" , contents) 
    
    # print("From" , login_info)

    