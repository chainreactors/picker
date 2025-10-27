---
title: CISA Warns for Flaws Affecting Industrial Control Systems from Major Manufacturers
url: https://thehackernews.com/2023/01/cisa-warns-for-flaws-affecting.html
source: The Hacker News
date: 2023-01-17
fetch_date: 2025-10-04T04:05:31.456465
---

# CISA Warns for Flaws Affecting Industrial Control Systems from Major Manufacturers

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

# [CISA Warns of Flaws Affecting Industrial Control Systems from Major Manufacturers](https://thehackernews.com/2023/01/cisa-warns-for-flaws-affecting.html)

**Jan 16, 2023**Ravie LakshmananIndustrial Control Systems

[![Industrial Control Systems](data:image/png;base64... "Industrial Control Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQgxgERSAI0fbVxtyCqFjbWnbhNO2vT6ZdEFZb-bG8KRiD2-fha33fTj3Ps6XjMYBketGoh5zg8PlAOERssXM8eYXMRbZ1hFGagsap_3b0Ny_B03RWT7_NygiM5_c2wDOxiRMuwWGZ2dqELrwpn1IdRvzieFncuqCxZsHd0AiqrnStxSM3pKB7VlZK/s790-rw-e365/ICS.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has released several Industrial Control Systems (ICS) [advisories](https://www.cisa.gov/uscert/ncas/current-activity/2023/01/12/cisa-releases-twelve-industrial-control-systems-advisories) warning of critical security flaws affecting products from Sewio, InHand Networks, Sauter Controls, and Siemens.

The most severe of the flaws relate to Sewio's RTLS Studio, which could be exploited by an attacker to "obtain unauthorized access to the server, alter information, create a denial-of-service condition, gain escalated privileges, and execute arbitrary code," [according to CISA](https://www.cisa.gov/uscert/ics/advisories/icsa-23-012-01).

This includes CVE-2022-45444 (CVSS score: 10.0), a case of hard-coded passwords for select users in the application's database that potentially grant remote adversaries unrestricted access.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Also notable are two command injection flaws (CVE-2022-47911 and CVE-2022-43483, CVSS scores: 9.1) and an out-of-bounds write vulnerability (CVE-2022-41989, CVSS score: 9.1) that could result in denial-of-service condition or code execution.

The vulnerabilities impact RTLS Studio version 2.0.0 up to and including version 2.6.2. Users are recommended to update to version 3.0.0 or later.

CISA, in a [second alert](https://www.cisa.gov/uscert/ics/advisories/icsa-23-012-03), highlighted a set of five security defects in InHand Networks InRouter 302 and InRouter 615, including CVE-2023-22600 (CVSS score: 10.0), that could lead to command injection, information disclosure, and code execution.

"If properly chained, these vulnerabilities could result in an unauthorized remote user fully compromising every cloud-managed InHand Networks device reachable by the cloud," the agency said.

All firmware versions of InRouter 302 prior to IR302 V3.5.56 and InRouter 615 before InRouter6XX-S-V2.3.0.r5542 are susceptible to the bugs.

Security vulnerabilities have also been [disclosed](https://www.cisa.gov/uscert/ics/advisories/icsa-23-012-05) in Sauter Controls Nova 220, Nova 230, Nova 106, and moduNet300 that could allow unauthorized visibility to sensitive information (CVE-2023-0053, CVSS score: 7.5) and remote code execution (CVE-2023-0052, CVSS score: 9.8).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Swiss-based automation company, however, does not plan to release fixes for the identified issues owing to the fact that the product line is no longer supported.

Lastly, the security agency [detailed](https://www.cisa.gov/uscert/ics/advisories/icsa-23-012-09) a cross-site scripting ([XSS](https://owasp.org/www-community/attacks/xss/)) flaw in Siemens Mendix SAML equipment (CVE-2022-46823, CVSS score: 9.3) that could permit a threat actor to gain sensitive information by tricking users into clicking a specially crafted link.

Users are advised to enable multi-factor authentication and update Mendix SAML to versions 2.3.4 (Mendix 8), 3.3.8 (Mendix 9, Upgrade Track), or 3.3.9 (Mendix 9, New Track) to mitigate potential risks.

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[industrial control system](https://thehackernews.com/search/label/industrial%20control%20system)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-expl...