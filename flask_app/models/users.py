#==========================================================
#MODEL FILE
#==========================================================

# import the function that will return an instance of a connection
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
  db = 'users_schema' #variable connected to schema
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']



  # Now we use class methods to query our database
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
    results = connectToMySQL(cls.db).query_db(query)
    # Create an empty list to append our instances of friends
    users_instances = []
    # Iterate over the db results and create instances of friends with cls.
    for user in results:
      users_instances.append( cls(user) )
    return users_instances

  @classmethod
  def get_one_user(cls, data):
    query = "SELECT * FROM users WHERE id = %(user_id)s;"
    results = connectToMySQL(cls.db).query_db(query, data)
    return cls(results[0])

  @classmethod
  def create_new_user(cls, data):
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() )"
    results = connectToMySQL(cls.db).query_db(query, data)
    return results

  @classmethod
  def update(cls,data):
    query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(user_id)s;"
    result = connectToMySQL(cls.db).query_db(query, data)
    return result

  @classmethod
  def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(user_id)s;"
        return connectToMySQL('users_schema').query_db(query,data)