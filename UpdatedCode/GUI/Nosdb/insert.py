import Nosdb.connection as conn
import datetime
import hashlib
from Crypt.secret import *

def hasher(password):
    hash_psd = hashlib.sha512(password.encode("utf-8")).hexdigest()
    return hash_psd
        


class users:


    def __init__(self,ref,username,email,password,ip,public_key):
        self.ref = ref
        p_hash = hasher(password)

        self.ts = str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        self.user_dict = {
            "name" : username.strip().lower(),
            "email" : email,
            "ip" : ip,
            "password_hash" : p_hash,
            "gen_pubkey" : public_key,
            "created" : self.ts
        }
  

    def db_add_new_user(self,private_key):
        
        u_ref = self.ref.child("User")
        r_ref = self.ref.child("Recived")
        s_ref = self.ref.child("Sent")

        exists = u_ref.child(self.user_dict["name"]).get()
        
        if not exists : 
            public = generate(self.user_dict["name"])
            self.user_dict["gen_pubkey"] = public

            

            u_ref.child(self.user_dict["name"]).set(self.user_dict)
            r_ref.child(self.user_dict["name"]).set({self.ts:"begening"})
            s_ref.child(self.user_dict["name"]).set({self.ts:"begening"})
            return True
        
        else:
            print("User_name exists \n please change the user_name \n or do you have an account??")            
            return False
    
    def db_is_user(self):
        
        u_ref = self.ref.child("User")

        exists = u_ref.child(self.user_dict["name"]).get()
        
        if exists :
            return True
        else:          
            return False

class current_users(users):

    checkdict = {} 

    def __init__(self,ref,username,password,ip,):
        self.ref = ref
        p_hash = hasher(password)

        self.user_dict = {
            "name" : username.strip().lower(),
            "ip" : ip,
            "password_hash" : p_hash,
        }
    
    def check(self,ui):
        self.checkdict=self.ref.child("User").child( self.user_dict["name"]).get()
        if self.user_dict["password_hash"] == self.checkdict["password_hash"] :
            ui.validated=1
            return True
        else :
            ui.validated=0
            self.checkdict = {}
            return False
    def get_cred(self):
        return self.checkdict

    