---
title: Multi-Stage ValleyRAT Targets Chinese Users with Advanced Tactics
url: https://thehackernews.com/2024/08/multi-stage-valleyrat-targets-chinese.html
source: The Hacker News
date: 2024-08-17
fetch_date: 2025-10-06T18:08:11.704842
---

# Multi-Stage ValleyRAT Targets Chinese Users with Advanced Tactics

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

# [Multi-Stage ValleyRAT Targets Chinese Users with Advanced Tactics](https://thehackernews.com/2024/08/multi-stage-valleyrat-targets-chinese.html)

**Aug 16, 2024**Ravie LakshmananCyber Attack / Malware

[![ValleyRAT Malware](data:image/png;base64... "ValleyRAT Malware")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgocyxFRn2lsyLw5VtWuCpcLhtHzy8PUZ_o8hqIhtu14ywUli_oqW3EZcJe6BMjLVzsTDb8-Npg8u9tVwMOjQw9C0ePqAUuiR7z8UeyRerEigB6rdwZqTMe9hsxuZJMEvTQ58LFeOpTNuUYi2I4qCjh1x1LOGSfrxYe8VmBZxoFzKhLaNfkfpykn-aGYmQ8/s790-rw-e365/c2.png)

Chinese-speaking users are the target of an ongoing campaign that distributes a malware known as ValleyRAT.

"ValleyRAT is a multi-stage malware that utilizes diverse techniques to monitor and control its victims and deploy arbitrary plugins to cause further damage," Fortinet FortiGuard Labs researchers Eduardo Altares and Joie Salvio [said](https://www.fortinet.com/blog/threat-research/valleyrat-campaign-targeting-chinese-speakers).

"Another noteworthy characteristic of this malware is its heavy usage of shellcode to execute its many components directly in memory, significantly reducing its file footprint in the victim's system."

Details about the campaign [first emerged](https://thehackernews.com/2024/06/china-linked-valleyrat-malware.html) in June 2024, when Zscaler ThreatLabz detailed attacks involving an updated version of the malware.

Exactly how the latest iteration of ValleyRAT is distributed is currently not known, although [previous campaigns](https://thehackernews.com/2023/09/sophisticated-phishing-campaign_20.html) have leveraged email messages containing URLs pointing to compressed executables.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Based on the filenames of the executables we found, they're likely using phishing emails as they did in past campaigns," the FortiGuard Labs research team told The Hacker News. "However, we weren't able to find actual related email samples so it’s hard to say for certain."

The attack sequence is a multi-stage process that starts with a first-stage loader that impersonates legitimate applications like Microsoft Office to make them appear harmless (e.g., "工商年报大师.exe" or "补单对接更新记录txt.exe").

Launching the executable causes the decoy document to be dropped and the shellcode to be loaded for advancing to the next phase of the attack. The loader also takes steps to validate that it's not running in a virtual machine.

The shellcode is responsible for initiating a beaconing module that contacts a command-and-control (C2) server to download two components – RuntimeBroker and RemoteShellcode – alongside setting persistence on the host and gaining administrator privileges by exploiting a legitimate binary named [fodhelper.exe](https://thehackernews.com/2023/07/casbaneiro-banking-malware-goes-under.html) to achieve a UAC bypass.

The second method used for privilege escalation concerns the abuse of the [CMSTPLUA COM interface](https://blogs.quickheal.com/uac-bypass-using-cmstp/), a technique previously adopted by threat actors connected to the [Avaddon ransomware](https://attack.mitre.org/techniques/T1548/002/) and also observed in recent [Hijack Loader](https://thehackernews.com/2024/06/cybercriminals-exploit-free-software.html) campaigns.

In a further attempt to make sure that the malware runs unimpeded on the machine, it configures exclusion rules to Microsoft Defender Antivirus and proceeds to terminate various antivirus-related processes based on matching executable filenames.

RuntimeBroker's primary task is to retrieve from the C2 server a component named Loader, which functions the same way as the first-stage loader and executes the beaconing module to repeat the infection process.

The Loader payload also exhibits some distinct characteristics, including carrying out checks to see if it's running in a sandbox and scanning the Windows Registry for keys related to apps like Tencent WeChat and Alibaba DingTalk, reinforcing the hypothesis that the malware exclusively targets Chinese systems.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

On the other hand, RemoteShellcode is configured to fetch the ValleyRAT downloader from the C2 server, which, subsequently, uses UDP or TCP sockets to connect to the server and receive the final payload.

ValleyRAT, attributed to a threat group called Silver Fox, is a fully-featured backdoor capable of remotely controlling compromised workstations. It can take screenshots, execute files, and load additional plugins on the victim system.

"This malware involves several components loaded in different stages and mainly uses shellcode to execute them directly in memory, significantly reducing its file trace in the system," the researchers said.

"Once the malware gains a foothold in the system, it supports commands capable of monitoring the victim's activities and delivering arbitrary plugins to further the threat actors' intentions."

The development comes amid ongoing malspam campaigns that attempt to exploit an old Microsoft Office vulnerability (CVE-2017-0199) to execute malicious code and deliver GuLoader, Remcos RAT, and Sankeloader.

"CVE-2017-0199 is still targeted to allow for execution of remote code from within an XLS file," Broadcom-owned Symantec [said](https://www.broadcom.com/support/security-center/protection-bulletin/new-malspam-campaigns-delivering-multiple-trojans). "The campaigns delivered a malicious XLS file with a link from which a remote HTA or RTF file would be executed to download the final payload."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#lin...