---
title: PY#RATION: New Python-based RAT Uses WebSocket for C2 and Data Exfiltration
url: https://thehackernews.com/2023/01/pyration-new-python-based-rat-utilizes.html
source: The Hacker News
date: 2023-01-27
fetch_date: 2025-10-04T05:01:08.576522
---

# PY#RATION: New Python-based RAT Uses WebSocket for C2 and Data Exfiltration

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

# [PY#RATION: New Python-based RAT Uses WebSocket for C2 and Data Exfiltration](https://thehackernews.com/2023/01/pyration-new-python-based-rat-utilizes.html)

**Jan 26, 2023**Ravie LakshmananThreat Detection / Endpoint Security

[![Python Malware Websockets](data:image/png;base64... "Python Malware Websockets")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi47NeO4QZdAl9Sa064nvEK-3pzud3_jbcaSJkcAzBAGSUstlImn8rqNqdeJM7Ovakfw8WZGjlrL2Ek7hBYzaxQTDR_8tAxwS9DJsjAyCo-e5oZC-lAHw886MzsxRXUzDnW2NHHuJcBFMdsRDydZkgHfp9tKFrI3MYKXPyBHJWeed9aOXgf43vqHgZm/s790-rw-e365/hackin.png)

Cybersecurity researchers have unearthed a new attack campaign that leverages a Python-based remote access trojan (RAT) to gain control over compromised systems since at least August 2022.

"This malware is unique in its utilization of [WebSockets](https://en.wikipedia.org/wiki/WebSocket) to avoid detection and for both command-and-control (C2) communication and exfiltration," Securonix [said](https://www.securonix.com/blog/security-advisory-python-based-pyration-attack-campaign/) in a report shared with The Hacker News.

The malware, dubbed PY#RATION by the cybersecurity firm, comes with a host of capabilities that allows the threat actor to harvest sensitive information. Later versions of the backdoor also sport anti-evasion techniques, suggesting that it's being actively developed and maintained.

The attack commences with a phishing email containing a ZIP archive, which, in turn, harbors two shortcut (.LNK) files that masquerade as front and back side images of a seemingly legitimate U.K. driver's license.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Opening each of the .LNK files retrieves two text files from a remote server that are subsequently renamed to .BAT files and executed stealthily in background, while the decoy image is displayed to the victim.

Also downloaded from a C2 server is another batch script that's engineered to retrieve additional payloads from the server, including the Python binary ("CortanaAssistance.exe"). The choice of using Cortana, Microsoft's virtual assistant, indicates an attempt to pass off the malware as a system file.

[![Python-based RAT](data:image/png;base64... "Python-based RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-cjqF5BcARh-XhgBaayEEAslOZy86uFJ1C2QR1uzCRZhSVydPB7k6NUreMPm3lOTm_vrHO8Q1iqr_sOdpzD2zXQ7ZDyXqKij9F3-GhSOmN2S6xP3WMPaKXXrhL9e0-Edi2CB4rz0E5rJ-CQwibTvUIM2w2BGiWehhlNPzwmMRpBgP0ppJcHyHVaeacA/s790-rw-e365/hack.png)

Two versions of the trojan have been detected (version 1.0 and 1.6), with nearly 1,000 lines of code added to the newer variant to support network scanning features to conduct a reconnaissance of the compromised network and conceal the Python code behind an encryption layer using the [fernet module](https://cryptography.io/en/latest/fernet/).

Other noteworthy functionalities comprise the ability to transfer files from host to C2 or vice versa, record keystrokes, execute system commands, extract passwords and cookies from web browsers, capture clipboard data, and check for the presence of antivirus software.

What's more, PY#RATION functions as a pathway for deploying more malware, which consists of another Python-based info-stealer designed to siphon data from web browsers and cryptocurrency wallets.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The origins of the threat actor remain unknown, but the nature of the phishing lures posits that the intended targets could likely be the U.K. or North America.

"The PY#RATION malware is not only relatively difficult to detect, the fact that it is a Python compiled binary makes this extremely flexible as it will run on almost any target including Windows, OSX, and Linux variants," researchers Den Iuzvyk, Tim Peck, and Oleg Kolesnikov said.

"The fact that the threat actors leveraged a layer of fernet encryption to hide the original source compounds the difficulty of detecting known malicious strings."

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

[Python](https://thehackernews.com/search/label/Python)[WebSocket](https://thehackernews.com/search/label/WebSocket)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Expl...