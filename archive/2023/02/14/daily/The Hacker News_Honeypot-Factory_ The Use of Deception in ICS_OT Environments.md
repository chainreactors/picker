---
title: Honeypot-Factory: The Use of Deception in ICS/OT Environments
url: https://thehackernews.com/2023/02/honeypot-factory-use-of-deception-in.html
source: The Hacker News
date: 2023-02-14
fetch_date: 2025-10-04T06:33:40.705738
---

# Honeypot-Factory: The Use of Deception in ICS/OT Environments

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

# [Honeypot-Factory: The Use of Deception in ICS/OT Environments](https://thehackernews.com/2023/02/honeypot-factory-use-of-deception-in.html)

**Feb 13, 2023**The Hacker NewsOT and ICS Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheTRuXLR34T447pGZgFN03OQ3Pvb84nZ4wJp_h5CEIym_-G6KLf9Ccdeo9MKymjR45aQn2yJ7IBhOUm68M4SmRblEV_Eb2MvfK7_CUfV7hmiKqsq_AASN18oR1BUBXANissOVj325bWQFGXLvCg2ay_mVQPHNqocNU7xnTZ0350xyeyJgsF5vSQB5m/s790-rw-e365/orange.png)

The recently published [Security Navigator](https://www.orangecyberdefense.com/global/security-navigator?utm_source=hackernews&utm_medium=media&utm_campaign=sn2023) report of Orange Cyberdefense shows there has been a rapid increase of attacks on industrial control systems (ICS) in the past few years. Looking a bit closer, most of the attacks seem to have spilt over from traditional IT. That's to be expected, as production systems are commonly connected to ordinary corporate networks at this point.

Though the data does not indicate at this point that a lot of threat actors specifically target industrial systems – in fact, most evidence points to purely opportunistic behaviour – the tide could turn any time, once the added complexity of compromising OT environments promises to pay off. Criminals will take any chance they get to blackmail victims into extortion schemes, and halting production can cause immense damage. It is likely only a matter of time. So cybersecurity for operational technology (OT) is vitally important.

Deception is an effective option to improve threat detection and response capabilities. However, ICS security differs from traditional IT security in several ways. While deception technology for defensive use like honeypots has progressed, there are still challenges due to fundamental differences like the protocols used. This article is intended to detail the progress and challenges when deception technology transits from traditional IT to ICS security.

## **The value of deception: taking back the initiative**

Deception technology is an active security defense method that detects malicious activities effectively. On the one hand, this strategy constructs an environment of false information and simulations to mislead an adversary's judgment, making unsuspecting attackers fall into a trap to waste their time and energy, increasing the complexity and uncertainty of the intrusion.

At the same time, the defenders can collect more comprehensive attack logs, deploy countermeasures, trace the source of attackers and monitor their attack behaviors. Recording everything to research the tactics, techniques, and procedures (TTP) an attacker uses is of great help for the security analysts. Deception techniques can give defenders back the initiative.

Discover the latest in cybersecurity with comprehensive "**[Security Navigator 2023](https://www.orangecyberdefense.com/global/security-navigator?utm_source=hackernews&utm_medium=media&utm_campaign=sn2023)**" report. This research-driven report is based on 100% first-hand information from 17 global SOCs and 13 CyberSOCs of Orange Cyberdefense, the CERT, Epidemiology Labs and World Watch and provides a wealth of valuable information and insights into the current and future threat landscape.

With some deception applications, for instance honeypots, the operating environment and configuration can be simulated, thus luring the attacker to penetrate the fake target. By this means, defenders will be able to grab the payloads the attackers drop and get information about the attacker's hosts or even web browser by JavaScript in web applications. What's more, it is possible to know the attacker's social media accounts by JSONP Hijacking as well as countering the attacker through 'honey files.' It can be predicted that deception technology will be more mature and widely used in the coming years.

Recently, the integration of information technology and industrial production has been accelerating with the rapid development of the Industrial Internet and intelligent manufacturing. The connection of massive industrial networks and equipment to IT technology will inevitably lead to increasing security risks in this field.

## **Production at risk**

Frequent security incidents such as ransomware, data breaches, and advanced persistent threats seriously affect industrial enterprises' production and business operations and threaten the digital society's security. Generally, these systems are prone to be weak and exploited easily by the attacker due to their simple architecture, which uses low processing power and memory. It is challenging to protect ICS from malicious activities as the components of ICS are unlikely to take any updates or patches due to their simple architecture. Installing endpoint protection agents is usually not possible either. Considering these challenges, deception can be an essential part of the security approach.

* **Conpot** is an open-source low-interactive honeypot that supports various industrial protocols, including IEC 60870-5-104, Building Automation and Control Network (BACnet), Modbus, s7comm, and other protocols such as HTTP, SNMP and TFTP. It is designed to be easy to deploy, modify and extend. The Conpot and Conpot-based honeypot are among the most popular ICS deception applications that have been used by researchers.

* **XPOT** is a software-based high-interactive PLC honeypot which can run programs. It simulates Siemens S7-300 series PLCs and allows the attacker to compile, interpret and load PLC programs onto XPOT. XPOT supports S7comm and SNMP protocols and is the first high-interactive PLC honeypot. Since it is software-based, it is very scalable and enables large decoy or sensor networks. XPOT can be connected to a simulated industrial process in order to make adversaries' experiences comprehensive.

* **CryPLH** is a high-interactive and virtual Smart-Grid ICS honeypot simulating Siemens Simatic S7-300 PLC. It runs on a Linux-based host and uses MiniWe...