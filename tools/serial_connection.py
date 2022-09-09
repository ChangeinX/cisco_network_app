# send command to serial port

import serial
import time

# open serial port
ser = serial.Serial('COM3', 115200, timeout=1)

# send command
ser.write(b'enable \r')

