
import sys
import socket
import time
import argparse
import httplib
import colored
import os

REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def printLogo():
    print "\033[93m\n\n\n\t\t\t /$$   /$$           /$$                          /$$       /$$$$$$$$/$$                 /$$                    ";
    time.sleep(0.5)
    print "\t\t\t | $$  | $$          | $$                         | $$      | $$_____/__/                | $$                    ";
    time.sleep(0.5)
    print "\t\t\t | $$  | $$  /$$$$$$ | $$  /$$$$$$  /$$$$$$   /$$$$$$$      | $$      /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ ";
    time.sleep(0.5)
    print "\t\t\t | $$  | $$ /$$__  $$| $$ /$$__  $$|____  $$ /$$__  $$      | $$$$$  | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$";
    time.sleep(0.5)
    print "\t\t\t | $$  | $$| $$  \ $$| $$| $$  \ $$ /$$$$$$$| $$  | $$      | $$__/  | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/";
    time.sleep(0.5)
    print "\t\t\t | $$  | $$| $$  | $$| $$| $$  | $$/$$__  $$| $$  | $$      | $$     | $$| $$  | $$| $$  | $$| $$_____/| $$      ";
    time.sleep(0.5)
    print "\t\t\t |  $$$$$$/| $$$$$$$/| $$|  $$$$$$/  $$$$$$$|  $$$$$$$      | $$     | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      ";
    time.sleep(0.5)
    print "\t\t\t  \______/ | $$____/ |__/ \______/ \_______/ \_______/      |__/     |__/|__/  |__/ \_______/ \_______/|__/      ";
    time.sleep(0.5)
    print "\t\t\t           | $$                                                                                                  ";
    time.sleep(0.5)
    print "\t\t\t           | $$                                                                                                  ";
    time.sleep(0.5)
    print "\t\t\t           |__/                                                                                                  ";
    time.sleep(1)
    print "\033[35m\n\t\t\t\t\t\t\t ____  ___ _   _ ____ __  __ __  __   __   ____  ";
    print "\t\t\t\t\t\t\t(  _ \/ __| )_( | ___|  \/  |  \/  ) /__\ (  _ \ ";
    print "\t\t\t\t\t\t\t )   ( (__ ) _ ( )__) )    ( )    ( /(__)\ )(_) )";
    print "\t\t\t\t\t\t\t(_)\_)\___|_) (_|____|_/\/\_|_/\/\_|__)(__|____/ ";
#COLOR DEFINE
CRED = '\033[91m'
CEND = '\033[0m'

GRED = '\033[92m'
GEND = '\033[0m'

YRED = '\033[93m'
YEND = '\033[0m'

CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'

parser=argparse.ArgumentParser()
parser.add_argument('-u','--url',help='Base url  needed',required=True)
parser.add_argument('-l','--list',help='Wordlist  needed',required=True)
parser.add_argument('-t','--timeout',help='Waiting time between each query. Default is 3 seconds',required=False)
parser.add_argument('-w','--write',help='Filename to write the found links',required=False)
parser.add_argument('-e','--extra',help='extra path from base url eg: www.example.com/portal. portal is extra',required=False)

arguments=parser.parse_args()
baseURL = arguments.url
wordfile = open(arguments.list, "r")

timeout=arguments.timeout or 3
extra=arguments.extra or ""
outputfile=arguments.write or False

if extra:
        extra="/"+extra
os.system('clear')
printLogo()
print CBLUE+"\n\n\nStarting Upload Finder"+CEND+"\n \33[36m Developed by Reethu Chemmad\033[0m [ My Leash is longer ]"
k=is_connected(REMOTE_SERVER)
print "\n\nChecking internet connectivity..." + str(k)

if k:
    print "\nSTARTING...\n\n"
    print "URL: "+baseURL+"\nWordlist file: "+arguments.list+"\nWaiting: "+str(timeout)+"\n\n"


    for word in wordfile:

        word = word.strip()
        checkword = extra+ "/" + word

        try:
            conn = httplib.HTTPConnection(baseURL)
            conn.request("HEAD", checkword)
            r1 = conn.getresponse()
            if r1.status == 200:
                print(GRED+ baseURL + checkword + " " + str(r1.status) + " " + r1.reason + GEND)
                if outputfile:
                    output = open(outputfile, "w+")
                    output.write(baseURL + checkword+"\n")
                    output.close()

            if r1.status == 301:
                print(YRED+ baseURL + checkword + " " + str(r1.status) + " " + r1.reason + YEND)
            if r1.status == 404:
                print(CRED+ baseURL + checkword + " " + str(r1.status) + " " + r1.reason + CEND)


        except Exception as e:
                print "Error:"+str(e)
                conn.close()

        time.sleep(int(timeout))
else:
    print "No internet connection\n exiting."