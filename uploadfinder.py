
import sys
import socket
import time
import argparse
import httplib

REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

parser=argparse.ArgumentParser()
parser.add_argument('-u','--url',help='Base url  needed',required=True)
parser.add_argument('-l','--list',help='Wordlist  needed',required=True)
parser.add_argument('-t','--timeout',help='Time out should be number',required=False)
parser.add_argument('-w','--write',help='Filename to write the found links',required=False)

arguments=parser.parse_args()
baseURL = arguments.url
wordfile = open(arguments.list, "r")
timeout=arguments.timeout or 3
print timeout
if is_connected(REMOTE_SERVER):


    for word in wordfile:
        word = word.strip()
        checkword = "/" + word

        try:
            conn = httplib.HTTPConnection(baseURL)
            conn.request("HEAD", checkword)
            r1 = conn.getresponse()

            if r1.status == 404:
                print("\033[1;33;40m")
            elif r1.status == 200:
                print("\033[1;32;40m")
            else:
                print("\033[1;37;40m")

                print baseURL + checkword + " " + str(r1.status) + " " + r1.reason
        except Exception as e:
                print "Error:"+str(e)
                conn.close()
        finally:
            conn.close()
        time.sleep(int(timeout))
else:
    print "No internet connection"