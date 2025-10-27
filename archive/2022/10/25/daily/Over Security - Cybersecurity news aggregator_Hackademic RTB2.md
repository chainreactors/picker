---
title: Hackademic RTB2
url: https://blog.g0tmi1k.com/2012/01/hackademic-rtb2/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:40.965675
---

# Hackademic RTB2

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# Hackademic RTB2

[Hackademic](https://blog.g0tmi1k.com/categories/hackademic/) is the second challenge in a series of "[boot-to-root](https://blog.g0tmi1k.com/categories/boot2root/)" operating systems which has purposely designed weakness(es) built into it. The user's end goal is to interact with system using the highest user privilege they can reach.

![Hackademic Logo](/images/hackademicrtb2.png "Hackademic")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/Hackademic-RTB2.mp4)

Download video: <http://download.g0tmi1k.com/videos_archive/Hackademic-RTB2.mp4>

## Method

* Scanned network for the target [Netdiscover]
* Port scanned the target [UnicornScan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted with the web server & bypass the login screen [Firefox & Burp Proxy]
* Decoded hidden message [Burp Proxy *& Xlate*]
* 'Port knock' certain ports [Netcat]
* Discovered & exploit an SQL injection vulnerably and download the configuration files [SQLMap]
* Inserted a encoded web shell backdoor [Pentestmonkey's PHP-Reverse-Shell & Metasploit]
* Escalated privileges via a vulnerable kernel version [CAN BCM exploit]
* *Accessed the 'flag' [Decoded image file]*

## Tools

* [Hackademic.RTB2.zip](https://ghostinthelab.wordpress.com/2011/09/06/hackademic-rtb1-root-this-box/) *(MD5: 4c35e875e0ae2f872af6751f259b82b7).*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/)).*
* [Netdiscover](http://www.nixgeneration.com/~jaime/netdiscover/) – *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/)).*
* [UnicornScan](http://www.unicornscan.org/) – *(Can be found in BackTrack 5's repository).*
* [NMap](http://nmap.org/) – *(Can be found in BackTrack 5).*
* [Firefox](https://www.mozilla.org/en-US/firefox)– *(Can be found in BackTrack 5).*
* [Burp Proxy](http://portswigger.net/burp/proxy.html) – *(Can be found in BackTrack 5).*
* *[Xlate](http://home.paulschou.net/tools/xlate/) - optional.*
* [Netcat](http://netcat.sourceforge.net/) – *(Can be found in* BackTrack 5).\_
* [SQLMap](http://sqlmap.sourceforge.net/) – *(Can be found in BackTrack 5).*
* [PHP-Reverse-Shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) – *(Can be found in BackTrack 5).*
* [Msfvenom](http://metasploit.com/) – *(Part of Metasploit & Can be found in BackTrack 5).*
* [CAN BCM](http://www.exploit-db.com/exploits/14814/) – *(Found on [exploit-db.com](http://www.exploit-db.com/) & Can be found in* BackTrack 5).\_
* [Base64Decode](http://www.opinionatedgeek.com/dotnet/tools/base64decode/)

## Walkthrough

To begin the attack the target needs to be located on the network. The attacker uses "Netdiscover" as it is able to quickly list all IP's, MAC addresses and known vendors. As the attacker knows the target hasn't spoofed their MAC address and are aware they are using VMware, the attacker has successfully identified the target due to only one VMware vendor being listed.

The attacker now focuses on the target by port scanning every TCP & UDP port. "UnicornScan" shows two open ports, TCP 80 (HTTP) & UDP 5353 (MDNS), which the attacker then verifies by using "nmap". During nmap's scan the attacker takes advantage of its scripting engine to detect which service is running on what port as well as to banner grab *(which could possibly identify the software being used & its version)*. Depending on the outcome of the scan, nmap then executes any other script(s). In this instance the [http methods](http://nmap.org/nsedoc/scripts/http-methods.html) was detected *(which shows what options are supported by the HTTP server)* along with the page's title. *Nmap also tries to fingerprint the operating system (Linux 2.6.17-2.6.36).*

By inspecting the web service using "firefox" the attacker is able to see if any web application is running and how they can interact with it. The web server responds and presents them with a page that has a message from the target's author and a login screen.

The attacker starts "Burp Proxy" and configures it along with firefox to allow burp to interpret & monitors the traffic between the attacker and the target. When the attacker enters an incorrect login, burp is able to capture the request and response allowing for the attacker to control and repeat using burp's "repeater" function. The attacker then repeats the same incorrect login request to verify the setup and then again however alters the password to reflex '*standard/common*' values to bypass login screens. *Editor's note: As it turns out, there isn't a backend database powering the login. The valid credentials have been hard coded into the source code (File: /var/www/welcome/check.php - Line: 17-20). Unless it's exactly the same (including case and spaces), it will not work!*

> $pass\_answer = "' or 1=1--'";
>
> $pass\_answer\_2 = "' OR 1=1--'";
>
> if($*POST['password'] == $pass\_answer or $*POST['password'] == $pass\_answer\_2){

After bypassing the login screen, the attacker is able to see the hidden message. When analysing the message, the attacker believes that the string has been HEX encoded, however due to the "%" which separates each value, the attacker uses burp's URL to decode the message. The output of the message still looks encoded to the attacker and repeats decoding the message, using burp's HEX mode. The output produce is now *(partly)* '*readable*'. The attacker remembered nmap reported one port as closed & due to the message repeating the phrase "knock", they start to suspect that the rest of the encoded message relates to the technique called '*port knocking*'. As the rest of the encoded message uses just '0' & '1' the attacker believes the message to be encoded in a binary format and attempts to decode it. The result produced looks familiar to the attacker and [recognises some values](http://www.ascii.cl/htmlcodes.htm) as *'html'*, however due to the *'formatting/markings'* burp is unable to decode it. The attacker takes the binary message and adds *'&#'* before every binary block (8 values) and '*;*' at the end of them too. This signals to burp to interpret the format differently and burp handles the message as html code. Upon decoding, the attacker sees a group of four values, all less than 65535 as well as believing the message is unable to be decoded any more.

*The attacker uses the web site, "paulschou.net", to simplify the decoding process and is able to decode all the messages without having to alter the format at any stage to reach the same result.*

The attacker scans the closed TCP port once more and by using "netcat" the attacker is able open to a port of their choice. They create a loop to connect to each of the ports which were decoded. Afterwards they repeat the same scan as before however this time they discover that the port response is open. Nmap reports that the service is HTTP, using *'Apache httpd 2.2.14 (ubuntu)'*, thus the same scripts are executed. *[http-robots](http://nmap.org/nsedoc/scripts/http-robots.txt.html) has detected that there is a /robots.txt files located and reports which folders have been forbidden to be indexed by internet spiders.*

Moving back to firefox, the attacker restores its proxy configuration as burp isn't needed and tries to connect to the newly discovered web service on the non-default port and is presented with a Joomla 1.5 instance. Upon exploring the web application they try to alter requested URLs and soon discover an MySQL error.

"SQLMap" automates the procedure of database injection dramatically speeding up the attack. The attacker starts to emulate the back end database and discovers software versions, the op...