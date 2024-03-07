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
        for user in user_collection.find():
            if(user["username"] == arg[0] and user["password"] == arg[1]):
                return "USER_OK"
            else:
                return "NO_USER"
    
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
            data = user_collection.update_one({"username":arg[0]}, 
                                        {"$set": {
                                            arg[1]: arg[2]
                                        }}) 
            return True
        except Exception as e:
            #print("An exception occurred ::", e)
            return False    

# ------ normal code ------
daemon = Pyro5.server.Daemon()
ns = Pyro5.core.locate_ns()
uri = daemon.register(Thing)
ns.register("mythingy", uri)
print("Hi. Server is now active.")
daemon.requestLoop()