---
title: New 'Helldown' Ransomware Variant Expands Attacks to VMware and Linux Systems
url: https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html
source: The Hacker News
date: 2024-11-20
fetch_date: 2025-10-06T19:23:42.397380
---

# New 'Helldown' Ransomware Variant Expands Attacks to VMware and Linux Systems

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

# [New 'Helldown' Ransomware Variant Expands Attacks to VMware and Linux Systems](https://thehackernews.com/2024/11/new-helldown-ransomware-expands-attacks.html)

**Nov 19, 2024**Ravie LakshmananRansomware / Linux

[![Ransomware attacks on VMware and Linux Systems](data:image/png;base64... "Ransomware attacks on VMware and Linux Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgE8xphOWedh16gVwUQlz12GBrZcmTrsitwHU6UUDeoshoSMSKB5W_YTFz7uMY6TiplJwG0CNwYkbIR0Pnwoh0dFtNcZO53yt9IPB8fyLEnVOnOuGzzWztAZ0c8oqmLB22b1iIIRDMEePEChwGsMSj1DNwOzHCXj_2CWaBwwai6Pzzwymh_oMRPN7xnMe7b/s790-rw-e365/locker.png)

Cybersecurity researchers have shed light on a Linux variant of a relatively new ransomware strain called Helldown, suggesting that the threat actors are broadening their attack focus.

"Helldown deploys Windows ransomware derived from the LockBit 3.0 code," Sekoia [said](https://blog.sekoia.io/helldown-ransomware-an-overview-of-this-emerging-threat/) in a report shared with The Hacker News. "Given the recent development of ransomware targeting ESX, it appears that the group could be evolving its current operations to target virtualized infrastructures via VMware."

Helldown was [first publicly documented](https://ransomwareattacks.halcyon.ai/attacks/helldown-ransomware-hits-vindix-23-gb-data-breach-analysis) by Halcyon in mid-August 2024, [describing](https://ransomwareattacks.halcyon.ai/news/ransomware-on-the-move-bianlian-helldown-meow-and-ransomhub) it as an "aggressive ransomware group" that [infiltrates](https://www.cyfirma.com/research/tracking-ransomware-august-2024/) target networks by exploiting security vulnerabilities. Some of the prominent sectors targeted by the cybercrime group include IT services, telecommunications, manufacturing, and healthcare.

Like other ransomware crews, Helldown is [known](https://cyberint.com/blog/research/ransomware-trends-2024-report/) for leveraging data leak sites to pressure victims into paying ransoms by threatening to publish stolen data, a tactic known as double extortion. It's estimated to have attacked at least 31 companies within a span of three months.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Truesec, in an [analysis](https://www.truesec.com/hub/blog/helldown-ransomware-group) published earlier this month, detailed Helldown attack chains that have been observed making use of internet-facing Zyxel firewalls to obtain initial access, followed by carrying out persistence, credential harvesting, network enumeration, defense evasion, and lateral movement activities to ultimately deploy the ransomware.

Sekoia's new analysis shows that the attackers are abusing known and unknown security flaws in Zyxel appliances to breach networks, using the foothold to [steal credentials and create SSL VPN tunnels](https://support.zyxel.eu/hc/en-us/articles/21878875707410-Zyxel-USG-FLEX-and-ATP-series-Upgrading-your-device-and-ALL-credentials-to-avoid-hackers-attacks) with temporary users.

The Windows version of Helldown, once launched, performs a series of steps prior to exfiltrating and encrypting the files, including deleting system shadow copies and terminating various processes related to databases and Microsoft Office. In the final step, the ransomware binary is deleted to cover up the tracks, a ransom note is dropped, and the machine is shut down.

Its Linux counterpart, per the French cybersecurity company, lacks obfuscation and anti-debugging mechanisms, while incorporating a concise set of functions to search and encrypt files, but not before listing and killing all active virtual machines (VMs).

"The static and dynamic analysis revealed no network communication, nor any public key or shared secret," it said. "This is notable, as it raises questions about how the attacker would be able to supply a decryption tool."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqj35ldl_SGonXi9pjT19xSgegrHEZfrLDihn3lU6SHgl_exxdVEoM5wbvmzgfg0mJ3cDlxQ1pVcPFOGPcyQOlrC-fuvhDMHRps4aANmK9K9v7sMVBCEq9xFzSep5yNCqsJwRX2tzmU4nilorsu5cKCm3qpZzUEotkiNR-MDJz8uyv9B4Ybs8XEGDHDDBU/s790-rw-e365/ransomware.png)

"Terminating VMs before encryption grants ransomware write access to image files. However, both static and dynamic analysis reveal that, while this functionality exists in the code, it is not actually invoked. All these observations suggest that the ransomware is not highly sophisticated and may still be under development."

Helldown Windows artifacts have been found to share behavioral similarities with DarkRace, which emerged in May 2023 using code from LockBit 3.0 and later rebranded to [DoNex](https://thehackernews.com/2024/07/new-ransomware-as-service-eldorado.html). A decryptor for DoNex was made available by Avast back in July 2024.

"Both codes are variants of LockBit 3.0," Sekoia said. "Given Darkrace and Donex's history of rebranding and their significant similarities to Helldown, the possibility of Helldown being another rebrand cannot be dismissed. However, this connection cannot be definitively confirmed at this stage."

The development comes as Cisco Talos disclosed another emerging ransomware family known as Interlock that has singled out healthcare, technology, and government sectors in the U.S., and manufacturing entities in Europe. It's capable of encrypting both Windows and Linux machines.

Attack chains distributing the ransomware have been observed using a fake Google Chrome browser updater binary hosted on a legitimate-but-compromised news website that, when run, unleashes a remote access trojan (RAT) that allows the attackers to extract sensitive data and execute PowerShell commands designed to drop payloads for harvesting credentials and conducting reconnaissance.

"In their blog, Interlock claims to target organizations' infrastructure by exploiting unaddressed vulnerabilities and claims their actions are in part motivated by a desire to hold companies' accountable for poor cyber...