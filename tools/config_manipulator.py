# Get text file from database folder
#
import json
from database import device_db_handler
from database import device_config_db
import os
import time
import datetime

import netmiko
from netmiko import ConnectHandler


def get_file():
    most_recent_path = ''
    return most_recent_path


# filter the text file each line that doesn't begins with a space or a ! is the parent
# each line that begins with a space is a child of the parent each line that begins with more than one space
# is a child of the child
def get_parent_child_dict():
    # Get the text file
    text_file = get_file()
    # Create a dictionary to store the parent and child
    parent_child_dict = {}
    # Create a list to store the parent and child
    parent_child_list = []
    # Open the text file
    with open(text_file) as f:
        # For each line in the text file
        for line in f:
            # If the line doesn't begin with a space or a !
            if not line.startswith(' ') and not line.startswith('!'):
                # Append the line to the parent and child list
                parent_child_list.append(line)
            # If the line begins with a space
            elif line.startswith(' '):
                # Append the line to the parent and child list
                parent_child_list.append(line)
    # For each item in the parent and child list
    for item in parent_child_list:
        # If the item doesn't begin with a space
        if not item.startswith(' '):
            # Set the parent to the item
            parent = item
        # If the item begins with a space
        elif item.startswith(' '):
            # Set the child to the item
            child = item
            # If the parent is already in the parent and child dictionary
            if parent in parent_child_dict:
                # Append the child to the parent
                parent_child_dict[parent].append(child)
            # If the parent isn't already in the parent and child dictionary
            else:
                # Set the parent and child to the parent and child dictionary
                parent_child_dict[parent] = [child]
            print(f'Parent: {parent} Child: {child}')
    # Return the parent and child dictionary
    return parent_child_dict


# method to send data to json file
def send_to_json():
    # Get the parent and child dictionary
    parent_child_dict = get_parent_child_dict()
    # Create a list to store the parent and child lines
    parent_child_list = []
    # For each key and value in the dictionary
    for key, value in parent_child_dict.items():
        # Append the key and value to the parent and child list
        parent_child_list.append(key)
        parent_child_list.append(value)
    # Return the parent and child list
    return parent_child_list


# save as json file
def save_as_json():
    # Get the parent and child list
    parent_child_list = send_to_json()
    # Create a json file
    with open('parent_child.json', 'w') as f:
        # Write the parent and child list to the json file and set indent to 4
        json.dump(parent_child_list, f, indent=4)


# download all device configs from by accessing ip address from database: if user wants to download all configs
def download_all_device_configs():
    # Get all the devices
    devices = device_db_handler.get_device_info()
    # Loop through each device
    for device in devices:
        # Get the device ip address
        ip = device['ip']
        # Get the device status
        status = device['status']
        # If the device status is up
        if status == 'online':
            # Create a dictionary to store the device information
            device_info = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': 'admin',
                'password': 'admin'
            }
            # Connect to the device
            net_connect = ConnectHandler(**device_info)
            # Get the device config
            config = net_connect.send_command('show run')
            # Create a text file
            with open(f'{ip}.txt', 'w') as f:
                # Write the config to the text file
                f.write(config)
            # Disconnect from the device
            net_connect.disconnect()
            print(f'Config downloaded for {ip}')
        # If the device status is down
        elif status == 'offline':
            # Print the device is offline
            print(f'{ip} is offline')


# create a database for the config files: Initial setup
def get_parent_child_dict_to_database():
    devices = device_db_handler.get_device_info()
    # Loop through each device
    for device in devices:
        # Get the device ip address
        ip = device['ip']
        # Get the device status
        status = device['status']
        name = device['name']
        # If the device status is up
        if status == 'online':
            # Create a dictionary to store the device information
            device_info = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': '',
                'password': ''
            }
            # continue if netmiko cannot connect to device
            try:
                # Connect to the device
                net_connect = ConnectHandler(**device_info)
                # Get the device config
                config = net_connect.send_command('show run')
                # parse the config
                config = config.splitlines()
                # Create a list to store the parent and child
                parent_child_list = []
                # For each line in the config
                for line in config:
                    # If the line doesn't begin with a space or a !
                    if not line.startswith(' ') and not line.startswith('!'):
                        # Append the line to the parent and child list
                        parent_child_list.append(line)
                    # If the line begins with a space
                    elif line.startswith(' '):
                        # Append the line to the parent and child list
                        parent_child_list.append(line)
                # Create a dictionary to store the parent and child
                parent_child_dict = {}
                # For each item in the parent and child list
                for item in parent_child_list:
                    # remember to save the parent if the parent has no child
                    # If the item doesn't begin with a space
                    if not item.startswith(' '):
                        # Set the parent to the item
                        parent = item
                    # If the item begins with a space
                    elif item.startswith(' '):
                        # Set the child to the item
                        child = item
                        # If the parent is already in the parent and child dictionary
                        if parent in parent_child_dict:
                            # Append the child to the parent
                            parent_child_dict[parent].append(child)
                        # If the parent isn't already in the parent and child dictionary
                        else:
                            # Set the parent and child to the parent and child dictionary
                            parent_child_dict[parent] = [child]
                        print(f'Parent: {parent} Child: {child}')
                # find parents with no children and add them to the dictionary
                for item in parent_child_list:
                    if not item.startswith(' '):
                        parent = item
                        if parent not in parent_child_dict:
                            parent_child_dict[parent] = []
            except:
                # continue if netmiko cannot connect to device
                # get device name and ip address that cannot be connected to and output to text file
                with open('offline_devices.txt', 'a') as f:
                    f.write(f'{name} {ip}\n')
                continue
            # Disconnect from the device
            net_connect.disconnect()
            # send the parent and child dictionary to the database
            device_config_db.get_unknown_amount_of_arguments(name, parent_child_dict)
