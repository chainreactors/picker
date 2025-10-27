---
title: Black Basta Ransomware Hackers Infiltrates Networks via Qakbot to Deploy Brute Ratel C4
url: https://thehackernews.com/2022/10/black-basta-ransomware-hackers.html
source: The Hacker News
date: 2022-10-18
fetch_date: 2025-10-03T20:10:53.876224
---

# Black Basta Ransomware Hackers Infiltrates Networks via Qakbot to Deploy Brute Ratel C4

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

# [Black Basta Ransomware Hackers Infiltrate Networks via Qakbot to Deploy Brute Ratel C4](https://thehackernews.com/2022/10/black-basta-ransomware-hackers.html)

**Oct 17, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkdBoPmIYGYphq730wxf5a1XzHNsd7DTIbmd1oOk_uz9tCXE9RQ4RM8p5zZbWaT86HI0G0ZbSV9_QKFdkAKqizDsEZ0nV4YBQeIv7OYG-_P3OxegcUsV-2uCAsjjexP08ayf-8bwA_nn4jTJvH2CjFKclcPYbcDvP1ENVYCgDxWaS9wInp6TZG7_GU/s790-rw-e365/brutal.jpg)

The threat actors behind the [Black Basta](https://thehackernews.com/2022/06/cybersecurity-experts-warn-of-emerging.html) [ransomware family](https://www.trendmicro.com/en_us/research/22/f/black-basta-ransomware-operators-expand-their-attack-arsenal-wit.html) have been observed using the Qakbot trojan to deploy the Brute Ratel C4 framework as a second-stage payload in recent attacks.

The development marks the first time the [nascent adversary simulation software](https://thehackernews.com/2022/07/hackers-abusing-brc4-red-team.html) is being delivered via a Qakbot infection, cybersecurity firm Trend Micro [said](https://www.trendmicro.com/en_us/research/22/j/black-basta-infiltrates-networks-via-qakbot-brute-ratel-and-coba.html) in a technical analysis released last week.

The intrusion, achieved using a phishing email containing a weaponized link pointing to a ZIP archive, further entailed the use of Cobalt Strike for lateral movement.

While these legitimate utilities are designed for conducting penetration testing activities, their ability to offer remote access has made them a lucrative tool in the hands of attackers looking to stealthily probe the compromised environment without attracting attention for extended periods of time.

This has been compounded by the fact that a [cracked version](https://blog.bushidotoken.net/2022/09/brute-ratel-cracked-and-shared-across.html) of Brute Ratel C4 (BRc4 v1.2.2) began circulating last month across the cybercriminal underground, prompting its developer to [update the licensing algorithm](https://twitter.com/NinjaParanoid/status/1575104655558049792) to make it harder to crack.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

[Qakbot](https://thehackernews.com/2022/07/researchers-uncover-new-attempts-by.html), also called QBot and QuackBot, is an information stealer and banking trojan that's known to be active since 2007. But its modular design and its ability to act as a downloader has turned it into an attractive candidate for dropping additional malware.

According to Trend Micro, the ZIP file in the email contains an ISO file, which, in turn, includes a LNK file that fetches the Qakbot payload, illustrating attempts on part of threat actors to [adapt to other tactics](https://asec.ahnlab.com/en/39537/) in the aftermath of [Microsoft's decision to block macros](https://thehackernews.com/2022/07/hackers-opting-new-attack-methods-after.html) by default for documents downloaded from the web.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhqOxqh2djyrkWvDbqB7Nt00q1NUGFjSkV-YS5x2MkJn3OZYa5kTqtaCZ3opDPQpkC8IQ1qj4iKj0tBSgnAQsO-vqmfuIU83A9oOa9zPwtoCcobedl4cjVtUbKwAbrR7_LalJocusjepISQm7QSS7XtrP-ohnBuUmb9-5PoRl9z_HShrnK97lXUYdlD/s790-rw-e365/hack.jpg)

The Qakbot infection is succeeded by the retrieval of Brute Ratel and Cobalt Strike, but not before performing automated reconnaissance through built-in command line tools such as arp, ipconfig, nslookup, netstat, and whoami.

The attack, however, was stopped before any malicious action could be taken by the threat actor, although it's suspected that the end goal may have been domain-wide ransomware deployment.

In another Qakbot execution chain spotted by the cybersecurity company, the ZIP file is delivered through an increasingly popular method called [HTML smuggling](https://thehackernews.com/2022/10/hackers-can-use-app-mode-in-chromium.html), resulting in the execution of Brute Ratel C4 as the second-stage.

"The Qakbot-to-Brute Ratel-to-Cobalt Strike kill chain is associated with the group behind the Black Basta Ransomware," the researchers said. "This is based on overlapping TTPs and infrastructure observed in Black Basta attacks."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiISvERrLd8qJZki7jV3zzLFcPJZ3vo2WeRDPhrJifXVcwpGcuZroXvsqmQkghe1b-R9ipJRKsYFt7a0gNT02U7I0K2_B31RbXGls27IYPz-xFlmt2lyamIPc3X5fj1H07k6AJH4E8Xn2BrkRlImVKFHtAZiLVY6HA9Jo0UUWDtiW_y-cpheIIvq1Qp/s790-rw-e365/hacking.jpg)

The findings coincide with a resurgence of Qakbot attacks in recent months by means of a variety of techniques like [HTML file attachments](https://www.fortinet.com/blog/threat-research/new-variant-of-qakbot-spread-by-phishing-emails), [DLL side-loading](https://blog.cyble.com/2022/07/21/qakbot-resurfaces-with-new-playbook/), and [email thread hijacking](https://blog.talosintelligence.com/2022/07/what-talos-incident-response-learned.html), the last of which entailed harvesting emails in bulk from successful [ProxyLogon attacks](https://thehackernews.com/2021/11/hackers-exploiting-proxylogon-and.html) aimed at Microsoft Exchange servers.

### IcedID Actors Diversify Delivery Methods

Qakbot is far from the only access-as-a-service malware that's being increasingly distributed via ISO and other file formats to get around macro restrictions, for [Emotet](https://thehackernews.com/2022/10/new-report-uncovers-emotets-delivery.html), [IcedID](https://thehackernews.com/2022/04/new-hacking-campaign-targeting.html), and [Bumblebee](https://thehackernews.com/2022/08/hackers-using-bumblebee-loader-to.html) campaigns have all followed similar trajectories.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Palo Alto Networks Unit 42, in late September 2022, [said](https://unit42.paloaltonetworks.com/polyglot-file-icedid-payload/) it discovered a malicious polyglot Microsoft Compiled HTML Help (CHM) f...