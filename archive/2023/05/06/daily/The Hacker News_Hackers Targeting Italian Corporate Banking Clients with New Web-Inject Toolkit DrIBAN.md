---
title: Hackers Targeting Italian Corporate Banking Clients with New Web-Inject Toolkit DrIBAN
url: https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html
source: The Hacker News
date: 2023-05-06
fetch_date: 2025-10-04T11:43:11.619254
---

# Hackers Targeting Italian Corporate Banking Clients with New Web-Inject Toolkit DrIBAN

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

# [Hackers Targeting Italian Corporate Banking Clients with New Web-Inject Toolkit DrIBAN](https://thehackernews.com/2023/05/hackers-targeting-italian-corporate.html)

**May 05, 2023**Ravie Lakshmanan

[![Corporate Banking](data:image/png;base64... "Corporate Banking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKXrZ4LStMDNyqa1ykeE_RdWiuKG8xHing_ooSbZi7rPM89WML58cpG-GSNrq2VIX7owJeVrNWjoXuTPpXkeeGWiPB_UzvnuVWWCGxkXVu6sCav5Yeu4mKV8AbLwV9m5gxJmDUm898U4AGxzJ0PTnTPzwkDuq3fPWPqDcFL3FId4FSkRJARNPsZKki/s790-rw-e365/bank.png)

Italian corporate banking clients are the target of an ongoing financial fraud campaign that has been leveraging a new web-inject toolkit called **drIBAN** since at least 2019.

"The main goal of drIBAN fraud operations is to infect Windows workstations inside corporate environments trying to alter legitimate banking transfers performed by the victims by changing the beneficiary and transferring money to an illegitimate bank account," Cleafy researchers Federico Valentini and Alessandro Strino [said](https://www.cleafy.com/cleafy-labs/uncovering-driban-fraud-operations-chapter1).

The bank accounts, per the Italian cybersecurity firm, are either controlled by the threat actors themselves or their affiliates, who are then tasked with laundering the stolen funds.

The use of web injects is a time-tested tactic that makes it possible for malware to inject custom scripts on the client side by means of a man-in-the-browser ([MitB](https://thehackernews.com/2022/01/trickbot-malware-using-new-techniques.html)) attack and intercept traffic to and from the server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The fraudulent transactions are often realized by means of a technique called Automated Transfer System ([ATS](https://www.cleafy.com/documents/how-ats-attacks-work-infographic)) that's capable of bypassing [anti-fraud systems](https://en.wikipedia.org/wiki/Strong_customer_authentication) put in place by banks and [initiating unauthorized wire transfers](https://www.malwaretech.com/2016/08/automatic-transfer-systems-ats-for-beginners.html) from a victim's own computer.

Over the years, the operators behind drIBAN have gotten more savvy at avoiding detection and developing effective social engineering strategies, in addition to establishing a foothold for long periods in corporate bank networks.

Cleafy said 2021 was the year when the classic "banking trojan" operation evolved into an advanced persistent threat. Furthermore, there are indications that the activity cluster overlaps with a [2018 campaign](https://www.proofpoint.com/us/threat-insight/post/sload-and-ramnit-pairing-sustained-campaigns-against-uk-and-italy) mounted by an actor tracked by Proofpoint as TA554 targeting users in Canada, Italy, and the U.K.

[![Corporate Banking](data:image/png;base64... "Corporate Banking")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg6tFLXXT8kwFKyKo1k2XPM2g-QlyMATbMZiif3MbIEE_fNM0p_Ms-OPCR-r4qX5lkAS14r12yCyIFB8EfON63_CqfJOnsmRxdvvnJOSfS-xkWtaZpIbytJnyqeOptwRjSPHN6pwNqk1xnata3iUtuwMTAHVGibhNiNMkcYGgtsfqyf1K_gWO9iuPpL/s790-rw-e365/hacking-process.png)

The attack chain begins with a [certified email](https://en.wikipedia.org/wiki/Certified_email) (or PEC email) in an attempt to lull victims into a false sense of security. These phishing emails come bearing an executable file that acts as a downloader for a malware called [sLoad](https://malpedia.caad.fkie.fraunhofer.de/details/ps1.sload) (aka Starslord loader).

A PowerShell loader, sLoad is a reconnaissance tool that collects and exfiltrates information from the compromised host, with the purpose of assessing the target and dropping a more significant payload like [Ramnit](https://malpedia.caad.fkie.fraunhofer.de/details/win.ramnit) if the target is deemed profitable.

"This 'enrichment phase' could continue for days or weeks, depending on the number of infected machines," Cleafy noted. "Additional data will be exfiltrated to make the resulting botnet more and more solid and consistent."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

sLoad also leverages living-off-the-land ([LotL](https://lolbas-project.github.io/)) techniques by abusing legitimate Windows tools like [PowerShell](https://learn.microsoft.com/en-us/powershell/) and [BITSAdmin](https://learn.microsoft.com/en-us/windows/win32/bits/bitsadmin-tool) as part of its evasion mechanisms.

Another characteristic of the malware is its ability to check against a predefined list of corporate banking institutions to determine if the hacked workstation is one among the targets, and if so, proceed with the infection.

"All the bots that successfully pass those steps will be selected by botnet operators and considered as 'new candidates' for banking fraud operations moving forward to the next stage, where Ramnit, one of the most advanced banking trojans, will be installed," the researchers said.

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

[banking Trojan](https://thehackernews.com/search/label/banking%20Trojan)[Malware](https://thehackernews.com/search/label/Malware)

[![c](data:image/svg+xml;base64...