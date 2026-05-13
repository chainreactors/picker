---
title: New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots
url: https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html
source: The Hacker News
date: 2026-05-12
fetch_date: 2026-05-13T05:47:29.737878
---

# New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots

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

# [New TrickMo Variant Uses TON C2 and SOCKS5 to Create Android Network Pivots](https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html)

**Ravie Lakshmanan**May 12, 2026Malware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbBy7H5qvorFUmJqREACqqxVC0ogVq88dP8wLyKyUPF9fCowpUSkb7foEsEPDALt0ccCpcJc6PXCJjFmQo0oX3furU-cYPULBa0-pjpiLGV04JD6kr4G0VIrvFoJo54WmgjU1YocsquA15N3hxDmwt4i82QpYdil7F4fI0SMFVv9YCkbqqGKjIi-dEmcIx/s1700-e365/tricks.jpg)

Cybersecurity researchers have flagged a new version of the **TrickMo** Android banking trojan that uses The Open Network (TON) for command-and-control (C2).

The new variant, observed by ThreatFabric between January and February 2026, has been observed actively targeting banking and cryptocurrency wallet users in France, Italy, and Austria.

"TrickMo relies on a runtime-loaded APK  (dex.module), used also by the previous variant, but updated with new features adding new network-oriented functionality, including reconnaissance, SSH tunnelling, and SOCKS5 proxying capabilities that allow infected devices to function as programmable network pivots and traffic-exit nodes," the Dutch mobile security company [said](https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app) in a report shared with The Hacker News.

TrickMo is the name assigned to a device takeover (DTO) malware that's been active in the wild since late 2019. It was [first flagged by CERT-Bund and IBM X-Force](https://thehackernews.com/2020/03/trickbot-two-factor-mobile-malware.html), describing its ability to abuse Android's accessibility services to hijack one-time passwords (OTPs).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

It's also [equipped](https://thehackernews.com/2024/10/trickmo-banking-trojan-can-now-capture.html) with a wide range of features to phish for credentials, log keystrokes, record screen, facilitate live screen streaming, intercept SMS messages, essentially granting the operator complete remote control of the device.

The latest versions, labeled TrickMo C, are distributed via phasing websites and dropper apps, the latter of which serve as a conduit for a dynamically loaded APK ("dex.module") that's retrieved at runtime from attacker-controlled infrastructure. A notable shift in the architecture entails the use of the TON decentralized blockchain for stealthy C2 communications.

"TrickMo carries an embedded native TON proxy that the host APK starts on a loopback port at process start," ThreatFabric said. "The bot's HTTP client is wired through that proxy, so every outbound command-and-control request is addressed to an .adnl hostname and resolved through the TON overlay."

Dropper apps containing the malware masquerade as adult-friendly versions of TikTok through Facebook, whereas the actual malware impersonates Google Play Services -

* [com.app16330.core20461](https://www.virustotal.com/gui/file/01889a9ec2abecb73e5e8792be68a4e3bc7dcbe1c3f19ac06763682d63aa8c21) or com.app15318.core1173 (Dropper)
* uncle.collop416.wifekin78 or nibong.lida531.butler836 (TrickMo)

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFZKSyOYh-8A_N96kM87oVcGaBo1V72axVpZNUDxei9obnpsskTgNaSWNA-hxOP0HBH2qjqsPiHCflUVQnF0rwiIN60Zw6pCCyVHLaLjHUUOnvOVVcKrB_vV-8rla7FKIGLYmRRyazfuY5e9g2RVilnHHeO5uRGARDixlWO-XPSESXNwWjYAdQAVEeiz3O/s1700-e365/trick.png)

While previous iterations of "dex.module" implemented the accessibility-driven remote control functionality through a socket.io-based channel, the new version utilizes a network-operative subsystem that turns the malware into a tool for managed foothold than a traditional banking trojan.

The subsystem supports commands like curl, dnslookup, ping, telnet, and traceroute, giving the attacker a "remote shell-equivalent for network reconnaissance from the victim's network position, including any internal corporate or home network the device is currently associated with," per ThreatFabric.

Another important feature is a SOCKS5 proxy that turns the compromised device into a network exit node that routes malicious traffic, while defeating IP-based fraud-detection signatures on banking, e-commerce and cryptocurrency exchange services.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Furthermore, TrickMo includes two dormant features that bundle the Pine hooking framework and declare extensive NFC-related permissions. But neither of them are actually implemented. This likely indicates the core developers are looking to expand on the trojan's capabilities in the future.

"Instead of relying on conventional DNS and public internet infrastructure, the malware communicates through .adnl endpoints routed via an embedded local TON proxy, reducing the effectiveness of traditional takedown and network-blocking efforts while making the traffic blend with legitimate TON activity," ThreatFabric said.

"This latest variant also expands the operational role of infected devices through SSH tunnelling and authenticated SOCKS5 proxying, effectively turning compromised phones into programmable network pivots and traffic-exit nodes whose connections originate from the victim’s own network environment."

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
[**Share on Hacker ...