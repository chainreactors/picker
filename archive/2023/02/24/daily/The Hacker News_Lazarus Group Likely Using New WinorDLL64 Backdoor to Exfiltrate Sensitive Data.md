---
title: Lazarus Group Likely Using New WinorDLL64 Backdoor to Exfiltrate Sensitive Data
url: https://thehackernews.com/2023/02/lazarus-group-using-new-winordll64.html
source: The Hacker News
date: 2023-02-24
fetch_date: 2025-10-04T07:59:55.021102
---

# Lazarus Group Likely Using New WinorDLL64 Backdoor to Exfiltrate Sensitive Data

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

# [Lazarus Group Likely Using New WinorDLL64 Backdoor to Exfiltrate Sensitive Data](https://thehackernews.com/2023/02/lazarus-group-using-new-winordll64.html)

**Feb 23, 2023**Ravie LakshmananCyber Threat / Data Security

[![Lazarus Group](data:image/png;base64... "Lazarus Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9XalzZXImYu8-pPP6Yo-3xvIecSPYklle6G-qc-WMndiwC7-xK98fI5FlFySXE4fHJzOpp3V6WADVbzWVQ0fq6zmF_j72tD06q81hgspT8pCk-a7h6EBs0EAFbFDxudS5xKW9nNwcUfUUwaeVnX3aNlQvF6JZGo4noVeBTeQis3q8-vS68uaJ_mdk/s790-rw-e365/hacking-malware.png)

A new backdoor associated with a malware downloader named **Wslink** has been discovered, with the tool likely used by the notorious North Korea-aligned Lazarus Group, new findings reveal.

The payload, dubbed **WinorDLL64** by ESET, is a fully-featured implant that can exfiltrate, overwrite, and delete files; execute PowerShell commands; and obtain comprehensive information about the underlying machine.

Its other features comprise listing active sessions, creating and terminating processes, enumerating drives, and compressing directories.

Wslink was [first documented](https://thehackernews.com/2021/10/new-wslink-malware-loader-runs-as.html) by the Slovak cybersecurity firm in October 2021, describing it as a "simple yet remarkable" malware loader that's capable of executing received modules in memory.

"The Wslink payload can be leveraged later for lateral movement, due to its specific interest in network sessions," ESET researcher Vladislav Hrčka [said](https://www.welivesecurity.com/2023/02/23/winordll64-backdoor-vast-lazarus-arsenal/). "The Wslink loader listens on a port specified in the configuration and can serve additional connecting clients, and even load various payloads."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Intrusions leveraging the malware are said to be highly targeted owing to the fact that only a handful of detections have been observed to date in Central Europe, North America, and the Middle East.

In March 2022, ESET [elaborated](https://thehackernews.com/2022/03/experts-detail-virtual-machine-used-by.html) on the malware's use of an "advanced multi-layered virtual machine" [obfuscator](https://github.com/eset/wslink-vm-analyzer) to evade detection and resist reverse engineering.

[![Lazarus Group](data:image/png;base64... "Lazarus Group")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipRssfF-80Ml7-epR-PBgNpZltQStIc2IyvmG2zDpHIUe5ePsbpuQGI_tck6dNOOtYY9GOkPsovMEbxNMIBH64M5mVU7VV2-DsvRqZX8ahpx5A6kFSvYvreYKf5W-2ufuphz4g4Xu1vbAZp2E4zylZnhtaqCrk_tbLMesx2_WXUJl6ZWx1LGydZ5z6/s790-rw-e365/ADS.png)

The links to Lazarus Group stem from overlaps in behavior and code to that of previous campaigns – [Operation GhostSecret](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/analyzing-operation-ghostsecret-attack-seeks-to-steal-data-worldwide/) and [Bankshot](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/hidden-cobra-targets-turkish-financial-sector-new-bankshot-implant/) – which have been attributed to the advanced persistent threat.

This includes similarities with the GhostSecret samples detailed by McAfee in 2018, which come with a "data-gathering and implant-installation component" that runs as a service, mirroring the same behavior of Wslink.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

ESET said the [payload](https://www.virustotal.com/gui/file/3bc8bbf4a1b3596e54e20609c398eab877c581ea369f6e1ef0ab0f9afe330d12/) was uploaded to the VirusTotal malware database from South Korea, where some of the victims are located, adding credence to the Lazarus involvement.

The findings are once again demonstrative of the [vast](https://thehackernews.com/2023/02/north-korean-hackers-exploit-unpatched.html) [arsenal](https://thehackernews.com/2023/02/north-korean-hackers-targeting.html) of [hacking tools](https://thehackernews.com/2023/02/norway-seizes-584-million-in.html) employed by the Lazarus Group to infiltrate its targets.

"Wslink's payload is dedicated to providing means for file manipulation, execution of further code, and obtaining extensive information about the underlying system that possibly can be leveraged later for lateral movement," ESET said.

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

[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[hacking news](https://thehackernews.com/search/label/hacking%20news)[lazarus group](https://thehackernews.com/search/label/lazarus%20group)[Malware](https://thehackernews.com/search/label/Malware)[North Korean hackers](https://thehackernews.com/search/label/North%20Korean%20hackers)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabl...