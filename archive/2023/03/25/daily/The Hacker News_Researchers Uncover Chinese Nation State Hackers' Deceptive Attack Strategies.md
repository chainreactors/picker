---
title: Researchers Uncover Chinese Nation State Hackers' Deceptive Attack Strategies
url: https://thehackernews.com/2023/03/researchers-uncover-chinese-nation.html
source: The Hacker News
date: 2023-03-25
fetch_date: 2025-10-04T10:40:21.211122
---

# Researchers Uncover Chinese Nation State Hackers' Deceptive Attack Strategies

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

# [Researchers Uncover Chinese Nation State Hackers' Deceptive Attack Strategies](https://thehackernews.com/2023/03/researchers-uncover-chinese-nation.html)

**Mar 24, 2023**Ravie LakshmananCyber Attack / Hacking

[![Chinese Nation State Hackers](data:image/png;base64... "Chinese Nation State Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSQngWvILLQHwNuuBJ0WJzUo-5Icthqaq-uzbcLqbzOhHYIMHmDxsxrXJGRQ5mYKoeRbkJhL0AlVtcWS-rmOi8lCZjSVVenyoXZUotRSkCwmIzCUHg328oqhF3N7LpQ15DB59hq0jfkFr5igQLK-6owMU1uU0FKNplS7avN1d9ETL9-EZLVICfAATF/s790-rw-e365/chinese-hackers.png)

A recent campaign undertaken by **Earth Preta** indicates that nation-state groups aligned with China are getting increasingly proficient at bypassing security solutions.

The [threat actor](https://thehackernews.com/2022/12/chinese-hackers-using-russo-ukrainian.html), active since at least 2012, is tracked by the broader cybersecurity community under Bronze President, HoneyMyte, Mustang Panda, RedDelta, and Red Lich.

Attack chains mounted by the group commence with a spear-phishing email to deploy a wide range of tools for backdoor access, command-and-control (C2), and data exfiltration.

These messages come bearing with malicious lure archives distributed via Dropbox or Google Drive links that employ DLL side-loading, LNK shortcut files, and fake file extensions as arrival vectors to obtain a foothold and drop backdoors like [TONEINS, TONESHELL, PUBLOAD](https://thehackernews.com/2022/11/chinese-mustang-panda-hackers-actively.html), and [MQsTTang](https://thehackernews.com/2023/03/chinese-hackers-targeting-european.html) (aka QMAGENT).

Similar infection chains utilizing Google Drive links have been observed [delivering Cobalt Strike](https://twitter.com/h2jazi/status/1379816750120861697) as early as April 2021.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Earth Preta tends to hide malicious payloads in fake files, disguising them as legitimate ones — a technique that has been proven effective for avoiding detection," Trend Micro [said](https://www.trendmicro.com/en_us/research/23/c/earth-preta-updated-stealthy-strategies.html) in a new analysis published Thursday.

This entry point method, which was first spotted late last year, has since received a slight tweak wherein the download link to the archive is embedded within another decoy document and the file is password-protected in an attempt to sidestep email gateway solutions.

[![Nation State Hackers](data:image/png;base64... "Nation State Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFCTA7fDE00_Lok6G2PvK0iYOoWnvz8EvnUcA3WZEivBcr_Ghv17W6r2RdDCHXOKHMRLkeg3Z7BcmEfrtopkAlj4SJ_2q0ZdKtXJLRgCYCGJOoP9oG5-9prxJQ3HFDwpmM7FNOjmaJUiWh1m9zG_zAyXq92BpYgQU0xlwDJ4WJ8q_T8gCbSMwrU8E5uA/s790-rw-e365/hack.png)

"The files can then be extracted inside via the password provided in the document," the researchers said. "By using this technique, the malicious actor behind the attack can successfully bypass scanning services."

Initial access to the victim's environment is followed by [account discovery](https://attack.mitre.org/techniques/T1087/) and privilege escalation phases, with Mustang Panda leveraging custom tools like ABPASS and CCPASS to [circumvent](https://www.elastic.co/security-labs/exploring-windows-uac-bypasses-techniques-and-detection-strategies) User Account Control ([UAC](https://attack.mitre.org/techniques/T1548/002/)) in Windows 10.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjpGD942Jd6B_t_fjid5W6JBB7bOkWEoFJPBAuLPg0tZyKrTvxhXCOee4EeY18OQWhScc__y6LqyhHaW2sa2ZESKHOukX7erLD-zxd_0-pAc4Ekmo2x3KPBZ2IX_AT9BFGB6WX7LwyDNGh3EhkDJTGtZnodl_I6-IWT4cTYh43owUHuhR7JbtmS23fg/s790-rw-e365/trend.png)

Additionally, the threat actor has been observed deploying malware such as "USB Driver.exe" (HIUPAN or [MISTCLOAK](https://thehackernews.com/2022/11/chinese-cyber-espionage-hackers-using.html)) and "rzlog4cpp.dll" ([ACNSHELL](https://news.sophos.com/en-us/2022/11/03/family-tree-dll-sideloading-cases-may-be-related/) or [BLUEHAZE](https://thehackernews.com/2022/11/chinese-cyber-espionage-hackers-using.html)) to install themselves to removable disks and create a [reverse shell](https://www.imperva.com/learn/application-security/reverse-shell/) with the goal of laterally moving across the network.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Other utilities deployed include CLEXEC, a backdoor capable of executing commands and clearing event logs; COOLCLIENT and TROCLIENT, implants that are designed to record keystrokes as well as read and delete files; and [PlugX](https://thehackernews.com/2023/03/hackers-exploiting-remote-desktop.html).

[![Deceptive Cyberattack Strategies](data:image/png;base64... "Deceptive Cyberattack Strategies")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhOGV_u3PAAdozWbjWpKkvreZ6FjLWtMLPKdCqXW9nTe3dOtnAQ2JmbfyJ7odls7rB08gXOCgB4gXwSIYpzejrNCkrsAPP_7xsxC4MfIRRQkzoDdRrwjE0RBIPBbtw0ISZKW_0gXJ2W_JsgBJbR-E5DeU8undJGqxd00lMSUMQHnjmGLpnu-u6tycx_/s790-rw-e365/exe.png)

"Apart from well-known legitimate tools, the threat actors also crafted highly customized tools used for exfiltration," the researchers noted. This comprises NUPAKAGE and ZPAKAGE, both of which are equipped to collect Microsoft Office files.

The findings once again highlight the increased operational tempo of Chinese cyber espionage actors and their consistent investment in advancing their cyber weaponry to evade detection.

"Earth Preta is a capable and organized threat actor that is continuously honing its TTPs, strengthening its development capabilities, and building a versatile arsenal of tools and malware," the researchers concluded.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [Linke...