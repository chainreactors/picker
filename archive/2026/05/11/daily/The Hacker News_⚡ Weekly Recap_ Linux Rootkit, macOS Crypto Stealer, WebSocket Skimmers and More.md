---
title: ⚡ Weekly Recap: Linux Rootkit, macOS Crypto Stealer, WebSocket Skimmers and More
url: https://thehackernews.com/2026/05/weekly-recap-linux-rootkit-macos-crypto.html
source: The Hacker News
date: 2026-05-11
fetch_date: 2026-05-12T05:39:07.095714
---

# ⚡ Weekly Recap: Linux Rootkit, macOS Crypto Stealer, WebSocket Skimmers and More

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [⚡ Weekly Recap: Linux Rootkit, macOS Crypto Stealer, WebSocket Skimmers and More](https://thehackernews.com/2026/05/weekly-recap-linux-rootkit-macos-crypto.html)

**Ravie Lakshmanan**May 11, 2026Cybersecurity / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiD4a3gzeAEAv4Bs5FqWbHG1cRyNqIOjygeSxxpNoChwyyMUWlbZHzkG0n8ysGpoAYuKqklfMtTKRct0OeYktaKLhdXpRH5pKH94tVaMX7iPeNDf7vZjFky3myBkFPJPl1xIdsWDlIYP30IeR7IZGhQZ5p82yHRdRO1OGkpAtTWgZcQSG3zXqh9tLbSSrgP/s1700-e365/cyber-recap.jpg)

Rough Monday.

Somebody poisoned a trusted download again, somebody else turned cloud servers into public housing, and a few crews are still getting into boxes with bugs that should’ve died years ago — the same old holes, same lazy access paths, same “how the hell is this still open” feeling. One report this week basically reads like a guy tripped over root access by accident and decided to stay there.

The weird part is how normal this all sounds now. Fake updates. Quiet backdoors. Remote tools are used like skeleton keys. Forum rats swapping stolen access while defenders burn another weekend chasing logs and praying the weird traffic is just monitoring noise. The Internet’s held together with duct tape and bad sleep.

Anyway, Monday recap time. Same fire. New smoke.

## **⚡ Threat of the Week**

**[Ivanti EPMM and Palo Alto Networks PAN-OS Flaws Under Attack](https://thehackernews.com/2026/05/ivanti-epmm-cve-2026-6973-rce-under.html)**—Ivanti warned customers that attackers have successfully weaponized CVE-2026-6973, an improper input validation defect in Endpoint Manager Mobile (EPMM) that allows authenticated users with administrative privileges to run code remotely. The company did not say when the first instance of exploitation occurred, or precisely how many customers have been impacted. In a related development, attackers are [actively exploiting](https://thehackernews.com/2026/05/pan-os-rce-exploit-under-active-use.html) a zero-day vulnerability affecting some Palo Alto Networks' customers' firewalls. As in the case of Ivanti, Palo Alto Networks did not say when or how it became aware of active exploitation, but said threat actors may have attempted to unsuccessfully exploit a recently disclosed critical security flaw as early as April 9, 2026. The memory corruption vulnerability, tracked as CVE-2026-0300, affects the authentication portal of PAN-OS and allows unauthenticated attackers to run code with root privileges on the PA-Series and VM-Series firewalls. Attack surface management platform Censys [said](https://censys.com/advisory/cve-2026-0300/) it detected about 263,000 Internet-exposed hosts running PAN-OS. Patches are expected to be released starting May 13, 2026.

[![Program Built on Compliance Theater](data:image/png;base64... "Program Built on Compliance Theater")

## Webinar: Transform Your SOC - From Generic Detection to Exposure Intelligence

Join Gartner and XM Cyber on May 12th at 10 AM EST. Learn to break the reactive cycle of alert fatigue by infusing real-time exposure context into your SIEM and SOAR. Discover how to prioritize threats based on their actual reachability to your critical assets.](https://thehackernews.uk/soc-proactive-management)
[Reserve my Seat ➝](https://thehackernews.uk/soc-proactive-management)

## **🔔 Top News**

* **[New Quasar Linux RAT Spotted](https://thehackernews.com/2026/05/quasar-linux-rat-steals-developer.html)**—Attackers have found a new way to turn Linux systems into entry points for a supply chain or cloud infrastructure breach that are resilient to takedowns. The new malware framework, dubbed Quasar Linux or QLNX, is a modular Linux remote access trojan (RAT) that can harvest data from compromised systems. But what sets it apart is its use of a peer-to-peer (P2P) mesh capability that turns individual compromises into an interconnected infection network, making the campaign difficult to kill and allowing infected hosts to communicate with one another rather than relying entirely on centralized servers. QLNX also combines kernel-level rootkit functionality, PAM-based authentication backdoors, and persistence mechanisms to stay hidden on compromised systems while enabling persistent access. It also hides malicious processes under names that mimic legitimate Linux services and system binaries to blend into routine workflows. "Quasar Linux RAT (QLNX) is a comprehensive Linux implant that combines remote access capabilities with advanced evasion, persistence, keylogging, and credential harvesting features," Trend Micro said. "The malware carries embedded C source code for both its PAM backdoor and LD\_PRELOAD rootkit as string literals within the binary."
* **[PCPJack Replaces TeamPCP Malware to Steal Cloud Secrets](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html)**—An unknown threat actor has launched a campaign to systematically clean up environments infected by the infamous TeamPCP hacking group and drop its own malicious tools to steal credentials from cloud, container, developer, productivity, and financial services for financial gain. Active since late April, the campaign is also capable of propagating itself by moving laterally both inside of a network and to other targets by breaking into open and exploitable cloud infrastructure. The broad credential harvesting sweep allows the malware to hack into more cloud servers and propagate the infection in a worm-like manner, while also rooting out any processes and artifacts belonging to TeamPCP. The external propagation is achieved by downloading parquet files from Common Crawl for target discovery. While threat actors aiming for cloud environments have long built methods to delete competing malware, particularly in cryptojacking campaigns, the lack of a miner and its specific targeting of TeamPCP tooling has raised the possibility that it may be someone who was previously associated with the group, is part of a rival crew, or is an unrelated thir...