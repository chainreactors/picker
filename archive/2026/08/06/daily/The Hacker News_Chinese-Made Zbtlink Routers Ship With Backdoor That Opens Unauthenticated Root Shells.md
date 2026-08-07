---
title: Chinese-Made Zbtlink Routers Ship With Backdoor That Opens Unauthenticated Root Shells
url: https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:26.118907
---

# Chinese-Made Zbtlink Routers Ship With Backdoor That Opens Unauthenticated Root Shells

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

# [Chinese-Made Zbtlink Routers Ship With Backdoor That Opens Unauthenticated Root Shells](https://thehackernews.com/2026/08/chinese-made-zbtlink-routers-ship-with.html)

**Ravie Lakshmanan**Aug 06, 2026IoT Security / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3VqhMa79pNymspvzHhSpHG4HCDAGn4nAD-7ZwQgDuSOELhM0xxHASqfnd2ThEv8XJ0tM58bPsGPHcobfoaEEWW4Am9H-Wd9bpb-QqYRQfFcFKrvbLjwEGYu0VfIAclBcVn9PpMWS02ZAtOa7hhwg8e45cYcgYYX0C1_yQptZh7-ZvqFHpf-9uqq5csbCj/s1700-e365/router-hacking.jpg)

Cybersecurity researchers have disclosed details of a "factory-shipped backdoor" implanted in at least 20 Chinese router models from Zbtlink.

According to a [new report](https://www.vulncheck.com/blog/zbt-endlessdoors) from VulnCheck, the implant appears in all 21 firmware images currently available from Zbtlink that span more than 2 years. The backdoors are designed such that they start automatically and attempt to beacon to Chinese command-and-control (C2) infrastructure as often as every 35 seconds.

They masquerade as a Linux kernel thread, but are actually userland processes running with root privileges while blending their true functionality with other legitimate kworker processes. The "phone home" implants have been codenamed **ENDLESSDOORS**.

"ENDLESSDOORS, at its core, is a small tool called [rctl](https://github.com/ycsunjane/rctl) (remote control linux)," Jacob Baines, VulnCheck Chief Technology Officer, said. "Uploaded to GitHub on January 14, 2015 and never touched again, this obscure repository implements a simple command and control client and server."

"The server listens on port 7000 for clients to connect. It can send the client individual shell commands or tell the client to spawn a reverse bash shell."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The "kworker" worker process running on Zbtlink AX3000, which VulnCheck analyzed, is a customized version of rctl that's configured to contact the following -

* 47.107.224[.]89
* rbdg4nzqadui[.]wikaba[.]com

What's more, there is no handshake, negotiation, or authentication involved. Once the implant sends a "hello" message to the server alongside the LAN MAC address, it's engineered to run whatever the server sends back in response.

"One reserved string, rctlbash, tells the implant to open a second connection to port 7001, allocate a pseudo-terminal, spawn /bin/sh, and bridge it," Baines explained. "That is a live interactive root shell."

"The vocabulary of this protocol is two phrases: run this as root, and give me a root shell. Anyone along the network path can hijack the client/server communication. Anyone who controls the resolution of rbdg4nzqadui.wikaba[.]com, or the address it resolves to, can control any ENDLESSDOORS implant that tries to phone home."

An attacker can take advantage of this loophole to hijack the outbound rctl communications and obtain a live root shell, and take over control of the router without having to be reachable from the internet.

VulnCheck noted that every firmware listed on zbtlink.com's download page embeds the rctl implant and starts it at boot with an init.d script named "skworker." The list of affected models is below -

* CPE2801
* WE1026-5G-WD
* WE1326
* WE2007
* WE2008-DSIM
* WE2416
* WE3326
* WE5927
* WE5931
* WE5931AC
* WE826-T3-DSIM
* WG108
* WG1602
* WG1608-DSIM
* WG209
* WG2105
* WG2107
* WG259
* WG3526
* Z8102AX-2DSIM

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Each of these models have been found to have been found to dial the same set of four primary and secondary endpoints -

* zbtctl.epplink[.]net (47.100.190[.]96)
* 47.107.224[.]89
* online-string[.]com (45.32.81[.]152)
* rbdg4nzqadui.wikaba[.]com (43.248.136[.]125)

As of writing, users [visiting the firmware downloads](https://www.zbtlink.com/pages/zbt-router-firmware-download) page on Zbtlink's website are displayed the below message -

*We have detected firmware security vulnerabilities affecting selected router firmware releases.*

*As a precautionary measure, the impacted firmware versions have been temporarily taken down from download channels. Our engineering team is working intensively to develop and validate secured patched firmware.*

*We will notify you immediately once the fixed, security-validated firmware is available for release.*

*We apologize for the inconvenience caused. Thank you for your understanding.*

When contacted for comment, a spokesperson for the Chinese router manufacturer told The Hacker News that the feature is "solely intended" for after-sales maintenance and serves no other purposes.

"It is generally retained only on sample units to assist customers with software debugging," the spokesperson added. "Our company specializes in OEM and ODM customization services."

"Our customers use their own self-developed software instead of ZBT's default firmware. Customer security and privacy are our top priority. We take this report very seriously and are working to expedite the implementation of a solution."

In the meantime, customers are advised to check the process list, scan the file system for files like /usr/sbin/kworker, /usr/lib/librctl.so, /etc/kworker.cfg, and /etc/init.d/skworker, and block the egress points.

*(The story was updated after publication to include a response from Zbtlink.)*

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

[Backdoor](https://thehackernews.com...