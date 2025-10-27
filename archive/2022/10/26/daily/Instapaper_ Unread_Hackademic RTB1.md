---
title: Hackademic RTB1
url: https://blog.g0tmi1k.com/2012/01/hackademic-rtb1
source: Instapaper: Unread
date: 2022-10-26
fetch_date: 2025-10-03T20:57:13.345143
---

# Hackademic RTB1

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Hackademic RTB1

[Hackademic](https://blog.g0tmi1k.com/categories/hackademic/) is the first in a collection of "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating systems which has purposely designed weakness(es) built into it. The user's end goal is to interact with it and get the highest user privilege they can.

![](/images/hackademicrtb1.png "Hackademic")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/Hackademic-RTB1.mp4)

Download video: <http://download.g0tmi1k.com/videos_archive/Hackademic-RTB1.mp4>

## Method

* Scanned network for the target [Netdiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted with the web server & enumerated the web application [Firefox & WPScan]
* Discovered & exploit an SQL injection vulnerably and download the configuration files [Exploit-DB & SQLMap]
* Brute Force the user credentials for the web application [John The Ripper]
* Hijacked a plugin for the the web application with a web shell backdoor [Pentestmonkey's Php-Reverse-Shell]
* Escalated privileges via a vulnerable kernel version [RDS Protocol exploit]
* Accessed the 'flag' [Text file]
* *Discovered other 'interesting files' [Forensics analysis?]*

## Tools

* [Hackademic.RTB1.zip](https://ghostinthelab.wordpress.com/2011/09/06/hackademic-rtb1-root-this-box/) *(MD5: C972E899A8B5A745963BEF78FBCAEC6F).*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/)).*
* [Netdiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/)).*
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository).*
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5).*
* [Firefox](https://www.mozilla.org/en-US/firefox) – *(Can be found in BackTrack 5).*
* [WPScan](http://code.google.com/p/wpscan/) – *(Can be found in BackTrack 5's repository).*
* [SQLMap](http://sqlmap.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [John The Ripper](http://www.openwall.com/john/) – *(Can be found in BackTrack 5).*
* [php-reverse-shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) – *(Can be found in BackTrack 5).*
* [NetCat](http://netcat.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [RDS Protocol](http://www.exploit-db.com/exploits/15285/) – *(Found on [exploit-db.com](http://www.exploit-db.com/) & Can be found in BackTrack 5).*

## Walkthrough

To start the attack, the target needs to be located. By using "NetDiscover" it is able to quickly list all IP's, Media Access Control (MAC) addresses and known vendors in the same subnet. As the attacker knows that the target is using VMware and the target hasn't spoofed their MAC address, they notice only one VMware vendor therefore they can successfully identify the target.

The attacker now concentrates on the target's single IP address by port scanning every TCP and UDP port. "UnicornScan" reported one open port, TCP 80 (HTTP), which the attacker then verifies by using "nmap". During the port scan the attacker uses nmap's scripting engine to detect the service on the port (which is a web server) and banner grab (which possible enumerates software and it's version). Depending on the outcome of the scan, nmap then executes other scripts. In this instance the [http methods](http://nmap.org/nsedoc/scripts/http-methods.html) were detected (which shows what options are supported by an HTTP server) along with the page's title. *Nmap also tries to fingerprint the operating system (Linux 2.6.22-2.6.36).*

By inspecting the web service the attacker is able to see if any web application is running and if they are able to interact with it. The web server responds when the attacker views the contents using "firefox". They are then presented with a page that has a message from the target's author forwarding them along to another page. Upon following the link, the attacker then views the blog. By viewing the page source code the attacker notices a possible web product that could be used to power the blog along with its version.

To confirm their findings the attacker installs and runs "wpscan", which is a vulnerability scanner specifically designed for the blogging software, wordpress. This program will automate the process of identifying known vulnerabilities using various different techniques. WPScan confirms its wordpress and its version along with a known vulnerability.

The attacker searches a public exploit database, "exploit-db", to see if they are able to find the exploit which was mentioned in wpscan. The database returned six exploits for wordpress. The attacker views the content of the first exploit code to discover how it functions. *Editor's note: When executing the exploit and targeting the target, the exploit didn't work, same with the exploit reported by wpscan.*

The attacker moves back to firefox and using the exploit code, manually tests for the same SQL injection vulnerability. Upon requesting the malformed URL with the injection code present, the attacker notices an SQL error message on the side, therefore confirming that the web application is vulnerable. The attacker then starts the process of SQL injection. To start off with the attacker needs to know the number of columns within the query that is to be injected into, which is done by increasing the value tested by 1 until they reach an error. Once the amount is known, they need to be able to locate the output of the SQL query on the page. Once this is done the attacker is able to start enumerating the back end database, by finding out the version, current user and current database in use. They are also able to read files locally *(as long as the database service has permission to do so)* on the server too, by encoding the filename into base64.

To speed up the SQL injection process, the attacker switches to "SQLMap" which automates a lot of the work. *The attacker repeats what was done before manually now with sqlmap automatically to demonstrate how simpler the process now is. At the same time they collect **hashed** passwords to the database.* The attacker continues by trying to view the web server configuration file(s). They start off by locating their local file, to see if it matches the targets and attempts to access it *- which fails.* They keep trying to access other possible default locations ([source](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)) until they are successful. After viewing the file the attacker now knows the local path of the root folder for the web server. From here the attacker wants to download the configuration file which is used for the blog software. As the blog needs to store the credentials to the database to be able to access it, the attacker tries the default filename for wordpress that contains the configuration. After sqlmap downloads the file, the attacker now has the credentials in plain-text to the MySQL database.

*The attacker then uses the hash which was collected by SQLMap to validate the configuration file by using "John The Ripper" (which has to have the 'jumbo' patch (aka community - enhanced version) applied to support the MySQL hash format).*

Now the attacker sets out to obtain the user credentials to the blog via the SQL injection. By viewing the wordpress documents, they are able to understand the [Database Description](https://codex.wordpress.org/Database_Description). They discover there are 6 users registered and the fields used to store all their values. The attacker creates a simple loop to request each user'...