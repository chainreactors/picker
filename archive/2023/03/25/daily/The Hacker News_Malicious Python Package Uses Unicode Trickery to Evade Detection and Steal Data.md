---
title: Malicious Python Package Uses Unicode Trickery to Evade Detection and Steal Data
url: https://thehackernews.com/2023/03/malicious-python-package-uses-unicode.html
source: The Hacker News
date: 2023-03-25
fetch_date: 2025-10-04T10:40:17.924810
---

# Malicious Python Package Uses Unicode Trickery to Evade Detection and Steal Data

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

# [Malicious Python Package Uses Unicode Trickery to Evade Detection and Steal Data](https://thehackernews.com/2023/03/malicious-python-package-uses-unicode.html)

**Mar 24, 2023**Ravie LakshmananDevSecOps / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLJLqr1E816GDkStOdptONV5SUoqyV6nFYOPbbCW-Z_NrowzrGOGp8HJKVJrVRnff-sul5DTkTb9ByNmfuRBv4_suK5RId2QU0FncGnu6Dqs0fBXRwmiHZFDE0fUlKoyOGtentUJlXtrfvDNQH3zWRHJS75yzVPOGbBBBRu75bHsMEv7s34VUKki9z/s790-rw-e365/hacking.png)

A malicious Python package on the Python Package Index (PyPI) repository has been found to use Unicode as a trick to evade detection and deploy an info-stealing malware.

The package in question, named [onyxproxy](https://pyup.io/packages/pypi/onyxproxy/), was uploaded to PyPI on March 15, 2023, and comes with capabilities to harvest and exfiltrate credentials and other valuable data. It has since been taken down, but not before attracting a total of [183 downloads](https://pepy.tech/project/onyxproxy).

According to software supply chain security firm Phylum, the package incorporates its malicious behavior in a setup script that's packed with thousands of seemingly legitimate code strings.

These strings include a mix of bold and italic fonts and are still readable and can be parsed by the Python interpreter, only to activate the execution of the stealer malware upon installation of the package.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"An obvious and immediate benefit of this strange scheme is readability," the company [noted](https://blog.phylum.io/malicious-actors-use-unicode-support-in-python-to-evade-detection). "Moreover, these visible differences do not prevent the code from running, which it does."

This is made possible owing to the use of Unicode variants of what appears to be the same character (aka [homoglyphs](https://en.wikipedia.org/wiki/Homoglyph)) to camouflage its true colors (e.g., self vs. 𝘀𝘦𝘭𝘧) among innocuous-looking functions and variables.

The use of Unicode to inject vulnerabilities into source code was previously disclosed by Cambridge University researchers Nicholas Boucher and Ross Anderson in an attack technique dubbed [Trojan Source](https://thehackernews.com/2021/11/new-trojan-source-technique-lets.html).

What the method lacks in sophistication, it makes up for it by creating a novel piece of obfuscated code, despite exhibiting telltale signs of copy-paste efforts from other sources.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development highlights [continued attempts](https://thehackernews.com/2023/02/python-developers-warned-of-trojanized.html) on part of threat actors to find new ways to slip through string-matching based defenses, leveraging "how the Python interpreter handles Unicode to obfuscate their malware."

On a related note, Canadian cybersecurity company PyUp [detailed](https://pyup.io/posts/pyup-discovers-new-malicious-pypi-packages/) the discovery of three new fraudulent Python packages – aiotoolbox, asyncio-proxy, and pycolorz – that were downloaded cumulatively over 1,000 times and designed to retrieve obfuscated code from a remote server.

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

[DevSecOps](https://thehackernews.com/search/label/DevSecOps)[Malware](https://thehackernews.com/search/label/Malware)[PyPI Repository](https://thehackernews.com/search/label/PyPI%20Repository)[Python](https://thehackernews.com/search/label/Python)[Python Package Index](https://thehackernews.com/search/label/Python%20Package%20Index)[software security](https://thehackernews.com/search/label/software%20security)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Atta...