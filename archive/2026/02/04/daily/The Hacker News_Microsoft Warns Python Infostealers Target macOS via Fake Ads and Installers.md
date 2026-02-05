---
title: Microsoft Warns Python Infostealers Target macOS via Fake Ads and Installers
url: https://thehackernews.com/2026/02/microsoft-warns-python-infostealers.html
source: The Hacker News
date: 2026-02-04
fetch_date: 2026-02-05T04:10:22.385701
---

# Microsoft Warns Python Infostealers Target macOS via Fake Ads and Installers

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

# [Microsoft Warns Python Infostealers Target macOS via Fake Ads and Installers](https://thehackernews.com/2026/02/microsoft-warns-python-infostealers.html)

**Ravie Lakshmanan**Feb 04, 2026Malvertising / Infostealer

[![macOS via Fake Ads and Installers](data:image/png;base64... "macOS via Fake Ads and Installers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitGprkuP7SdfHIWnVVo7pZJ941c_TOVgrrZCPM9BosshMNfva3UbHAZG791-XufHdEc6hGRcFX3Ucak4XRDOgoSa4KCyPHeuxwWKr8y_LNLmo6mOqxgKvLOfbcAVDoACJ9MTSDkq25noRCdjHTBZVtGCulkPK5cjRBsQGf0LQQQkUujppEe6K4i0lq7VZF/s1700-e365/macos-malware.jpg)

Microsoft has warned that information-stealing attacks are "rapidly expanding" beyond Windows to target Apple macOS environments by leveraging cross-platform languages like Python and abusing trusted platforms for distribution at scale.

The tech giant's Defender Security Research Team said it observed macOS-targeted infostealer campaigns using social engineering techniques such as [ClickFix](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html) since late 2025 to distribute disk image (DMG) installers that deploy stealer malware families like Atomic macOS Stealer ([AMOS](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html)), [MacSync](https://thehackernews.com/2025/12/new-macsync-macos-stealer-uses-signed.html), and [DigitStealer](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploited-chinas.html#:~:text=New%20DigitStealer%20macOS%20Malware%20Spotted).

The campaigns have been found to use techniques like fileless execution, native macOS utilities, and AppleScript automation to facilitate data theft. This includes details like web browser credentials and session data, iCloud Keychain, and developer secrets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The starting point of these attacks is often a malicious ad, often served through Google Ads, that redirects users searching for tools like DynamicLake and artificial intelligence (AI) tools to fake sites that employ ClickFix lures, tricking them into infecting their own machines with malware.

"Python-based stealers are being leveraged by attackers to rapidly adapt, reuse code, and target heterogeneous environments with minimal overhead," Microsoft [said](https://www.microsoft.com/en-us/security/blog/2026/02/02/infostealers-without-borders-macos-python-stealers-and-platform-abuse/). "They are typically distributed via phishing emails and collect login credentials, session cookies, authentication tokens, credit card numbers, and crypto wallet data."

One such stealer is [PXA Stealer](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html), which is linked to Vietnamese-speaking threat actors and is capable of harvesting login credentials, financial information, and browser data. The Windows maker said it identified two PXA Stealer campaigns in October 2025 and December 2025 that used phishing emails for initial access.

Attack chains involved the use of registry Run keys or scheduled tasks for persistence and Telegram for command-and-control communications and data exfiltration.

In addition, bad actors have been observed weaponizing popular messaging apps like WhatsApp to distribute malware like [Eternidade Stealer](https://thehackernews.com/2025/11/python-based-whatsapp-worm-spreads.html) and gain access to financial and cryptocurrency accounts. Details of the campaign were publicly documented by LevelBlue/Trustwave in November 2025.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

Other stealer-related attacks have revolved around fake PDF editors like Crystal PDF that are distributed via malvertising and search engine optimization (SEO) poisoning through Google Ads to deploy a Windows-based stealer that can stealthily collect cookies, session data, and credential caches from Mozilla Firefox and Chrome browsers.

To counter the threat posed by infostealer threats, organizations are advised to educate users on social engineering attacks like malvertising redirect chains, fake installers, and ClickFix‑style copy‑paste prompts. It's also advised to monitor for suspicious Terminal activity and access to the iCloud Keychain, as well as inspect network egress for POST requests to newly registered or suspicious domains.

"Being compromised by infostealers can lead to data breaches, unauthorized access to internal systems, business email compromise (BEC), supply chain attacks, and ransomware attacks," Microsoft said.

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

[Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Infostealer](https://thehackernews.com/search/label/Infostealer), [MacOS](https://thehackernews.com/search/label/MacOS), [malvertising](https://thehackernews.com/search/label/malvertising), [Malware](https://thehackernews.com/search/label/Malware), [Phishing](https://thehackernews.com/search/label/Phishing), [social engineering](https://thehackernews.com/search/label/social%20engineering), [Threat Intelligence](https://thehackernews.com/search/...