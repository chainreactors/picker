---
title: Firefox Zero-Day Under Attack: Update Your Browser Immediately
url: https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html
source: The Hacker News
date: 2024-10-11
fetch_date: 2025-10-06T19:01:15.049585
---

# Firefox Zero-Day Under Attack: Update Your Browser Immediately

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

# [Firefox Zero-Day Under Attack: Update Your Browser Immediately](https://thehackernews.com/2024/10/mozilla-warns-of-active-exploitation-in.html)

**Oct 10, 2024**Ravie LakshmananVulnerability / Browser Security

[![Mozilla](data:image/png;base64... "Mozilla")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggD4ZKyiD0qBm6TageDMjP09XKT1aXed9k-nrmfyx383YR6nBXGM_5WWbwisWlJ5i-Zj2iMBSDGJL9aBWYhNH5K-dtIVah5qhLlV8Wm1hLfIhkfnFRoBilYv_ENfiRxunSIZelKtYEDMXyfGhlvcGjYGZzJ3Rlj8nlg_jlXh1CVklXtTqUS6OLwo5E759H/s790-rw-e365/firefox.png)

Mozilla has revealed that a critical security flaw impacting Firefox and Firefox Extended Support Release (ESR) has come under active exploitation in the wild.

The vulnerability, tracked as [CVE-2024-9680](https://nvd.nist.gov/vuln/detail/CVE-2024-9680) (CVSS score: 9.8), has been described as a use-after-free bug in the Animation timeline component.

"An attacker was able to achieve code execution in the content process by exploiting a use-after-free in Animation timelines," Mozilla [said](https://www.mozilla.org/en-US/security/advisories/mfsa2024-51/) in a Wednesday advisory.

"We have had reports of this vulnerability being exploited in the wild."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Security researcher Damien Schaeffer from Slovakian company ESET has been credited with discovering and reporting the vulnerability.

The issue has been addressed in the following versions of the web browser -

* Firefox 131.0.2
* Firefox ESR 128.3.1, and
* Firefox ESR 115.16.1.

There are currently no details on how the vulnerability is being exploited in real-world attacks and the identity of the threat actors behind them.

That said, such remote code execution vulnerabilities could be weaponized in several ways, either as part of a [watering hole attack](https://thehackernews.com/2024/09/watering-hole-attack-on-kurdish-sites.html) targeting specific websites or by means of a [drive-by download](https://www.kaspersky.com/resource-center/definitions/drive-by-download) campaign that tricks users into visiting bogus websites.

Users are advised to update to the latest version to stay protected against active threats.

### Update

The Tor project has released an emergency update to the Tor Browser (version 13.5.7) to address CVE-2024-9680, which has come under active exploitation in the wild.

"Using this vulnerability, an attacker could take control of Tor Browser, but probably not deanonymize you in Tails," it [said](https://blog.torproject.org/new-release-tails-6-8-1/). "Mozilla is aware of this attack being used in the wild against Tor Browser users."

Mozilla, in a separate post on October 11, 2024, [said](https://blog.mozilla.org/security/2024/10/11/behind-the-scenes-fixing-an-in-the-wild-firefox-exploit/) it was sent by ESET a sample containing a "full exploit chain that allowed remote code execution on a user's computer." It also revealed that the fix was shipped within 25 hours of responsible disclosure.

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

[browser security](https://thehackernews.com/search/label/browser%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Malware](https://thehackernews.com/search/label/Malware)[software security](https://thehackernews.com/search/label/software%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[web browser](https://thehackernews.com/search/label/web%20browser)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Netwo...