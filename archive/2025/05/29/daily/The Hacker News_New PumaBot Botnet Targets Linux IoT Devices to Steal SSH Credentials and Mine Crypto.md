---
title: New PumaBot Botnet Targets Linux IoT Devices to Steal SSH Credentials and Mine Crypto
url: https://thehackernews.com/2025/05/new-pumabot-botnet-targets-linux-iot.html
source: The Hacker News
date: 2025-05-29
fetch_date: 2025-10-06T22:32:03.663500
---

# New PumaBot Botnet Targets Linux IoT Devices to Steal SSH Credentials and Mine Crypto

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [New PumaBot Botnet Targets Linux IoT Devices to Steal SSH Credentials and Mine Crypto](https://thehackernews.com/2025/05/new-pumabot-botnet-targets-linux-iot.html)

**May 28, 2025**Ravie LakshmananIoT Security / Cryptocurrency

[![PumaBot Botnet](data:image/png;base64... "PumaBot Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh80ShmZ5hHfdqjsLl1j_gpExC_AKXq-ez-qQwiBYIXeOOl7RAnKwf3cjTJfDm5yr5QM4CLR9_0iUXZQvUlDUDnRtCSFSHv2FKFpBwgyCLIG54oRprric6e2iz-IhmEq0mntnb-XcKdiG4wBavldoq84K3Ocl5edleFQSuttfuNZMWZchd2lSp4CvP24v5Z/s790-rw-e365/linux.jpg)

Embedded Linux-based Internet of Things (IoT) devices have become the target of a new botnet dubbed **PumaBot**.

Written in Go, the botnet is designed to conduct [brute-force attacks against SSH instances](https://thehackernews.com/2025/04/outlaw-group-uses-ssh-brute-force-to.html) to expand in size and scale and deliver additional malware to the infected hosts.

"Rather than scanning the internet, the malware retrieves a list of targets from a command-and-control (C2) server and attempts to brute force SSH credentials," Darktrace [said](https://www.darktrace.com/blog/pumabot-novel-botnet-targeting-iot-surveillance-devices) in an analysis shared with The Hacker News. "Upon gaining access, it receives remote commands and establishes persistence using system service files."

The botnet malware is designed to obtain initial access via successfully brute-forcing SSH credentials across a list of harvested IP addresses with open SSH ports. The list of IP addresses to target is retrieved from an external server ("ssh.ddos-cc[.]org").

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As part of its brute-force attempts, the malware also performs various checks to determine if the system is suitable and is not a honeypot. Furthermore, it checks the presence of the string "Pumatronix," a manufacturer of surveillance and traffic camera systems, indicating either an attempt to specifically single them out or exclude them.

The malware then proceeds to collect and exfiltrate basic system information to the C2 server, after which it sets up persistence and executes commands received from the server.

"The malware writes itself to /lib/redis, attempting to disguise itself as a legitimate Redis system file," Darktrace said. "It then creates a persistent systemd service in /etc/systemd/system, named either redis.service or mysqI.service (note the spelling of mysql with a capital I) depending on what has been hardcoded into the malware."

In doing so, it allows the malware to give the impression that it's benign and also survive reboots. Two of the commands executed by the botnet are "xmrig" and "networkxm," indicating that the compromised devices are being used to mine cryptocurrency in an illicit manner.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgINl_WH6yPSMFZd7J3oDhcy9CTblc8qdJLI9X8DA3t1bU-nlvM2P9Ske7VmrFiFbz0C-aN4xsbMMGFxY6Pw_qPvBeCfTqtIhieCj4IHelEyx51EsAXvD2yAMYbVqo-ncwBol71nsSkTfVmYujlWMGOHld7CjEvSaNTo0esRO3hddGhh_-87Tncvyr8c00s/s790-rw-e365/wget.png)

"I believe the end goal is to deploy a cryptominer, given the reference to XMRig, however since C2 was down at the time of analysis, it can't be determined what commands were being sent or received," Tara Gould, threat research lead at Darktrace, told The Hacker News. "It is possible another payload, or cryptominer was being sent from the C2."

However, the commands are launched without specifying the full paths, an aspect that signals that the payloads are likely downloaded or unpacked elsewhere on the infected host. Darktrace said its analysis of the campaign uncovered other related binaries that are said to be deployed as part of a broader campaign -

* ddaemon, a Go-based backdoor which is retrieve the binary "networkxm" into "/usr/src/bao/networkxm" and execute the shell script "installx.sh"
* networkxm, an SSH brute-force tool that functions similar to the botnet's initial stage by fetching a password list from a C2 server and attempts to connect via SSH across a list of target IP addresses
* installx.sh, which is used to retrieve another shell script "jc.sh" from "1.lusyn[.]xyz," grant it read, write, and execute permissions for all access levels, run the script, and clear bash history
* jc.sh, which is configured to download a malicious "pam\_unix.so" file from an external server and use it to replace the legitimate counterpart installed on the machine, as well as retrieve and run another binary named "1" from the same server
* pam\_unix.so, which acts as a rootkit that steals credentials by intercepting successful logins and writing them to the file "/usr/bin/con.txt"
* 1, which is used to monitor for the file "con.txt" being written or moved to "/usr/bin/" and then exfiltrate its contents to the same server

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Given that the SSH brute-force capabilities of the botnet malware lends it worm-like capabilities, users are required to keep an eye out for anomalous SSH login activity, particularly failed login attempts, audit systemd services regularly, review authorized\_keys files for the presence of unknown SSH keys, apply strict firewall rules to limit exposure, and filter HTTP requests with non-standard headers, such as X-API-KEY: jieruidashabi.

"The botnet represents a persistent Go-based SSH threat that leverages automation, credential brute-forcing, and native Linux tools to gain and maintain control over compromised systems," Darktrace said.

"By mimicking legitimate binaries (e.g., Redis), abusing systemd for persistence, and embedding fingerprinting logic to avoid detection in honeypots or restricted environments, it demonstrates an intent to evade defenses."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](h...