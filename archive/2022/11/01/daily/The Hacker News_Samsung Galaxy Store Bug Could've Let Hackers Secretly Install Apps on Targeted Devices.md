---
title: Samsung Galaxy Store Bug Could've Let Hackers Secretly Install Apps on Targeted Devices
url: https://thehackernews.com/2022/10/samsung-galaxy-store-bug-couldve-let.html
source: The Hacker News
date: 2022-11-01
fetch_date: 2025-10-03T21:29:40.282659
---

# Samsung Galaxy Store Bug Could've Let Hackers Secretly Install Apps on Targeted Devices

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

# [Samsung Galaxy Store Bug Could've Let Hackers Secretly Install Apps on Targeted Devices](https://thehackernews.com/2022/10/samsung-galaxy-store-bug-couldve-let.html)

**Oct 31, 2022**Ravie Lakshmanan

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgLFBnqU0_iBloyDGJnDqyqSKGfWEtumRO1AF_UsTteOODxxpYWG8YRkL-Vj_CtZnZjIK2sH12xTU_kWL_Seix_3QckT6bjIp2FzHiGorbdpku66HbJVtKnKNYAU3YvMgakJYE6937DihtLpDgnhH1aEMY4Wq815zVpXweHT5-eQUhF9QOyvAGWUnVG/s790-rw-e365/samsung-galay-store.jpg)

A now-patched security flaw has been disclosed in the Galaxy Store app for Samsung devices that could potentially trigger remote command execution on affected phones.

The vulnerability, which affects Galaxy Store version 4.5.32.4, relates to a cross-site scripting (XSS) bug that occurs when handling certain [deep links](https://developer.android.com/training/app-links/deep-linking). An independent security researcher has been credited with reporting the issue.

"Here, by not checking the deep link securely, when a user accesses a link from a website containing the deeplink, the attacker can execute JS code in the webview context of the Galaxy Store application," SSD Secure Disclosure [said](https://ssd-disclosure.com/ssd-advisory-galaxy-store-applications-installation-launching-without-user-interaction/) in an advisory posted last week.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2OhHlw0O_TO2EISk0Q1gaqOCrc2oMvzA87ezkLe7FuHbN0nfbDgKkmitqkSgclgVuLO52rXANDoMpU-VMJ__33LAKz6JDGXj2aZHZZgckE-nrwdpbkSJHeYbVdlRcO5l-lVfwK9krICEDrOTwOaaifGe6752NSI9YWRSzcDmP-X3c7Q_Zl4rqpWTh/s790-rw-e365/code-hack.jpg)

[XSS attacks](https://owasp.org/www-community/attacks/xss/) allow an adversary to inject and execute malicious JavaScript code when visiting a website from a browser or another application.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The issue identified in the Galaxy Store app has to do with how deep links are configured for Samsung's Marketing & Content Service ([MCS](https://us-mktg.mcsvc.samsung.com/)), potentially leading to a scenario where arbitrary code injected into the MCS website could lead to its execution.

This could then be leveraged to download and install malware-laced apps on the Samsung device when visiting the link.

"To be able to successfully exploit the victim's server, it is necessary to have HTTPS and CORS bypass of chrome," the researchers noted.

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

[Galaxy Store](https://thehackernews.com/search/label/Galaxy%20Store)[hacking news](https://thehackernews.com/search/label/hacking%20news)[Samsung](https://thehackernews.com/search/label/Samsung)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw.html)

[![Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](data:image/svg+xml;base64... "Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware")

Cisco ASA Firewall Zero-Day Exploits Deploy RayInitiator and LINE VIPER Malware](https://thehackernews.com/2025/09/cisco-asa-firewall-zero-day-exploits.html)

[![Urgent: Cisco ASA Zero-Day Duo Under Attack; CISA Triggers Emergency Mitigation Directive](data:image/svg+xml;base64... "Urgent: Cisco ASA Zero-Day...