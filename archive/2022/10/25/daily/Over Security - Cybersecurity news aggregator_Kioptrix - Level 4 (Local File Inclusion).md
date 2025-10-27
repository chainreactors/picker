---
title: Kioptrix - Level 4 (Local File Inclusion)
url: https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-local-file/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:45.123926
---

# Kioptrix - Level 4 (Local File Inclusion)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Kioptrix - Level 4 (Local File Inclusion)

[Kioptrix](https://blog.g0tmi1k.com/categories/kioptrix/) is a "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating system which has purposely designed weakness(es) built into it. The user's end goal is to interact with system using the highest user privilege they can reach.

There are other vulnerabilities using different techniques to gain access into this box such as breaking through a [limited shell](https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-limited-shell/) as well as backdooring via [MySQL](https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-sql-injection/) injection.

![Kioptrix Logo](/images/kioptrix.png "Kioptrix")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/Kioptrix_-_Level_4_%28Local_File_Inclusion%29.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/Kioptrix*-*Level\_4\_(Local\_File\_Inclusion).mp4](http://download.g0tmi1k.com/videos_archive/Kioptrix_-_Level_4_%28Local_File_Inclusion%29.mp4)

## Method

* Scanned network for the target [Netdiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted with the web server & logged into the system anonymously [Firefox & Burp Proxy]
* Discovered & exploited an local file inclusion vulnerably to enumerate possible users. [Burp Proxy]
* Exploited the same local file inclusion to fingerprint the web service & inject code into the PHP session data [Burp Proxy]
* Created a web shell on the target [Burp Proxy & Netcat] *(Limited user)*
* Created a shell and to escalated privileges executed it from a service running as superuser [Burp Proxy & Metasploit]
* *Accessed the 'flag' [Text file]*

## Tools

* [Kioptrix4\_vmware.rar](http://www.kioptrix.com/blog/?p=604) *(MD5: BB4E81EFAAD0E77CD2FCAF02B01A36A3).*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/)).*
* [Netdiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/)).*
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository).*
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5).*
* [Firefox](https://www.mozilla.org/en-US/firefox) – *(Can be found in BackTrack 5).*
* [Burp Proxy](http://portswigger.net/burp/proxy.html) – *(Can be found in BackTrack 5).*
* [Netcat](http://netcat.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [Msfvenom](http://metasploit.com/) – *(Part of Metasploit & Can be found in BackTrack 5).*

## Walkthrough

The scope of this attack is a certain target; therefore the attacker needs to discover it on their network. Scanning with "Netdiscover" produces a list of all IP's & MAC addresses and known vendors which are currently connected to the network. The attacker has prior knowledge and knows the target hasn't spoofed their MAC address as well as being inside a VM. Due to only one vendor which relates to a VM, VMware, they successfully identified the target.

By having the target's IP address, the attacker now focuses specifically on the target. The next thing they do is a port scan of every TCP & UDP port. "UnicornScan" shows five open ports; TCP 22 (SSH), TCP 80 (HTTP), TCP 139 (NetBIOS), TCP 445 (SMB) & UDP 137 (NetBIOS). "nmap" verifies the port scan results and at the same time the attacker takes advantage of nmap's inbuilt scripting engine, which detects what services are listening on each port, banner grab *(which could possibly identify the software being used & its version)* as well as fingerprinting the operating system. Depending on the outcome produced by the scan, nmap could decide to execute any other script(s). In this instance various samba scripts were executed to automatically enumerate it. *Nmap fingerprintted the operating system as Linux 2.6.9-2.6.31.*

By interacting with the web service using "firefox" the attacker is able to see if any web application is running. The web server responds and presents them with a login screen.

The attacker starts "Burp Proxy" and configures it. Burp is able to monitor & interpret the traffic between the attacker and the target. To do so, firefox's proxy settings are altered to direct the traffic into burp. Now when the attacker tries to login, burp has captured the request. Using burp's "repeater" function the attacker is able to manipulate the request as they wish. The attacker repeats the same incorrect login to verify the setup and gain a "base line" to compare results. On the next request the attacker has altered the password value to reflex a '*standard common*' SQL statement which affects login screens by always returning true. Upon the successful request to login, a cookie value has been set, 'PHPSESSID', which is used for storing values in between pages (*even if they are not always on the same domain!)* for a certain amount of time allowing for every user to be remembered. The attacker attaches the cookie value, repeats the login request and follows the redirect.

After bypassing the login system, the attacker is presented with the 'members' page, however the attacker isn't using a 'correct' username, thus the requested information is invalid which is why the attacker is given an error message. This is an error message produced from the code that is being executed on the page. The attacker repeats the last request, but replaces the username with a known filename *(the login page 'index.php')*. This request caused an error, however the error message produced is from the backend engine itself, PHP, saying that it wasn't able to include the file (along with the filename requested). From this error message the attacker notices how the code has altered the request from the original:

> Requested username: index.php
>
> Processed username: index.php/index.php.php

The attacker wishes for only the first part to be processed by the code, instead of adding a "/" *(to signal that its directory)* along with the value again and adding ".php" at the end *(as a file extension)*. The attacker can achieve their aim by adding "" afterwards which is a [NUL](https://en.wikipedia.org/wiki/Null_character) [meta character](https://en.wikipedia.org/wiki/Meta_character) which signals it's the end, thus the code does not process anything else afterwards. The attacker tries the updated request again, and is able to see that the login screen is included.

The attacker uses this vulnerability to collect as much as possible to help enumerate the system, for example, discovering which users have access into the system that could allow for the attacker to login the Web UI as a valid user. Upon requesting the standard 'passwd' file for a Linux operating system *(which has been identified multiple times),* the requested 'username' (aka filename) doesn't match up to what was processed and produces an error message. It's in the same format as the first one, which means there is some type of filtering being processed on the 'username' value that is being requested. After inspecting the filename in the error message the attacker notices, the only thing which is incorrect is 'etc' as it appears it's been taken out. The attacker repeats the request again and duplicate '/etc/' in the filename to see if that has an effect. The target responds and includes the file, giving the attacker a list of valid users on the system. This means the filtering system appears to search and replace 'etc' once with a blank value. *Editor's note: The users in the web service might not always match up to the system itself or vice versa as well as having a more complex...