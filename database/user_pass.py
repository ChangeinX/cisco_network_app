# this file is used to build the database for the user and password using mongodb

import pymongo
from pymongo import MongoClient
import bcrypt

# connect to the database
client = MongoClient('localhost', 27017)
db = client['user_pass']
users = db['users']


# create a new user
def create_user(username, password):
    # hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # insert the new user into the database
    users.insert_one({
        'username': username,
        'password': hashed_password,
        'admin': False
    })

# check if the user exists
def check_user(username):
    if users.find_one({'username': username}):
        print(f'{username} exists')
        return True
    else:
        print(f'{username} does not exist')
        return False

# check if the password is correct
def check_password(username, password):
    hashed_password = users.find_one({'username': username})['password']
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print(f'{username} password is correct')
        return True
    else:
        print(f'{username} password is incorrect')
        return False

# check if the user is an admin
def check_admin(username):
    if users.find_one({'username': username})['admin']:
        print(f'{username} is an admin')
        return True
    else:
        print(f'{username} is not an admin')
        return False

# create a new admin user
def create_admin(username, password):
    # hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # insert the new user into the database
    users.insert_one({
        'username': username,
        'password': hashed_password,
        'admin': True
    })


# create a new admin user for initial setup
# create_admin('admin', 'admin')
