---
title: Eclipse Foundation Mandates Pre-Publish Security Checks for Open VSX Extensions
url: https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html
source: The Hacker News
date: 2026-02-04
fetch_date: 2026-02-05T04:10:22.529713
---

# Eclipse Foundation Mandates Pre-Publish Security Checks for Open VSX Extensions

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Eclipse Foundation Mandates Pre-Publish Security Checks for Open VSX Extensions](https://thehackernews.com/2026/02/eclipse-foundation-mandates-pre-publish.html)

**Ravie Lakshmanan**Feb 04, 2026Supply Chain Security / Secure Coding

[![Open VSX Extensions](data:image/png;base64... "Open VSX Extensions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXHoCQzirCKCGciIltPFi7LbjpANR75gNFmH6Lbsm5FOdl40UHJT4Xd3aWxxSdUe6r7wlqMWKuLSkUWmg11yfF7pnvIcETtkv5S5gtEeYFaHh8hKUoSicCcMvUn8UO9WUTVUDzSpEyXEaS01P6Wza6weGp2iqIbAnQKlN3I3f2_F2bGXSyssfhG2iIE591/s1700-e365/openvsx.jpg)

The Eclipse Foundation, which maintains the Open VSX Registry, has announced plans to enforce security checks before Microsoft Visual Studio Code (VS Code) extensions are published to the open-source repository to combat supply chain threats.

The move marks a shift from a reactive to a proactive approach to ensure that malicious extensions don't end up getting published on the Open VSX Registry.

"Up to now, the Open VSX Registry has relied primarily on post-publication response and investigation. When a bad extension is reported, we investigate and remove it," Christopher Guindon, director of software development at the Eclipse Foundation, [said](https://blogs.eclipse.org/post/christopher-guindon/strengthening-supply-chain-security-open-vsx).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

"While this approach remains relevant and necessary, it does not scale as publication volume increases and threat models evolve."

The change comes as open-source package registries and extension marketplaces have increasingly become attack magnets, enabling bad actors to target developers at scale through a variety of methods such as namespace impersonation and typosquatting. As recently as last week, Socket [flagged](https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html) an incident where a compromised publisher's account was used to push poisoned updates.

By implementing pre-publish checks, the idea is to limit the window of exposure and flag the following scenarios, as well as quarantine suspicious uploads for review instead of publishing them immediately -

* Clear cases of extension name or namespace impersonation
* Accidentally published credentials or secrets
* Known malicious patterns

It's worth noting that Microsoft already has a [similar multi-step vetting process](https://developer.microsoft.com/blog/security-and-trust-in-visual-studio-marketplace) in place for its Visual Studio Marketplace. This includes scanning incoming packages for malware, then rescanning every newly published package "shortly" after it's been published, and periodic bulk rescanning of all the packages.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

The extension verification program is expected to be rolled out in a staged fashion, with the maintainers using the month of February 2026 to monitor newly published extensions without blocking publication to fine-tune the system, reduce false positives, and improve feedback. The enforcement will begin next month.

"The goal and intent are to raise the security floor, help publishers catch issues early, and keep the experience predictable and fair for good-faith publishers," Guindon said.

"Pre-publish checks reduce the likelihood that obviously malicious or unsafe extensions make it into the ecosystem, which increases confidence in the Open VSX Registry as shared infrastructure."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Eclipse Foundation](https://thehackernews.com/search/label/Eclipse%20Foundation), [Malware](https://thehackernews.com/search/label/Malware), [Open Source](https://thehackernews.com/search/label/Open%20Source), [secure coding](https://thehackernews.com/search/label/secure%20coding), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [Visual Studio Code](https://thehackernews.com/search/label/Visual%20Studio%20Code)

Trending News

[![Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas](data:image/svg+xml;base64... "Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas")

Critical Grist-Core Vulnerability Allows RCE Attacks via Spreadsheet Formulas](https://thehackernews.com/2026/01/critical-grist-core-vulnerability.html)

[![Microsoft Office Zero-Day (CVE-2026-21509) - Emergency Patch Issued for Active Exploitation](data:image/svg+xml;base64... "Microsoft Office Zero-Day (CVE-2026-21509) - Emergency Patch Issued for Active Exploitation")

Microsoft Office Zero-Day (CVE-2026-21509) - Emergency Patch Issued for Active Exploitation](https://thehackernews.com/2026/01/microsoft-issues-emergency-patch-for.html)

[![ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services](data:image/svg+xml;base64... "ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services")

ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted Web Services](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)

[![Whats...