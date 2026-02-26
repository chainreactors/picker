---
title: Google Disrupts UNC2814 GRIDTIDE Campaign After 53 Breaches Across 42 Countries
url: https://thehackernews.com/2026/02/google-disrupts-unc2814-gridtide.html
source: The Hacker News
date: 2026-02-25
fetch_date: 2026-02-26T04:12:07.946989
---

# Google Disrupts UNC2814 GRIDTIDE Campaign After 53 Breaches Across 42 Countries

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Google Disrupts UNC2814 GRIDTIDE Campaign After 53 Breaches Across 42 Countries](https://thehackernews.com/2026/02/google-disrupts-unc2814-gridtide.html)

**Ravie Lakshmanan**Feb 25, 2026Cyber Espionage / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyrJTi6YIFc4PWNVjyVZgjQfbHNpfH-WtwcxIIEgUSin8DR8zz_VZBauDnlTA42bh7LT7nj1Y-OtoKL34tEKUKo4JrNuWgnhC1r54tIkws6OC8SWqucU0OrWysv2-pzj_YCinatv9FwUUsvADoPMVngfmR8wB2xr_lS1viUQHoK_Vom83SmBZMOBJPe6Nb/s1700-e365/google.jpg)

Google on Wednesday disclosed that it worked with industry partners to disrupt the infrastructure of a suspected China-nexus cyber espionage group tracked as **UNC2814** that breached at least 53 organizations across 42 countries.

"This prolific, elusive actor has a long history of targeting international governments and global telecommunications organizations across Africa, Asia, and the Americas," Google Threat Intelligence Group (GTIG) and Mandiant [said](https://cloud.google.com/blog/topics/threat-intelligence/disrupting-gridtide-global-espionage-campaign) in a report published today.

UNC2814 is also suspected to be linked to additional infections in more than 20 other nations. The tech giant, which has been tracking the threat actor since 2017, has been observed using API calls to communicate with software-as-a-service (SaaS) apps as command-and-control (C2) infrastructure. The idea, it added, is to disguise their malicious traffic as benign.

Central to the hacking group's operations is a novel backdoor dubbed GRIDTIDE that abuses Google Sheets API as a communication channel to disguise C2 traffic and facilitate the transfer of raw data and shell commands. It's a C-based malware that supports file upload/download and the execution of arbitrary shell commands.

Exactly how UNC2814 obtains initial access remains a topic of investigation, but the group is said to have a history of exploiting and compromising web servers and edge systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

Attacks mounted by the threat actor have leveraged a service account to move laterally within the environment via SSH. Also put to use are living-off-the-land (LotL) binaries to conduct reconnaissance, escalate privileges, and set up persistence for the backdoor.

"To achieve persistence, the threat actor created a service for the malware at /etc/systemd/system/xapt.service, and once enabled, a new instance of the malware was spawned from /usr/sbin/xapt," Google explained.

Another noteworthy aspect is the deployment of SoftEther VPN Bridge to establish an outbound encrypted connection to an external IP address. It's worth mentioning here that the abuse of SoftEther VPN has been [linked](https://thehackernews.com/2023/08/china-linked-flax-typhoon-cyber.html) to [multiple](https://thehackernews.com/2025/10/chinese-cybercrime-group-runs-global.html) [Chinese hacking groups](https://thehackernews.com/2026/01/china-linked-uat-8099-targets-iis.html).

There is evidence indicating that GRIDTIDE is dropped on endpoints containing personally identifiable information (PII), an aspect that's consistent with cyber espionage activity focused on monitoring persons of interest. Google, however, noted that it did not observe any data exfiltration taking place during the course of the campaign.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg01Sx3mjIosp9QfbTLVvwKJTFWnp7mrEbVD1GIe-73bkOGzSZuZyemI8OYfME8eCNsvyptdtNnbjqh0XBIlW5HFrkDNPBKdvQZ_XGQ3ilHFoTVfVE9JQkapemKPyaWb1AaMTnBcedPz-hmvmNXfS3khVmCm2TN49fIMr-em84pLNba8-i3WxSlfTeJb9QI/s1700-e365/GRIDTIDE.jpg) |
| GRIDTIDE execution lifecycle |

GRIDTIDE's C2 mechanism involves a cell-based polling mechanism, where specific roles are assigned to certain spreadsheet cells to enable bidirectional communication -

* A1, to poll for attacker commands and overwrite it with a status response (e.g., S-C-R or Server-Command-Success)
* A2-An, to transfer data, such as command output and files
* V1, to store system data from the victim endpoint

As part of the action, Google said it terminated all Google Cloud Projects controlled by the attacker, disabled all known UNC2814 infrastructure, and cut off access to attacker-controlled accounts and Google Sheets API calls leveraged by the actor for command-and-control (C2) purposes.

The tech giant described UNC2814 as one of the "most far-reaching, impactful campaigns" encountered in recent years, adding that it has issued formal victim notifications to each of the targets and that it is actively supporting organizations with verified compromises resulting from this threat.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The latest discovery is one of many concurrent efforts by Chinese nation-state groups to embed themselves into networks for long-term access. The development also highlights that the network edge continues to take the brunt of internet-wide exploitation attempts, with threat actors frequently exploiting vulnerabilities and misconfigurations in such appliances as a common entry point into enterprise networks.

These appliances have [become attractive targets](https://www.greynoise.io/blog/2026-greynoise-state-of-the-edge-report-where-attacks-concentrate-defenses-fall-short) in recent years as they typically lack endpoint malware detection, yet provide direct network access or pivot points to internal services if compromised.

"The global scope of UNC2814's activity, evidenced by confirmed or suspected operations in over 70 countries, underscores the serious threat facing telecommunications and government sectors, and the capacity for these intrusions to evade detection by defenders, Google said.

"Prolific intrusions of this scale are generally the result of years of focused effort and will not be easily re-established. We expect that UNC2814...