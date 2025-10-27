---
title: Sophos and SonicWall Patch Critical RCE Flaws Affecting Firewalls and SMA 100 Devices
url: https://thehackernews.com/2025/07/sophos-and-sonicwall-patch-critical-rce.html
source: The Hacker News
date: 2025-07-25
fetch_date: 2025-10-06T23:53:15.115436
---

# Sophos and SonicWall Patch Critical RCE Flaws Affecting Firewalls and SMA 100 Devices

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

# [Sophos and SonicWall Patch Critical RCE Flaws Affecting Firewalls and SMA 100 Devices](https://thehackernews.com/2025/07/sophos-and-sonicwall-patch-critical-rce.html)

**Jul 24, 2025**Ravie LakshmananNetwork Security / Vulnerability

[![Sophos and SonicWall](data:image/png;base64... "Sophos and SonicWall")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiJ6hZCXeBcj81MW3OHzDhkqd234YOI1mbUXoo7p5VgWM_cayVWYUG2C5APO-ueCyCRgm5MUjzlVA0d96qone2Pqhv32-mdnCH3LAcXBMvqBUcjBSj230tWRst064Mjtm4eBpnzPyvyiFHnaYTVrjn2EOpex0GZFoNpB8xpszAJ8TXWFdHB8qTvQJdH2xQH/s790-rw-e365/sonic.jpg)

Sophos and SonicWall have alerted users of critical security flaws in Sophos Firewall and Secure Mobile Access (SMA) 100 Series appliances that could be exploited to achieve remote code execution.

The two vulnerabilities [impacting](https://www.sophos.com/en-us/security-advisories/sophos-sa-20250721-sfos-rce) Sophos Firewall are listed below -

* **[CVE-2025-6704](https://nvd.nist.gov/vuln/detail/CVE-2025-6704)** (CVSS score: 9.8) - An arbitrary file writing vulnerability in the Secure PDF eXchange (SPX) feature can lead to pre-auth remote code execution, if a specific configuration of SPX is enabled in combination with the firewall running in High Availability (HA) mode
* **[CVE-2025-7624](https://nvd.nist.gov/vuln/detail/CVE-2025-7624)** (CVSS score: 9.8) - An SQL injection vulnerability in the legacy (transparent) SMTP proxy can lead to remote code execution, if a quarantining policy is active for Email and SFOS was upgraded from a version older than 21.0 GA

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Sophos said CVE-2025-6704 affects about 0.05% of devices, while CVE-2025-7624 impacts as many as 0.73% of devices. Both vulnerabilities have been addressed alongside a high-severity command injection vulnerability in the WebAdmin component ([CVE-2025-7382](https://nvd.nist.gov/vuln/detail/CVE-2025-7382), CVSS score: 8.8) that could result in pre-auth code execution on High Availability (HA) auxiliary devices, if OTP authentication for the admin user is enabled.

Also patched by the company are two other vulnerabilities -

* **[CVE-2024-13974](https://nvd.nist.gov/vuln/detail/CVE-2024-13974)** (CVSS score: 8.1) - A business logic vulnerability in the Up2Date component can lead to attackers controlling the firewall's DNS environment to achieve remote code execution
* **[CVE-2024-13973](https://nvd.nist.gov/vuln/detail/CVE-2024-13973)** (CVSS score: 6.8) - A post-auth SQL injection vulnerability in WebAdmin can potentially lead to administrators achieving arbitrary code execution

The U.K. National Cyber Security Centre (NCSC) has been credited with discovering and reporting both CVE-2024-13974 and CVE-2024-13973. The issues affect the following versions -

* CVE-2024-13974 - Affects Sophos Firewall v21.0 GA (21.0.0) and older
* CVE-2024-13973 - Affects Sophos Firewall v21.0 GA (21.0.0) and older
* CVE-2025-6704 - Affects Sophos Firewall v21.5 GA (21.5.0) and older
* CVE-2025-7624 - Affects Sophos Firewall v21.5 GA (21.5.0) and older
* CVE-2025-7382 - Affects Sophos Firewall v21.5 GA (21.5.0) and older

The disclosure comes as SonicWall [detailed](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0014) a critical bug in the SMA 100 Series web management interface (CVE-2025-40599, CVSS score: 9.1) that a remote attacker with administrative privileges can exploit to upload arbitrary files and potentially achieve remote code execution.

The flaw impacts SMA 100 Series products (SMA 210, 410, 500v) and has been addressed in version 10.2.2.1-90sv.

SonicWall also pointed out that while the vulnerability has not been exploited, there exists a potential risk in light of a [recent report](https://thehackernews.com/2025/07/unc6148-backdoors-fully-patched.html) from the Google Threat Intelligence Group (GTIG), which found evidence of a threat actor dubbed UNC6148 leveraging fully-patched SMA 100 series devices to deploy a backdoor called **OVERSTEP**.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Besides applying the fixes, the company is also recommending that customers of SMA 100 Series devices carry out the following steps -

* Disable remote management access on the external-facing interface (X1) to reduce the attack surface
* Reset all passwords and reinitialize OTP (One-Time Password) binding for users and administrators on the appliance
* Enforce multi-factor authentication (MFA) for all users
* Enable Web Application Firewall (WAF) on SMA 100

Organizations using SMA 100 Series devices are also advised to review appliance logs and connection history for anomalies and check for any signs of unauthorized access.

Organizations using the SMA 500v virtual product are required to backup the OVA file, export the configuration, remove the existing virtual machine and all associated virtual disks and snapshots, reinstall the new OVA from SonicWall using a hypervisor, and restore the configuration.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall](https://thehackernews.com/search/lab...