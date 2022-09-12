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

# method to return all device information
def get_device_info():
    # Get all the devices
    devices = get_devices()
    # Create a list to store the device information
    device_info = []
    # Loop through each device
    for device in devices:
        # Get the device information
        device_info.append({
            'id': str(device['_id']),
            'name': device['name'],
            'type': device['type'],
            'location': device['location'],
            'ip': device['ip'],
            'status': device['status']
        })
    # Return the device information
    return device_info


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


# get length of all items in the database
def get_length():
    return collection.count_documents({})

# function to get device information by name
def get_device_by_name(name):
    # Get the device
    device = collection.find_one({'name': name})
    # Return the device
    return device


# create large amounts of sample data
def create_sample_data():
    # Add x amount of devices to the database
    for i in range(254):
        add_device('192.168.1.' + str(i), 'Sample' + str(i), 'Router_' + str(i), 'Basement' + str(i), 'offline')
