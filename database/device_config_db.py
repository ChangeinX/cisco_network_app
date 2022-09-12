# used to build database of device configuration using mongodb

import subprocess

from pymongo import MongoClient

# connect to the database
client = MongoClient('localhost', 27017)
db = client['device_config_db']

# get the collection
collection = db['device_configs']


# method to get unknown amount of arguments for data entry into database dictionary
def get_unknown_amount_of_arguments(name, *args):
    # get the arguments
    arguments = args
    # loop through each argument and insert all parent and child data as one entry in the database
    # for argument in arguments:
    print(f'Argument: {arguments}')
    collection.insert_one({
        name: arguments,
    })

# find device config by ip address
def find_device_config_by_ip(ip):
    device_config = collection.find_one({'ip': ip})
    return device_config

# find device config by name
def find_device_config_by_name(name):
    device_config = collection.find_one({'name': name})
    return device_config


