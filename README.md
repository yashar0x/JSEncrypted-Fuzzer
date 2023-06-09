# JSEncrypted-Fuzzer
Nowadays some applications are using Mr. Travis Tidwell's [JSEncrypt library](https://travistidwell.com/jsencrypt/) to encrypt forms while posting,
And as you know you cannot manipulate these types of forms while Intercepting because the parameters are encrypted with a public key which was sent by the server to the client at the first step that he visits the form, and then only the encrypted parameters will be accepted by the server.

So if you want to inject your payload in these types of forms, you have to encrypt them before sending,
But when the form has also a client side protection that prevents you from injecting malicious payloads, you should inject your payload while intercepting the packet, which is impossible as described above, and also doing tests like brute forcing a form is almost impossible without an automated tool

So now is when you need a solution to make it possible

# What does JSEncrypted-Fuzzer do?
This is a Python app that GETs the login page, derives the public key from the source code of the page, encrypts your provided wordlists with the public key using a simple Node.js app which uses jsencrypt.min.js library, url-encodes the username and password, sends the encrypted data using a POST request and if the response code is what you specified at the first step, It will save the correct username and password in a .txt file in output directory

# Installation

        # pip install -r requirements.txt

# Guidance

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


           Author:  Yashar Mohagheghi
           Twitter: yashar0x
           Github:  yashar0x
           Website: yashar.pro
           
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
        

# Sample
For a better understanding of how JSEncrypted-Fuzzer works I intercepted the packets using Burp:

![Screenshot](./img/SC1.jpg)


GET Request for login page:

![Screenshot](./img/SC2.jpg)


The app will derive the public key from the hidden input:

![Screenshot](./img/SC3.jpg)


Sending the encrypted username and password:

![Screenshot](./img/SC4.jpg)


Successfully logged in with provided username and password:

![Screenshot](./img/SC5.jpg)


**Tested on Python 3.10.8**

**Note:** This app will test all the passwords for each username, The same as Cluster-Bomb Attack Type in Burp Intruder.

## Disclaimer
**This tool is made for educational purposes only and I am not responsible for any abusive**
