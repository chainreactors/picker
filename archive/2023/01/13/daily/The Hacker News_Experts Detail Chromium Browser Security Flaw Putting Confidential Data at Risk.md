---
title: Experts Detail Chromium Browser Security Flaw Putting Confidential Data at Risk
url: https://thehackernews.com/2023/01/experts-detail-chromium-browser.html
source: The Hacker News
date: 2023-01-13
fetch_date: 2025-10-04T03:46:50.178538
---

# Experts Detail Chromium Browser Security Flaw Putting Confidential Data at Risk

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

# [Experts Detail Chromium Browser Security Flaw Putting Confidential Data at Risk](https://thehackernews.com/2023/01/experts-detail-chromium-browser.html)

**Jan 12, 2023**Ravie LakshmananBrowser Security / Data Safety

[![Chromium Browser Security](data:image/png;base64... "Chromium Browser Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg4JB1ilrp9TgAvbmVT9xJuRCtIvyD6PSQE8jZBBkumgoQoCQ6O8Nqao5MOTgyBCgKC0yWZBJ7EZsk2gBuCTkn0CkeOkzHbf3GAYvpUUAea5UHM01cnDnGDTrFY2KCDCefol49hVB-GiRhDXLVqMaoXcE4AxGEAaSdH_uhWQp-XRgdMn9cROF1RCP3H/s790-rw-e365/chrome-hacking.gif)

Details have emerged about a now-patched vulnerability in Google Chrome and Chromium-based browsers that, if successfully exploited, could have made it possible to siphon files containing confidential data.

"The issue arose from the way the browser interacted with [symlinks](https://en.wikipedia.org/wiki/Symbolic_link) when processing files and directories," Imperva researcher Ron Masas [said](https://www.imperva.com/blog/google-chrome-symstealer-vulnerability/). "Specifically, the browser did not properly check if the symlink was pointing to a location that was not intended to be accessible, which allowed for the theft of sensitive files."

Google characterized the medium-severity issue (CVE-2022-3656) as a case of insufficient data validation in File System, [releasing](https://chromereleases.googleblog.com/2022/10/stable-channel-update-for-desktop_25.html) [fixes](https://chromereleases.googleblog.com/2022/11/stable-channel-update-for-desktop_29.html) for it in versions 107 and 108 released in October and November 2022.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Dubbed SymStealer, the vulnerability, at its core, relates to a type of weakness known as symbolic link (aka symlink) following, which [occurs](https://cwe.mitre.org/data/definitions/61.html) when an attacker abuses the feature to bypass the file system restrictions of a program to operate on unauthorized files.

Imperva's [analysis](https://bugs.chromium.org/p/chromium/issues/detail?id=1345275) of Chrome's file handling mechanism (and by extension Chromium) found that when a user directly dragged and dropped a folder onto a [file input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file), the browser resolved all the symlinks recursively without presenting any warning.

In a hypothetical attack, a threat actor could trick a victim into visiting a bogus website and downloading a ZIP archive file containing a symlink to a valuable file or folder on the computer, such as wallet keys and credentials.

When the same symlink file is uploaded back to the website as part of the infection chain – e.g., a crypto wallet service that prompts users to upload their recovery keys – the vulnerability could be exploited to access the actual file storing the key phrase by traversing the symbolic link.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

To make it even more reliable, a proof-of-concept (PoC) devised by Imperva employs CSS trickery to alter the size of the file input element such that the file upload is triggered regardless of where the folder is dropped on the page, effectively allowing for information theft.

"Hackers are increasingly targeting individuals and organizations holding cryptocurrencies, as these digital assets can be highly valuable," Masas said. "One common tactic used by hackers is to exploit vulnerabilities in software [...] in order to gain access to crypto wallets and steal the funds they contain."

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

[browser hacking](https://thehackernews.com/search/label/browser%20hacking)[browser security](https://thehackernews.com/search/label/browser%20security)[Chromium](https://thehackernews.com/search/label/Chromium)[Data Safety](https://thehackernews.com/search/label/Data%20Safety)[Google Chrome](https://thehackernews.com/search/label/Google%20Chrome)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and ...