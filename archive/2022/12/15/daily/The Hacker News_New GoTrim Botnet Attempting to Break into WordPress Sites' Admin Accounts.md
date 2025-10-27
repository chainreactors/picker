---
title: New GoTrim Botnet Attempting to Break into WordPress Sites' Admin Accounts
url: https://thehackernews.com/2022/12/new-gotrim-botnet-attempting-to-break.html
source: The Hacker News
date: 2022-12-15
fetch_date: 2025-10-04T01:34:43.939304
---

# New GoTrim Botnet Attempting to Break into WordPress Sites' Admin Accounts

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

# [New GoTrim Botnet Attempting to Break into WordPress Sites' Admin Accounts](https://thehackernews.com/2022/12/new-gotrim-botnet-attempting-to-break.html)

**Dec 14, 2022**Ravie LakshmananWebsite Security / Linux

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLDsaZup-0fIMwaCBan8Pjf4vn1Hd6l8SikNBI6zu8djwFCKPJIYSHEeWjUH495qOryfM69e9o8Ka7w_5sppey45_-qHplBISweasZYqURy2_PKFc_czRjjl4si94y5Tp5vHAW4c3eaMy2AYa6pIz6CgeyUi_v6tB-tiVNXwtRZjY5EGjnpfb_ligK/s790-rw-e365/wordpress.png)

A new Go-based botnet has been spotted scanning and brute-forcing self-hosted websites using the WordPress content management system (CMS) to seize control of targeted systems.

"This new brute forcer is part of a new campaign we have named GoTrim because it was written in Go and uses ':::trim:::' to split data communicated to and from the C2 server," Fortinet FortiGuard Labs researchers Eduardo Altares, Joie Salvio, and Roy Tay [said](https://www.fortinet.com/blog/threat-research/gotrim-go-based-botnet-actively-brute-forces-wordpress-websites).

The active campaign, observed since September 2022, utilizes a bot network to perform distributed brute-force attacks in an attempt to login to the targeted web server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A successful break-in is followed by the operator installing a downloader PHP script in the newly compromised host that, in turn, is designed to deploy the "bot client" from a hard-coded URL, effectively adding the machine to the growing network.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhrVV7lAKfHzxqJOJThoX-rrewkYWzFT01Lj89T1c8GlpSmeaaOQP3tXNBCDleNFGRgHX7X3_M8_vThkn6zVIIg9LWNna2x3l-veIsa8320wHwZBbA2U2gPzWawYt6cAtOW0V4KEZxAftwwVIehvY--g5c9HHbzIlOlQl2FmOf48ZG7FBWSQRj9SoM3/s790-rw-e365/botnet.png)

In its present form, GoTrim does not have self-propagation capabilities of its own, nor can it distribute other malware or maintain persistence in the infected system.

The primary purpose of the malware is to receive further commands from an actor-controlled server that include conducting brute-force attacks against WordPress and OpenCart using a set of provided credentials.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiQFEjPe_QalJR4aM9Ql_9IScVZKWlEjGQQvFjbVe7vHR9r_SJUp7S4Qgis8OdvMKDJc0iz70qq6XzM_zYV8fK4UG3ktOtLfD_g-4wETDGCP1eF926wOKTISjwX60AkD6m5DKokhfxKeo0abQ3G51g4_h2nO7dQA_BfN4FPoJ2m8K85wTnEWBdEZRfd/s790-rw-e365/code.png)

GoTrim can alternatively function in a server mode where it starts a server to listen for incoming requests sent by the threat actor through the command-and-control (C2) server. This, however, only occurs when the breached system is directly connected to the Internet.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Another key feature of the botnet malware is its ability to mimic legitimate requests from the Mozilla Firefox browser on 64-bit Windows to bypass anti-bot protections, in addition to solving CAPTCHA barriers present in WordPress sites.

"Although this malware is still a work in progress, the fact that it has a fully functional WordPress brute forcer combined with its anti-bot evasion techniques makes it a threat to watch for," the researchers said.

"Brute-forcing campaigns are dangerous as they may lead to server compromise and malware deployment. To mitigate this risk, website administrators should ensure that user accounts (especially administrator accounts) use strong passwords."

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

[Brute force](https://thehackernews.com/search/label/Brute%20force)[content management system](https://thehackernews.com/search/label/content%20management%20system)[FortiGuard](https://thehackernews.com/search/label/FortiGuard)[Fortinet](https://thehackernews.com/search/label/Fortinet)[linux](https://thehackernews.com/search/label/linux)[php programming language](https://thehackernews.com/search/label/php%20programming%20language)[WordPress](https://thehackernews.com/search/label/WordPress)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Crede...