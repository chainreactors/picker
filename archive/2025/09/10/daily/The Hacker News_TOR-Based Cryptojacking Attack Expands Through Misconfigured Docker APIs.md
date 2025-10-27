---
title: TOR-Based Cryptojacking Attack Expands Through Misconfigured Docker APIs
url: https://thehackernews.com/2025/09/tor-based-cryptojacking-attack-expands.html
source: The Hacker News
date: 2025-09-10
fetch_date: 2025-10-02T19:56:15.818787
---

# TOR-Based Cryptojacking Attack Expands Through Misconfigured Docker APIs

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

# [TOR-Based Cryptojacking Attack Expands Through Misconfigured Docker APIs](https://thehackernews.com/2025/09/tor-based-cryptojacking-attack-expands.html)

**Sep 09, 2025**Ravie LakshmananCloud Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTyVEL-sVGK04WfS6I9fiQcWLnTLiP7kInJxyq-ngjBUXeaVY-5Qz28Ry2RAYdhfxpYZQj7_7Y6QM5k4MLyWLd7MB8fI8rnJ-9m6AhwT8DymYkZvNWxX3TGJYWWNyYBzf2xpV3nHV6X1fCVgeZy1jjUv4hxA6xWgf1teDdEsImJh15RViyra8BVcBOXvlZ/s790-rw-e365/docker.jpg)

Cybersecurity researchers have discovered a variant of a recently disclosed campaign that abuses the TOR network for cryptojacking attacks targeting exposed Docker APIs.

Akamai, which discovered the latest activity last month, said it's designed to block other actors from accessing the Docker API from the internet.

The findings build on a [prior report](https://thehackernews.com/2025/06/hackers-exploit-misconfigured-docker.html) from Trend Micro in late June 2025, which uncovered a malicious campaign that targeted exposed Docker instances to stealthily drop an XMRig cryptocurrency miner using a TOR domain for anonymity.

"This new strain seems to use similar tooling to the original, but may have a different end goal – including possibly setting up the foundation of a complex botnet," security researcher Yonatan Gilvarg [said](https://www.akamai.com/blog/security-research/new-malware-targeting-docker-apis-akamai-hunt).

The attack chain essentially involves breaking into misconfigured Docker APIs to execute a new container based on the Alpine Docker image and mount the host file system into it. This is followed by the threat actors running a Base64-encoded payload to download a shell script downloader from a .onion domain.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The script, besides altering SSH configurations to set up persistence, also installs other tools such as masscan, libpcap, libpcap-dev, zstd, and torsocks to conduct reconnaissance, contact a command-and-control (C2) server, and download a compressed binary from a second .onion domain.

"The first file that is downloaded is a dropper written in Go that includes the content it wants to drop, so it won't communicate out to the internet," Gilvarg explained. "Except for dropping another binary file, it parses the utmp file to find who is currently logged in to the machine."

Interestingly, the binary file's source code includes an emoji to depict users who are signed in to the system. This indicates that the artifact may have been crafted using a large language model (LLM).

The dropper also launches Masscan to scan the internet for open Docker API services at port 2375 and propagate the infection to those machines by repeating the same process of creating a container with the Base64 command.

Furthermore, the binary includes checks for two more ports: 23 ([Telnet](https://en.wikipedia.org/wiki/Telnet)) and 9222 ([remote debugging port](https://developers.google.com/cast/docs/debugging/remote_debugger) for Chromium browsers), although the functionality to spread via those ports is yet to be fully fleshed out.

The Telnet attack method entails using a set of known, default routers and device credentials to brute-force logins and exfiltrate successful sign-in attempts to a webhook[.]site endpoint with details about the destination IP address and victim authentication credentials.

In the case of port 9222, the malware utilizes a Go library named chromedp to interact with the web browser. It has been previously weaponized by [North Korean threat actors](https://thehackernews.com/2023/12/kimsuky-hackers-deploying-appleseed.html) to communicate with C2 servers and even by [stealer malware](https://redcanary.com/blog/threat-intelligence/google-chrome-app-bound-encryption/) to bypass Chrome's [app-bound encryption](https://thehackernews.com/2025/05/eddiestealer-malware-uses-clickfix.html), connect remotely to Chromium sessions, and siphon cookies and other private data.

It then proceeds to attach to an existing session with the open remote port and ultimately send a POST to the same .onion domain used to retrieve the shell script downloader with information about the source IP address on which the malware is and the destination it found access to on port 9222.

The details are transmitted to an endpoint named "httpbot/add," raising the possibility that devices with exposed remote debugging ports for Chrome/Chromium could be enlisted into a botnet for delivering additional payloads that can steal data or be used to conduct distributed denial-of-service (DDoS) attacks.

"As the malware only scans for port 2375, the logic for handling ports 23 and 9222 is currently unreachable and will not be executed," Gilvarg said. "However, the implementation exists, which may indicate future capabilities."

"Attackers can gain significant control over systems affected by abused APIs. The importance of segmenting networks, limiting exposure of services to the internet, and securing default credentials cannot be overstated. By adopting these measures, organizations can significantly reduce their vulnerability to such threats."

### Wiz Flags AWS SES Abuse Campaign

The disclosure comes as cloud security firm Wiz detailed an Amazon Simple Email Service (SES) campaign in May 2025 that leveraged compromised Amazon Web Services (AWS) access keys as a launchpad for a mass phishing attack.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's currently not known how the keys were obtained. However, various methods exist by which an attacker can accomplish this: accidental public exposure in code repositories or through misconfigured assets, or theft from a developer workstation using stealer malware.

"The attacker used the compromised key to access the victim's AWS environment, bypass SES's built-in restrictions, verify new 'sender' identities, and methodically prepare and conduct a phish...