---
title: New 'Bad Magic' Cyber Threat Disrupt Ukraine's Key Sectors Amid War
url: https://thehackernews.com/2023/03/new-bad-magic-cyber-threat-disrupt.html
source: The Hacker News
date: 2023-03-22
fetch_date: 2025-10-04T10:17:51.537957
---

# New 'Bad Magic' Cyber Threat Disrupt Ukraine's Key Sectors Amid War

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

# [New 'Bad Magic' Cyber Threat Disrupts Ukraine's Key Sectors Amid War](https://thehackernews.com/2023/03/new-bad-magic-cyber-threat-disrupt.html)

**Mar 21, 2023**Ravie LakshmananCyber War / Cyber Threat

[![Cyber Threat](data:image/png;base64... "Cyber Threat")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlNV28ZruCGm_-xVy5q2kQRVN-gP-MlaeAobAtNhUi-hM4Cy1hv2XLTHZ6I8bwOhk12VlcpPJGtPLLhjcHwkGJIeoFJK8as9mgqOoa9dk7RmlgINmk9TbPfOjd5gyrfop5UM63cC_Si4hOmS7Pz84Qc1e2ZEyYn6ShqgtwylmUgn0xgld1xCZ5E1fV/s790-rw-e365/loader.png)

Amid the [ongoing war](https://thehackernews.com/2023/03/from-ransomware-to-cyber-espionage-55.html) between Russia and Ukraine, government, agriculture, and transportation organizations located in Donetsk, Lugansk, and Crimea have been attacked as part of an active campaign that drops a previously unseen, modular framework dubbed **CommonMagic**.

"Although the initial vector of compromise is unclear, the details of the next stage imply the use of spear phishing or similar methods," Kaspersky [said](https://securelist.com/bad-magic-apt/109087/) in a new report.

The Russian cybersecurity company, which detected the attacks in October 2022, is tracking the activity cluster under the name "Bad Magic."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Attack chains entail the use of booby-trapped URLS pointing to a ZIP archive hosted on a malicious web server. The file, when opened, contains a decoy document and a malicious LNK file that culminates in the deployment of a backdoor named PowerMagic.

Written in PowerShell, PowerMagic establishes contact with a remote server and executes arbitrary commands, the results of which are exfiltrated to cloud services like Dropbox and Microsoft OneDrive.

[![Cyber Threat](data:image/png;base64... "Cyber Threat")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkAwRFoxgUrW8FWUNvVzZJ4sRjdz_2VZzrLvzkRRR5zQbhGe9gU5yVE3N8D0j6-BhHym92QcS0Lr7t56cWNp3hMHjG3FYKAqadwKaZCNsCP4Ff8W7y8btCALTdoXPwzVsFF2x4DPHqknQcc490ghnnN-Ce03QuwubcFwe9Xq9SY3Q2M_t4QcnpmGD4/s790-rw-e365/powermagic.png)

PowerMagic also serves as a conduit to deliver the CommonMagic framework, a set of executable modules that are designed to carry out specific tasks such as interacting with the command-and-control (C2) server, encrypting and decrypting C2 traffic, and executing plugins.

Two of the plugins discovered so far come with capabilities to capture screenshots every three seconds and gather files of interest from connected USB devices.

Kaspersky said it found no evidence linking the operation and its tooling to any known threat actor or group. The earliest ZIP archive attachment dates back to September 2021, indicating that the campaign may have flown under the radar for more than 1.5 years.

"Geopolitics always affect the cyberthreat landscape and lead to the emergence of new threats," Kaspersky's Leonid Besverzhenko [said](https://usa.kaspersky.com/about/press-releases/2023_kaspersky-uncovers-ongoing-apt-campaign-targeting-organizations-in-russian-ukrainian-conflict-area). "Although the malware and techniques employed in the CommonMagic campaign are not particularly sophisticated, the use of cloud storage as the command-and-control infrastructure is noteworthy."

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

[Kaspersky](https://thehackernews.com/search/label/Kaspersky)[powershell](https://thehackernews.com/search/label/powershell)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS ...