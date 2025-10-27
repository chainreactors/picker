---
title: Kioptrix - Level 4 (SQL Injection)
url: https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-sql-injection/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:43.506621
---

# Kioptrix - Level 4 (SQL Injection)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Kioptrix - Level 4 (SQL Injection)

[Kioptrix](https://blog.g0tmi1k.com/categories/kioptrix/) which is a "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating system which has purposely designed weaknesses built into it. The user's end goal is to interact with system using the highest user privilege they can reach.

There are other vulnerabilities using different techniques to gain access into this box such as breaking through a [limited shell](https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-limited-shell/) as well as [local file inclusion](https://blog.g0tmi1k.com/2012/02/kioptrix-level-4-local-file/) using PHP session data.

![Kioptrix Logo](/images/kioptrix.png "Kioptrix")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/Kioptrix_-_Level_4_%28SQL_Injection%29.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/Kioptrix*-*Level\_4\_%28SQL\_Injection%29.mp4](http://download.g0tmi1k.com/videos_archive/Kioptrix_-_Level_4_%28SQL_Injection%29.mp4)

## Method

* Scanned network for the target [Netdiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted with the web server & discovered a the web application that is possibly subject to a SQL injection vulnerability [Firefox]
* Exploited the SQL injection and enumerated database *[SQLMap]*
* Uploaded a web shell backdoor [SQLMap & Netcat] *(Limited user)*
* Manually performed SQL injection injection to dump database [Burp Proxy]
* Created a web shell on the target [Burp Proxy & Netcat] *(Limited user)*
* Created a backdoor shell via a cron job [Burp Proxy & Netcat] *(Superuser)*
* *Accessed the 'flag' [Text file]*
* Created a backdoor shell via a cron job [Burp Proxy & Metasploit] *(Superuser)*

## Tools

* [Kioptrix4\_vmware.rar](http://www.kioptrix.com/blog/?p=604) *(MD5: BB4E81EFAAD0E77CD2FCAF02B01A36A3).*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/)).*
* [Netdiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/)).*
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository).*
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5).*
* [Firefox](https://www.mozilla.org/en-US/firefox) – *(Can be found in BackTrack 5).*
* [Tamper Data](https://addons.mozilla.org/en-US/firefox/addon/tamper-data/) – *(Can be found in BackTrack 5).*
* [Burp Proxy](http://portswigger.net/burp/proxy.html) – *(Can be found in BackTrack 5).*
* [Netcat](http://netcat.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [SQLMap](http://sqlmap.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [Msfvenom](http://metasploit.com/) – *(Part of Metasploit & Can be found in BackTrack 5).*

## Walkthrough

The first step to attack the target, is to discover it. Scanning with "Netdiscover" produces a list of all IP's & MAC addresses and known vendors which are currently connected to the network. The attacker has prior knowledge and knows the target hasn't spoofed their MAC address as well as being inside a VM. Due to there being only one vendor which relates to a VM, VMware, they successfully identified the target.

By having the target's IP address, the attacker now focuses specifically on the target. The next thing they do is a port scan of every TCP & UDP port. "UnicornScan" shows five open ports; TCP 22 (SSH), TCP 80 (HTTP), TCP 139 (NetBIOS), TCP 445 (SMB) & UDP 137 (NetBIOS). "nmap" verifies the port scan results and at the same time the attacker takes advantage of nmap's inbuilt scripting engine, which detects what services are listening on each port, banner grab *(which could possibly identify the software being used & its version)* as well as fingerprinting the operating system. Depending on the outcome produced by the scan, nmap could decide to execute any other script(s). In this instance various samba scripts were executed to automatically enumerate it. *Nmap fingerprintted the operating system as Linux 2.6.9-2.6.31.*

By interacting with the web service using "firefox" the attacker is able to see if any web application is running. The web server responds and presents them with a login screen. The attacker fills in a common username, "admin" and uses "'" as a password. The server responds with a MySQL error message saying there has been a problem processing our request. This signals there is a possible MySQL injection vulnerability.

The attacker can automate the database injection procedure by using "SQLMap" which dramatically speeds up the attack. The attacker uses the same URL which the error was produced on, and with the aid of "tamper data" they are also able easily to clone the same (POST) data which is sent to the target. *Editor's note: It could have been just as quick to manually type out the request using the page's source code!).* The first attempt to exploit the database, fails, however SQLMap states it can try more 'aggressive and complex' injection methods by increasing the level and risk factor, which the attacker does on the second try. This is successful, allowing the SQLMap to function fully benefiting the attacker. The attacker starts to emulate the back end database and discovers software versions, the operating system, current database & user and if they are a database administrator. Afterwards the attacker starts to view the content of the databases. This is a common procedure as MySQL has an option to automate this, '--dbs', however if there is a specific SQL statement the attacker manually wishes to execute, they can use,' --sql-shell', to do so. The attacker demonstrates this by viewing the contents of the table "members" *(however this could have been automated with '-D members -T members --dump').* Editor's note: I also wanted to demonstrate SQLMap output modes; 'minimal' *(-v 0)* which is just the outcome of the request as well as being able to show the SQL statements its currently sending (-v 3), therefore educating the attacker! SQLMap can also [display a lot more detail](http://sqlmap.sourceforge.net/doc/README.html#ss5.1) - such as what SQLmap sees by the server response).\_

Another feature of SQLMap (like its ability to give an interactive shell to the database), it can also attempt to get an interactive shell on the system itself, thus giving the attacker remote access to the target. The attacker tries out this feature and it is successful, allowing the attacker to execute commands locally on the target. *Editor's note: Due to the web root folder permissions set to superuser, and how sqlmap works (it writes using MySQL to the web root folder, a small client which then the web server uses to execute commands/upload files, thus it uses two different user accounts - this is covered later), the attacker needs to use the 'same method used for file stager'.* The attacker creates another shell *(a fall back, which is useful incase one shell is terminated for whatever reason...)* using a reverse netcat shell.

SQLMap has automated alot of aspects in the database injection, however the attacker wishes to have a little bit more 'control' by manually performing the attack themselves. The attacker starts "Burp Proxy" and configures it as burp allows for easy alternating and repeating requests. Firefox's proxy settings are altered to direct the traffic into burp. Now when the attacker tries to login using firefox, burp captures the request which they can manipulate. The attacker alters the password field to write every value in the database into a file located in the web root folder, as this would al...