---
title: Iran-Linked Hackers Disrupt U.S. Critical Infrastructure by Targeting Internet-Exposed PLCs
url: https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html
source: The Hacker News
date: 2026-04-08
fetch_date: 2026-04-09T04:32:34.714976
---

# Iran-Linked Hackers Disrupt U.S. Critical Infrastructure by Targeting Internet-Exposed PLCs

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Iran-Linked Hackers Disrupt U.S. Critical Infrastructure by Targeting Internet-Exposed PLCs](https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html)

**Ravie Lakshmanan**Apr 08, 2026Malware / Operational Technology

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBiMBUkucAS1NG7NHlk46hGqNyjv5iU5w1Z6HVNXgQywcDfTSOdtQWSqYA5ccSojgRB45ScYHFfyPWqe_9QbOZYo6u6V5qUAcRQIm4CfIDvkRqhs7rtPhmD7yNR4bn_StYbNZm2UWqXfeqXCUeDL1eneK7VyGnHfGbk3EatILzs_fKtRN6VxF8vnKDgQL_/s1700-e365/plc.jpg)

Iran-affiliated cyber actors are targeting internet-facing operational technology (OT) devices across critical infrastructures in the U.S., including programmable logic controllers (PLCs), cybersecurity and intelligence agencies [warned](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) Tuesday.

"These attacks have led to diminished PLC functionality, manipulation of display data and, in some cases, operational disruption and financial loss," the U.S. Federal Bureau of Investigation (FBI) [said](https://x.com/FBICyberDiv/status/2041566548691660897) in a post on X.

The agencies said the [campaign](https://thehackernews.com/2025/06/us-agencies-warn-of-rising-iranian.html) is part of a [recent escalation](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html) in cyber attacks orchestrated by Iranian hacking groups against U.S. organizations in response to the ongoing conflict between Iran, and the U.S. and Israel.

Specifically, the activity has led to PLC disruptions across several U.S. critical infrastructure sectors via what the authoring agencies described as malicious interactions with the project file and manipulation of data on human-machine interface (HMI) and supervisory control and data acquisition (SCADA) displays.

These attacks have singled out Rockwell Automation and Allen-Bradley PLCs deployed in government services and facilities, Water and Wastewater Systems (WWS), and energy sectors.

"The actors used leased, third-party hosted infrastructure with configuration software, such as Rockwell Automation's Studio 5000 Logix Designer software, to create an accepted connection to the victim's PLC," the advisory said. "Targeted devices include CompactLogix and Micro850 PLC devices."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

Upon obtaining initial access, the threat actors established command-and-control by deploying Dropbear, a Secure Shell (SSH) software, on victim endpoints to enable remote access through port 22 and facilitate the extraction of the device's project file and data manipulation on HMI and SCADA displays.

To combat the threat, organizations are advised to avoid exposing the PLC to the internet, take steps to prevent remote modification either via a physical or software switch, implement multi-factor authentication (MFA), and erect a firewall or network proxy in front of the PLC to control network access, keep PLC devices up-to-date, disable any unused authentication features, and monitor for unusual traffic.

This is not the first time Iranian threat actors have targeted OT networks and PLCs. In late 2023, Cyber Av3ngers (aka Hydro Kitten, Shahid Kaveh Group, and UNC5691) was [linked](https://thehackernews.com/2023/11/iranian-hackers-exploit-plcs-in-attack.html) to the active exploitation of Unitronics PLCs to target the Municipal Water Authority of Aliquippa in western Pennsylvania. These attacks compromised at least 75 devices.

"This advisory confirms what we've observed for months: Iran's cyber escalation follows a known playbook. Iranian threat actors are now moving faster and broader and targeting both IT and OT infrastructure," Sergey Shykevich, threat intelligence group manager at Check Point Research, said in a statement shared with The Hacker News.

"We documented identical targeting patterns against Israeli PLCs in March. It is not the first time Iranian actors are targeting operational technology in the US for disruption purposes, so organizations shouldn't treat this as a new threat, but as an accelerating one."

The development comes amid a [new-found surge](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html) in distributed denial-of-service (DDoS) attacks and claims of hack-and-leak operations carried out by cyber proxy groups and hacktivists targeting Western and Israeli entities, according to Flashpoint.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7W8LInOXE8F6a39wHidYzWarzH9aT7ltfdTqpH6RI8JFyh2jkWqjC8KhMKTNvPSVRJBsFH9o8y3qALMSp-MW7mreghnyK2sHefLpVni6QJR8DGUidJSgec1S-qXIwBep3zMo4IOJ_osMGniqWhlINxNUt-ZR1_MNBONUxWD6aRLYqytsIv6wt8KLcctbO/s1700-e365/Telegram.png)

In a report published this week, DomainTools Investigations (DTI) described activity attributed to Homeland Justice, Karma/KarmaBelow80, and Handala Hack as a "single, coordinated cyber influence ecosystem" aligned with Iran's Ministry of Intelligence and Security (MOIS) rather than a set of distinct hacktivist groups.

"These personas function as interchangeable operational veneers applied to a consistent underlying capability," DTI [said](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment). "Their purpose is not to reflect organizational separation, but to enable segmentation of messaging, targeting, and attribution while preserving continuity of infrastructure and tradecraft."

Public-facing domains and Telegram channels serve as the primary dissemination and amplification hub, with the messaging platform also playing a huge role in command-and-control (C2) operations by allowing the malware to communicate with threat actor-controlled bots, reduce infrastructure overhead, and blend in with normal operations.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

"This ecosystem repr...