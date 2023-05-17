import './jsencrypt.min.js';
import readline from 'readline';

const publicKey = process.argv[2];
const phrase = process.argv[3];

function getInput() {
       var encrypt = new JSEncrypt();
        encrypt.setPublicKey(publicKey);
        var encrypted = encrypt.encrypt(phrase);
        console.log(encrypted);
}

getInput();
