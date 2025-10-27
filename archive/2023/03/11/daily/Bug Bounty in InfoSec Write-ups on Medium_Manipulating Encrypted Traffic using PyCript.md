---
title: Manipulating Encrypted Traffic using PyCript
url: https://infosecwriteups.com/manipulating-encrypted-traffic-using-pycript-b637612528bb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:38.091405
---

# Manipulating Encrypted Traffic using PyCript

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb637612528bb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmanipulating-encrypted-traffic-using-pycript-b637612528bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmanipulating-encrypted-traffic-using-pycript-b637612528bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b637612528bb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b637612528bb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Manipulating Encrypted Traffic for Manual and Automation

[![Sourav Kalal](https://miro.medium.com/v2/resize:fill:64:64/1*3dHIoCEZxeENLBxleec9sw.png)](https://blog.souravkalal.tech/?source=post_page---byline--b637612528bb---------------------------------------)

[Sourav Kalal](https://blog.souravkalal.tech/?source=post_page---byline--b637612528bb---------------------------------------)

7 min read

·

Mar 6, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

### **Introduction**

I have been doing the pentest of mobile and web applications and recently I found that many applications are implementing client-side encryption in both mobile and web applications. Earlier I hosted a simple Javascript-based AES encryption and decryption script on GitHub. The script allows me to encrypt and decrypt the parameter to continue testing. The script was created after I found that many applications use the CryptoJS library with AES CBC 256 or 128-bit encryption.

The same method could be applied by writing the same encryption logic as your application. As or alternative method we can use the browser console and breakpoint in web applications and JavaScript-based mobile applications.

### **Problem**

The problem with the above method is you need to perform the encryption and decryption for each parameter or request again and again. This approach slows down the testing process and the time taken to complete the pentesting. Another problem is many time application is vulnerable and requires any type of automation to exploit it like OTP brute-force. If encryption is there it's not possible to perform any kind of automation.

A few months back I was pentesting a web application vulnerable to OTP brute force and due to encryption, I was not able to perform the brute force. I came up with the solution of writing a simple python script that will go through the text file with 4-digit OTP and will create a new text file with an encrypted version of the OTP. I could use the encrypted OTP to bypass the OTP. I create several burp extensions to perform the encryption especially to run automation like an intruder or SQLMAP.

The major problem was modifying the burp suite extension based on the parameter and encryption logic used by the application. Also, the one problem with manually decrypting and encrypting parameters is it takes a lot of time.

### **Solution**

I came up with the idea of creating a new burp suite extension that works on all the applications and allows you to just provide the encryption and decryption logic and the extension will take care of everything whether is manual pentesting or automation.

I created an extension named PyCript that solves all the problems. The extension decrypts the encrypted parameters on the fly and allows you to modify the value in the plain text directly inside the burp suite. This solves the problem of manually encrypting and decrypting each parameter and request again and again and we can test the application as there is no encryption.

I also added functionality that allows running automation on plain text requests and the extension will take care of encryption. This solves the challenge of running the tools like SQLMAP, Intruder or Burp Scanner.

### Analysis

I have one of the applications I am working on and by intercepting the traffic I can confirm that the request is using some kind of client-side encryption.

Press enter or click to view image in full size

![]()

Encrypted Request

The post body seems to have some kind of encryption and won’t allow us to perform any attacks on parameters. At this stage, I try to find out the encryption logic including key and iv from the Javascript code.

Using the browser dev tool and searching for some strings like `aes,encrypt,cryptojs,secretkey,iv,padding` I can see the encryption logic.

Press enter or click to view image in full size

![]()

Encryption

The search result shows that it uses AES encryption using the CryptoJS library. The result shows that it has two different encryption codes. By clicking on both files I can verify that the encryption logic is the same for both.

Press enter or click to view image in full size

![]()

Encryption JS Code

Press enter or click to view image in full size

![]()

Encryption Code

As mentioned I have hosted the Cryptojs-based encryption decryption script on GitHub. Using the provided key and IV from the above code I can decrypt the request parameters.

Press enter or click to view image in full size

![]()

Decrypt

### PyCript and Decryption

Now I am able to confirm that I can decrypt the encrypted strings. Now I can use the same encryption logic to write the encryption and decryption script in PyCript format.

```
//Decryption
var CryptoJS = require("crypto-js");
const program = require("commander");
const {
    Buffer
} = require('buffer');
program.option("-d, --data <data>", "Data to process").parse(process.argv);
const options = program.opts();
const requestbody = Buffer.from(options.data, 'base64').toString('utf8');
var key = CryptoJS.enc.Utf8.parse('8080808080808080');
var iv = CryptoJS.enc.Utf8.parse('8080808080808080');
var plainText = CryptoJS.AES.decrypt(requestbody, key, {
    keySize: 128 / 8,
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
});
console.log(plainText.toString(CryptoJS.enc.Utf8))
```

```
//Encryption
var CryptoJS = require("crypto-js");
const program = require("commander");
const {
    Buffer
} = require('buffer');
program.option("-d, --data <data>", "Data to process").parse(process.argv);
const options = program.opts();
const requestbody = Buffer.from(options.data, 'base64').toString('utf8');
var key = CryptoJS.enc.Utf8.parse('8080808080808080');
var iv = CryptoJS.enc.Utf8.parse('8080808080808080');
var encryptedclientDetail = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(requestbody), key, {
    keySize: 128 / 8,
    iv: iv,
    mode: CryptoJS.mode.CBC,
    padding...