---
title: New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables
url: https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:01.342700
---

# New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables

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

![cybersecurity](data:image/svg+xml;base64...)

# [New NatJack Attacks Hijack TCP Sessions and Spoof DNS by Manipulating NAT Tables](https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html)

**Swati Khandelwal**Aug 07, 2026Network Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx8dmEkj0rsX2NREBfPOczKn7zadWRaVVOyVPVeaCPzCDdBAPhocCwP1CVbX_p1pj4Q7DVYsdusvWc9u9G7lO4BGYihT6BXnXY099zIs1B1PBefH71cXCHZucxaG2gEzqKdf9B3FVr9MJ34SntVezm4gNXWSxIMF05DpYUNF6qmfhb0hMiyNpsWDOtuRE/s1700-e365/NatJack.jpg)

Security researcher **Malcolm Stagg** has disclosed a new attack class called **NatJack** that manipulates network address translation (NAT) connection state to hijack active TCP sessions, spoof DNS responses, expose mapped ports, and exhaust NAT tables.

Presented at [Black Hat USA 2026](https://blackhat.com/us-26/briefings/schedule/#breaking-trust-boundaries-exploiting-design-assumptions-in-network-infrastructure-53311), the research found affected behavior across independently developed implementations, including Windows and Linux.

Two implementation-specific flaws have been assigned CVEs: **CVE-2026-56181** (CVSS score: 8.3) in Windows NAT used by Hyper-V, and **CVE-2026-63913** (CVSS score: 8.2) in Linux Netfilter conntrack.

NatJack generally requires the attacker to have privileged access to a system behind the same NAT as the victim. The mitigation guidance therefore emphasizes separating untrusted workloads from trusted systems that share NAT infrastructure.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

There is no single patch for the broader attack class. Organizations should apply available Windows and Linux updates and encrypt traffic even within internal networks. The research also recommends Internet Protocol (IP) Source Guard where applicable.

The [NatJack research](https://natjack.io/), conducted independently by Stagg through SODIUM-24, targets an assumption built into many NAT implementations: hosts behind the same NAT are generally assumed not to manipulate one another's connection state. An attacker controlling a system behind the same NAT can, depending on the implementation, manipulate connection-tracking entries belonging to another system.

The research describes four main paths. One can redirect traffic from an active TCP connection by replacing its NAT mapping. Another interferes with a victim's DNS request so the legitimate DNS response reaches the attacker, allowing a forged response to be sent back.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjios0cfQsvRYZqchMG_eHZpK3vM-BLYt7C7sJIETjJamZwsxNGSaqsH7sU7SdomHRxkp2i9c1MoYdiAqu059swFJ0p_EQo69ZL6LFGBsl-ZohD9sz44nZ7unkBLQZ9BaOTwDG7ThA64OGfIN8s9ZVhyAFquZtBPlbFrO5yn3InK98fTtioFjhv3ATOafk/s1700-e365/tcp.jpg)

Other techniques disclose externally mapped ports or fill the NAT connection table with spoofed flows until legitimate clients cannot create new connections.

Synack [said](https://www.synack.com/blog/malcolm-stagg-black-hat-2026/) Stagg tested the techniques against dozens of real-world network infrastructure products from multiple vendors and demonstrated proof-of-concept exploitation in a controlled environment.

The NatJack site does not publish a complete product-by-product matrix. The Hacker News found no public evidence that NatJack techniques have been exploited in the wild as of August 7, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

For Linux, the [kernel.org CNA record](https://nvd.nist.gov/vuln/detail/CVE-2026-63913) says a crafted SYN followed by a reset packet with an invalid sequence number can prematurely force an active Netfilter NAT entry into a closed state because the conntrack logic failed to validate its direction. Fixed stable releases include 5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.93, 6.18.35, 7.0.12, and 7.1.

Stagg says the kernel change fixes the code flaw but only mitigates the broader downstream-spoofing technique, increasing attack complexity rather than fully addressing it.

Microsoft's [CNA record](https://nvd.nist.gov/vuln/detail/CVE-2026-56181) describes the Windows issue as an origin-validation error that enables spoofing from an adjacent network. Affected releases include Windows 11 24H2 before 26100.8875, 25H2 before 26200.8875, 26H1 before 28000.2525, and Windows Server 2025 before 26100.33158.

NatJack also builds on [earlier research into NAT-state manipulation](https://thehackernews.com/2024/06/new-snailload-attack-exploits-network.html). An [NDSS 2024 study](https://www.ndss-symposium.org/ndss-paper/exploiting-sequence-number-leakage-tcp-hijacking-in-nat-enabled-wi-fi-networks/) demonstrated TCP hijacking through NAT mapping manipulation and found 52 of 67 tested routers susceptible to its attack, work that produced ten CVEs.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Container Security](https://thehackernews.com/search/label/Container%20Security), [denial of service](https://thehackernews.com/search/label/denial%20of%20service), [DNS Security](https://thehackernews.com/search/label/DNS%20Security), [linux](https://thehackernews.com/search/label/linux), [Microsoft](https://thehackernews.com/search/label/Microsoft), [network security](https://thehackernews.com/search/label/network%20security), [Virtualization Security](https://th...