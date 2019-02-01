import sys
from datetime import datetime
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

def main():
  try:
    c = MongoClient("localhost", 27017)
    dbh = c["mydb"]
    
    # Informacion del nuevo usuario
    user_doc = {
      "username"    : "jonedoe",
      "fistname"    : "Jane",
      "surname"     : "Doe",
      "dateofbirth" : datetime(1974,4,12),
      "email"       : "janedoe74@example.com",
      "score"       : 0
    }

    dbh.users.insert_one(user_doc)
    print("Successfully inserted document: %s" % user_doc)
  except ConnectionFailure as e:
    sys.stderr.write("Could not connect to mongodb %s" % e)         

if __name__ == "__main__":
  main()