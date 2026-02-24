---
title: MuddyWater Targets MENA Organizations with GhostFetch, CHAR, and HTTP_VIP
url: https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html
source: The Hacker News
date: 2026-02-23
fetch_date: 2026-02-24T04:12:16.049176
---

# MuddyWater Targets MENA Organizations with GhostFetch, CHAR, and HTTP_VIP

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

# [MuddyWater Targets MENA Organizations with GhostFetch, CHAR, and HTTP\_VIP](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)

**Ravie Lakshmanan**Feb 23, 2026Threat Intelligence / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk6M5M47ZmJ-KuhYC2JC8UwHjdNPLoS3oSeT38cnI8sCmd9NbNFmjNh8qCUXxC7XexLVdUBTBsEIELNLfj2nM-LTRKJajmvwbdehC_bNch-kE98Py-CaDoSAZHCxQztFszsWePupECSqKuasUv8lu9IXYhg8qAS2V7ojLqicNp_HRnyhnc74n_vWYHeEQ-/s1700-e365/muddy.jpg)

The Iranian hacking group known as [MuddyWater](https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html) (aka Earth Vetala, Mango Sandstorm, and MUDDYCOAST) has targeted several organizations and individuals mainly located across the Middle East and North Africa (MENA) region as part of a new campaign codenamed **Operation Olalampo**.

The activity, first observed on January 26, 2026, has resulted in the deployment of new malware families that share overlapping samples previously identified as used by the threat actor, according to a report published by Group-IB. These include downloaders like GhostFetch and HTTP\_VIP, along with a Rust backdoor called CHAR and an advanced implant codenamed GhostBackDoor that's dropped by GhostFetch.

"These attacks follow similar patterns and align with the killchains previously observed in MuddyWater attacks; starting with a phishing email with a Microsoft Office document attached to it that contains malicious macro code that decodes the embedded payload and drops it on the system and executes it, providing the adversary with remote control of the system," the company [said](https://www.group-ib.com/blog/muddywater-operation-olalampo/).

One such attack chain employing a malicious Microsoft Excel document prompts users to enable macros in order to activate the infection and ultimately drop CHAR. Another variant of the same attack has been found to lead to the deployment of the GhostFetch downloader, which then downloads GhostBackDoor.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

A third version of the attack leverages themes such as flight tickets and reports, in contrast to using lures mimicking an energy and marine services company in the Middle East, to distribute the HTTP\_VIP downloader that subsequently deploys the AnyDesk remote desktop software.

A brief description of the four tools is as follows -

* **GhostFetch**, a first-stage downloader that profiles the system, validates mouse movements and checks screen resolution, checks for the presence of debuggers, virtual machine artifacts, and antivirus software, and fetches and executes secondary payloads directly in memory.
* **GhostBackDoor**, a second-stage backdoor delivered by GhostFetch that supports an interactive shell, file read/write, and re-run GhostFetch.
* **HTTP\_VIP**, a native downloader that conducts system reconnaissance, connects to an external server ("codefusiontech[.]org") to authenticate and deploy AnyDesk from the C2 server. A new variant of the malware also adds the ability to retrieve victim information and retrieve instructions to start an interactive shell, download/upload files, capture clipboard contents, and update the sleep/beaconing interval.
* **CHAR**, a Rust backdoor that's controlled by a Telegram bot (whose first name is "Olalampo" and username is "stager\_51\_bot") to change directory and execute a cmd.exe or PowerShell command.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9codiElaXflP03LdRbTq-nazzyJg9afA33hoJJJYw6SEgccvJ3Mb801nozDT8dzpn6WnkEWlnTvHH5ZNGPIIvLsX32d2lga5MUukWPeZ3MQl2_gJdF5a7shBN1c1YUp-clQD-JvVck2t8az-B0JimfGW5BvZZQPkydZoW2thBVF9Su75pVtwGCNU_cvHy/s1700-e365/killchain.jpg)

The PowerShell command is designed to execute a SOCKS5 reverse proxy or another backdoor named Kalim, upload data stolen from web browsers, and run unknown executables referred to as "sh.exe" and "gshdoc\_release\_X64\_GUI.exe."

Group-IB's analysis of CHAR's source code has revealed signs of artificial intelligence (AI)-assisted development owing to the presence of emojis in debug strings, a finding that's consistent with [Google's revelations](https://thehackernews.com/2025/11/google-uncovers-promptflux-malware-that.html) last year that the threat actor is experimenting with generative AI tools to facilitate the development of custom malware to support file transfer and remote execution.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Another notable aspect is that CHAR shares a similar structure and development environment as the Rust-based malware [BlackBeard](https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html) (aka Archer RAT and RUSTRIC), which was flagged by CloudSEK and Seqrite Labs as put to use by the threat actor to target various entities in the Middle East.

MuddyWater has also been observed exploiting recently disclosed vulnerabilities on public-facing servers as a way to obtain initial access to target networks.

"The MuddyWater APT group remains an active threat within the META [Middle East, Turkey, and Africa] region, with this operation primarily targeting organizations in the MENA region," Group-IB concluded. "The group's continued adoption of AI technology, combined with continued development of custom malware and tooling and diversified command-and-control (C2) infrastructures, underscores their dedication and intent to expand their operations."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[...