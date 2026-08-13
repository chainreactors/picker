---
title: 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One
url: https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:20.604840
---

# 737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One

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

# [737 Chrome VPN Extensions Caught Routing Traffic Through Proxies. Check If You Have One](https://thehackernews.com/2026/08/737-chrome-vpn-extensions-caught.html)

**Ravie Lakshmanan**Aug 12, 2026Browser Security / Privacy

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI8aMtoRcWh4THmHEumFrk1X_t6xuq3Z6RsJwVKoyozs0nuRDIc7ffcIFNr5dFuUgTeeKZ0KLdeFoeHRRSFgqcTvK4VaO54Js2FADwBztN4Qlf0L8viPKGCY7lVEHF50K2xOaopCphCPL0ooDKna2E3S_4R4UzOsuh9m8dK4XQMo98_b6GjKqHRi_lm38i/s1700-e365/chrome-plugins.jpg)

A massive set of 737 free VPN and proxy extensions have been found to mainly target Russian-speaking users seeking access to blocked services with an aim to intercept browser traffic and route them through a proxy infrastructure.

The extensions, published across at least 40 Chrome Web Store developer accounts, racked up 75,486 installs. Of those identified, 274 have been found to impersonate 66 established VPN and privacy brands, including Proton VPN, NordVPN, Surfshark, AdGuard VPN, Browsec, ExpressVPN, CyberGhost, Windscribe, TunnelBear, Cloudflare's 1.1.1.1, and Google's Outline, per Socket.

The censorship circumvention extensions "route the user's entire browser session through SOCKS5 proxies operated by a single provider," security researcher Kush Pandya [said](https://socket.dev/blog/chrome-vpn-extension-impersonation). "520 of the 522 in the bulk corpus route browser traffic through the same SOCKS5 infrastructure."

The vast majority of the extensions have been found to route users' entire browser sessions by setting "chrome.proxy.settings" to a fixed SOCKS5 server on port 1082, placing the threat actor in an adversary-in-the-middle (AitM) position to observe browser destinations, source IP addresses, TLS SNI values, and any request body sent over plain HTTP.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Every extension that configures a proxy also comes with a bypass list that only includes loopback addresses (i.e., the localhost or 127.0.0.1"), meaning every other browser request is funnelled through the SOCKS5 relay on port 1082 once the user connects to the purported VPN service.

As many as 221 browser add-ons have been removed from the Chrome Web Store, while the remaining 516 extensions have been listed as active. The threat actor is said to be running a subscription VPN business in Russia, based on a 12-digit taxpayer number and the fact that some of them leak their Windows build path ("C:\Users\ollob\OneDrive\Документы\1.myxa-work\08.06.26\<domain>\<product>\<product>-release.zip").

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjCELZrm7I7HZn9wYOAJ3rKogOJbn-pE66qOVxovDD-ippNPsYcn-w6aFfFhWIZFX4ydU5725lCVUoP0OurRpavxIKKOKIRqNoYi4eQNc-isQ96bUmwuGoSPqGbccH6GmHjhcdQmANPgF5Qwy4KAcrTu6shi_b9eTi4O0VfXu-INecuQ669NgV8FX3CGR3/s1700-e365/vpns.jpg)

Ideally, the functionality is no different from a legitimate VPN or proxy service. The defining aspect of this activity is its attempt to impersonate established brands as opposed to offering it under their own name. Some of the other red flags include -

* Advertising paid tiers (or premium locations) that do not exist
* DNS-over-HTTPS blocklist evasion
* Failing every connection attempt while showing a complete fake interface, including a working connecting animation and status indicator
* Shipping an internal manual named "Промт для сотрудников" (translated to "Prompt for employees") that instructs them to avoid putting the domain directly into "chrome.proxy.settings" (and instead provide only the resolved IP) and refrain from using a domain from another extension without separate instructions
* Presence of comments that indicate a deliberate attempt to evade Chrome Web Store policies
* Adding a new remote-configuration layer after extension approval
* Attempts to game the Chrome Web Store review process by submitting identical justifications, stating "No data transmitted to external servers" or "No user tracking or logging"

"For each affected user, while the extension is connected, every request passes through a server the threat actor controls," Pandya said. "Whether the threat actor owns those proxy servers or resells capacity from an upstream provider is not resolvable from the extension code. If it resells, a further party is in the same position."

"What is established from the packages and from public infrastructure is the impersonation, the undisclosed proxy configuration, the non-existent premium servers, the false statements submitted to store reviewers, and the post-approval code substitution."

### Removed Chrome Extension Resurfaces with Monetization Scheme

The development comes as Netskope Threat Labs [highlighted](https://www.netskope.com/blog/ai-sidebar-extension-monetizes-its-own-updates) the return of a Google Chrome extension named "AI Sidebar with Deepseek, ChatGPT, Claude, and more." months after it was [removed](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html) for engaging in Prompt Poaching tactics.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The clean-then-poisoned update sequence, spread across versions 1.7.2.0 and 1.7.3.0, took place via Google's CRX content delivery network on July 31, 2026, pushing out a monetization scheme – a "surgical" 21-line addition – built around extension update and uninstall events.

"The extension released a benign update removing the data theft code and acknowledged its wrongdoing. After 2 weeks, it pulled the rug again with a new update," the cybersecurity company said.

"While it no longer contains the conversation-exfiltration code, it now contains a monetization payload that opens an affiliate link in a foreground browser tab every single time the extension updates and uninstalls. Additionally, it suppresses the redirection of DeepSeek users to ChatGPT."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_...