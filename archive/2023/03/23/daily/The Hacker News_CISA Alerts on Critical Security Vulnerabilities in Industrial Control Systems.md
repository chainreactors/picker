---
title: CISA Alerts on Critical Security Vulnerabilities in Industrial Control Systems
url: https://thehackernews.com/2023/03/cisa-alerts-on-critical-security.html
source: The Hacker News
date: 2023-03-23
fetch_date: 2025-10-04T10:26:59.415030
---

# CISA Alerts on Critical Security Vulnerabilities in Industrial Control Systems

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

# [CISA Alerts on Critical Security Vulnerabilities in Industrial Control Systems](https://thehackernews.com/2023/03/cisa-alerts-on-critical-security.html)

**Mar 22, 2023**Ravie LakshmananICS/SCADA Security

[![Industrial Control Systems](data:image/png;base64... "Industrial Control Systems")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiWGTX6tSVjf9dc2cgJkMMjhWAN3chuGHyGdAdbdozp5BP5OF7OEpWbrz5AsXRzWV94Fazh0QNs659PXECws8AvH6gscZoIsfCAOYBqAm98s-iAM3VnQduk8qSNF6XLHi8DhrLDnr7O3JJ7LTk43OQViOYZGXst0Z3AiNsP5EwR4G3z71hEBb00vEu/s790-rw-e365/hacking.png)

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has released eight Industrial Control Systems (ICS) [advisories](https://www.cisa.gov/news-events/alerts/2023/03/21/cisa-releases-eight-industrial-control-systems-advisories) on Tuesday, warning of critical flaws affecting equipment from Delta Electronics and Rockwell Automation.

This includes 13 security vulnerabilities in Delta Electronics' InfraSuite Device Master, a real-time device monitoring software. All versions prior to 1.0.5 are affected by the issues.

"Successful exploitation of these vulnerabilities could allow an unauthenticated attacker to obtain access to files and credentials, escalate privileges, and remotely execute arbitrary code," CISA [said](https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02).

At the top of the list is [CVE-2023-1133](https://nvd.nist.gov/vuln/detail/CVE-2023-1133) (CVSS score: 9.8), a critical flaw that arises from the fact that InfraSuite Device Master accepts unverified UDP packets and [deserializes the content](https://www.mandiant.com/resources/blog/hunting-deserialization-exploits), thereby allowing an unauthenticated remote attacker to execute arbitrary code.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Two other deserialization flaws, [CVE-2023-1139](https://nvd.nist.gov/vuln/detail/CVE-2023-1139) (CVSS score: 8.8) and [CVE-2023-1145](https://nvd.nist.gov/vuln/detail/CVE-2023-1145) (CVSS score: 7.8), could also be weaponized to obtain remote code execution, CISA cautioned.

Piotr Bazydlo and an anonymous security researcher have been credited with discovering and reporting the shortcomings to CISA.

Another set of vulnerabilities relates to Rockwell Automation's ThinManager ThinServer and affects the following versions of the thin client and remote desktop protocol (RDP) server management software -

* 6.x – 10.x
* 11.0.0 – 11.0.5
* 11.1.0 – 11.1.5
* 11.2.0 – 11.2.6
* 12.0.0 – 12.0.4
* 12.1.0 – 12.1.5, and
* 13.0.0 – 13.0.1

The most severe of the issues are two path traversal flaw tracked as [CVE-2023-28755](https://nvd.nist.gov/vuln/detail/CVE-2023-28755) (CVSS score: 9.8) and [CVE-2023-28756](https://nvd.nist.gov/vuln/detail/CVE-2023-28756) (CVSS score: 7.5) that could permit an unauthenticated remote attacker to upload arbitrary files to the directory where the ThinServer.exe is installed.

Even more troublingly, the adversary could weaponize CVE-2023-28755 to overwrite existing executable files with trojanized versions, potentially leading to remote code execution.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Successful exploitation of these vulnerabilities could allow an attacker to potentially perform remote code execution on the target system/device or crash the software," CISA [noted](https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-06).

Users are advised to update to versions 11.0.6, 11.1.6, 11.2.7, 12.0.5, 12.1.6, and 13.0.2 to mitigate potential threats. ThinManager ThinServer versions 6.x – 10.x are retired, requiring that users upgrade to a supported version.

As workarounds, it is also recommended that remote access of port 2031/TCP is limited to known thin clients and ThinManager servers.

The disclosure arrives more than six months after CISA [alerted](https://www.cisa.gov/news-events/ics-advisories/icsa-22-270-03) of a high-severity buffer overflow vulnerability in Rockwell Automation ThinManager ThinServer ([CVE-2022-38742](https://nvd.nist.gov/vuln/detail/CVE-2022-38742), CVSS score: 8.1) that could result in arbitrary remote code execution.

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

[CISA](https://thehackernews.com/search/label/CISA)[industrial control system](https://thehackernews.com/search/label/industrial%20control%20system)[Rockwell](https://thehackernews.com/search/label/Rockwell)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Ad...