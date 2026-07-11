---
title: New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic
url: https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html
source: The Hacker News
date: 2026-07-10
fetch_date: 2026-07-11T05:04:37.183232
---

# New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New MODBEACON RAT Uses gRPC Streaming for Encrypted C2 Traffic](https://thehackernews.com/2026/07/new-modbeacon-rat-uses-grpc-streaming.html)

**Ravie Lakshmanan**Jul 10, 2026Malware / Enterprise Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKTCUzhkUq2Y7DPv0yS2FatrHQTcHfupRly6f5kSWyQU-So3FOjpC8pt_VKR4qo1SoUGR65ycOEQonbW5heKWj1g_A8qDy69YtWGZDO4m2t46Sip-jdPAlNs2fpRj-w1yd8WpyJpNFUpj1iTBO0X6fy3n9DJ4aEdsWaQz_tN-VV-PxDrufKZR9wkznmXJQ/s1700-e365/MODBEACON.jpg)

The China-linked cybercrime group known as **[Silver Fox](https://thehackernews.com/2026/07/suspected-china-nexus-hackers-use-fake.html)** has been attributed to a new Rust-based remote access trojan (RAR) called **MODBEACON**.

Chinese cybersecurity company QiAnXin said that while the threat cluster may appear like a low-sophistication, high-activity operation that propagates malware via counterfeit installers using SEO poisoning techniques, it belies their [true organizational structure](https://thehackernews.com/2025/09/silver-fox-exploits-microsoft-signed.html), which compromises multiple distributors.

"These distributors conduct activities across Asia using counterfeit software installers distributed through SEO campaigns, leveraging variants of Gh0st RAT and WinOS (ValleyRAT) trojan families," QiAnXin [said](https://ti.qianxin.com/blog/articles/operation-phnom-penh-silverfox-ghost-distributor-targets-specific-victims-with-modbeacon-en/).

One such campaign observed in mid-June 2026 involved a distributor delivering a previously undocumented modular RAT targeting technology, education, and state-owned enterprises in the country. MODBEACON's requested command-and-control (C2) infrastructure is hosted on Amazon and Cloudflare's Content Delivery Network (CDN).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The distributor is assessed to be a hybrid threat actor, acting as a composite of "cybercriminal arms dealer" and "traffic broker." One arm of its operations involves expanding its infection footprint across Asia through daily SEO operations for fraud business, while the other focuses on propagating advanced trojans, or renting high-value access to downstream customers, or establishing "criminal-on-criminal" schemes targeting the Cambodian gambling sector.

The newly discovered campaign combines social engineering, custom malware, and post-compromise tooling to establish long-term access while minimizing detection on infected hosts. The memory-resident malware functions as a remote implant capable of fetching additional modules, running operator commands, and maintaining encrypted communications with attacker infrastructure.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwAzKrmZ3t5tWfoBOn9nGVogfS5gMgnKK2YZcRl5VV33zCax0-xBlkeuYaShQezBelYRCOkjFtGhPk4shpXRBmLzMJp67KtLWQVchV_vRYzn7Wv2vXfd_zHBfVyTdVIjD7UyXTdnKcDYWTi7xn8MVdlBKBljrBgHByLxemMTPVTRAY8Qk0OIQ5Zf22tRm0/s1700-e365/code-exe.png)

"The Trojan is a professional and private C2 framework: the loader and beacon are separated, the configuration is injectable, the beacon employs a plugin-based architecture (native-v3 plugins with entry/init/fini RVA), and it uses gRPC tunnel streaming for communication," QiAnXin explained. "The overall engineering quality is high. Its core highlight is the reuse of the transport layer from an open-source anti-censorship proxy framework (Xray/V2Ray) as its C2 channel."

Like previous campaigns attributed to the Silver Fox intrusion ecosystem, the attack chain uses counterfeit domains advertising bogus installers for popular domestic software as lures to trick unsuspecting users into downloading malicious ZIP archives responsible for deploying the malware.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The core capabilities of MODBEACON include -

* Fingerprinting the host
* Loading plugins in memory
* Sending heartbeat messages
* Reporting the results of command execution
* Setting persistence using scheduled tasks

"This capability can be used for subsequent on-demand expansion of information theft, lateral movement, proxy forwarding, or other payloads," QiAnXin said.

The disclosure comes amid a gradual broadening of Silver Fox's arsenal, which has deployed malware families tracked as [Atlas RAT](https://thehackernews.com/2026/03/silver-fox-expands-asia-cyber-campaign.html), [ABCDoor](https://thehackernews.com/2026/05/silver-fox-deploys-abcdoor-malware-via.html), [RomulusLoader, and SilentRunLoader](https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html), indicating that the threat actor is actively refining its tradecraft.

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Cybercrime](https://thehackernews.com/search/label/Cybercrime...