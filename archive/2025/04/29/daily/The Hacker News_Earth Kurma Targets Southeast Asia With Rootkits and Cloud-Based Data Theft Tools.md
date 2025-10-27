---
title: Earth Kurma Targets Southeast Asia With Rootkits and Cloud-Based Data Theft Tools
url: https://thehackernews.com/2025/04/earth-kurma-targets-southeast-asia-with.html
source: The Hacker News
date: 2025-04-29
fetch_date: 2025-10-06T22:08:57.562347
---

# Earth Kurma Targets Southeast Asia With Rootkits and Cloud-Based Data Theft Tools

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

# [Earth Kurma Targets Southeast Asia With Rootkits and Cloud-Based Data Theft Tools](https://thehackernews.com/2025/04/earth-kurma-targets-southeast-asia-with.html)

**Apr 28, 2025**Ravie LakshmananCyber Espionage / Cloud Security

[![Rootkits and Cloud-Based Data T](data:image/png;base64... "Rootkits and Cloud-Based Data T")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhmsXUN3WnmPTfwjpCt8J5loFaanOpGJUIkL6cPMHaYydEaH0UKlTi2MEucrbG9CTqZLVzjDiWdnm46lWeUIVOjM4C0C_4NksF4eY3qjAslI8_PCncAtXO52uwjZcObc0pf9BON8JO5eJlUiCvH117DwEXDO9gRzyMKKUjgQKXro0gZWLS3p0LpWWAjC-C/s790-rw-e365/cyberattack.jpg)

Government and telecommunications sectors in Southeast Asia have become the target of a "sophisticated" campaign undertaken by a new advanced persistent threat (APT) group called **Earth Kurma** since June 2024.

The attacks, per Trend Micro, have leveraged custom malware, rootkits, and cloud storage services for data exfiltration. The Philippines, Vietnam, Thailand, and Malaysia are among the prominent targets.

"This campaign poses a high business risk due to targeted espionage, credential theft, persistent foothold established through kernel-level rootkits, and data exfiltration via trusted cloud platforms," security researchers Nick Dai and Sunny Lu [said](https://www.trendmicro.com/en_us/research/25/d/earth-kurma-apt-campaign.html) in an analysis published last week.

The threat actor's activities date back to November 2020, with the intrusions primarily relying on services like Dropbox and Microsoft OneDrive to siphon sensitive data using tools like TESDAT and SIMPOBOXSPY.

Two other noteworthy malware families in its arsenal include rootkits such as KRNRAT and [Moriya](https://thehackernews.com/2021/05/new-stealthy-rootkit-infiltrated.html), the latter of which has been observed previously in attacks aimed at high-profile organizations in Asia and Africa as part of an espionage campaign dubbed TunnelSnake.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Trend Micro also said that SIMPOBOXSPY and the exfiltration script used in the attacks share overlaps with another APT group codenamed [ToddyCat](https://thehackernews.com/2025/04/new-tcesb-malware-found-in-active.html). However, a definitive attribution remains inconclusive.

It's currently not known as to how the threat actors gain initial access to target environments. The initial foothold is then abused to scan and conduct lateral movement using a variety of tools like NBTSCAN, Ladon, FRPC, WMIHACKER, and ICMPinger. Also deployed is a keylogger referred to as KMLOG to harvest credentials.

It's worth noting that the use of the open-source [Ladon](https://github.com/k8gege/Ladon) framework has been previously [attributed](https://thehackernews.com/2022/08/chinese-hackers-targeted-dozens-of.html) to a China-linked hacking group called TA428 (aka Vicious Panda).

Persistence on the hosts is accomplished by three different loader strains referred to as DUNLOADER, TESDAT, and DMLOADER, which are capable of loading next-stage payloads into memory and executing them. These consist of Cobalt Strike Beacons, rootkits like KRNRAT and Moriya, as well as data exfiltration malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpy8N7tOKVUjTGB2FjaHt2pVcEmLZx6c8r061eTYcg1pgOdlPvCy8Z0tdIlPJZoexoSjvqQd-Fq_oj3Xvavn2qQBVbyJQCmYMsL0NEu57sePEdrBoc7t1oBCyJ1CCBXkZ56FfOz3DQtg-oDOJVrlxsPX1XFcmipQDRY5HFAgm8A8-Zp1e84U8R93w4q9AR/s790-rw-e365/attack.png)

What distinguishes these attacks is the use of living-off-the-land (LotL) techniques to install the rootkits, where hackers employ legitimate system tools and features, in this case, syssetup.dll, rather than introducing easily detectable malware.

While Moriya is engineered to inspect incoming TCP packets for a malicious payload and inject shellcode into a newly spawned "svchost.exe" process, KRNRAT is an amalgamation of five different open-source projects with capabilities such as process manipulation, file hiding, shellcode execution, traffic concealment, and command-and-control (C2) communication.

KRNRAT, like Moriya, is also designed to load a user-mode agent the rootkit and inject it into "svchost.exe." The user-mode agent serves as a backdoor to retrieve a follow-on payload from the C2 server.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Before exfiltrating the files, several commands executed by the loader TESDAT collected specific document files with the following extensions: .pdf, .doc, .docx, .xls, .xlsx, .ppt, and .pptx," the researchers said. "The documents are first placed into a newly created folder named "tmp," which is then archived using WinRAR with a specific password."

One of the bespoke tools used for data exfiltration is SIMPOBOXSPY, which can upload the RAR archive to Dropbox with a specific access token. According to a Kasperksy report from October 2023, the [generic Dropbox uploader](https://thehackernews.com/2023/10/researchers-unveil-toddycats-new-set-of.html) is "probably not exclusively used by ToddyCat."

ODRIZ, another program used for the same purpose, uploads the collected information to OneDrive by specifying the OneDrive refresh token as an input parameter.

"Earth Kurma remains highly active, continuing to target countries around Southeast Asia," Trend Micro said. "They have the capability to adapt to victim environments and maintain a stealthy presence."

"They can also reuse the same code base from previously identified campaigns to customize their toolsets, sometimes even utilizing the victim's infrastructure to achieve their goals."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_s...