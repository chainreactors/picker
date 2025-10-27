---
title: VulnImage - Manual Method
url: https://blog.g0tmi1k.com/2011/12/vulnimage-manual-method/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:38.007901
---

# VulnImage - Manual Method

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# VulnImage - Manual Method

[VulnImage](https://blog.g0tmi1k.com/categories/vulnimage/) is an obscure *(I can't even find a 'homepage' as such for it!)* "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating system which has purposely crafted weakness(es) inside itself. The user's end goal is to interact with it and get the highest user privilege they can.

The 'manual' tag is due to the way the login system is bypassed as well as privilege escalation *(via Linux exploit development, covering fuzzing to metasploit module)*. Another method is located [here](https://blog.g0tmi1k.com/2011/12/vulnimage-automated-method/).

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
    - [vulnimage.rb](#vulnimage.rb)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/VulnImage_-_Manual.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/VulnImage*-*Manual.mp4](http://download.g0tmi1k.com/videos_archive/VulnImage_-_Manual.mp4)

## Method

* Scanned network for the target [NetDiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Bypass login system [Firefox]
* Modified page requests to the web server [Tamper Data]
* Manipulate the blog to upload an backdoor [Pentestmonkey's PHP-Reverse-Shell]
* Brute forced directories & files on the web server [DirBuster]
* Discovered a custom application running and downloaded the source code ['buffd']
* Escalated privileges via a vulnerable kernel version [udp\_sendmsg]
  + **Exploit development starts at 5:28**
* Fuzzed the custom application until it crashed [NetCat & Python]
* Verified and located which part of the buffer is overwriting the EIP address in the registers [Metasploit's pattern\_create & pattern\_offset & GDB]
* Created shellcode to be executed [Metasploit's msfvenom]
* Updated the buffer with the shellcode and verified everything so far [Python & GDB]
* Final update of the buffer to include the ESP address [GDB]
* Escalated privileges via the new exploit ['buffd']
* Restart the target machine to verified the exploit
* Created metasploit module [Geany]
* Escalated privileges via the new exploit using metasploit ['buffd']
* Restored the targets machine back to its original state
* Instantly gained root access via the new exploit [metasploit]

## Tools

* [VulnImage.zip](http://ds.mathematik.uni-marburg.de/) *(MD5: 8CB0E628AEB3C7E1F771764D07280655)*.
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/))*.
* [NetDiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/))*.
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository)*.
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5)*.
* [Firefox](https://www.mozilla.org/en-US/firefox) – *(Can be found in BackTrack 5)*.
* [Tamper Data](https://addons.mozilla.org/en-US/firefox/addon/tamper-data/) – *(Can be found in BackTrack 5)*.
* [PHP-Reverse-Shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) – *(Can be found in BackTrack 5)*.
* [NetCat](http://netcat.sourceforge.net/) – *(Can be found in BackTrack 5)*.
* [DirBuster](https://www.owasp.org/index.php/Category%3AOWASP_DirBuster_Project) – *(Can be found in BackTrack 5)*.
* [udp\_sendmsg](http://www.exploit-db.com/exploits/9574/) – *(Found on exploit-db.com & Can be found in BackTrack 5)*.
* [Python](http://python.org/) – *(Can be found in BackTrack 5)*.
* [Metasploit](http://metasploit.com/) – *(Can be found in BackTrack 5)*.
* A Text Editor *(e.g. [Geany](http://www.geany.org/))* – *(Can be found in BackTrack 5's repository)*.

## Walkthrough

The first stage is to locate the target, which the attacker does by using "NetDiscover" as this quickly scans all the subnets for IP's, Media Access Control (MAC) addresses and any known vendors that relate to their MAC address. The attacker knows that the target is using VMware, as there aren’t any other virtual machines in use and the target hasn't spoofed their MAC address, therefore they have successfully identified the target.

The attacker then port scans the target as this discovers any services which are listening on the exposed interface. The attacker chooses to use "UnicornScan" as it is accurate & efficient whilst scanning at speed. The port scan shows there are 7 open TCP ports; 22 (SSH), 25 (SMTP), 80 (HTTP), 139 (NETBIOS), 445 (SAMBA), 3306 (MySQL) and 7777 (CBT). There is only 1 UDP port open, 137 (NETBIOS). The attacker then chooses to verify the TCP results by using "nmap" to do another port scan. At the same time, the attacker takes advantage of some other features built into nmap, such as its scripting engine. This enumerates the open port's protocols and services which have been detected, as well as banner grabbing. The attacker chooses to interact with the web service which is running on the default TCP port 80. The justification for this is because it is a very graphical, friendly and common way in allowing the end user to interact, because of this there could be lots of information which could be enumerated as well as poorly written code which could be taken advantage of.

The attacker starts "DirBuster" to brute force directories and files on the web server by connecting to a list of common paths used on a web server and to then analyse the HTTP response codes. As this takes a while, it is left running in the background.

The web service responds normally when the attacker interacts with it using a web browser, for example "firefox". The attacker then explores the web application structure by clicking through on links and soon sees the web service is running a blog, and, at the same time sees that two posts have been posted by the user, blogger. The attacker keeps on following links on the blog and soon is presented with a login page for user profiles. The first thing the attacker looks at is the page source code, which they notice has a hidden field called "fname" and a value of "sig.txt", which appears to be a text document for signatures. Next they test the login system by entering data which wouldn't be correct as this can be used to see if the login system is working as well as the error message(s) for an incorrect login. The attacker uses the possible username, 'blogger' and the password, 'password'. The attacker then goes back and repeats the request, however; this time uses a different password to attempt to alter the login process. Editor's note: Before recording the video, the attacker noticed that phpMyAdmin was running on the web server (due to DirBuster). This is a GUI to manage MySQL databases, which are commonly used to validate credentials. The attacker then replaces their password with a MySQL statement in which to modify (by 'injecting' their code) the MySQL statement which has been hardcoded on the server side. This "password" will cause the original MySQL statement to return true, therefore it will login as the chosen user without the correct password being present. Editor's note: An explanation of the vulnerable code is below:

*File: /var/www/admin/profile.php, line 31*

> Original statement: `$sql = "SELECT * FROM blog_users WHERE poster = '$username' AND password = '$password'";`
>
> Expected input (user: blogger, Password: password): `$sql = "SELECT * FROM blog_users WHERE poster = 'blogger' AND password = 'password'";`
>
> Injected input (user: blogger, Password: ' or 1=1-- -): `$sql = "SELECT * FROM blog_users WHERE poster = 'blogger' AND password = '' or 1=1-- -'";`

In the MySQL statement the 'WHERE' clause needs two parts to equal true due to the 'AND' operator. The username is...