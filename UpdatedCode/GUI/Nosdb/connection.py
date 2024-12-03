import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

def connect_ui(ui , ref ,ip):
    ui.ref = ref
    ui.ip = ip

def connect():
    
    cred = credentials.Certificate(os.path.join(os.path.dirname(__file__),"cred.json"))
    firebase_admin.initialize_app(cred,{'databaseURL':"--YOUR firebase APP LINK HERE--" })

    #firebase_admin.
    ref = db.reference("/")
    return ref

#returns the external ip , it will be 0.0.0.0 if the 
def ip():
    externalIP  = os.popen('curl -s ifconfig.me').readline()
    if externalIP == "":
        return "0.0.0.0" 
    else:
        return externalIP 


