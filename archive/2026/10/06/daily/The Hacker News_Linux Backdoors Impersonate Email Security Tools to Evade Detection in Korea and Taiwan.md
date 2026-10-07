---
title: Linux Backdoors Impersonate Email Security Tools to Evade Detection in Korea and Taiwan
url: https://thehackernews.com/2026/10/linux-backdoors-impersonate-email.html
source: The Hacker News
date: 2026-10-06
fetch_date: 2026-10-07T07:55:35.040962
---

# Linux Backdoors Impersonate Email Security Tools to Evade Detection in Korea and Taiwan

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [Linux Backdoors Impersonate Email Security Tools to Evade Detection in Korea and Taiwan](https://thehackernews.com/2026/10/linux-backdoors-impersonate-email.html)

**Ravie Lakshmanan**Oct 06, 2026Cyber Espionage / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj42ncE2ZMHIbAm_fj5U9fqCYUvPwhyUiNbARM3CC5IxhnMXjIZ2ENa99UDGeaZqGPlqn53A7y7Nkz1ZxzzyykKxEb4GT0jxWhrar9Q5yPmBN1NL6599HRdbzbLSYf3WPuU7tkkY5eOsvhAT9dw-24DXuusztPyRr2H66840cWZx17MZ0B-rB877W19bgX1/s1700-nu-rw-lo-l85-e365/linux-spam.jpg)

Linux backdoors targeting telecom and network appliances in South Korea and Taiwan have been disguising their traffic as email services and seemingly legitimate processes to blend in and evade detection.

Threat actors are known to name their malicious software after a legitimate operating system component or a process as a defense evasion measure. By borrowing the name of a real binary, it may make it appear less conspicuous among other Windows processes, lend it a false sense of trust, or be overlooked by an analyst during casual inspection.

However, the backdoors [examined](https://www.rapid7.com/blog/post/tr-smtp-is-the-key-bpfdoor-averat-hitting-the-network-edge/) by Rapid7 have been found to go beyond imitating file names by assuming the identities of email security products like [SpamSniper](https://global.jiran.com/spamsniper) and [ShareTech](https://www.sharetech.com.tw/en-us/) that are widely used in enterprise environments in South Korea and Taiwan.

According to vendor Jiran Group, SpamSniper is advertised as "Korea's leading email security solution" that defends organizations against spam, malware, and server attacks.

The malicious artifacts include a new BPFDoor variant and a BPF Rekoobe build used against South Korean targets, and a previously unreported Linux implant dubbed AVERAT that's delivered via a dropper and deployed against Taiwanese appliances.

"The BPFDoor variants seen against South Korean systems impersonate the PID file of SpamSniper, a Korean anti-spam product, and rotate through ten Linux daemon names," Rapid7 said. "Across the samples, each component adopts names and conventions designed to look unremarkable in the environment it targets."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

BPFdoor and its many iterations were the subject of an [extensive analysis](https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html) by Rapid7 earlier this year, with the activity linked to a threat group dubbed Red Menshen (aka Earth Bluecrow, DecisiveArchitect, and Red Dev 18), which has targeted telecom providers across the Middle East and Asia going all the way back to 2021.

At a high level, BPFDoor abuses the Berkeley Packet Filter (BPF) functionality to inspect incoming network traffic and activate its behavior only upon detecting a [magic packet](https://en.wikipedia.org/wiki/Wake-on-LAN). The detection of a new BPFDoor version indicates that the threat actors behind the malware are actively refining and retooling their arsenal in response to public disclosures.

"Once security vendors wrote static network signatures (Suricata/Snort) to detect these Layer 4 anomalies, the operators began targeting the edge proxies," Rapid7 said. "By wrapping the magic packet in standard HTTPS POST requests and relying on SSL offloading common in telecom environments, the trigger can be delivered to the BPFDoor-infected node in a way that may evade conventional deep packet inspection."

While some BPFDoor samples spoof SpamSniper, another artifact sets its process name to "ora\_ppmond," mimicking the naming convention associated with Oracle-backed telecom subscriber and provisioning platforms. Specifically, the name appears to be a reference to "[ora\_pmon\_\*](https://docs.oracle.com/communications/G13327_01/doc.151/ncc_sysadmin.pdf)," which represents the Process Monitor (PMON) background process of an Oracle Database instance.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ0sSPqJcd6DcBjttWVADIyQ7RanZLc1iF_bS5kK-8f26GmYZJgFhGmsZdLoNKTgScl-ZCdROUZBVbmuM4gJARvOmClyFgPpHFWvFo6umwWjwfFgJNyKr__Aa2kXcZzF_9FHa4ZG8juIPOzTRZLih5rs3qrZsmo3FcyyLOGGhwwv0-z9-BCFWQ-yClWqgN/s1700-nu-rw-lo-l85-e365/rapid7.png)

Once triggered, the BPFDoor sample launches a TinyShell session and supports commands to facilitate interactive shell, upload, and download capabilities. Interestingly, the use of [TinyShell](https://en.wikipedia.org/wiki/TinyShell) has been previously attributed to China-nexus clusters like [Liminal Panda](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html), [UNC3886](https://thehackernews.com/2025/03/chinese-hackers-breach-juniper-networks.html) (aka [Fire Ant](https://thehackernews.com/2026/08/weekly-recap-chinese-spy-proxy-ai.html#:~:text=Fire%20Ant%20Targets%20Trusted%20Infrastructure%20in%202026)), and [Velvet Ant](https://thehackernews.com/2024/08/chinese-hackers-exploit-zero-day-cisco.html), all of which have singled out [telecom networks and edge devices](https://www.sygnia.co/blog/operation-highland-velvet-ant/).

"These samples show BPFDoor operating as a modular framework that adapts to the telecom layer it targets, integrating TinyShell and Rekoobe logic to support exfiltration," Rapid7 explained.

Also observed in conjunction with the activity is a [Rekoobe](https://thehackernews.com/2022/06/new-syslogk-linux-rootkit-lets.html)-based BPF [backdoor](https://intezer.com/blog/linux-rekoobe-operating-with-new-undetected-malware-samples) that intercepts TCP/UDP/SCTP IPv4 and UDP IPv6 traffic with source and destination ports equal 25. Furthermore, it names its processes after components of SpamSniper.

The dropper observed in an overlapping campaign is an ELF binary that acts as a local installer for AVERAT, a modular implant that uses the Simple Mail Transfer Protocol (SMTP) ...