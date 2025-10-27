---
title: VirusTotal Finds 44 Undetected SVG Files Used to Deploy Base64-Encoded Phishing Pages
url: https://thehackernews.com/2025/09/virustotal-finds-44-undetected-svg.html
source: The Hacker News
date: 2025-09-06
fetch_date: 2025-10-02T19:46:13.450830
---

# VirusTotal Finds 44 Undetected SVG Files Used to Deploy Base64-Encoded Phishing Pages

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

# [VirusTotal Finds 44 Undetected SVG Files Used to Deploy Base64-Encoded Phishing Pages](https://thehackernews.com/2025/09/virustotal-finds-44-undetected-svg.html)

**Sep 05, 2025**Ravie LakshmananMalware / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZvs8na9Ip78ucoHGvbHyiSCVP5nGr3Wy3A7cGn5gYzvSN6rU4ydJzqHK8499QP3OmYhhVuYUD5MHK3hPewmyBDkr_ZxbvC9OdIWby5B-7IqDnnMFMG2MuH0d538_rvZiYiUydNQNM1oNrE_vCDOuC9infEE2Z2OMY3_JwPWR5inApa79OCvBslf9rW9WY/s790-rw-e365/vt.jpg)

Cybersecurity researchers have flagged a new malware campaign that has leveraged Scalable Vector Graphics (SVG) files as part of phishing attacks impersonating the Colombian judicial system.

The SVG files, according to [VirusTotal](https://blog.virustotal.com/2025/09/uncovering-colombian-malware-campaign.html), are distributed via email and designed to execute an embedded JavaScript payload, which then decodes and injects a Base64-encoded HTML phishing page masquerading as a portal for Fiscalía General de la Nación, the Office of the Attorney General of Colombia.

The page then simulates an official government document download process with a fake progress bar, while it stealthily triggers the download of a ZIP archive in the background. The exact nature of the ZIP file was not disclosed.

The Google-owned malware scanning service said it found 44 unique SVG files, all of which have remained undetected by antivirus engines, owing to the use of techniques like obfuscation, polymorphism, and large amounts of junk code to evade static detection methods.

In all, as many as 523 SVG files have been detected in the wild, with the earliest sample dating back to August 14, 2025.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"Looking deeper, we saw that the earliest samples were larger, around 25 MB, and the size decreased over time, suggesting the attackers were evolving their payloads," VirusTotal said.

The disclosure comes as cracked versions of legitimate software and ClickFix-style tactics are being used to lure users into infecting their Apple macOS systems with an information stealer called Atomic macOS Stealer ([AMOS](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html)), exposing businesses to credential stuffing, financial theft, and other follow-on attacks.

"AMOS is designed for broad data theft, capable of stealing credentials, browser data, cryptocurrency wallets, Telegram chats, VPN profiles, keychain items, Apple Notes, and files from common folders," Trend Micro [said](https://www.trendmicro.com/en_us/research/25/i/an-mdr-analysis-of-the-amos-stealer-campaign.html). "AMOS shows that macOS is no longer a peripheral target. As macOS devices gain ground in enterprise settings, they have become a more attractive and lucrative focus for attackers."

The attack chain essentially involves targeting users looking for cracked software on sites like haxmac[.]cc, redirecting them to bogus download links that provide installation instructions designed to trick them into running malicious commands on the Terminal app, thus triggering the deployment of AMOS.

It's worth noting that Apple prevents the installation of .dmg files lacking proper notarization due to macOS's Gatekeeper protections, which require the application packages to be signed by an identified developer and notarized by Apple.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-RWvpyVATk4TS8auodkHf2csB_XHvraXdBlwNo3R5xxGndjvy0pGBDYSdEdpJZTy2V6wB62bp1menRZl7sWRKhviiKmV43DTRfuTJyZlLU8WV-vE7LMUkKSmzIgQ5C05_ZtmdU17QpjKfMplGqQtvUPiQT5hCJJqZ9v0QxyoROHbsrY_POQJBpP8wiZTY/s790-rw-e365/haxmax.png)

"With the release of macOS Sequoia, attempts to install malicious or unsigned .dmg files, such as those used in AMOS campaigns, are blocked by default," the company added. "While this doesn't eliminate the risk entirely, especially for users who may bypass built-in protections, it raises the barrier for successful infections and forces attackers to adapt their delivery methods."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This is why threat actors are increasingly banking on ClickFix, as it allows the stealer to be installed on the machine using Terminal by means of a curl command specified in the software download page.

"While macOS Sequoia's enhanced Gatekeeper protections successfully blocked traditional .dmg-based infections, threat actors quickly pivoted to terminal-based installation methods that proved more effective in bypassing security controls," Trend Micro said. "This shift highlights the importance of defense-in-depth strategies that don't rely solely on built-in operating system protections."

The development also follows the discovery of a "sprawling cyber campaign" that's targeting gamers on the lookout for cheats with [StealC](https://thehackernews.com/2025/01/mintsloader-delivers-stealc-malware-and.html) stealer and crypto theft malware, netting the threat actors more than $135,000.

Per [CyberArk](https://www.cyberark.com/resources/threat-research-blog/cheaters-never-win-large-scale-campaign-targets-gamers-who-cheat-with-stealc-and-cryptojacking), the activity is notable for leveraging StealC's loader capabilities to download additional payloads, in this case, a cryptocurrency stealer that can siphon digital assets from users on infected machines.

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
...