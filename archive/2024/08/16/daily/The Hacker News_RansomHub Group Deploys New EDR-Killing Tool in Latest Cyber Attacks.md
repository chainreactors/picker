---
title: RansomHub Group Deploys New EDR-Killing Tool in Latest Cyber Attacks
url: https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html
source: The Hacker News
date: 2024-08-16
fetch_date: 2025-10-06T18:07:06.337319
---

# RansomHub Group Deploys New EDR-Killing Tool in Latest Cyber Attacks

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

# [RansomHub Group Deploys New EDR-Killing Tool in Latest Cyber Attacks](https://thehackernews.com/2024/08/ransomhub-group-deploys-new-edr-killing.html)

**Aug 15, 2024**Ravie LakshmananRansomware / Cybercrime

[![EDR-Killing Tool](data:image/png;base64... "EDR-Killing Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmkvMRdgdYiNd3kiBTIudu8V7y7qV9U5XWyS55nMHJ_6vgBTmtK-ohlr3btHImwtMLV4RFWLfXxn4iJeiSf39bnoUa8BYYU2ULw1L0PsStsEuaPpwhpNSsEBe1vQJI8iAUjxsSaX_A1GM0Z-QXqGwrWlSwCEGJaig4PCAouAoH98GCJseBu4DNshnZr6Fk/s790-rw-e365/edr-killer.png)

A cybercrime group with links to the RansomHub ransomware has been observed using a new tool designed to terminate endpoint detection and response (EDR) software on compromised hosts, joining the likes of other similar programs like [AuKill](https://thehackernews.com/2024/07/fin7-group-advertises-security.html) (aka AvNeutralizer) and [Terminator](https://thehackernews.com/2024/03/teamcity-flaw-leads-to-surge-in.html).

The EDR-killing utility has been dubbed EDRKillShifter by cybersecurity company Sophos, which discovered the tool in connection with a failed ransomware attack in May 2024.

"The EDRKillShifter tool is a 'loader' executable – a delivery mechanism for a legitimate driver that is vulnerable to abuse (also known as a 'bring your own vulnerable driver,' or [BYOVD](https://www.securityjoes.com/post/security-s-achilles-heel-vulnerable-drivers-on-the-prowl), tool)," security researcher Andreas Klopsch [said](https://news.sophos.com/en-us/2024/08/14/edr-kill-shifter/). "Depending on the threat actor's requirements, it can deliver a variety of different driver payloads."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[RansomHub](https://thehackernews.com/2024/06/rebranded-knight-ransomware-targeting.html), a suspected rebrand of the Knight ransomware, surfaced in February 2024, leveraging known security flaws to obtain initial access and drop legitimate remote desktop software such as Atera and Splashtop for persistent access.

Last month, Microsoft [revealed](https://thehackernews.com/2024/07/scattered-spider-adopts-ransomhub-and.html) that the notorious e-crime syndicate known as Scattered Spider has incorporated ransomware strains such as RansomHub and Qilin into its arsenal.

[![EDR-Killing Tool](data:image/png;base64... "EDR-Killing Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZNPBArtbrITFjjp1s27QI6nuUJDcLwzJhEtOL7i9sbViY9ni9oehpZmNKMHtTSTj2522dCcbroUjy-oMOFg-91ToHOrPSRvR6O6K165dXXh9-79Dln2DTYB5qR648SWHOuxRgRqn7G_tC5Oh5SWYqGQ5KKw7axA1mDsSybKsQtmVtHUhSB82s1LdxhP6b/s790-rw-e365/layer1.png)

Executed via command-line along with a password string input, the executable decrypts an embedded resource named BIN and executes it in memory. The BIN resource unpacks and runs a Go-based final, obfuscated payload, which then takes advantage of different vulnerable, legitimate drivers to gain elevated privileges and disarm EDR software.

"The binary's language property is Russian, indicating that the malware author compiled the executable on a computer with Russian localization settings," Klopsch said. "All of the unpacked EDR killers embed a vulnerable driver in the .data section."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

To mitigate the threat, it's recommended to keep systems up-to-date, enable tamper protection in EDR software, and practice strong hygiene for Windows security roles.

"This attack is only possible if the attacker escalates privileges they control, or if they can obtain administrator rights," Klopsch said. "Separation between user and admin privileges can help prevent attackers from easily loading drivers."

The development comes as threat actors have been observed delivering a new stealthy malware called SbaProxy by modifying legitimate antivirus binaries from BitDefender, Malwarebytes, and Sophos, and signing the files again with counterfeit certificates in order to establish proxy connections through a command-and-control (C2) server as part of an [ongoing campaign](https://news.sophos.com/en-us/2024/04/26/malware-campaign-abuses-legit-defender-binaries/).

SbaProxy is engineered to set up a proxy connection between the client and the target such that it routes the traffic through the C2 server and the infected machine. The malware only supports TCP connections.

"This threat has a significant impact, as it can be used to create proxy services that facilitate malicious activities and potentially be sold for financial gain," AT&T LevelBlue Labs [said](https://cybersecurity.att.com/blogs/labs-research/hijacked-how-cybercriminals-are-turning-anti-virus-software-against-you). "This tool, distributed in various formats such as DLLs, EXEs, and PowerShell scripts, is challenging to detect due to its sophisticated design and legitimate appearance."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Cybercrime](https://thehackernews.com/search/label/Cybercrime)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[EDR](https://thehackernews.com/search/label/EDR)[Malware](https://thehackernews.com/search/label/Malware)[RansomHub](https://...