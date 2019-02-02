import sys

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def main():
  """user_doc = {
    'username' : 'foouser',
    'twitter': {
      'username'  : 'footwitter',
      'password'  : 'secret',
      'email'     : 'twitter@example.com'
    },
    'facebook': {
      'username'  : 'foofacebokk',
      'password'  : 'secret',
      'email'     : 'facebook@example.com'
    },
    'irc': {
      'username'  : 'footirc',
      'password'  : 'secret'
    }
  }
  """
  user_doc = {
    "username" : "foouser",
    "emails"   : [
      { "email": "foouser1@example.com", "primary": True },
      { "email": "foouser2@example.com", "primary": False },
      { "email": "foouser3@example.com", "primary": False },
    ]
  }
  try:
    client = MongoClient("mongodb://localhost:27017")
    db = client['mydb']
    # db.users.insert_one(user_doc, True)
    #db.users.delete_many({  "username" : "foouser" })
    #db.users.delete_one({  "username" : "jonedoe" })
    #db.users.update_one({ "facebook.username" : "foofacebokk" }, { "$set" : { "facebook.username": "bar" }})
    """ users = db.users.find()
    for user in users:
      print(user) """
    
    # Borramos de el paquete de correos aquel que tiene el correo 'foouser2@example.com"'
    #db.users.update_one({"username":"foouser"}, {"$pull":{"emails":{"email":"foouser2@example.com"}}})
    # db.users.update_one({"username":"foouser"}, {"$pull": { "emails": { "primary" : { "$ne" : True }}}})
    # db.users.update_one({"username":"foouser"}, { "$push": { "emails": { "email": "foouser4@example.com", "primary": False }}})
    
    print(db.users.find_one({ "username" : "foouser" }))
  except ConnectionFailure as e:
    sys.stdout.write("%s" % e)
    sys.exit(1)

if __name__ == "__main__":
    main()