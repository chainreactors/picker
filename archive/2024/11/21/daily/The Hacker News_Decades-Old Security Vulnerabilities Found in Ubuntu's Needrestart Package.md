---
title: Decades-Old Security Vulnerabilities Found in Ubuntu's Needrestart Package
url: https://thehackernews.com/2024/11/decades-old-security-vulnerabilities.html
source: The Hacker News
date: 2024-11-21
fetch_date: 2025-10-06T19:17:40.574553
---

# Decades-Old Security Vulnerabilities Found in Ubuntu's Needrestart Package

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

# [Decades-Old Security Vulnerabilities Found in Ubuntu's Needrestart Package](https://thehackernews.com/2024/11/decades-old-security-vulnerabilities.html)

**Nov 20, 2024**Ravie LakshmananLinux / Vulnerability

[![Ubuntu Vulnerabilities](data:image/png;base64... "Ubuntu Vulnerabilities")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha6IrZq-eToUnYF5kKE-Sl-8hXcj76iLRZ18oULNinUx8bWcHn1IAKiT3tNwTchm4HN-1-B5qquu1QNwYfGxFRAYT377PMLra-UwHDuj91SW9GkZL-Yp0QJoalxVXxolCZNw5-yVPSKlRZmXw5c-lGRJmCUCS6tQ-IghVCHqusqqVHeflsTSn1X1MvsqZY/s790-rw-e365/ubuntu.png)

Multiple decade-old security vulnerabilities have been disclosed in the needrestart package installed by default in Ubuntu Server (since version 21.04) that could allow a local attacker to gain root privileges without requiring user interaction.

The Qualys Threat Research Unit (TRU), which [identified and reported](https://blog.qualys.com/vulnerabilities-threat-research/2024/11/19/qualys-tru-uncovers-five-local-privilege-escalation-vulnerabilities-in-needrestart) the flaws early last month, said they are trivial to exploit, necessitating that users move quickly to apply the fixes. The vulnerabilities are believed to have existed since the introduction of interpreter support in [needrestart 0.8](https://github.com/liske/needrestart/releases/tag/v0.8), which was released on April 27, 2014.

"These needrestart exploits allow Local Privilege Escalation (LPE) which means that a local attacker is able to gain root privileges," Ubuntu [said](https://ubuntu.com/blog/needrestart-local-privilege-escalation) in an advisory, noting they have been addressed in version 3.8. "The vulnerabilities affect Debian, Ubuntu, and other Linux distributions."

Needrestart is a utility that scans a system to determine the services that need to be restarted after applying shared library updates in a manner that avoids a complete system reboot.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The five flaws are listed below -

* **[CVE-2024-48990](https://ubuntu.com/security/CVE-2024-48990)** (CVSS score: 7.8) - A vulnerability that allows local attackers to execute arbitrary code as root by tricking needrestart into running the Python interpreter with an attacker-controlled PYTHONPATH environment variable
* **[CVE-2024-48991](https://ubuntu.com/security/CVE-2024-48991)** (CVSS score: 7.8) - A vulnerability that allows local attackers to execute arbitrary code as root by winning a race condition and tricking needrestart into running their own, fake Python interpreter
* **[CVE-2024-48992](https://ubuntu.com/security/CVE-2024-48992)** (CVSS score: 7.8) - A vulnerability that allows local attackers to execute arbitrary code as root by tricking needrestart into running the Ruby interpreter with an attacker-controlled RUBYLIB environment variable
* **[CVE-2024-11003](https://ubuntu.com/security/CVE-2024-11003)** (CVSS score: 7.8) and **[CVE-2024-10224](https://ubuntu.com/security/CVE-2024-10224)** (CVSS score: 5.3) - Two vulnerabilities that allows a local attacker to execute arbitrary shell commands as root by taking advantage of an issue in the libmodule-scandeps-perl package (before version 1.36)

Successful exploitation of the aforementioned shortcomings could allow a local attacker to set specially crafted environment variables for PYTHONPATH or RUBYLIB that could result in the execution of arbitrary code pointing to the threat actor's environment when needrestart is run.

"In CVE-2024-10224, [...] attacker-controlled input could cause the Module::ScanDeps Perl module to run arbitrary shell commands by open()ing a 'pesky pipe' (such as by passing 'commands|' as a filename) or by passing arbitrary strings to eval()," Ubuntu noted.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"On its own, this is not enough for local privilege escalation. However, in CVE-2024-11003 needrestart passes attacker-controlled input (filenames) to Module::ScanDeps and triggers CVE-2024-10224 with root privilege. The fix for CVE-2024-11003 removes needrestart's dependency on Module::ScanDeps."

While it's highly advised to download the latest patches, Ubuntu said users can disable interpreter scanners in needrestart the configuration file as a temporary mitigation and ensure that the changes are reverted after the updates are applied.

"These vulnerabilities in the needrestart utility allow local users to escalate their privileges by executing arbitrary code during package installations or upgrades, where needrestart is often run as the root user," Saeed Abbasi, product manager of TRU at Qualys, said.

"An attacker exploiting these vulnerabilities could gain root access, compromising system integrity and security."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[linux](https://thehackernews.com/search/label/linux)[Needrestart](https://thehackernews.com/search/label/Needrestart)[Qualys](https://thehackernews.com/search/label/Qualys)[Ubuntu](https://thehackernews.com/search/label/Ubuntu)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](dat...