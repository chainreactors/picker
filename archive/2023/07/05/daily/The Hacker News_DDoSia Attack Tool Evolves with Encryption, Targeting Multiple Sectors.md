---
title: DDoSia Attack Tool Evolves with Encryption, Targeting Multiple Sectors
url: https://thehackernews.com/2023/07/ddosia-attack-tool-evolves-with.html
source: The Hacker News
date: 2023-07-05
fetch_date: 2025-10-04T11:55:59.898924
---

# DDoSia Attack Tool Evolves with Encryption, Targeting Multiple Sectors

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

# [DDoSia Attack Tool Evolves with Encryption, Targeting Multiple Sectors](https://thehackernews.com/2023/07/ddosia-attack-tool-evolves-with.html)

**Jul 04, 2023**Ravie LakshmananMalware / Cyber Attack

[![DDoSia Attack Tool](data:image/png;base64... "DDoSia Attack Tool")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifbeYEQfkB5nBwJc9vZFQINx21Y-pSLwxWlXdHCkztoBKD-CcBgfPDB8uYWqTMvqfdDdvRK3IQua9UmKTJsng56E7cl8ct4uRqOp9nPAKgJwF5IZIUBjULzYdutXwRj9NJvEAxv4KdFmQPbnwGoZYkxidG-e6-ZXWhkUM6SJMsvF6HF69s_iliQoIYhqE/s790-rw-e365/ddos.jpg)

The threat actors behind the **DDoSia** attack tool have come up with a new version that incorporates a new mechanism to retrieve the list of targets to be bombarded with junk HTTP requests in an attempt to bring them down.

The updated variant, written in Golang, "implements an additional security mechanism to conceal the list of targets, which is transmitted from the [command-and-control] to the users," cybersecurity company Sekoia [said](https://blog.sekoia.io/following-noname05716-ddosia-projects-targets/) in a technical write-up.

DDoSia is attributed to a pro-Russian hacker group called [NoName(057)16](https://decoded.avast.io/martinchlumecky/ddosia-project/). Launched in 2022 and a successor of the [Bobik botnet](https://decoded.avast.io/martinchlumecky/bobik/), the attack tool is [designed](https://decoded.avast.io/martinchlumecky/ddosia-project-how-noname05716-is-trying-to-improve-the-efficiency-of-ddos-attacks/) for staging distributed denial-of-service (DDoS) attacks against targets primarily located in Europe as well as Australia, Canada, and Japan.

Lithuania, Ukraine, Poland, Italy, Czechia, Denmark, Latvia, France, the U.K., and Switzerland have emerged as the most targeted countries over a period ranging from May 8 to June 26, 2023. A total of 486 different websites were impacted.

Python and Go-based implementations of DDoSia have been unearthed to date, making it a cross-platform program capable of being used across Windows, Linux, and macOS systems.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"DDoSia is a multi-threaded application that conducts denial-of-service attacks against target sites by repeatedly issuing network requests," SentinelOne [explained](https://www.sentinelone.com/labs/noname05716-the-pro-russian-hacktivist-group-targeting-nato/) in an analysis published in January 2023. "DDoSia issues requests as instructed by a configuration file that the malware receives from a C2 server when started."

DDoSia is distributed through a fully-automated process on Telegram that allows individuals to register for the crowdsourced initiative in exchange for a cryptocurrency payment and a ZIP archive containing the attack toolkit.

What's noteworthy about the new version is the use of encryption to mask the list of targets to be attacked, indicating that the tool is being actively maintained by the operators.

"NoName057(16) is making efforts to make their malware compatible with multiple operating systems, almost certainly reflecting their intent to make their malware available to a large number of users, resulting in the targeting of a broader set of victims," Sekoia said.

[![DDoSia Attack](data:image/png;base64... "DDoSia Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikCvaFxbPOrNFNtC4i-jhBPpIPYDFPkkMmWpjmdDBo2j0fTZtKqR0mQYaHH2pUJWU2xX8OkOBMrML_xlic-iPWVgCNj46mdfrfMQ1booM3VXLemz4yesii6gnL1cA09yKexzxDZfFyXbNIHn84RFwPYtIGnx8Nz_7Uwis_t8tNeQEgZaVOZW41UlB2uco/s790-rw-e365/cyber.jpg)

The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned of targeted denial-of-service (DoS) and DDoS attacks against multiple organizations in multiple sectors.

"These attacks can cost an organization time and money and may impose reputational costs while resources and services are inaccessible," the agency [said](https://www.cisa.gov/news-events/alerts/2023/06/30/dos-and-ddos-attacks-against-multiple-sectors) in a bulletin.

Although CISA did not provide any additional specifics, the warning overlaps with claims by [Anonymous Sudan](https://www.truesec.com/hub/blog/what-is-anonymous-sudan) on its Telegram channel that it had taken down the websites of the Department of Commerce, Social Security Administration (SSA), and the Treasury Department's Electronic Federal Tax Payment System (EFTPS).

Anonymous Sudan [attracted](https://thehackernews.com/2023/06/microsoft-blames-massive-ddos-attack.html) attention last month for carrying Layer 7 DDoS attacks against various Microsoft services, including OneDrive, Outlook, and Azure web portals. The tech giant is tracking the cluster under the name Storm-1359.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The hacking crew has asserted it's conducting cyber strikes out of Africa on behalf of oppressed Muslims across the world. But cybersecurity researchers believe it to be a pro-Kremlin operation with no ties to Sudan and a member of the KillNet hacktivist collective.

In an analysis released on June 19, 2023, Australian cybersecurity vendor CyberCX [characterized](https://cybercx.com.au/a-bear-in-wolfs-clothing/) the entity as a "smokescreen for Russian interests." The company's website has since become inaccessible, greeting visitors with a "403 Forbidden" message. The threat actor claimed responsibility for the cyber attack.

"The reason for the attack: stop spreading rumors about us, and you must tell the truth and stop the investigations that we call the investigations of a dog," Anonymous Sudan said in a message posted on June 22, 2023.

Anonymous Sudan, in a [Bloomberg report](https://www.bloomberg.com/news/articles/2023-06-28/anonymous-sudan-does-group-behind-microsoft-cyberattack-have-ties-to-russia) last week, further denied it was connected to Russia but acknowledged they share similar interests, and that it goes after "everything that is hostile to Islam."

CISA's latest advisory ...