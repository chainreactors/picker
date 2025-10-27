---
title: pWnOS 2 (PHP Web Application)
url: https://blog.g0tmi1k.com/2012/09/pwnos-2-php-web-application/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:51.986650
---

# pWnOS 2 (PHP Web Application)

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# pWnOS 2 (PHP Web Application)

This is the second release in the "[pWnOS](https://blog.g0tmi1k.com/categories/pwnos/)" [vulnerable machine](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/) collection, however, it has a different creator from the previous one (which explains why it has a different "feel" to it). As always with "[boot2root](https://blog.g0tmi1k.com/categories/boot2root/)" machines, it has purposely built "issues" allowing for the machine to become compromised, with the end goal being to become the super user, "root". This method uses a vulnerability in a PHP web application (see [here](https://blog.g0tmi1k.com/2012/09/pwnos-2-sql-injection/) for exploiting via SQL injection).

![pwnOS Logo](/images/pwnos2.png "pwnOS2")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/pWnOS_2_%28PHP%29.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/pWnOS\_2\_(PHP).mp4](http://download.g0tmi1k.com/videos_archive/pWnOS_2_%28PHP%29.mp4)

## Method

* Scanned the network to discover the target [Net Discover]
* Port scanned the target to determine the running services on the target [Unicorn Scan]
* Emulated the services by grabbing the banner/header of the running service(s) [NMap]
* Discovered a hidden web application [DirB]
* Located a public exploit for the out dated web application [Exploit-DB]
* Created an additional user that uploaded a PHP shell onto the target to gain remote command access into the system [Pentest Monkey PHP Shell]
* Automated the same attack [Metasploit]
* Located hard coded plain text credentials, which had been re-used, allowing for complete system access

## Tools

* [pWnOS\_v2.0.7z](http://pwnos.com/files/pWnOS_v2.0.7z) *(md5: 1eb0960c0ba29335230ada1df80cd22c)*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/))*
* [Net Discover](http://nixgeneration.com/~jaime/netdiscover/) - *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/))*
* [Unicorn Scan](http://www.unicornscan.org/) - *(Can be found in BackTrack 5)*
* [NMap](http://nmap.org/) - *(Can be found in BackTrack 5)*
* [Firefox](http://www.mozilla.org/firefox/new/) - *(Can be found in BackTrack 5)*
* [cURL](http://curl.haxx.se/) - *(Can be found in BackTrack 5)*
* [Simple PHP Blog <= 0.4.0 Multiple Remote Exploits](http://www.exploit-db.com/exploits/1191/) - *(Can be found in BackTrack 5)*
* [php-reverse-shell](http://pentestmonkey.net/tools/web-shells/php-reverse-shell) - *(Can be found in BackTrack 5)*
* [Netcat](http://netcat.sourceforge.net/) - *(Can be found in BackTrack 5)*
* [Metasploit](http://www.metasploit.com/download/) - *(Can be found in BackTrack 5)*

## Walkthrough

By reading the readme file, "pWnOS\_INFO-2\_0.txt", the attacker soon learns not only the IP range which the target is using, they also now know the target's network configuration *(it's using a static IP address of 10.10.10.100/24)*. The attacker confirms the given information, by sweeping the network range with "net discover", which only displays a single result that matches the specified IP from the readme file.

As soon as the attacker has updated their IP address to fit inside the target's subnet range, they try to discover what services the target is running. "Unicorn Scan" is able to quickly scan every port, both TCP and UDP, which belongs to the target. This shows that port TCP 22 *(SSH)* & TCP 80 *(HTTP)* are open. To verify the result, the attacker repeats port scanning all TCP ports with "nmap". An additional feature of nmap is its inbuilt scripting engine, which can emulate the services during the scan. This produces more relevant information about the target. Nmap confirms the same ports are open and which default port's numbers are used for their default services *(for example, SSH service on port TCP 22 and a web server running on TCP 80)*. As SSH services are normally used to remotely execute commands, and due to their nature they normally require a form of authentication before access to the service is granted. This leaves the attacker to start with the web service.

When the attacker visits the default web application with "Firefox" to graphically render the code, they are presented a form to fill in to which leads to further access to use the web application. After navigating around the site, they only discover three pages: the login form, a place to register in order to be able to login, and a home page. The home page contains an email address, "admin@isints.com". This could mean "admin" is a possible username *(which is very common)*, and the domain the target is connected to.

The attacker then starts to brute force various possible folders & filenames for common paths relating to web services by using "dirb". This displays three "interesting" results, "/includes", "/info", and "/blog". "/includes" contains pages relating to the source code, which are repeated throughout the web application *(for example, the header and footer)*. When they looked at the code, the attacker is able to see the PHP code as the file extensions is ".html" and the web server isn't configured to process this file extension as server side code. "/info" is a page to show the output of "[phpinfo()](http://php.net/manual/en/function.phpinfo.php)". *(Editor's note: This file contains lots of useful information which would benefit the attacker as they would be able to understand the configuration of PHP on the system. However, I chose not to use this as a source of information, as this wasn't part of the vulnerable web application)*.

After the attacker visits the URI of "/blog", they discover it has a hidden web application, which is meant for internal use for the company, "isints". By clicking around, they try to see if they can locate any private internal data which they can use to their advantage, however, they didn't notice anything. The attacker believes this wasn't a bespoke custom application like before, so they try to identify what application and its version. Upon viewing the home page source code, they discover it is "Simple PHP Blog 0.4".

The attacker re-runs dirb, however uses /blog as the default path, to see if there is any more hidden material located inside the application. This time, the attacker notices an "interesting" folder name, "/config". Using firefox they navigate to the folder and find it contains two files, "config.txt" and "password.txt". They both hold information which relates to their filename and the attacker downloads them both for an offline copy, in case they might be needed later.

The attacker takes their knowledge of the hidden web application and searches a public database of known exploits provided by "exploit-db" *(to see if they are able to exploit the target's web application and version, simple php blog v0.4)*. They find six exploits which match simple php blog and of those results, one result matches the target's version. After checking the exploit code will run, as sometimes there are additional values added at the start of the file that would means the file isn't correctly executed, the attacker runs the exploit code. The code presents a help screen that shows which command line arguments are required, for what function, as the supports multiple exploit.

The attacker starts the exploit code to display the hashes on the system, which they have already acquired. This allows for the attacker to see if they are issuing the commands correctly into the exploit. The response from the exploit shows the hashes match the same value that the attacker discovered when they used dirb.

Next they add another user into the web application with a usernam...