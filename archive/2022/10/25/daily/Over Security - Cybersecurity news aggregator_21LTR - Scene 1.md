---
title: 21LTR - Scene 1
url: https://blog.g0tmi1k.com/2012/09/21ltr-scene-1/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:48.465518
---

# 21LTR - Scene 1

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# 21LTR - Scene 1

[21ltr](https://blog.g0tmi1k.com/categories/21ltr/) is another [boot2root](https://blog.g0tmi1k.com/categories/boot2root/) collection, with its own unique twist. It has various 'issues' with the operating system, which have been purposely put in place to make it [vulnerable by design](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/). The end goal is to become the '*super user*' of the system *(aka 'root')*. There is an optional stage afterwards, in which the user can try and find the '*flag*', proving *(to themselves)* that they successfully completed it.

![21ltr Logo](/images/21ltr.png "21ltr")

Table of Contents

* + [Links](#Links)
  + [Method](#Method)
  + [Tools](#Tools)
  + [Walkthrough](#Walkthrough)
  + [Commands](#Commands)
  + [Notes](#Notes)

## Links

Watch video on-line: [](http://download.g0tmi1k.com/videos_archive/21LTR_-_Scene_1.mp4)

Download video: [http://download.g0tmi1k.com/videos\_archive/21LTR*-*Scene\_1.mp4](http://download.g0tmi1k.com/videos_archive/21LTR_-_Scene_1.mp4)

## Method

* Scanned the network to locate the target [Net Discover]
* Port scanned the target to discover services [Unicorn Scan]
* Banner grabbed the services running on the open port(s) [NMap]
* Interacted with the web server by testing the default page, then brute forced to discover folders & files in the web root [Firefox & DirB]
* Cloned the FTP root folder with credentials learned from the web service [ftp]
* Analysed the 'loot' collected from the FTP service, in which to locate an additional file positioned on the web server [grep & cURL]
* Impersonated 'Dev Server Backup', and waited for the target to communicate to the attacker using the information collected from the FTP & Web services [Unicorn Scan & IPTables & NetCat]
* Injected a PHP payload into the backup logs, creating a backdoor into the system [Netcat & WebHandler]
* Discovered unprotected SSH credentials, which, as it turns out are for a 'privileged' account
* Used a kernel exploit to modify a restricted file to view what additional functions the wheel group can execute [UDEV]
* Downloaded the user credentials for the operating system and brute forced the passwords [John The Ripper]
* Remote logged back into the system via SSH and logged in with valid credentials for the super user
* Discovered the flag in a different user's home folder, which has been deleted but not yet, removed from the operating system
* Explored the 'backup service' which was also triggered at the same time as the log port.

## Tools

* [21LTR.com\_Scene1\_2.120\_v1.0.iso](http://21ltr.com/scenes/) *(md5: c57d2b39cdf1216300d078eed88f24cb)*
* A virtual machine *(Example: [VMware Player](http://www.filehippo.com/download_vmware_player/) or [Virtual Box](http://www.filehippo.com/download_virtualbox/))*
* Net Discover - *(Can be found in [BackTrack 5](http://www.backtrack-linux.org/downloads/))*
* Unicorn Scan - *(Can be found in BackTrack 5)*
* NMap - *(Can be found in BackTrack 5)*
* Firefox - *(Can be found in BackTrack 5)*
* DirB - *(Can be found in BackTrack 5)*
* FTP - *(Can be found in BackTrack 5)*
* cURL - *(Can be found in BackTrack 5)*
* Netcat - *(Can be found in BackTrack 5)*
* WebHandler - *(Can be found in BackTrack 5)*
* UDEV Exploit - *(Can be found in BackTrack 5)*
* John The Ripper - *(Can be found in BackTrack 5)*
* darkc0de.lst - *(Can be found in BackTrack 5)*

## Walkthrough

The README of this challenge gave the attacker the scope of the attack as well as the network configuration (the target is using a static IP address). By using "Netdiscover", the attacker was able to confirm that the target is located in a different IP range from themselves (192.168.2.x).

After moving to the new IP range, the attacker port scans the selected target, which reveals any services that are running on open ports. By using "UnicornScan", it displays that there are only three open ports; TCP 21 (FTP), TCP 22 (SSH), TCP 80 (HTTP). The attacker checks Unicorn Scan's results by using "Nmap", but only scanning for TCP services. Nmap confirms the same result as before, however, the attacker uses nmap scripting engine to start emulating the services, allowing for the attacker to collect more information on the target. FTP primary function is for transferring files, SSH is used to remotely control the machine and HTTP is used to display web applications. SSH normally requires some form of credentials with which to use the service, whereas FTP can allow for anonymous usage; it is much more common for a web service to allow anyone to interact with it. Using this, the attacker views the default web page on the target's machine, using a graphical web browser, "firefox", to render the page's output.

By looking through the source code which is displayed to them, the attacker notices that hidden away from the displayed view are comments in the code, which appear to be a username and password.

The attacker keeps pursuing the web service, with the aid of "DirB". Once DirB is running, it will try and connect to all the combinations of folders and pages in a wordlist on the target's web service, and display the results. This allows for pages to be exposed that normally wouldn't be, unless the address is known (e.g. there aren't any hyperlinks pointing to the pages). One of the results from the default wordlist matches the username which was discovered in the source code from before. DirB reported when it tried to access the folder and the web server responded with "403", meaning it doesn't have permission to access that folder for a certain reason. The attacker repeats the same request, however, this time uses curl to access the page. The error message doesn't exactly say why they are not allowed to access the page. The attacker knows this could be for multiple reasons, for example; not authenticated, missing an index file and directory listing is disabled, file permissions on the web server etc.

As the attacker has seen multiple occurrences of the word 'logs' (e.g. in the web page's source code, hinting at a username, plus it's the name of the hidden web folder), the attacker tries the credentials for the FTP service. The consequence of using it is that it has logged the attacker into the FTP service, to display a single file, which the attacker downloads. Accessing the file offline, the attacker understands that the file is for 'Intranet Dev Server Backup Log'. The code itself contains PHP tags plus looking at the file extension, the attacker spots that the server could have PHP installed.

As there was only one file inside the ftp folder, a reason why the hidden web folder was returning 403, could be there isn't an 'index' page to display once inside the sub directory. The attacker goes back to the cURL which they made before and amends the filename that was downloaded. This time, the request displays the source code to the page, after it has been processed on the server. This means that:

* The file requested was valid (so the attacker has discovered a 'hidden' file in the hidden folder)
* The attacker could have the source code for the file (The files might be different!)
* If it is the same, then it appears PHP is successfully installed and is able to process code
* The ftp folder could be inside the web folder

The attacker now looks at the web page, and makes a note of a few things:

* It's a log page for the backup system (Web page title)
* It's not reading any values, therefore a different process has to update the log file (FTP offline file)
* In the error log, the IP address is 'static' (192.168.2.240)
* When the errors happen in the logs, the time has a pattern (7 requests, all happen at "something-one" minute). Therefore is there a scheduled event?

Using the information above, the attacker changes their IP address to match the one that was displayed on the page as well as continuously port scanning the target. Af...