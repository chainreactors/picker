---
title: Alert: Exposed JDWP Interfaces Lead to Crypto Mining, Hpingbot Targets SSH for DDoS
url: https://thehackernews.com/2025/07/alert-exposed-jdwp-interfaces-lead-to.html
source: The Hacker News
date: 2025-07-06
fetch_date: 2025-10-06T23:28:19.898572
---

# Alert: Exposed JDWP Interfaces Lead to Crypto Mining, Hpingbot Targets SSH for DDoS

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

# [Alert: Exposed JDWP Interfaces Lead to Crypto Mining, Hpingbot Targets SSH for DDoS](https://thehackernews.com/2025/07/alert-exposed-jdwp-interfaces-lead-to.html)

**Jul 05, 2025**Ravie LakshmananVulnerability / Botnet

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhowdOqQ15Mu_xz0HDY-2c9KyAioaotlAiFSc-p6Rlu3pyGYj8bdS4IyCbo0mO9qD_NjGYSni-yWULJSssUPnO8B4nL1x31h_ruhkYPc2exq8mryc4o_ZK1AebD6542p-rI5q9DvvuM8LzjKggLYzkYlgU5hZ1fbcflhfmXpM8SeenPqc4zvvD2qt4ZIvrs/s790-rw-e365/java-mining.jpg)

Threat actors are weaponizing exposed Java Debug Wire Protocol ([JDWP](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/jdwp-spec.html)) interfaces to obtain code execution capabilities and deploy cryptocurrency miners on compromised hosts.

"The attacker used a modified version of XMRig with a hard-"coded configuration, allowing them to avoid suspicious command-line arguments that are often flagged by defenders," Wiz researchers Yaara Shriki and Gili Tikochinski [said](https://www.wiz.io/blog/exposed-jdwp-exploited-in-the-wild) in a report published this week. "The payload used mining pool proxies to hide their cryptocurrency wallet address, thereby preventing investigators from pivoting on it."

The cloud security firm, which is being acquired by Google Cloud, said it observed the activity against its honeypot servers running TeamCity, a popular continuous integration and continuous delivery (CI/CD) tool.

JDWP is a communication protocol used in Java for debugging purposes. With JDWP, users can leverage a debugger to work in a different process, a Java application, on the same computer, or on a remote computer.

But given that JDWP lacks authentication or access control mechanisms, exposing the service to the internet can open up a new attack vector that attackers can abuse as an entry point, enabling full control over the running Java process.

Simply put, the misconfiguration can be utilized to inject and execute arbitrary commands in order to set up persistence on and ultimately run malicious payloads.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"While JDWP is not enabled by default in most Java applications, it is commonly used in development and debugging environments," Wiz said. "Many popular applications automatically start a JDWP server when run in debug mode, often without making the risks obvious to the developer. If improperly secured or left exposed, this can open the door to remote code execution (RCE) vulnerabilities."

Some of the applications that may launch a JDWP server when in debug mode include TeamCity, Jenkins, Selenium Grid, Elasticsearch, Quarkus, Spring Boot, and Apache Tomcat.

Data from [GreyNoise](https://viz.greynoise.io/tags/java-debug-wire-protocol-scanner) shows [more than 2,600 IP addresses](https://viz.greynoise.io/query/tags%3A%22Java%20Debug%20Wire%20Protocol%20Scanner%22%20last_seen%3A1d) scanning for JDWP endpoints within the last 24 hours, out of which over 1,500 IP addresses are malicious and 1,100 IP addresses are classified as suspicious. The vast majority of these IP addresses originate from China, the United States, Germany, Singapore, and Hong Kong.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPXLsYOiOsbNjEYQpKFO4WVSqf3d_BNHMC6qzR3Y4vNX4Tyz828qnbEXQZoQwsFJTmWVP6nzKjXByCCKdcutJAoFukGKjbUxOA5Ob5_O25upWPC7wqhM-m_g4dhN0uoEk1S_jqA8yLqHcb23M638RazPkkVs4uVgVmGZ5H54DvLcM16m2hjBpoCeIXblza/s790-rw-e365/wiz.png)

In the attacks observed by Wiz, threat actors take advantage of the fact that the Java Virtual Machine (JVM) listens for debugger connections on port 5005 to initiate scanning for open JDWP ports across the internet. In the next phase, a JDWP-Handshake request is sent to confirm if the interface is active and establish a JDWP session.

Once it's confirmed that the service is exposed and interactive, the attackers move to execute a curl command to fetch and execute a dropper shell script that performs a series of actions -

* Kill competing miners or any high‐CPU processes
* Drop a modified version of XMRig miner for the appropriate system architecture from an external server ("awarmcorner[.]world") into "~/.config/logrotate"
* Establish persistence by setting cron jobs to ensure that payload is re-fetched and re-executed after every shell login, reboot, or a scheduled time interval
* Delete itself on exit

"Being open-source, XMRig offers attackers the convenience of easy customization, which in this case involved stripping out all command-line parsing logic and hardcoding the configuration," Wiz said. "This tweak not only simplifies deployment but also allows the payload to mimic the original logrotate process more convincingly."

### New Hpingbot Botnet Emerges

The disclosure comes as NSFOCUS [detailed](https://nsfocusglobal.com/hpingbot-a-new-botnet-family-based-on-pastebin-payload-delivery-chain-and-hping3-ddos-module/) a new, rapidly-evolving Go-based malware named Hpingbot that's capable of targeting both Windows and Linux systems to enlist them into a botnet that can launch distributed denial-of-service (DDoS) attacks using [hping3](https://thehackernews.com/2024/12/juniper-warns-of-mirai-botnet-targeting.html), a [freely-available utility](https://www.infosectrain.com/blog/firewall-testing-with-hping3-a-comprehensive-guide/) for crafting and sending custom ICMP/TCP/UDP packets.

A notable aspect of the malware is that unlike other trojans that are typically derived from known botnet malware families like Mirai and Gafgyt, Hpingbot is an entirely new strain. At least since June 17, 2025, a few hundred DDoS instructions have been issued, with Germany, the United States, and Turkey being the main targets.

"This is a new botnet family built from scratch, showing strong innovation capabilities and efficiency in using existing resources, such as distributing loads through the online text storage and sharing platform Pastebin and launching DD...