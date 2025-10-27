---
title: VulnImage - Automated Method
url: https://blog.g0tmi1k.com/2011/12/vulnimage-automated-method/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:36.571512
---

# VulnImage - Automated Method

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# VulnImage - Automated Method

[VulnImage](https://blog.g0tmi1k.com/categories/vulnimage/) is an obscure *(I can't even find a 'homepage' as such for it!)* "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating system which has purposely crafted weakness(es) inside itself. The user's end goal is to interact with it and get the highest user privilege they can.

The 'automated' tag is because of the combination of Burp Proxy & SQLMap to discover the SQL injection vulnerability with very limited user interaction as well as using a kernel exploit to escalate privileges to gain root access. A more advanced method can be found [here](https://blog.g0tmi1k.com/2011/12/vulnimage-manual-method/).

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/VulnImage_-_Automated.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/VulnImage*-*Automated.mp4](http://download.g0tmi1k.com/videos_archive/VulnImage_-_Automated.mp4)

## Method

* Scanned network for the target [NetDiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted & intercepted with the web server [Firefox & Burp Proxy]
* Discovered an SQL injection vulnerably [SQLMap]
* Manipulate the blog to upload an encoded backdoor [Pentestmonkey's Php-Reverse-Shell & Metasploit]
* Escalated privileges via a vulnerable kernel version [udp\_sendmsg]
* Accessed the 'flag' [Phrack]

## Tools

* [VulnImage.zip](http://ds.mathematik.uni-marburg.de/) *(MD5: 8CB0E628AEB3C7E1F771764D07280655)*.
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/))*.
* [NetDiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/)).*
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository).*
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5).*
* [Firefox](https://www.mozilla.org/en-US/firefox) – *(Can be found in BackTrack 5).*
* [Burp Proxy](http://portswigger.net/burp/proxy.html) – *(Can be found in BackTrack 5).*
* [SQLMap](http://sqlmap.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [Msfvenom](http://metasploit.com/) – *(Part of Metasploit & Can be found in BackTrack 5).*
* [php-reverse-shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) – *(Can be found in BackTrack 5).*
* [NetCat](http://netcat.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [udp\_sendmsg](http://www.exploit-db.com/exploits/9574/) – *(Found on exploit-db.com & Can be found in BackTrack 5).*

## Walkthrough

The first stage is to locate the target, which the attacker does by using "NetDiscover" as this quickly lists all IP's, Media Access Control (MAC) addresses and any known vendors that relate to the MAC address in any subnet. The attacker knows that the target is using VMware, as there aren't any other virtual machines in use and the target hasn't spoofed their MAC address, therefore, the target is successfully identified.

As the attacker can now isolate the target on the network, the attacker proceeds by port scanning the target as this allows the attacker to see if there are any services which are listening on the exposed interface. The attacker chooses to use "UnicornScan" as it is accurate & efficient whilst scanning at speed. The result being it discovers 7 open TCP ports; 22 (SSH), 25 (SMTP), 80 (HTTP), 139 (NETBIOS), 445 (SAMBA), 3306 (MySQL) and 7777 (CBT). There is only 1 UDP port, 137 (NETBIOS). The attacker then chooses to verify the TCP results by using "nmap" to do another port scan. At the same time, the attacker takes advantage of some other features built into nmap, such as its scripting engine. This enumerates the open port's protocols and services which have been detected, as well as banner grabbing. The attack chooses to interact with the web service which is running on the default TCP port 80. The justification for this is because it is a very graphical, friendly and common way in, allowing the end user to interact. As a result there could be lots of information which could be enumerated as well as very poorly written code which could be taken advantage of.

The web service responds normally when the attacker interacts with it using a web browser, "firefox", however the attacker then takes it one stage further by capturing any requests which are made to it using "burp proxy".

> **'Normal'**
>
> Attacker (Firefox) <---> Target (Web server)
>
> **'Intercepted'**
>
> Attacker (Firefox) <---> Burp Proxy <---> Target (Web server)

By using burp proxy, the attacker is able to monitor every aspect of what is being requested and then how the web server responds. The attacker then just interacts normally with the target by viewing pages. The attacker soon sees the web service is running a blog, and notes the username (blogger) from which two posts have been made. After freely clicking a few links, the attacker sees that anyone can view the page which can make new blog posts, however there is a username & password field which the attacker doesn't have credentials for along with a page to update their profile. The attacker doesn't know any credentials and therefore fills in random junk data into the fields before submitting. This is done for burps benefit as it will capture the requests thus knowing data can be entered on this page. The attacker is presented with a message saying the username and or password is wrong. *At this point the attack restores proxy settings as firefox is not needed any longer.*

When the attacker was interacting the with the web application, they made a request with data that they entered. The data which was filled in was checked against a form of database to see if there was an entry that matched. By using "SQLMap" allows the attacker to manipulate the database in ways the original request wasn't meant for (providing that the field hasn't been 'correctly' filtered). SQLMap allows for multiple database formats, using different injection techniques and inbuilt enumeration to be tested without any user interaction. The attacker simply uses the log file which was created from burp and requests what information is to be enumerated. The attacker soon discovers the web service which is being used, as well as the operating system, the database and user which is connected to it, and, if that user is database administrator. The attacker then 'dumps' all the username and passwords for the database - *these could be cracked to see if any credentials were re-used.* The attacker checks to see if any users to the database and the operating system match. The attacker moves on by viewing the database structure as well as the contents. Upon inspection they enumerated three databases along with the column names, types and number of entries. The last stage for the attacker was to view the contents of the blog's credentials. As the attacker has successfully managed to enumerate the whole database, the attacker was able to very easily locate the credentials, and soon discover that they are stored in 'plain text'.

Another feature of burp is its 'repeater', which allows for data to be easily viewed, edited and sent multiple times. The attacker locates the request which was made at the beginning with junk data and passes it to the repeater and updates the respectable fields with the newly acquired credentials. The attacker notices another field, which, when they made the 'normal' request with the junk data, they didn't have 'control' over. This 'hidden' field looks like it as a file extension that is commonly used for text files. Be...