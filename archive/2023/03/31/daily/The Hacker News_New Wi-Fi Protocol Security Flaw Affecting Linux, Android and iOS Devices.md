---
title: New Wi-Fi Protocol Security Flaw Affecting Linux, Android and iOS Devices
url: https://thehackernews.com/2023/03/new-wi-fi-protocol-security-flaw.html
source: The Hacker News
date: 2023-03-31
fetch_date: 2025-10-04T11:18:01.867589
---

# New Wi-Fi Protocol Security Flaw Affecting Linux, Android and iOS Devices

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

# [New Wi-Fi Protocol Security Flaw Affecting Linux, Android and iOS Devices](https://thehackernews.com/2023/03/new-wi-fi-protocol-security-flaw.html)

**Mar 30, 2023**Ravie LakshmananNetwork Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirzH1Mbgznd5JkWU4XTQQiyKow69Kqjg70OlkzG37-8ygvdifznnH1uLbPnDx0WglC7Y0JNexGJVc9nh8ahiHlRh_q1RPXUmn-2UrvJMjrKV2MrQIOpdTXK2HdfF65zfCasupb7ycu7qbCvao6QhkMD4zIcUJVlEjM9mA6mziuVkLDLW4RyLoK0vE_/s790-rw-e365/mac.png)

A group of academics from Northeastern University and KU Leuven has disclosed a fundamental design flaw in the IEEE 802.11 Wi-Fi protocol standard, impacting a wide range of devices running Linux, FreeBSD, Android, and iOS.

Successful exploitation of the shortcoming could be abused to hijack TCP connections or intercept client and web traffic, researchers Domien Schepers, Aanjhan Ranganathan, and Mathy Vanhoef said in a paper published this week.

The [approach](https://www.blackhat.com/asia-23/briefings/schedule/index.html#sweet-dreams-abusing-sleep-mode-to-break-wi-fi-encryption-and-disrupt-wpa-networks-30942) exploits [power-save mechanisms](https://jwcn-eurasipjournals.springeropen.com/articles/10.1186/s13638-016-0524-5) in endpoint devices to trick access points into leaking [data frames](https://en.wikipedia.org/wiki/802.11_Frame_Types) in plaintext, or encrypt them using [an all-zero key](https://www.eset.com/int/kr00k/).

"The unprotected nature of the power-save bit in a frame's header [...] also allows an adversary to force queue frames intended for a specific client resulting in its disconnection and trivially executing a denial-of-service attack," the researchers noted.

In other words, the goal is to leak frames from the access point destined to a victim client station by taking advantage of the fact that most Wi-Fi stacks do not adequately dequeue or purge their transmit queues when the security context changes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Besides manipulating the security context to leak frames from the queue, an attacker can override the client's security context used by an access point to receive packets intended for the victim. This attack pre-supposes that the targeted party is connected to a hotspot-like network.

"The core idea behind the attack is that the manner in which clients are authenticated is unrelated to how packets are routed to the correct Wi-Fi client," Vanhoef [explained](https://github.com/vanhoefm/macstealer).

"A malicious insider can abuse this to intercept data towards a Wi-Fi client by disconnecting a victim and then connecting under the MAC address of the victim (using the credentials of the adversary). Any packets that were still underway to the victim, such website data that the victim was still loading, will now be received by the adversary instead."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhe9Yo6Tu8eqbXRwEr2FgDoCwaWNYRaMG8QDchQK9K4UF_7eKUf6PneNufzwtCv9GhiaN6Jyg0-iFmd8hXhqTVlQbBTtbhluVGbpNksmL2XvD0kHQXIlFPylaBLqYdHWdXNYeWZq0_rkYPAl3pORSRkrQ7xbLxx7-_gEvCbtuFJc_2nevL6mP8wiOja/s790-rw-e365/wifihacking.png)

Cisco, in an informational advisory, [described](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-wifi-ffeb-22epcEWu) the vulnerabilities as an "opportunistic attack and the information gained by the attacker would be of minimal value in a securely configured network."

However, the company acknowledged that the attacks presented in the study may be successful against Cisco Wireless Access Point products and Cisco Meraki products with wireless capabilities.

To reduce the probability of such attacks, it's recommended to implement transport layer security (TLS) to encrypt data in transit and apply policy enforcement mechanisms to restrict network access.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings arrive months after researchers Ali Abedi and Deepak Vasisht demonstrated a location-revealing privacy attack called [Wi-Peep](https://dl.acm.org/doi/abs/10.1145/3495243.3560530) that also exploits the 802.11 protocol's power-saving mechanism to localize target devices.

The research also follows other recent studies that have leveraged the Google Maps' [Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview) to launch [location spoofing attacks](https://dl.acm.org/doi/abs/10.1145/3548606.3560623) in urban areas, not to mention use Wi-Fi signals to [detect and map human movement](https://arxiv.org/abs/2301.00250) in a room.

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

[hacking news](https://thehackernews.com/search/label/hacking%20news)[network security](https://thehackernews.com/search/label/network%20security)[wifi hacking](https://thehackernews.com/search/label/wifi%20hacking)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Co...