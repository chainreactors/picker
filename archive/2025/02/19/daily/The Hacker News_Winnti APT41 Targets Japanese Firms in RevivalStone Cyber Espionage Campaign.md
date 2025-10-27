---
title: Winnti APT41 Targets Japanese Firms in RevivalStone Cyber Espionage Campaign
url: https://thehackernews.com/2025/02/winnti-apt41-targets-japanese-firms-in.html
source: The Hacker News
date: 2025-02-19
fetch_date: 2025-10-06T20:49:35.379713
---

# Winnti APT41 Targets Japanese Firms in RevivalStone Cyber Espionage Campaign

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

# [Winnti APT41 Targets Japanese Firms in RevivalStone Cyber Espionage Campaign](https://thehackernews.com/2025/02/winnti-apt41-targets-japanese-firms-in.html)

**Feb 18, 2025**Ravie LakshmananMalware / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGeWNKFsCurwnUB-hkVoPnr-j1Aihnf5o9wJ5z_uu_Yae13w4_iJM57lx7S9NysrtMbDCpgwEmy6k0ZCYl6SKGMQPQSjyKPbnY5Rma3P6aSqFzn8AJbzMHNdRJ2Upz4IZmR32cfyawvp_mHhGE-RSHrOrutruXpYnZqvuU_39N1oFb8jdMJruuHEeECCMx/s790-rw-e365/hackers.png)

The China-linked threat actor known as Winnti has been attributed to a new campaign dubbed **RevivalStone** that targeted Japanese companies in the manufacturing, materials, and energy sectors in March 2024.

The activity, [detailed](https://www.lac.co.jp/lacwatch/report/20250213_004283.html) by Japanese cybersecurity company LAC, overlaps with a threat cluster tracked by Trend Micro as [Earth Freybug](https://thehackernews.com/2024/04/china-linked-hackers-deploy-new.html), which has been assessed to be a subset within the APT41 cyber espionage group. It's also monitored by Cybereason under the name [Operation CuckooBees](https://thehackernews.com/2022/10/chinese-spyder-loader-malware-spotted.html), and by Symantec as Blackfly.

[APT41](https://thehackernews.com/2024/08/apt41-hackers-use-shadowpad-cobalt.html) has been described as a highly skilled and methodical actor with the ability to mount espionage attacks as well as poison the supply chain. Its campaigns are often designed with stealth in mind, leveraging a bevy of tactics to achieve its goals by using a custom toolset that not only bypasses security software installed in the environment, but also harvests critical information and establishes covert channels for persistent remote access.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The group's espionage activities, many of which are aligned with the nation's strategic objectives, have targeted a wide range of public and private industry sectors around the world," LAC said.

"The attacks of this threat group are characterized by the use of Winnti malware, which has a unique rootkit that allows for the hiding and manipulation of communications, as well as the use of stolen, legitimate digital certificates in the malware."

Winnti, active since at least 2012, has primarily singled out manufacturing and materials-related organizations in Asia as of 2022, with [recent campaigns](https://jsac.jpcert.or.jp/archive/2025/pdf/JSAC2025_1_2_theo-chen_leon-chang_en.pdf) between November 2023 and October 2024 targeting the Asia-Pacific (APAC) region exploiting weaknesses in public-facing applications like IBM Lotus Domino to deploy malware as follows -

* **DEATHLOTUS** - A passive CGI backdoor that supports file creation and command execution
* **UNAPIMON** - A defense evasion utility written in C++
* **PRIVATELOG** - A loader that's used to drop Winnti RAT (aka [DEPLOYLOG](https://thehackernews.com/2022/05/chinese-hackers-caught-stealing.html)) which, in turn, delivers a kernel-level rootkit named WINNKIT by means of a rootkit installer
* **CUNNINGPIGEON** - A backdoor that uses Microsoft Graph API to fetch commands – file and process management, and custom proxy – from mail messages
* **WINDJAMMER** - A rootkit with capabilities to intercept TCPIP Network Interface, as well as create covert channels with infected endpoints within intranet
* **SHADOWGAZE** - A passive backdoor reusing listening port from IIS web server

The latest attack chain documented by LAC has been found to exploit an SQL injection vulnerability in an unspecified enterprise resource planning (ERP) system to drop web shells such as China Chopper and Behinder (aka Bingxia and IceScorpion) on the compromised server, using the access to perform reconnaissance, collect credentials for lateral movement, and deliver an improved version of the Winnti malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhq232PSDETPRTr-akKDRlZArH7zjdbxkh7kIMvpgq6GZVd2Tk-AgURvqOyLaFgBjMcS05xvjqpsFClEVPwXU8Nsejxp_MhyphenhyphenLrbuoLG-ERJ9l46vxk3ieeZJ7U8mcvdcrW0Qk8bRid2FTzVzo5H3XRn5pnpnIaZVY3JDOtJnKdmQDw4oAp2IzoeKsqneJFD/s790-rw-e365/malware.png)

The intrusion's reach is said to have been expanded further to breach a managed service provider (MSP) by leveraging a shared account, followed by weaponizing the company's infrastructure to propagate the malware further to three other organizations.

LAC said it also found references to [TreadStone](https://thehackernews.com/2020/09/apt41-hackers-wanted-by-fbi.html) and StoneV5 in the RevivalStone campaign, with the former being a controller that's designed to work with the Winnti malware and which was also [included](https://thehackernews.com/2024/03/two-chinese-apt-groups-ramp-up-cyber.html) in the [I-Soon (aka Anxun) leak](https://unit42.paloaltonetworks.com/i-soon-data-leaks/) of [last year](https://www.kelacyber.com/blog/i-soon-leak-kelas-insights/) in connection with a Linux malware control panel.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"If TreadStone has the same meaning as the Winnti malware, it is only speculation, but StoneV5 could also mean Version 5, and it is possible that the malware used in this attack is Winnti v5.0," researchers Takuma Matsumoto and Yoshihiro Ishikawa said.

"The new Winnti malware has been implemented with features such as obfuscation, updated encryption algorithms, and evasion by security products, and it is likely that this attacker group will continue to update the functions of the Winnti malware and use it in attacks."

The disclosure comes as Fortinet FortiGuard Labs [detailed](https://www.fortinet.com/blog/threat-research/analyzing-elf-sshdinjector-with-a-human-and-artificial-analyst) a Linux-based attack suite dubbed SSHDInjector that's equipped to hijack the SSH daemon on network appliances by injecting malware into the process for ...