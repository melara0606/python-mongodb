import sys
import copy
import pymongo

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
  try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydb"]

    #users = db.users.find_one({ "username" : "jonedoe" })
    #users = db.users.find({ "username" : "jonedoe" }, { "email" : 1 })

    #if not users:
    #  print("Lo sentimos pero no hay datos para el usuario selecionado")
    #else:
    #  for user in users:
    #    print(user.get("fistname"))

    # Cantidad de registros
    #count = db.users.count_documents({})
    #print("La cantidad de registros actuales son : %s" % count)

    # Ordernamiento
    #db.users.find({ "fistname" : "jonedoe" }).sort("dateofbirth", direction=pymongo.DESCENDING)
    #db.users.find({ "fistname" : "jonedoe" }, sort=[("dateofbirth", pymongo.DESCENDING)])

    #limit
    #db.users.find().sort("dateofbirth", direction=pymongo.DESCENDING).limit(10)

    #limit y comenzado en un punto especifico
    #db.users.find().sort("dateofbirth", direction=pymongo.DESCENDING).limit(10).skip(20)

    # Actualizado un campo (metodo uno)
    #new_user_data = copy.deepcopy(user_old)
    #new_user_data['email'] = "janedoe74@example2.com"    
    #db.users.replace_one({ "username" : "jonedoe" }, new_user_data, True)
    
    #Actualizado un campo (metodo dos)
    #db.users.update_one({ "username" : "jonedoe" }, {"$set" : { "email" :  "janedoe74@example3.com", "score" : 1 }})
  except ConnectionFailure as e:
    sys.stdout.write("Error: %s" % e)
    sys.exit(1)

if __name__ == "__main__":
  main()