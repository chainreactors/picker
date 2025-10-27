---
title: Malicious Google Play Store App Spotted Distributing Xenomorph Banking Trojan
url: https://thehackernews.com/2022/11/these-two-google-play-store-apps.html
source: The Hacker News
date: 2022-11-12
fetch_date: 2025-10-03T22:35:25.410733
---

# Malicious Google Play Store App Spotted Distributing Xenomorph Banking Trojan

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

# [Malicious Google Play Store App Spotted Distributing Xenomorph Banking Trojan](https://thehackernews.com/2022/11/these-two-google-play-store-apps.html)

**Nov 11, 2022**Ravie Lakshmanan

[![Xenomorph Banking Trojan](data:image/png;base64... "Xenomorph Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyRpA-mhaIyCcRLeylp9_GHSZcRHYfPLJHXHgWT_6DQLzNUiO4CLPfBMjjWOBQ68lLRz4xBwEXqXmm_T-zOXaS-TUH3hl4UhToG-Xq7qE5YrW_BMTYbrEbKXfVWwFEL2A0Zy3rJCothsY-k2jRmhcqxIv6PBYlIPhR_r0BQM6PeHIWPhOP208nrsza/s790-rw-e365/malware.jpg)

Google has removed two new malicious dropper apps that have been detected on the Play Store for Android, one of which posed as a lifestyle app and was caught distributing the Xenomorph banking malware.

"Xenomorph is a trojan that steals credentials from banking applications on users' devices," Zscaler ThreatLabz researchers Himanshu Sharma and Viral Gandhi [said](https://www.zscaler.com/blogs/security-research/rise-banking-trojan-dropper-google-play-0) in an analysis published Thursday.

"It is also capable of intercepting users' SMS messages and notifications, enabling it to steal one-time passwords and multi-factor authentication requests."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The cybersecurity firm said it also found an expense tracker app that exhibited similar behavior, but noted that it couldn't extract the URL used to fetch the malware artifact.

[![Xenomorph Banking Trojan](data:image/png;base64... "Xenomorph Banking Trojan")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieABvknKhqKCxzQAs0IBfPTCITOMZiqWDdhESl4VbDUCxSUe4d24rE0ncvQ1whqweMkP8DqioRszEIQyekY-ouXtG_BYRN5x_njXwPDOI24V-RkcqcIeuRUnnoiwv-H8n2BSvAty9syFoTSx66ab44h0yTd3nVKhvt_vQzou8nJ1VZQZwJ1VQpDtQv/s790-rw-e365/image.jpg)

The two malicious apps are as follows -

* Todo: Day manager (com.todo.daymanager)
* 経費キーパー (com.setprice.expenses)

Both the apps function as a dropper, meaning the apps themselves are harmless and are a conduit to retrieve the actual payload, which, in the case of Todo, is hosted on GitHub.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Xenomorph, first [documented](https://thehackernews.com/2022/02/xenomorph-android-banking.html) by ThreatFabric earlier this February, is known to abuse Android's accessibility permissions to conduct overlay attacks, wherein fake login screens are presented atop legitimate bank apps to steal victims' credentials.

What's more, the malware leverages a Telegram channel's description to decode and construct the command-and-control (C2) domain used to receive additional commands.

The development follows the [discovery of four rogue](https://thehackernews.com/2022/11/these-android-apps-with-million-play.html) apps on Google Play that were found directing victims to malicious websites as part of an adware and information-stealing campaign. Google told The Hacker News that it has since banned the developer.

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

[Android](https://thehackernews.com/search/label/Android)[Google](https://thehackernews.com/search/label/Google)[Malware](https://thehackernews.com/search/label/Malware)[Play Store](https://thehackernews.com/search/label/Play%20Store)[Zscaler](https://thehackernews.com/search/label/Zscaler)

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

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](data:image/svg+xml;base64... "Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure")

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Da...