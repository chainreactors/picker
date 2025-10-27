---
title: High Severity Vulnerabilities Reported in F5 BIG-IP and BIG-IQ Devices
url: https://thehackernews.com/2022/11/high-severity-vulnerabilities-reported.html
source: The Hacker News
date: 2022-11-18
fetch_date: 2025-10-03T23:10:33.113165
---

# High Severity Vulnerabilities Reported in F5 BIG-IP and BIG-IQ Devices

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

# [High Severity Vulnerabilities Reported in F5 BIG-IP and BIG-IQ Devices](https://thehackernews.com/2022/11/high-severity-vulnerabilities-reported.html)

**Nov 17, 2022**Ravie Lakshmanan

[![F5 BIG-IP and BIG-IQ Devices](data:image/png;base64... "F5 BIG-IP and BIG-IQ Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirxx9Y9QPuT5YjS4qVUHPX6HrTMxaZvdzQAGYAGa4c3ZmQ0d9frPiE2XxlWHjKea_UmoQ_QM5xRb18kEv7DcTQfztfQ2ifqniNVN8lPEwA-zA3BrWjAfRP7OzkqlIWxyFYdhKsh0LPZ6poG9X8NYV7IltViMModBVtUZLm8-RS7HZm_Bi7kJ_oR86t/s790-rw-e365/f5.jpg)

Multiple security vulnerabilities have been disclosed in F5 BIG-IP and BIG-IQ devices that, if successfully exploited, to completely compromise affected systems.

Cybersecurity firm Rapid7 said the [flaws](https://support.f5.com/csp/article/K97843387) could be abused to remote access to the devices and defeat security constraints. The issues impact BIG-IP versions 13.x, 14.x, 15.x, 16.x, and 17.x, and BIG-IQ Centralized Management versions 7.x and 8.x.

The two high-severity issues, which were reported to F5 on August 18, 2022, are as follows -

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

* **CVE-2022-41622** (CVSS score: 8.8) - A cross-site request forgery ([CSRF](https://owasp.org/www-community/attacks/csrf)) vulnerability through iControl SOAP, leading to unauthenticated remote code execution.
* **CVE-2022-41800** (CVSS score: 8.7) - An iControl REST vulnerability that could allow an authenticated user with an Administrator role to bypass [Appliance mode](https://support.f5.com/csp/article/K12815) restrictions.

"By successfully exploiting the worst of the vulnerabilities (CVE-2022-41622), an attacker could gain persistent root access to the device's management interface (even if the management interface is not internet-facing)," Rapid7 researcher Ron Bowes [said](https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/).

However, it's worth noting that such an exploit requires an administrator with an active session to visit a hostile website.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also identified were [three different instances](https://support.f5.com/csp/article/K05403841) of security bypass, which F5 said cannot be exploited without first breaking existing security barriers through a previously undocumented mechanism.

Should such a scenario arise, an adversary with Advanced Shell ([bash](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29)) access to the appliance could weaponize these weaknesses to execute arbitrary system commands, create or delete files, or disable services.

While F5 has made no mention of any of the vulnerabilities being exploited in attacks, it's recommended that users apply the necessary "engineering hotfix" released by the company to mitigate potential risks.

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

[BIG-IQ](https://thehackernews.com/search/label/BIG-IQ)[F5 BIG-IP](https://thehackernews.com/search/label/F5%20BIG-IP)[Firewall](https://thehackernews.com/search/label/Firewall)[hacking news](https://thehackernews.com/search/label/hacking%20news)

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

Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Disclosure](https://thehackernews.com/2025/09/fortra-goanywhere-cvss-10-flaw....