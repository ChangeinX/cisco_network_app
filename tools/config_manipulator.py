# Get text file from database folder
#
import json
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


# download a config from a device using netmiko
def download_config(ip, username, password):
    # Create a dictionary to store the device information
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
        'port': 22,
        'verbose': True
    }

    # Connect to the device
    net_connect = ConnectHandler(**device)
    # Enter enable mode
    net_connect.enable()
    # Send the command to download the config
    output = net_connect.send_command('show run')
    # Write the output to a text file
    with open('config_parsing.txt', 'w') as f:
        f.write(output)
    # Disconnect from the device
    net_connect.disconnect()







