---
title: Meta Details WhatsApp and Messenger Interoperability to Comply with EU's DMA Regulations
url: https://thehackernews.com/2024/03/meta-details-whatsapp-and-messenger.html
source: The Hacker News
date: 2024-03-09
fetch_date: 2025-10-04T12:12:31.773596
---

# Meta Details WhatsApp and Messenger Interoperability to Comply with EU's DMA Regulations

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

# [Meta Details WhatsApp and Messenger Interoperability to Comply with EU's DMA Regulations](https://thehackernews.com/2024/03/meta-details-whatsapp-and-messenger.html)

**Mar 08, 2024**Ravie LakshmananInteroperability / Encryption

[![WhatsApp and Messenger Interoperability](data:image/png;base64... "WhatsApp and Messenger Interoperability")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjddpt4dmAATHeNFzsgNTW_un3Jn3O4q0WiAYK_pVS6g2MuUyO4T8gdSrTfkXIJpBHPS4o-g_iVRJSeDVOZowtCZoN8QOc1-Ty-FO9uzyqmHsd7QiqR4vf7rdR7n-SKfClYd6TmoiGMgRvf-iQUtIbCq1k1hz7YgIJ7mD2bd9GR0dO503sFpw3pf3rZudZj/s790-rw-e365/whatsapp.jpg)

Meta has offered details on how it intends to implement interoperability in WhatsApp and Messenger with third-party messaging services as the Digital Markets Act (DMA) went into effect in the European Union.

"This allows users of third-party providers who choose to enable interoperability (interop) to send and receive messages with opted-in users of either Messenger or WhatsApp – both designated by the European Commission (EC) as being required to independently provide interoperability to third-party messaging services," Meta's Dick Brouwer [said](https://engineering.fb.com/2024/03/06/security/whatsapp-messenger-messaging-interoperability-eu/).

DMA, which officially [became enforceable](https://ec.europa.eu/commission/presscorner/detail/en/ip_24_1342) on March 7, 2024, requires companies in gatekeeper positions – Apple, Alphabet, Meta, Amazon, Microsoft, and ByteDance – to meet certain obligations as part of the European Commission's efforts to clamp down on anti-competitive practices from tech players, level the playing field, as well as compel them to open some of their services to competitors.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As part of its efforts to comply with the landmark regulations, the social media giant said it expects third-party providers to use the [Signal Protocol](https://github.com/signalapp/libsignal), which is used in both WhatsApp and Messenger for end-to-end encryption (E2EE).

The third-parties are also required to package the encrypted communications into [message stanzas](https://xmpp.org/extensions/xep-0226.html) in eXtensible Markup Language (XML). Should the message contain media content, an encrypted version is downloaded by Meta clients from the third-party messaging servers using a Meta proxy service.

The company is also proposing what's called a "plug-and-play" model that allows third-party providers to connect to its infrastructure for achieving interoperability.

"Taking the example of WhatsApp, third-party clients will connect to WhatsApp servers using our protocol (based on the Extensible Messaging and Presence Protocol – XMPP)," Brouwer said.

"The WhatsApp server will interface with a third-party server over HTTP in order to facilitate a variety of things including authenticating third-party users and push notifications."

Furthermore, third-party clients are mandated to execute a WhatsApp Enlistment API when opting into its network, alongside providing cryptographic proof of their ownership of the third-party user-visible identifier when connecting or a third-party user registers on WhatsApp or Messenger.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The technical architecture also has provisions for a third-party provider to add a proxy or an intermediary between their client and the WhatsApp server to provide more information about the kinds of content their client can receive from the WhatsApp server.

"The challenge here is that WhatsApp would no longer have direct connection to both clients and, as a result, would lose connection level signals that are important for keeping users safe from spam and scams such as TCP fingerprints," Brouwer noted.

"This approach also exposes all the chat metadata to the proxy server, which increases the likelihood that this data could be accidentally or intentionally leaked."

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

[DMA Compliance](https://thehackernews.com/search/label/DMA%20Compliance)[end-to-end encryption](https://thehackernews.com/search/label/end-to-end%20encryption)[Interoperability](https://thehackernews.com/search/label/Interoperability)[Messaging Service](https://thehackernews.com/search/label/Messaging%20Service)[Meta](https://thehackernews.com/search/label/Meta)[Plug-and-Play](https://thehackernews.com/search/label/Plug-and-Play)[Privacy](https://thehackernews.com/search/label/Privacy)[Proxy server](https://thehackernews.com/search/label/Proxy%20server)[push notification](https://thehackernews.com/search/label/push%20notification)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical E...