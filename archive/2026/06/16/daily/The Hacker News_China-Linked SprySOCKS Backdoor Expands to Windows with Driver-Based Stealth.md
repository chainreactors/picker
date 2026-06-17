---
title: China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth
url: https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html
source: The Hacker News
date: 2026-06-16
fetch_date: 2026-06-17T07:04:12.300487
---

# China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [China-Linked SprySOCKS Backdoor Expands to Windows with Driver-Based Stealth](https://thehackernews.com/2026/06/china-linked-sprysocks-backdoor-expands.html)

**Ravie Lakshmanan**Jun 16, 2026Malware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxym2hiE83TbiNOrIeH3s4QCF0wQ_BYcSYPKlC3m9LGSuJnH7UNicbkgIk4kQTbpPiLRul9dSxQ180XW656_9NPtlqWoTGivTamDVl24ZfUQFPgUleakZq6aZI5kZqszNz3GpVyJQnPiXis_kjlMqAxKBxGKZsDdAvb-rX20fxszdd0pCKRO9GqK3CSu-p/s1700-e365/chinese-proxy.png)

Cybersecurity researchers have flagged two previously undocumented Windows variants of what was believed to be a Linux-only backdoor called **SprySOCKS**.

"The Windows variants discovered are internally marked as WIN\_DRV and WIN\_PLUS," ESET [said](https://www.welivesecurity.com/en/eset-research/fishmongers-arsenal-upgraded-sprysocks-windows/) in a report shared with The Hacker News. "Both come with a hard-coded C&C [command-and-control] configuration and support communication over TCP, UDP, and WebSocket protocols."

Like its Linux counterpart, the Windows versions support more than 30 commands to facilitate system information collection, process enumeration, service management, and file system operations. WIN\_DRV has also been found to utilize kernel drivers to conceal the malware's network connections, processes, files, and registry keys.

In addition, the variant enables TCP traffic diversion that allows the malware operators to send commands to the backdoor through a random TCP port on the victim's device without exposing the backdoor's actual listening port in the network traffic.

SprySOCKS was [first publicly documented](https://thehackernews.com/2023/09/earth-luscas-new-sprysocks-linux.html) by Trend Micro in September 2023, attributing its use to a China-nexus state-sponsored threat actor known as Earth Lusca, which is also [tracked](https://thehackernews.com/2025/03/china-linked-apt-aquatic-panda-10-month.html) by the cybersecurity community under the monikers Aquatic Panda, Bronze University, Charcoal Typhoon, and RedHotel. The adversary is assessed to be active since at least 2021 and [operated](https://web-assets.esetstatic.com/wls/en/papers/threat-reports/eset-apt-activity-report-q4-2023-q1-2024.pdf) by a Chinese contractor named [i-Soon](https://thehackernews.com/2025/03/us-charges-12-chinese-nationals-in.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The Slovakian cybersecurity vendor, which has assigned the name FishMonger to the threat cluster, has described it as a cyber espionage group that falls under the broader Winnti umbrella. In a report published in March 2025, the company [linked](https://thehackernews.com/2025/03/china-linked-apt-aquatic-panda-10-month.html) the hacking group to a global campaign dubbed Operation FishMedley targeting seven organizations in Taiwan, Hungary, Turkey, Thailand, France, and the U.S. between January and October 2022.

SprySOCKS is based on a Windows remote access trojan called Trochilus, and shares several common traits with [RedLeaves](https://blogs.jpcert.or.jp/en/2017/04/redleaves---malware-based-on-open-source-rat.html), a backdoor that also exhibits extensive source code overlaps with Trochilus. What's more, the use of Trochilus is linked to another Chinese threat actor known as [Webworm](https://thehackernews.com/2026/05/webworm-deploys-echocreep-and-graphworm.html), which, in turn, has tradecraft commonalities with both FishMonger and SixLittleMonkeys.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNGJh5vyrWZbbA1Uj-J4LOMpOjlgr5rigNCQ6I9b5qYZnDu9GjSkX76_VARxp4kWDk_C89Y_tusbbujojmngcGOXr67NlJNhyphenhyphenhHQ3vuOmNC1VgolKB_fQyCR5ZtCNvI2i94JSN4PrqUHYZVIwghjBAiaATrGxvpKmUs0uhrlVwYfPG_8bq1xJudpsVdOu6/s1700-e365/1.png) |
| WIN\_DRV Execution Chain |

The Windows variants are part of version 1.8 of SprySOCKS, with the [WIN\_DRV sample](https://www.virustotal.com/gui/file/68aec5085599e8a272767f50da66c83a6582e4e16ed97c209f65f81538b0c028/details) using a kernel driver referred to as RawWNPF ("KW1B5206BDC1743FP.dat") for advanced stealth, while retaining the functionality present in the Linux variant. The driver is loaded using another encrypted kernel driver named DriverLoader ("KX1B5206BDC1743DD.dat").

The attack chain makes use of an as-yet-undetermined initial access pathway to drop a batch script, which then creates and executes a scheduled task responsible for triggering a DLL side-loading chain that drops the SprySOCKS backdoor and the driver components. However, it's worth noting that the group has previously exploited N-day security flaws in public-facing Fortinet, GitLab, Microsoft Exchange Server, Progress Telerik UI, and Zimbra instances to obtain a foothold.

"The Windows version retains most of the core architecture of its Linux predecessor — including the C&C protocol, encryption used, and overall command handling logic — while substituting Windows-native mechanisms where required and improving the stealthiness of the backdoor by bringing the kernel drivers to the game," ESET researcher Martin Smolár said.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9WxLLYKIRRW1GSKGeDp8sKMw3YI9-x7wSQ3OLYKmWpgzUIWOjnQcPutSriE9Cy0CUxFFqf81wGerg1ezD2IwqQw7f-vm6iOfHm01verxpItsN2e-cqrPA-O2TcJh1Sx0cjEiGki1btxigNmcQAOfc8YKd_bzgBFqLG28-xqueFUAePYUG7oLdkcdBSzsH/s1700-e365/2.png) |
| WIN\_PLUS Execution Chain |

"The most notable differences can be spotted in the way the final backdoor is loaded, in the improved stealthiness, and in the component names and paths used.

The WIN\_PLUS execution scheme, in contrast, adopts a different approach. It leverages the Windows Print Spooler service ("spoolsv.exe") as a starting point to execute a first-stage loader that runs as a [print processor](https://learn.microsoft.com/en-us/windows-hardware/drivers/print/introduction-to-...