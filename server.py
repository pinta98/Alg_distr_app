import Pyro5.server
import Pyro5.core
from pymongo import MongoClient


import config
client = MongoClient("mongodb+srv://"+config.id_mongodb+":"+config.psw_mongodb+"@"+config.cluster_mongodb+".sah1v.mongodb.net/?retryWrites=true&w=majority")

mydb = client[config.client_mongodb]
user_collection = mydb["User"]

@Pyro5.server.expose
class Thing(object):
    def login(self, arg):
        user_ok = ""
        for user in user_collection.find():
            if(user["username"] == arg[0] and user["password"] == arg[1]):
                user_ok = "USER_OK"
                break
            else:
                user_ok = "NO_USER"
        
        return user_ok

    
    def register(self, arg):
        duplicato = False
        for user in user_collection.find():
            if(user["username"] == arg[0]):
                duplicato = True
                break
        if(duplicato):
            return "DUPLICATO"
        else:
            new_user = {
                "username": arg[0],
                "password": arg[1]
            }
            try:
                user_collection.insert_one(new_user)
                return "INSERITO"
            except Exception as e:
                #print("An exception occurred ::", e)
                return "PROBLEMI"

    def personal_data(self, arg):     
        data = user_collection.find_one({"username":arg})        
        return data
    
    def mod_personal_data(self, arg):     
        try:
            user_collection.update_one({"username":arg[0]}, 
                                       {"$set": {
                                            arg[1]: arg[2]
                                        }}) 
            return True
        except Exception as e:
            #print("An exception occurred ::", e)
            return False 

    def delete_msg(self, arg):
        try:           
            user_collection.update_one({"username": arg[0]}, {"$pull": {"messaggi":{"data": arg[1]}}})
            return True
        except Exception as e:
            print("An exception occurred ::", e)
            return False     
        
    def matching_user(self, arg):     
        data = user_collection.find({"username": {"$regex":arg}})        
        return data  

    def un_follow(self, arg):
        if(arg[2]):
            try:         
                user_collection.update_one( {"username": arg[0]}, {"$inc":{"seguiti":+1}, "$push": {"utenti_seguiti": arg[1]}})
                user_collection.update_one( {"username": arg[1]}, {"$inc":{"seguaci":+1}})

                data = user_collection.find_one({"username":arg[1]}) 
                
                return data
            except Exception as e:
                print("An exception occurred ::", e)
                return None
        else:
            try:           
                user_collection.update_one( {"username": arg[0]}, {"$inc":{"seguiti":-1}, '$pull': {'utenti_seguiti': arg[1]}})
                user_collection.update_one( {"username": arg[1]}, {"$inc":{"seguaci":-1}})
                return True
            except Exception as e:
                print("An exception occurred ::", e)
                return False
            
    def get_followed_msg(self, arg):
        msg = {}
        followed = user_collection.find_one({"username": arg}) 
        for user_followed in user_collection.find():
            if user_followed["username"] in followed["utenti_seguiti"] or user_followed["username"] == arg:
                if len(user_followed["messaggi"]) > 0:
                    msg[user_followed["username"]] = user_followed["messaggi"]
        
        return msg

    def publish_msg(self, arg):
        print(arg[0])
        print(arg[1])
        print(arg[2])

        user_collection.update_one({"username":arg[0]}, 
                                       {"$push": {"messaggi": {"testo": arg[1], "data": arg[2], "user": arg[0]}}
                                            
                                        }) 
        print("_________")

'''
# ------ normal code ------
daemon = Pyro5.server.Daemon()
ns = Pyro5.core.locate_ns()
uri = daemon.register(Thing)
ns.register("mythingy", uri)
print("Hi. Server is now active.")
daemon.requestLoop()
'''

import Pyro5.api
import Pyro5.socketutil
import socket


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)  # get ip address of current machine
daemon = Pyro5.server.Daemon(host=ip_address)  # make a Pyro daemon
ns = Pyro5.api.locate_ns()  # find the name server
uri = daemon.register(Thing)  # register the greeting maker as a Pyro object
ns.register("mythingy", uri)  # register the object with a name in the name server
print("Hi. Server is now active.")
daemon.requestLoop()  # start the event loop of the server to wait for calls