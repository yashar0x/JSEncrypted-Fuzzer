# JSEncrypted-Fuzzer
Nowdays most of the applications are using Mr. Travis Tidwell's JSEncrypt library (https://travistidwell.com/jsencrypt/) to encrypt forms while posting,
And as you know you cannot manipulate these types of forms while Intercepting because the parameters are encrypted with a public key which was sent by the server to the client at the first step that he visits the form, and then only the encrypted parameters will be accepted by the server.

So if you want to inject your payload in these types of forms, you have to encrypt them before sending,
But when the form has also a client side protection that prevents you from injecting malicious payloads, you should inject your payload while intercepting the packet, which is impossible as described above, and also doing tests like brute forcing a form is almost impossible without an automated tool

So now is when you need a solution to make it possible

# What does JSEncrypted-Fuzzer do?
This is a Python app that will GETs the login page, derives the public key from the source code of the page, encrypts your provided wordlists with the public key using a simple Node.js app which uses jsencrypt.min.js library, url-encodes the username and password, sends the encrypted data using a POST request and if the response code is what you specified at the first step, It will save the correct username and password in a .txt file in output directory

# Installation

        pip install requirements.txt
