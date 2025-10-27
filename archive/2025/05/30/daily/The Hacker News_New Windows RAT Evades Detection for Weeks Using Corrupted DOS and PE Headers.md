---
title: New Windows RAT Evades Detection for Weeks Using Corrupted DOS and PE Headers
url: https://thehackernews.com/2025/05/new-windows-rat-evades-detection-for.html
source: The Hacker News
date: 2025-05-30
fetch_date: 2025-10-06T22:38:42.118840
---

# New Windows RAT Evades Detection for Weeks Using Corrupted DOS and PE Headers

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

# [New Windows RAT Evades Detection for Weeks Using Corrupted DOS and PE Headers](https://thehackernews.com/2025/05/new-windows-rat-evades-detection-for.html)

**May 29, 2025**Ravie LakshmananMalware / Windows Security

[![Windows RAT Evades Detection](data:image/png;base64... "Windows RAT Evades Detection")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEit9YukymDpffFTdGngx2h9PdI4_IKR-DGLB_ySx6QNIQakfcbQpVNf32aN3wHSPrIXJ0R_o3ZLrs8Jcgn2aVULrIzXfY36PAr5DdYCFtHkfbO6MrXbyueniFw21PFW0pOnILaCfGYdSdK5Fw6p6kCMbhHevCNqEQzk4kCcfJ5X_QtzsDh1zUOHvHPTG9jr/s790-rw-e365/windows-malware.jpg)

Cybersecurity researchers have taken the wraps off an unusual cyber attack that leveraged malware with corrupted DOS and PE headers, according to [new findings](https://www.fortinet.com/blog/threat-research/deep-dive-into-a-dumped-malware-without-a-pe-header) from Fortinet.

The DOS (Disk Operating System) and PE (Portable Executable) headers are [essential parts](https://offwhitesecurity.dev/malware-development/portable-executable-pe/dos-header/) of a [Windows PE file](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format), providing information about the executable.

While the [DOS header](https://learn.microsoft.com/en-us/archive/msdn-magazine/2002/february/inside-windows-win32-portable-executable-file-format-in-detail) makes the executable file backward compatible with MS-DOS and allows it to be recognized as a valid executable by the operating system, the PE header contains the metadata and information necessary for Windows to load and execute the program.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"We discovered malware that had been running on a compromised machine for several weeks," researchers Xiaopeng Zhang and John Simmons from the FortiGuard Incident Response Team said in a report shared with The Hacker News. "The threat actor had executed a batch of scripts and PowerShell to run the malware in a Windows process."

Fortinet said while it was unable to extract the malware itself, it acquired a memory dump of the running malware process and a full memory dump of the compromised machine. In a statement shared with the publication, the company said that it observed the behavior in a single incident involving ransomware activity and that the threat was neutralized before any ransomware could be deployed.

"The threat actor gained initial access through remote access infrastructure and attempted to distribute malware using a PowerShell script executed via PsExec, however the script itself was not recovered during the investigation," it added.

The malware, running within a dllhost.exe process, is a 64-bit PE file with corrupted DOS and PE headers in a bid to challenge analysis efforts and reconstruct the payload from memory.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCkIJaax8h4tA1W-dWoQuEfJja2fne1_IwGtZdPa0yQdyvfap0TKpww_zyqORmxA3nc8DHZ3FMxdGI0aYHbdc718v-_Np1pxQ0NVQYym8vSzQGDqlvn1NbeuOqOyJtRnVmywtiL6b0_Z5eDVn_Q_08yiXMsvrv1Bgoz1SzxKSdq0wUnrUH6iUzZT-_si5I/s790-rw-e365/code.png)

Despite these roadblocks, the cybersecurity company further noted that it was able to take apart the dumped malware within a controlled local setting by replicating the compromised system's environment after "multiple trials, errors, and repeated fixes."

The malware, once executed, decrypts command-and-control (C2) domain information stored in memory and then establishes contact with the server ("rushpapers[.]com") in a newly created thread.

"After launching the thread, the main thread enters a sleep state until the communication thread completes its execution," the researchers said. "The malware communicates with the C2 server over the TLS protocol."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Further analysis has determined the malware to be a remote access trojan (RAT) with capabilities to capture screenshots; enumerate and manipulate the system services on the compromised host; and even act as a server to await incoming "client" connections.

"It implements a multi-threaded socket architecture: each time a new client (attacker) connects, the malware spawns a new thread to handle the communication," Fortinet said. "This design enables concurrent sessions and supports more complex interactions."

"By operating in this mode, the malware effectively turns the compromised system into a remote-access platform, allowing the attacker to launch further attacks or perform various actions on behalf of the victim."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fortinet](https://thehackernews.com/search/label/Fortinet)[Malware](https://thehackernews.com/search/label/Malware)[Memory Forensics](https://thehackernews.com/search/label/Memory%20Forensics)[network security](https://thehackernews.com/search/label/network%20security)[powershell](https://thehackernews.com/search/label/powershell)[Remote Access Trojan](https://thehackernews.com/search/label/Remote%20Access%20Trojan)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20I...