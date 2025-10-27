---
title: How-to: Make Your Own Cert With Web OpenSSL
url: https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/
source: Didier Stevens
date: 2023-02-18
fetch_date: 2025-10-04T07:22:35.863231
---

# How-to: Make Your Own Cert With Web OpenSSL

# [Didier Stevens](https://blog.didierstevens.com/)

## Friday 17 February 2023

### How-to: Make Your Own Cert With Web OpenSSL

Filed under: [Encryption](https://blog.didierstevens.com/category/encryption/) — Didier Stevens @ 0:00

I explain how to create certificates with OpenSSL on your Windows computer in my blog post “[How-to: Make Your Own Cert With OpenSSL on Windows (Reloaded)](https://blog.didierstevens.com/2021/06/07/how-to-make-your-own-cert-with-openssl-on-windows-reloaded/)“.

If you can’t or don’t want to install OpenSSL, there is a solution now with [Web OpenSS](https://www.cryptool.org/en/cto/openssl)L.

With Web OpenSSL, you can just run OpenSSL and the commands in your browser, like this (for more info on these commands , read my [blog post](https://blog.didierstevens.com/2021/06/07/how-to-make-your-own-cert-with-openssl-on-windows-reloaded/)).

Go to [Web OpenSSL](https://www.cryptool.org/en/cto/openssl):

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-203457.png)

Scroll down a bit:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-203512.png)

Click “Enter split screen”. You will now have a command-line interface to the left and the folder with files to the right:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-203551.png)

Enter this command:

**openssl genrsa -out ca.key 4096**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-203839.png)

Notice that 2 files have been created. You can take a look at them, for example ca.key:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-203948.png)

Enter this command and answer the questions:

**openssl req -new -x509 -days 1826 -key ca.key -out ca.crt**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204136.png)

Enter this command:

**openssl genrsa -out ia.key 4096**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204212.png)

Enter this command and answer the questions:

**openssl req -new -key ia.key -out ia.csr**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204432.png)

Create a text file named **altname.cnf** and enter your domain name, this is the content for my domain name: **subjectAltName=DNS:www.didierstevens.com**

Upload this file (button Browse in Files) and check it was properly uploaded:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204612.png)

Enter this command:

**openssl x509 -req -days 730 -in ia.csr -CA ca.crt -CAkey ca.key -set\_serial 01 -out ia.crt -extfile altname.cnf**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204704.png)

Enter this command:

**openssl pkcs12 -export -out ia.p12 -inkey ia.key -in ia.crt -chain -CAfile ca.crt**

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204757.png)

You can then download all your files:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-204910.png)

Verify and start using them:

![](https://blog.didierstevens.com/wp-content/uploads/2023/02/20230213-205129.png)

If you want to understand what these commands exactly do, read my blog post “[How-to: Make Your Own Cert With OpenSSL on Windows (Reloaded)](https://blog.didierstevens.com/2021/06/07/how-to-make-your-own-cert-with-openssl-on-windows-reloaded/)“.

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/?share=x)

### *Related*

[Comments (2)](https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/#comments)

## 2 Comments [»](#postcomment "Leave a comment")

1. Elliptical Curve keys are superior in most ways, would be helpful if the guide showed how to generate those. 🙂

   Comment by Emil Kraus — Friday 17 February 2023 @ [7:26](#comment-615685)
2. What would be helpful to you precisely? EC for the ia key? Or the ca key, or both? And which predefined curve?

   Comment by [Didier Stevens](https://didierstevens.wordpress.com/) — Saturday 18 February 2023 @ [10:22](#comment-615728)

[RSS feed for comments on this post.](https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/feed/) [TrackBack URI](https://blog.didierstevens.com/2023/02/17/how-to-make-your-own-cert-with-web-openssl/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
  + [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
  + [Overview of Content Published in September](https://blog.didierstevens.com/2025/10/02/overview-of-content-published-in-september-9/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
* ## Categories

  + [.NET](https://blog.didierstevens.com/category/net/)
  + [010 Editor](https://blog.didierstevens....