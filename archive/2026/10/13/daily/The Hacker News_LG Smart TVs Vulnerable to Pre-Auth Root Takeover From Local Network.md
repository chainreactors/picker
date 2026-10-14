---
title: LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network
url: https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html
source: The Hacker News
date: 2026-10-13
fetch_date: 2026-10-14T06:53:24.975626
---

# LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network

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

# [LG Smart TVs Vulnerable to Pre-Auth Root Takeover From Local Network](https://thehackernews.com/2026/10/lg-smart-tvs-vulnerable-to-pre-auth.html)

**Swati Khandelwal**Oct 13, 2026Vulnerability / IoT Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgs2Z0M9u8vYqE8SBNBzfOGoc4Crog-_PBWeZNY8IprfYaa08ZyZ_PTfMhosBFrQNS_f1JecVbl_HEq7sutExV_92yaZWVIA51YD59JOFa_fKZQyEvpZNUxai8pgDrQX_Kp_wQqJoEFFQIFEwa2c3vhyphenhyphenQtU0U9w5XDwjSAij3BPz_qRs7-t0eu8ZssOZuE/s1700-nu-rw-lo-l85-e365/lg-tv.jpg)

Three vulnerabilities in LG's webOS can be chained to give an attacker on the same local network root access to certain smart TVs without a PIN or any interaction from the owner.

LG has issued a fix, according to an advisory [published](https://ssd-disclosure.com/lg-webos-sync-demo-preauth-rce/) by SSD Secure Disclosure on October 12.

The chain was tested on two TV models, the 32LQ636BPSA and the 27TQ600SW, running webOS 7.5.7-25 on firmware 04.54.40. Whether other models or firmware versions are affected is not known.

Owners of affected TVs should check for a firmware update. No workaround is available for those who cannot update yet.

The attack enters through a service that the TV exposes on port 3001, which is used by the LG ThinQ app for pairing. An attacker replays a manifest from sync-demo, a built-in app already on the device, signed with a test certificate the firmware trusts. A permission in the manifest causes the pairing service to skip the PIN prompt and hand over a privileged key.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

With that key, the attacker launches another built-in app, cmp-client, and points it to an attacker-controlled page. The app does not check where it navigates, and the loaded page keeps access to PalmServiceBridge, an internal interface to the TV's system services.

Through that bridge, the attacker calls the system logging service, pmlogd, passing shell commands through an input field the service does not check. Because pmlogd runs as root, the injected command runs as root.

This is not the first time the local network attack surface has led to root access on LG smart TVs. In 2024, Bitdefender disclosed [a different set of webOS vulnerabilities](https://thehackernews.com/2024/04/researchers-discover-lg-smart-tv.html) that also allowed unauthenticated access from the network, affected different components, and were patched in March 2024. A [separate chain demonstrated at TyphoonPWN 2025](https://ssd-disclosure.com/lg-webos-tv-path-traversal-authentication-bypass-and-full-device-takeover/) used a path traversal on a different port.

The chain was demonstrated by an anonymous researcher who won third place in the LG webOS category at TyphoonPWN 2026, held in Seoul in May. No CVE identifiers have been assigned, and no exploitation in the wild has been reported.

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

[Firmware Security](https://thehackernews.com/search/label/Firmware%20Security), [iot security](https://thehackernews.com/search/label/iot%20security), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

P7 DarkSword iOS Exploit Kit Adds Crypto Wallet Data Theft and Remote Commands](https://thehackernews.com/2026/10/p7-darksword-ios-exploit-kit-adds.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Cuts Live Internet Access for Internal AI Tests After Claude Exploits Injection Flaws](https://thehackernews.com/2026/10/anthropic-cuts-live-internet-access-for.html)

[![The Hacker News](data:image/svg+xml;base64...)

FBI Arrests Another ShinyHunters Suspect Reportedly Involved in Its Jobs Portal Hack](https://thehackernews.com/2026/10/fbi-arrests-another-shinyhunters.html)

[![The Hacker News](data:image/svg+xml;base64...)

TP-Link Sued by Four More U.S. States Over Router Security and China Ties](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html)

[![The Hacker News](data:image/svg+xml;base64...)

Anthropic Launches Free AI Vulnerability Scanner for Open-Source Projects](https://thehackernews.com/2026/10/anthropic-launches-free-ai.html)

[![The Hacker News](data:image/svg+xml;base64...)

GoBalance Flaw Lets Attackers Hijack .onion Addresses by Recovering Tor-Format Keys](https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html)

[![The Hacker News](data:image/svg+xml;base64...)

Three Teams Demonstrate Remote Hacks of Fully Patched Google Pixel 10 at Pwn2Own](https://thehackernews.com/2026/10/three-teams-demonstrate-remote-hacks-of.html)

[![The Hacker News](data:image/svg+xml;base64...)

ThreatsDay: Ransomware Affiliate Betrayal, WhatsApp RAT, Exposed Hacker Tools and 12 More Stories](https://thehackernews.com/2026/10/threatsday-ransomware-affiliate.html)

[![The Hacker News](data:image/svg+xml;base64...)

ARTEX AI Pentesting Tool Used in Data Theft Attacks on South Korean Financial Firms](https://thehackernews.com/2026/1...