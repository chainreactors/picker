---
title: Alert: HotPage Adware Disguised as Ad Blocker Installs Malicious Kernel Driver
url: https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html
source: The Hacker News
date: 2024-07-19
fetch_date: 2025-10-06T17:44:14.241215
---

# Alert: HotPage Adware Disguised as Ad Blocker Installs Malicious Kernel Driver

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

# [Alert: HotPage Adware Disguised as Ad Blocker Installs Malicious Kernel Driver](https://thehackernews.com/2024/07/alert-hotpage-adware-disguised-as-ad.html)

**Jul 18, 2024**Ravie LakshmananMalware / Windows Security

[![HotPage Adware](data:image/png;base64... "HotPage Adware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9vsUgwYZu-8gHpGYvC1pB1KM8oWnlBKZah-fgrhWSMo9NWGhPzgyP-duusyHzRwm5U1HWK9tzCOwLV4no_rlsqRCKXfib37teOiQ1Srt-aHuFBFuVxph9M9vTVvyjU80R5Sd3pFd8z-ZUN8QVnUWxCcLc0te5W5QSMXWYR2ZQsOygo9aivaNvsLRzlMz2/s790-rw-e365/shell.png)

Cybersecurity researchers have shed light on an adware module that purports to block ads and malicious websites, while stealthily offloading a kernel driver component that grants attackers the ability to run arbitrary code with elevated permissions on Windows hosts.

The malware, dubbed HotPage, gets its name from the eponymous installer ("HotPage.exe"), according to new findings from ESET, which discovered the malware towards the end of 2023.

The installer "deploys a driver capable of injecting code into remote processes, and two libraries capable of intercepting and tampering with browsers' network traffic," ESET researcher Romain Dumont [said](https://www.welivesecurity.com/en/eset-research/hotpage-story-signed-vulnerable-ad-injecting-driver/) in a technical analysis published today.

"The malware can modify or replace the contents of a requested page, redirect the user to another page, or open a new page in a new tab based on certain conditions."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Besides leveraging its browser traffic interception and filtering capabilities to display game-related ads, it is designed to harvest and exfiltrate system information to a remote server associated with a Chinese company named Hubei Dunwang Network Technology Co., Ltd (湖北盾网网络科技有限公司).

This is accomplished by means of a driver, whose primary objective is to inject the libraries into browser applications and alter their execution flow to change the URL being accessed or ensure that the homepage of the new web browser instance is redirected to a particular URL specified in a configuration.

That's not all. The absence of any access control lists ([ACLs](https://github.com/MicrosoftDocs/windows-driver-docs/blob/staging/windows-driver-docs-pr/driversecurity/windows-security-model.md)) for the driver meant that an attacker with a non-privileged account could leverage it to obtain elevated privileges and run code as the NT AUTHORITY\System account.

"This kernel component unintentionally leaves the door open for other threats to run code at the highest privilege level available in the Windows operating system: the System account," Dumont said. "Due to improper access restrictions to this kernel component, any processes can communicate with it and leverage its code injection capability to target any non-protected processes."

[![HotPage Adware](data:image/png;base64... "HotPage Adware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipF0KVZlaW844rR3k9LizpOgyWLGUi2g629-bHmUlE9jWrdkdKCDtZxuUFOWzbtNhY3n_MrBDFY1nU6tXkdrXyhHbw1alHpqMfar-d3XDIybbsEjg9S11xuZWDN-iOp7YsssT1lnS8ewaEkqe-vokkqH4pVkldz1glVqjVNefGVwrtq2rBivRWaverf5rs/s790-rw-e365/exe.png)

Although the exact method by which the installer is distributed is not known, evidence gathered by the Slovakian cybersecurity firm shows that it has been advertised as a security solution for internet cafés that's intended to improve users' browsing experience by stopping ads.

The embedded driver is notable for the fact that it's signed by Microsoft. The Chinese company is believed to have gone through Microsoft's [driver code signing requirements](https://learn.microsoft.com/en-us/windows-hardware/drivers/dashboard/code-signing-reqs) and managed to obtain an Extended Verification (EV) certificate. It has been removed from the [Windows Server Catalog](https://www.windowsservercatalog.com/) as of May 1, 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Kernel-mode drivers have been required to be [digitally signed](https://thehackernews.com/2022/12/ransomware-attackers-use-microsoft.html) to be loaded by the Windows operating system, an important layer of defense erected by Microsoft to protect against malicious drivers that could be weaponized to subvert security controls and interfere with system processes.

That said, Cisco Talos [revealed](https://thehackernews.com/2023/07/hackers-exploit-windows-policy-loophole.html) last July how native Chinese-speaking threat actors are exploiting a Microsoft Windows policy loophole to forge signatures on kernel-mode drivers.

"The analysis of this rather generic-looking piece of malware has proven, once again, that adware developers are still willing to go the extra mile to achieve their goals," Dumont said.

"Not only that, they have developed a kernel component with a large set of techniques to manipulate processes, but they also went through the requirements imposed by Microsoft to obtain a code-signing certificate for their driver component."

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

[adware](htt...