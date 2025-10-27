---
title: SystemBC Powers REM Proxy With 1,500 Daily VPS Victims Across 80 C2 Servers
url: https://thehackernews.com/2025/09/systembc-powers-rem-proxy-with-1500.html
source: The Hacker News
date: 2025-09-20
fetch_date: 2025-10-02T20:27:20.426213
---

# SystemBC Powers REM Proxy With 1,500 Daily VPS Victims Across 80 C2 Servers

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

# [SystemBC Powers REM Proxy With 1,500 Daily VPS Victims Across 80 C2 Servers](https://thehackernews.com/2025/09/systembc-powers-rem-proxy-with-1500.html)

**Sep 19, 2025**Ravie LakshmananBotnet / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-w6283s1VaRjYcIVD7ekrmBAw8jRjpNp4q0ME7At7VVRZFjRLqRONytP45AdKFxsP8c2c9f4SyVQfzMCq7Qc0KEDLJ3zNqywZPdWw2xfn-1A0Uo_Sf3Jta9dHeUOJnJAwUcU-XFQyBDyu63hhwuOlu_9FPd-b-wwr0XZb9rnTjG5ECGqzutLX-Vegv9iL/s790-rw-e365/botnet.jpg)

A proxy network known as REM Proxy is powered by malware known as **SystemBC**, offering about 80% of the botnet to its users, according to new findings from the Black Lotus Labs team at Lumen Technologies.

"REM Proxy is a sizeable network, which also markets a [pool of 20,000 Mikrotik routers](https://thehackernews.com/2025/01/13000-mikrotik-routers-hijacked-by.html) and a variety of open proxies it finds freely available online," the company [said](https://blog.lumen.com/systembc-bringing-the-noise/) in a report shared with The Hacker News. "This service has been a favorite for several actors such as those behind [TransferLoader](https://thehackernews.com/2025/07/ta829-and-unkgreensec-share-tactics-and.html), which has ties to the Morpheus ransomware group."

[SystemBC](https://thehackernews.com/2024/01/systembc-malwares-c2-server-analysis.html) is a C-based malware that turns infected computers into SOCKS5 proxies, allowing infected hosts to communicate with a command-and-control (C2) server and download additional payloads. First documented by Proofpoint in 2019, it's capable of targeting both [Windows](https://thehackernews.com/2025/07/credential-theft-and-remote-access.html) and [Linux systems](https://blog.polyswarm.io/systembc-now-targeting-linux).

In a report earlier this January, ANY.RUN [revealed](https://x.com/anyrun_app/status/1884207667058463188) that the Linux variant of SystemBC proxy implant is potentially designed for internal corporate services, and that it's mainly used to target corporate networks, cloud servers, and IoT devices.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As is typically the case with any proxy solution, users of the network reach out to SystemBC C2s on high-numbered ports, which then route the user through to one of the victims before reaching their destination.

According to Lumen, the SystemBC botnet comprises over 80 C2 servers and a daily average of 1,500 victims, of which nearly 80% are compromised virtual private server (VPS) systems from several large commercial providers. Interestingly, 300 of those victims are part of another botnet called [GoBruteforcer](https://thehackernews.com/2023/03/gobruteforcer-new-golang-based-malware.html) (aka GoBrut).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjaXsW5g9h5qWrQcz_tZBflWnjmPNEpERHKrj8wdqdOM_5PMpiiqNhnFYDRiljOi5lZn0g4FiWWL3KNhQq0Gm4Gvp49m_4OuX3l11vOJTHJjc4FkUzIa1wAJFbDyJEds1cA8pPDvTeON6tXqFZGs1CoUMwY9JUDetiwHKZiQy7Fhp-PVwmDv2citGADDt8C/s790-rw-e365/systembc.jpg)

Of these, close to 40% of the compromises have "extremely long average" infection lifespans, lasting over 31 days. To make matters worse, the vast majority of the victimized servers have been found to be susceptible to several known security flaws. Each victim has 20 unpatched CVEs and at least one critical CVE on average, with one of the identified VPS servers in the U.S. city of Atlanta vulnerable to more than 160 unpatched CVEs.

"The victims are made into proxies that enable high volumes of malicious traffic for use by a host of criminal threat groups," the company noted. "By manipulating VPS systems instead of devices in residential IP space, as is typical in malware-based proxy networks, SystemBC can offer proxies with massive amounts of volume for longer periods of time."

Besides REM Proxy, some of the other customers of the SystemBC include at least two different Russia-based proxy services, one Vietnamese proxy service called VN5Socks (aka Shopsocks5), and a Russian web scraping service.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEpgKGxKde_5hD4QlB9AwBpmKx7mPYs_SgPNmlPM3Fe5Eau8dB142hFghsOaNdrvakKymzpCs0IxPYTRsYLA6Xd4IpGyXM4wWu0CdNK6iCOY7hODes5DJ9AG7WTSKiXT-61dfKdMiUbpGEAtYnPietIUpMXmDxZXfcZiSEWQFWxxf5ZZ-7G0HR3M5Gs8AJ/s790-rw-e365/rem.jpg)

Crucial to the functioning of the malware is the IP address 104.250.164[.]214, which not only hosts the artifacts but also appears to be the source of attacks to recruit potential victims. Once new victims are ensnared, a shell script is dropped on the machine to subsequently deliver the malware.

The botnet operates with little regard for stealth, with the primary goal being to expand in volume to enlist as many devices as possible into the botnet. One of the largest use cases of the illicit network is by the threat actors behind SystemBC themselves, who use it to brute-force WordPress site credentials.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The end goal is likely to sell the harvested credentials to other criminal actors in underground forums, who then weaponize them to [inject malicious code](https://www.godaddy.com/resources/news/threat-actors-push-clickfix-fake-browser-updates-using-stolen-credentials) into the sites in question for follow-on campaigns.

"SystemBC has exhibited sustained activity and operational resilience across multiple years, establishing itself as a persistent vector within the cyber threat landscape," Lumen said. "Originally used by threat actors to enable ransomware campaigns, the platform has evolved to offer the assembly and sale of bespoke botnets."

"Their model offers considerable advantages: it enables the execution of widespread reconnaissance, spam dissemination, and related activities, allowing an attacker to reserve more selective proxy resources for targeted attacks informed by p...