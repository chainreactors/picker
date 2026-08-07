---
title: Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses
url: https://thehackernews.com/2026/08/webkit-proxy-bypasses-can-expose-real.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:25.473363
---

# Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses

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

# [Apple iCloud Private Relay Can Expose Real IPs Through WebKit Proxy Bypasses](https://thehackernews.com/2026/08/webkit-proxy-bypasses-can-expose-real.html)

**Ravie Lakshmanan**Aug 06, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi53VbynsVNPTCihg9qrqybX7Yu90yM3Tm7KlJnJCHz2_MOUQPyJys1uK6H5QkVqxGekck8qe-pA55tcy19IDYQ4_ndOKasvoaFiPJCI_NJClfHv6G14Ga5P_FPr0zyNijjRMBM-GBlt-XYRqCGAcrZxm9ETsAAu4kPh829ZKABQonHDlx2GuWG9-B-V383/s1700-e365/apple-relay.jpg)

Cybersecurity researchers have [disclosed](https://mysk.blog/2026/08/04/webkit-proxy-icloud-private-relay-ip-leak/) a security issue with Apple's iCloud Private Relay tool that can expose a user's real IP address.

Introduced with iOS 15, iCloud Private Relay [employs](https://thehackernews.com/2021/06/top-10-privacy-and-security-features.html) a [dual-hop architecture](https://support.apple.com/102602) to ensure users' privacy by routing their Safari web traffic through two relays so that no single third-party, including Apple, can determine where the request is originating from and what sites are being visited. It's available as part of the iCloud+ subscription.

Researchers Talal Haj Bakry and Tommy Mysk, who found the issue, said the problem is rooted in three features in Apple's WebKit: DNS prefetching, WebAuthn Related Origin Requests, and WebTransport. WebKit is the default web browser engine used by Safari and all third-party browsers on iOS and iPadOS, such as Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, and others.

The three features "bypass the configured proxy and send traffic directly from the device, which exposes the user's real network," the researchers said. "The same leaks also affect Apple's iCloud Private Relay."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The issues also affect macOS, as well as any other WebKit-based browser that relies on WebKit's proxy configuration APIs. In each of these cases, the device's actual IP address is leaked -

* [DNS prefetching](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/dns-prefetch), which resolves hostnames through the device's normal DNS path instead of the proxy set by the browser
* WebAuthn Related Origin Requests, which make the operating system's credential service fetch a validation file directly from the device
* WebTransport, which opens a direct HTTP/3 connection and bypasses the proxy

Given that WebAuthn lets users log into websites using passkeys, any website that claims to support the web standard can view a user's real IP address even if iCloud Private Relay is on.

"Any website can configure WebAuthn (the API used for passkeys) in a way that causes WebKit to reveal the browser's real IP address, bypassing both proxy configurations and iCloud Private Relay in Safari," Mysk told The Hacker News.

"Because of the nature of the bug, the website has to deliberately exploit it to associate the user's current browsing session with the leaked IP address. This does not require any user interaction or the use of passkeys."

A proof-of-concept (PoC) website named "[leaks.psylo[.]app](https://leaks.psylo.app/)" has been made available for anyone to check if their real IP address leaks, even when Private Relay is on.

While the "HTTPS Traffic" section refers to the regular network traffic that WebKit generates when connecting to a website, "Possible IP leaks" shows how the device's real IP address can leak out of the configured proxy path.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

"We use the term 'possible' because not every browser is affected (for example, desktop Chrome is not), and the leaks are also mitigated when the user is connected to a VPN," Mysk added.

Apple did not immediately respond to a request for comment. But the company [told](https://www.404media.co/apples-private-relay-is-exposing-users-real-ip-addresses/) 404 Media that it's investigating the researchers' report.

This is not the first time security issues have been discovered in iCloud Private Relay. Shortly after the feature was released in 2021, FingerprintJS [highlighted](https://thehackernews.com/2021/09/apples-new-icloud-private-relay-service.html) a WebRTC-based mechanism that leaked a client's real IP address.

The disclosure comes a little over a month after Cupertino [addressed](https://thehackernews.com/2026/07/apple-fixes-hide-my-email-bug-that.html) another vulnerability in its Hide My Email service that enabled users' real email addresses to be unmasked under certain conditions, undermining the feature's privacy guarantees.

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

[Apple](https://thehackernews.com/search/label/Apple), [Authentication Security](https://thehackernews.com/search/label/Authentication%20Security), [browser security](https://thehackernews.com/search/label/browser%20security), [ios security](https://thehackernews.com/search/label/ios%20security), [MacOS](https://thehackernews.com/search/label/MacOS), [mobile security](https://thehackernews.com/search/label/mobile%20security), [network security](https://thehackernews.com/search/label/network%20security), [Privacy](https://thehackernews.com/search/label/Privacy), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![New Bit...