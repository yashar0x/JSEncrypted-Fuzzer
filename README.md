## What does JSEncrypted-Fuzzer do?
This is a Python app that GETs the login page, derives the public key from the source code of the page, encrypts your provided wordlists with the public key using a simple Node.js app which uses jsencrypt.min.js library, url-encodes the output, sends the encrypted data using a POST request and if the response code is what you specified at the first step, It will save the correct username and password in a .txt file in output directory.

## Installation

        # git clone https://github.com/yashar0x/JSEncrypted-Fuzzer
        # cd JSEncrypted-Fuzzer
        # pip install -r requirements.txt

## Guidance

        # python fuzzer.py -h
        
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


           Author:  Yashar
           Twitter: yashar0x
           Github:  yashar0x
           
        usage: fuzzer.py [-h] [-u USERNAMES] [-p PASSWORDS] [-uLabel USERNAMELABEL] [-pLabel PASSWORDLABEL] [-r RESPONSECODE] url

        positional arguments:
          url                   Exact URL of the login page

        options:
          -h, --help            show this help message and exit
          -u USERNAMES, --usernames USERNAMES
                                Username Wordlist File
          -p PASSWORDS, --passwords PASSWORDS
                                Password Wordlist File
          -uLabel USERNAMELABEL, --usernamelabel USERNAMELABEL
                                The label of Username field, Default is: username
          -pLabel PASSWORDLABEL, --passwordlabel PASSWORDLABEL
                                The lable of Password field, Default is: password
          -r RESPONSECODE, --responsecode RESPONSECODE
                                Successful response code, Default is 200
        

**If you want to see JSEncrypted-Fuzzer in action: [How to bypass asymmetric client-side encryption](https://infosecwriteups.com/how-to-brute-force-encrypted-login-forms-9f6c952cb97d)**

**Note:** This app will test all the passwords for each username, The same as Cluster-Bomb Attack Type in Burp Intruder.

**Tested on Python 3.10.8**

## Disclaimer
**This tool is made for educational purposes only and I am not responsible for any abusive**
