---
title: China-Backed Hackers Leverage SIGTRAN, GSM Protocols to Infiltrate Telecom Networks
url: https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html
source: The Hacker News
date: 2024-11-21
fetch_date: 2025-10-06T19:17:46.104927
---

# China-Backed Hackers Leverage SIGTRAN, GSM Protocols to Infiltrate Telecom Networks

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

# [China-Backed Hackers Leverage SIGTRAN, GSM Protocols to Infiltrate Telecom Networks](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html)

**Nov 20, 2024**Ravie LakshmananCyber Espionage / Telecom Security

[![Hacking Telecom Networks](data:image/png;base64... "Hacking Telecom Networks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1_A6A_kZ_Y1erxy64FvDxGHfrjx5qK55BKnuKq9aU9eCPY_CqFK15LH6iCY4Q5WgRvWheEtn-3WgaAdWP6Y2_8w8_lbEZT3APIwaFf4mUowEePU6Mq7C5g9w0_8AzcB8xvmqsg67oFcAUyKdR7pBBHC2NxldwrGmS4Xuw7MmzJJx0ChmRlTMKPEBwuf5G/s790-rw-e365/telecom.png)

A new China-linked cyber espionage group has been attributed as behind a series of targeted cyber attacks targeting telecommunications entities in South Asia and Africa since at least 2020 with the goal of enabling intelligence collection.

Cybersecurity company CrowdStrike is tracking the adversary under the name **Liminal Panda**, describing it as possessing deep knowledge about telecommunications networks, the protocols that undergird telecommunications, and the various interconnections between providers.

The threat actor's malware portfolio includes bespoke tools that facilitate clandestine access, command-and-control (C2), and data exfiltration.

"Liminal Panda has used compromised telecom servers to initiate intrusions into further providers in other geographic regions," the company's Counter Adversary Operations team [said](https://www.crowdstrike.com/en-us/blog/liminal-panda-telecom-sector-threats/) in a Tuesday analysis.

"The adversary conducts elements of their intrusion activity using protocols that support mobile telecommunications, such as emulating global system for mobile communications (GSM) protocols to enable C2, and developing tooling to retrieve mobile subscriber information, call metadata, and text messages (SMS)."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Adam Meyers, head of Counter Adversary Operations at CrowdStrike, told The Hacker News that 15 of the 63 China-based adversaries it monitors have targeted telecommunications entities in recent months.

"The adversary demonstrates extensive knowledge of telecommunications networks, including interconnections between providers and the protocols that support mobile telecommunications," Meyers said. "This problem is extremely widespread and affects providers globally. While CrowdStrike has observed Liminal Panda targeting telcos in Southeast Asia and Africa, compromised infrastructure enables them to move laterally between providers across regions."

It's worth noting that some aspects of the intrusion activity were [documented](https://thehackernews.com/2021/10/lightbasin-hackers-breach-at-least-13.html) by the cybersecurity company back in October 2021, attributing it then to a different threat cluster dubbed LightBasin (aka UNC1945), which also has a track record of targeting telecom entities since at least 2016.

CrowdStrike noted that its extensive review of the campaign revealed the presence of an entirely new threat actor, and that the misattribution three years ago was the result of multiple hacking crews conducting their malicious activities on what it said was a "highly contested compromised network."

Some of the custom tools in its arsenal are SIGTRANslator, CordScan, and PingPong, which come with the following capabilities -

* SIGTRANslator, a Linux ELF binary designed to send and receive data using SIGTRAN protocols
* CordScan, a network-scanning and packet-capture utility containing built-in logic to fingerprint and retrieve data relating to common telecommunication protocols from infrastructure such as the Serving GPRS Support Node (SGSN)
* PingPong, a backdoor that listens for incoming magic ICMP echo requests and sets up a TCP reverse shell connection to an IP address and port specified within the packet

Liminal Panda attacks have been observed infiltrating external DNS (eDNS) servers using password spraying extremely weak and third-party-focused passwords, with the hacking crew using TinyShell in conjunction with a publicly available SGSN emulator called [sgsnemu](https://github.com/osmocom/osmo-ggsn) for C2 communications.

"TinyShell is an open-source Unix backdoor used by multiple adversaries," CrowdStrike said. "SGSNs are essentially GPRS network access points, and the emulation software allows the adversary to tunnel traffic via this telecommunications network."

The end goal of these attacks is to collect network telemetry and subscriber information or to breach other telecommunications entities by taking advantage of the industry's interoperation connection requirements.

"Liminal Panda's known intrusion activity has typically abused trust relationships between telecommunications providers and gaps in security policies, allowing the adversary to access core infrastructure from external hosts," the company said.

The disclosure comes as U.S. telecom providers like AT&T, Verizon, T-Mobile, and Lumen Technologies have become the target of another China-nexus hacking group dubbed [Salt Typhoon](https://thehackernews.com/2024/11/chinese-hackers-exploit-t-mobile-and.html). If anything, these incidents serve to highlight how telecommunications and other critical infrastructure providers are vulnerable to compromise by state-sponsored attackers.

French cybersecurity company Sekoia has characterized the Chinese offensive cyber ecosystem as a joint enterprise that includes government-backed units such as the Ministry of State Security (MSS) and the Ministry of Public Security (MPS), civilian actors, and private entities to whom the work of vulnerability research and toolset development is outsourced.

"China-nexus APTs are likely to be a mix of private and state actors cooperating to conduct operations, rather than strictly being associated with single units," it [said](https://blog.sekoia.io/a-three-beats-waltz-the-ecosystem-behind-chinese-state-sponsored-cyber-threats/), pointing out the challenge...