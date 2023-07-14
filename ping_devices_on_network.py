import socket
import sys
import os
import time

while True:
    devices = []

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Server IP ex: 10.0.0.')
    server_ip = input('Enter server IP: ')
    #for i in range(1, 256):
    for i in range(1, 30):
        device_ip = server_ip + str(i)
        rep = os.system('ping -t 2 ' + device_ip)
        if rep == 0:
            print(device_ip + ': device is online!')
            print(' ')
            devices.append(device_ip)
            os.system('nslookup ' + device_ip)
            print('--------------------------------------------------------------')
            #print(' ')

        else:
            print(device_ip + ': device is not online!')
            print('--------------------------------------------------------------')
            print(' ')

    print("Number devices online: " + str(devices))
    break

    