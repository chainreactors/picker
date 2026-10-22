---
title: Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion
url: https://thehackernews.com/2026/10/hackers-hid-vasilek-backdoor-in-vmware.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:44.887073
---

# Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Hackers Hid Vasilek Backdoor in VMware Tools During 2-Year Russian Healthcare Intrusion](https://thehackernews.com/2026/10/hackers-hid-vasilek-backdoor-in-vmware.html)

**Ravie Lakshmanan**Oct 21, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwNHgVe_6hmXG-V6Nx8pk56jDEW1WRCKtvvG9RHugoj65LqTTVGLvgl1Eh1E7ClmyMDn9k4RrF7Yp1kteZvZ_r7v9IxQPG_Eif3nk_13gz_MSddPcBtJdLKFwYAPa4BKMN5FdZLvvTIjahr4aTdiiLeQMuVzrj8Ff9wvgmUCW_6_OyfXPSGIEEIxZgdtQ-/s1700-nu-rw-lo-l85-e365/vmware-healthcare.jpg)

A Belarus-aligned hacktivist group spent nearly two years within the network of a Russian healthcare organization.

According to a report [published](https://rt-solar.ru/solar-4rays/blog/7027/) by Russian cybersecurity firm Solar, the activity has been attributed to a threat cluster dubbed **Partisan Zmiy**, which is also known as the **Cyber Partisans**.

Known to be active since at least 2020, the group has a [track record](https://thehackernews.com/2025/06/weekly-recap-iphone-spyware-microsoft-0.html#:~:text=Cyber%20Partisans%20Targets%20Belarus%20and%20Russia) of striking industrial enterprises and government agencies in Russia and Belarus with a backdoor called Vasilek that uses Telegram for command-and-control (C2) and data exfiltration.

Some of the attacks have also leveraged phishing lures to deliver an installer that simultaneously deploys the legitimate FortiClient VPN program on the system as well as an open-source program known as [DNSCat2](https://github.com/iagox86/dnscat2) that allows attackers to gain control of the infected host.

A notable aspect of the threat actor is their ability to stage [destructive attacks](https://en.iz.ru/en/2037876/iana-shturma/systemic-position-which-targets-were-chosen-politically-motivated-hackers-russia) with a wiper referred to as Pryanik, alongside taking steps to systematically clear Windows event logs using a utility dubbed Evlx.

The Rostelecom subsidiary said it discovered the intrusion in December 2025, although evidence suggests that the earliest signs of compromise date back to early 2024. The name of the targeted organization was not identified. The exact initial access vector used to breach the entity is also not known.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

Unlike other attacks linked to Cyber Partisans, the threat actors remained on the network for an extended period of time without carrying out any destructive activity, marking something of a shift in modus operandi.

"The attacked organization possessed an extensive infrastructure and two-way trusted relationships with numerous subsidiary medical institutions," Solar said. "We hypothesize that the lack of infrastructure disruption is due precisely to the value of this access for further espionage and trusted relationship attacks."

Observed as part of the intrusion is a loader-scheduler service ("vmauad") that masquerades as a legitimate VMware component to maintain persistence and evade cursory inspection. To accomplish this, the attackers are said to have taken advantage of a trusted-but-unmonitored VMware Tools directory location to plant malicious executables or replace legitimate VMware DLLs with a malicious version ("[vmtools.dll](https://hijacklibs.net/entries/3rd_party/vmware/vmtools.html)") containing the backdoor.

The primary responsibility of the Windows service is to launch the rogue binary "C:\Program Files\VMware\VMware Tools\authd.exe" that, besides launching a [GOST tunnel](https://gost.run/en/) every Saturday from 10 p.m. to 11 p.m., runs an updated version of Vasilek (version 1.5.8) once, eight hours after the service begins.

Once installed, Vasilek is equipped to collect information about an infected computer, execute Windows commands, launch and terminate processes, transfer files, capture screenshots, record keystrokes, and escalate privileges via [runas](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771525%28v%3Dws.11%29). It can also prevent the machine from going into sleep mode, and update or remove itself.

One new addition is the "move\_cursor" command that, as the name implies, allows the backdoor to move the cursor and simulate user input on the victim's screen.

"The group consistently invests in stealth and operational security, rather than new capabilities: hostname binding in two independent components, nightly scheduled payload launches, system proxy inheritance, disguise as legitimately installed but unused software, file rotation across the same paths, time-stomping, outgoing message suppression, and anonymous messages on behalf of the group in operator chats," Solar said.

"The backdoor's feature set has remained largely unchanged over four revisions. Due to Telegram being blocked in Russia by ISPs, communication between the Vasilek backdoor and C2 has become unstable."

The disclosure comes as Solar also disclosed details of a phishing campaign that employs JavaScript attachments mimicking business-themed documents, such as payments and purchase orders, to deliver a previously unreported malware family known as [HypeAgent](https://rt-solar.ru/solar-4rays/blog/7135/).

The Windows malware is a full-featured trojan designed to take complete control over infected systems, packing the ability to steal files, open a console, change desktop wallpaper, turn on a webcam, log keystrokes, launch [hidden VNC](https://attack.mitre.org/techniques/T1564/003/) and RDP sessions, control the mouse, and even deploy a cryptocurrency miner.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

It's also capable of stealing cookies associated with Discord, Steam, GitHub, Instagram, Telegram, Binance, ChatGPT, Claude, and Cursor, and tampering with the installed Exodus wallet app to inject JavaScript that can collect the victim's password, PIN, mnemonic phr...