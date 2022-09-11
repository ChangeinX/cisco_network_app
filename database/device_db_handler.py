# This python file is used to handle the database of the devices using mongodb

import pymongo
import subprocess
from pymongo import MongoClient
from bson.objectid import ObjectId

# connect to the database
client = MongoClient('localhost', 27017)
db = client['device_db']

# get the collection
collection = db['devices']


# get all the devices
def get_devices():
    devices = collection.find()
    return devices


# get a device by ip address
def get_device(ip):
    device = collection.find_one({'ip': ip})
    return device


# add a device to the database
def add_device(ip, name, type, location, status):
    collection.insert_one({'name': name, 'type': type, 'location': location, 'ip': ip, 'status': status})


# update a device in the database
def update_device(ip, name, type, location):
    collection.update_one(
        {'ip': ip}, {
            '$set': {'name': name, 'type': type, 'location': location, 'status': get_device_status_by_ping(ip)}
        }
    )


# get device status by ping ip address
def get_device_status_by_ping(ip):
    # Ping the ip address
    ping = subprocess.call(['ping', '-n', '1', ip], stdout=subprocess.DEVNULL)
    # If the ping is successful
    if ping == 0:
        # Return online
        return 'online'
    # If the ping is unsuccessful
    else:
        # Return offline
        return 'offline'


# set status of device in database
def set_device_status(ip):
    # Get the device status by ping
    status = get_device_status_by_ping(ip)
    # Update the device status
    collection.update_one({'ip': ip}, {'$set': {'status': status}})
    # Return the status
    return status


# make a device to initialize the database
def make_device():
    add_device('192.168.1.1', 'Home_Router', 'SuddenlinkCrap', 'office', f'{get_device_status_by_ping("192.168.1.1")}')
