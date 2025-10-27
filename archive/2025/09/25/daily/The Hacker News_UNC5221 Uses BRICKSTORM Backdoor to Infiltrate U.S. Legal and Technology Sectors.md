---
title: UNC5221 Uses BRICKSTORM Backdoor to Infiltrate U.S. Legal and Technology Sectors
url: https://thehackernews.com/2025/09/unc5221-uses-brickstorm-backdoor-to.html
source: The Hacker News
date: 2025-09-25
fetch_date: 2025-10-02T20:40:34.570837
---

# UNC5221 Uses BRICKSTORM Backdoor to Infiltrate U.S. Legal and Technology Sectors

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

# [UNC5221 Uses BRICKSTORM Backdoor to Infiltrate U.S. Legal and Technology Sectors](https://thehackernews.com/2025/09/unc5221-uses-brickstorm-backdoor-to.html)

**Sep 24, 2025**Ravie LakshmananCyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVHQRjvC6pO0azWfdLYA74JU51lHJwZMFjS8BvUza34zi3aeUm6Za6F3RlGzVBCHXDzd1ZhRbgC_t1R8NLkAKF0fQWoMUUV2rv0LNPuZSu_cpfiiKSZBKWsFjUsvLOHDufigPy7wEEXmHAbZDr8mLFiLn2XE2ruI9iTJXPwymxLaR92Sk9eGXusBtNJ7DU/s790-rw-e365/backdoor.jpg)

Companies in the legal services, software-as-a-service (SaaS) providers, Business Process Outsourcers (BPOs), and technology sectors in the U.S. have been targeted by a suspected China-nexus cyber espionage group to deliver a known backdoor referred to as **BRICKSTORM**.

The activity, attributed to UNC5221 and closely related, suspected China-nexus threat clusters, is designed to facilitate persistent access to victim organizations for over a year, Mandiant and Google Threat Intelligence Group (GTIG) [said](https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign) in a new report shared with The Hacker News.

It's assessed that the objective of BRICKSTORM targeting SaaS providers is to gain access to downstream customer environments or the data SaaS providers host on their customers' behalf, while the targeting of the U.S. legal and technological spheres is likely an attempt to gather information related to national security and international trade, as well as steal intellectual property to advance the development of zero-day exploits.

BRICKSTORM was [first](https://thehackernews.com/2024/05/china-linked-hackers-used-rootrot.html) [documented](https://thehackernews.com/2024/05/hackers-created-rogue-vms-to-evade.html) by the tech giant last year in connection with the zero-day exploitation of Ivanti Connect Secure zero-day vulnerabilities (CVE-2023-46805 and CVE-2024-21887). It has also been used to [target Windows environments](https://thehackernews.com/2025/04/mustang-panda-targets-myanmar-with.html) in Europe since at least November 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A Go-based backdoor, BRICKSTORM comes fitted with capabilities to set itself up as a web server, perform file system and directory manipulation, carry out file operations such as upload/download, execute shell commands, and act as a SOCKS relay. It communicates with a command-and-control (C2) server using WebSockets.

Earlier this year, the U.S. government [noted](https://thehackernews.com/2025/03/us-charges-12-chinese-nationals-in.html) that the China-aligned threat cluster tracked as APT27 (aka Emissary Panda) overlaps with that of Silk Typhoon, UNC5221, and UTA0178. However, GTIG [told](https://thehackernews.com/2025/04/critical-ivanti-flaw-actively-exploited.html) The Hacker News at the time that it does not have enough evidence on its own to confirm the link and that it's treating them as two distinct entities.

"These intrusions are conducted with a particular focus on maintaining long term stealthy access by deploying backdoors on appliances that do not support traditional endpoint detection and response (EDR) tools," GTIG said, adding it has responded to several intrusions since March 2025.

"The actor employs methods for lateral movement and data theft that generate minimal to no security telemetry. This, coupled with modifications to the BRICKSTORM backdoor, has enabled them to remain undetected in victim environments for 393 days, on average."

In at least one case, the threat actors are said to have exploited the aforementioned security flaws in Ivanti Connect Secure edge devices to obtain initial access and drop BRICKSTORM. But the prolonged dwell time and the threat actor's efforts to erase traces of their activity has made it challenging to determine the initial access vector used in other instances to deliver the malware on Linux and BSD-based appliances from multiple manufacturers.

There is evidence to suggest that the malware is under active development, with one sample featuring a "delay" timer that waits for a hard-coded date months in the future before initiating contact with its C2 server. The BRICKSTORM variant, Google said, was deployed on an internal VMware vCenter server after the targeted organization had commenced its incident response efforts, indicating the agility of the hacking group to maintain persistence.

The attacks are also characterized by the use of a malicious Java Servlet filter for the Apache Tomcat server dubbed BRICKSTEAL to capture vCenter credentials for privilege escalation, subsequently using it to clone Windows Server VMs for key systems such as Domain Controllers, SSO Identity Providers, and secret vaults.

"Normally, installing a filter requires modifying a configuration file and restarting or reloading the application; however, the actor used a custom dropper that made the modifications entirely in memory, making it very stealthy and negating the need for a restart," Google said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Furthermore, the threat actors have been found to leverage valid credentials for lateral movement to pivot to the VMware infrastructure and establish persistence by modifying init.d, rc.local, or systemd files to ensure that the backdoor is automatically sstarted on appliance reboot. Another method involves deploying a JavaServer Pages (JSP) web shell known as SLAYSTYLE (aka BEEFLUSH) to receive and execute arbitrary operating system commands passed through an HTTP request.

The primary goal of the campaign is to access the emails of key individuals within the victim entities, including developers, system administrators, and individuals involved in matters that align with China's economic and espionage interests. BRICKSTORM's SOCKS proxy feature is used to create a tunnel and directly access the applications dee...