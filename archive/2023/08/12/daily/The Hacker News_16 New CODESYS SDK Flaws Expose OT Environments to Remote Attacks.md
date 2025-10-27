---
title: 16 New CODESYS SDK Flaws Expose OT Environments to Remote Attacks
url: https://thehackernews.com/2023/08/15-new-codesys-sdk-flaws-expose-ot.html
source: The Hacker News
date: 2023-08-12
fetch_date: 2025-10-04T12:03:45.490112
---

# 16 New CODESYS SDK Flaws Expose OT Environments to Remote Attacks

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

# [16 New CODESYS SDK Flaws Expose OT Environments to Remote Attacks](https://thehackernews.com/2023/08/15-new-codesys-sdk-flaws-expose-ot.html)

**Aug 11, 2023**Ravie LakshmananOperational Technology / Vulnerability

[![CODESYS SDK Flaw](data:image/png;base64... "CODESYS SDK Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh_TSm63Fsm28_7fymnUBsQl1JqPlB7XeKSgbizxUcYI9hHGHh18HjnGs8xQ_nnc3uIdt0yLvY5pKNdRsQGmZfDeTxjuJUCDrYlDIc5PfwNqSF-K-8PN9RmWCuudc63OsTiALipiTmIPKRX64EWHVUNwrv7AC0kDlr35j7rFFTn-oi19D6IXZ8x8xHtwPQi/s790-rw-e365/exploit.jpg)

A set of 16 high-severity security flaws have been disclosed in the [CODESYS V3](https://thehackernews.com/2022/06/critical-security-flaws-identified-in.html) software development kit (SDK) that could result in remote code execution and denial-of-service under specific conditions, posing risks to operational technology (OT) environments.

The flaws, tracked from CVE-2022-47378 through CVE-2022-47393 and dubbed [CoDe16](https://github.com/microsoft/CoDe16), carry a CVSS score of 8.8 with the exception of CVE-2022-47391, which has a severity rating of 7.5. Twelve of the flaws are buffer overflow vulnerabilities.

"Exploitation of the discovered vulnerabilities, which affect all versions of CODESYS V3 prior to version 3.5.19.0, could put operational technology (OT) infrastructure at risk of attacks, such as remote code execution (RCE) and denial-of-service (DoS)," Vladimir Tokarev of the Microsoft Threat Intelligence Community [said](https://www.microsoft.com/en-us/security/blog/2023/08/10/multiple-high-severity-vulnerabilities-in-codesys-v3-sdk-could-lead-to-rce-or-dos/) in a report.

While a successful weaponization of the flaws requires user authentication as well as an in-depth knowledge of the proprietary protocol of CODESYS V3, the issues could have serious impacts that could result in shutdowns and malicious tampering of critical automation processes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The remote code execution bugs, in particular, could be abused to backdoor OT devices and interfere with the functioning of programmable logic controllers (PLCs) in a manner that could pave the way for information theft.

"Exploiting the vulnerabilities requires user authentication as well as bypassing the Data Execution Prevention (DEP) and Address Space Layout Randomization (ASLR) used by both the PLCs," Tokarev explained.

To get past the user authentication barrier, a known vulnerability ([CVE-2019-9013](https://nvd.nist.gov/vuln/detail/CVE-2019-9013), CVSS score: 8.8) is employed to steal credentials by means of a replay attack against the PLC, followed by leveraging the flaws to trigger a buffer overflow and gain control of the device.

Patches for the flaws were [released](https://customers.codesys.com/index.php?eID=dumpFile&t=f&f=17554&token=5444f53b4c90fe37043671a100dffa75305d1825&download=) in [April 2023](https://customers.codesys.com/index.php?eID=dumpFile&t=f&f=17555&token=212fc7e39bdd260cab6d6ca84333d42f50bcb3da&download=). A brief description of the issues is as follows -

* **CVE-2022-47378 -** After successful authentication, specific crafted communication requests with inconsistent content can cause the CmpFiletransfer component to read internally from an invalid address, potentially leading to a denial-of-service condition.
* **CVE-2022-47379** - After successful authentication, specific crafted communication requests can cause the CmpApp component to write attacker-controlled data to memory, which can lead to a denial-of-service condition, memory overwriting, or remote code execution.
* **CVE-2022-47380 and CVE-2022-47381** - After successful authentication, specific crafted communication requests can cause the CmpApp component to write attacker-controlled data to stack, which can lead to a denial-of-service condition, memory overwriting, or remote code execution.
* **CVE-2022-47382, CVE-2022-47383, CVE-2022-47384, CVE-2022-47386, CVE-2022-47387, CVE-2022-47388, CVE-2022-47389, and CVE-2022-47390** - After successful authentication, specific crafted communication requests can cause the CmpTraceMgr component to write attacker-controlled data to stack, which can lead to a denial-of-service condition, memory overwriting, or remote code execution.
* **CVE-2022-47385** - After successful authentication, specific crafted communication requests can cause the CmpAppForce component to write attacker-controlled data to stack, which can lead to a denial-of-service condition, memory overwriting, or remote code execution.
* **CVE-2022-47391** - Crafted communication requests can cause the affected products to read internally from an invalid address, potentially leading to a denial-of-service condition.
* **CVE-2022-47392** - After successful authentication, specific crafted communication requests with inconsistent content can cause the CmpApp/CmpAppBP/CmpAppForce components to read internally from an invalid address, potentially leading to a denial-of-service condition.
* **CVE-2022-47393** - After successful authentication, specific crafted communication requests can cause the CmpFiletransfer component to dereference addresses provided by the request for internal read access, which can lead to a denial-of-service situation.

"With CODESYS being used by many vendors, one vulnerability may affect many sectors, device types, and verticals, let alone multiple vulnerabilities," Tokarev said.

"Threat actors could launch a DoS attack against a device using a vulnerable version of CODESYS to shut down industrial operations or exploit the RCE vulnerabilities to deploy a backdoor to steal sensitive data, tamper with operations, or force a PLC to operate in a dangerous way."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/...