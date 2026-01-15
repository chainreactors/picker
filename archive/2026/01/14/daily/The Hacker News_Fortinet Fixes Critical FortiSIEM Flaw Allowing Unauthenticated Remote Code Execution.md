---
title: Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution
url: https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html
source: The Hacker News
date: 2026-01-14
fetch_date: 2026-01-15T03:32:13.665119
---

# Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code Execution](https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html)

**Jan 14, 2026**Ravie LakshmananVulnerability / Patch Management

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimc7gjS2ZNi7kOnZXqH-FOYhQ5snGQ-zfhTA1NvxSNOo0dFaX62BEJSqr0qVmPJ9wY4jNffKZ8P5mciZC34btvRAJ4KH6dKXmcOOZpmFUZOU0cOtyJxNf-eImO9Gq8CIc3aVPlNo267-_RSUqTHyrjTkkfSbCnLb2lqjECHgqqo78Y-2Gib0Pxy8m3D-S9/s790-rw-e365/fort.jpg)

Fortinet has released updates to fix a critical security flaw impacting FortiSIEM that could allow an unauthenticated attacker to achieve code execution on susceptible instances.

The operating system (OS) injection vulnerability, tracked as **CVE-2025-64155**, is rated 9.4 out of 10.0 on the CVSS scoring system.

"An improper neutralization of special elements used in an OS command ('OS command injection') vulnerability [CWE-78] in FortiSIEM may allow an unauthenticated attacker to execute unauthorized code or commands via crafted TCP requests," the company [said](https://www.fortiguard.com/psirt/FG-IR-25-772) in a Tuesday bulletin.

Fortinet said the vulnerability affects only Super and Worker nodes, and that it has been addressed in the following versions -

* FortiSIEM 6.7.0 through 6.7.10 (Migrate to a fixed release)
* FortiSIEM 7.0.0 through 7.0.4 (Migrate to a fixed release)
* FortiSIEM 7.1.0 through 7.1.8 (Upgrade to 7.1.9 or above)
* FortiSIEM 7.2.0 through 7.2.6 (Upgrade to 7.2.7 or above)
* FortiSIEM 7.3.0 through 7.3.4 (Upgrade to 7.3.5 or above)
* FortiSIEM 7.4.0 (Upgrade to 7.4.1 or above)
* FortiSIEM 7.5 (Not affected)
* FortiSIEM Cloud (Not affected)

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Horizon3.ai security researcher Zach Hanley, who is credited with discovering and reporting the flaw on August 14, 2025, [said](https://horizon3.ai/attack-research/disclosures/cve-2025-64155-three-years-of-remotely-rooting-the-fortinet-fortisiem/) it comprises two moving parts -

* An unauthenticated argument injection vulnerability that leads to arbitrary file write, allowing for remote code execution as the admin user
* A file overwrite privilege escalation vulnerability that leads to root access and completely compromises the appliance

Specifically, the problem has to do with how FortiSIEM's [phMonitor](https://thehackernews.com/2025/08/fortinet-warns-about-fortisiem.html) service – a crucial backend process [responsible](https://docs.fortinet.com/document/fortisiem/7.5.0/user-guide/174517/viewing-cloud-health) for health monitoring, task distribution, and inter-node communication via TCP port 7900 – handles incoming requests related to logging security events to Elasticsearch.

This, in turn, invokes a shell script with user-controlled parameters, thereby opening the door to argument injection via curl and achieving arbitrary file writes to the disk in the context of the admin user.

This limited file write can be weaponized to achieve full system takeover by weaponizing the curl argument injection to write a reverse shell to "/opt/charting/redishb.sh," a file that's writable by an admin user and is executed every minute by the appliance by means of a cron job that runs with root-level permissions.

In other words, writing a reverse shell to this file enables privilege escalation from admin to root, granting the attacker unfettered access to the FortiSIEM appliance. The most important aspect of the attack is that the phMonitor service exposes several command handlers that do not require authentication. This makes it easy for an attacker to invoke these functions simply by obtaining network access to port 7900.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

Fortinet has also shipped fixes for another [critical security vulnerability](https://www.fortiguard.com/psirt/FG-IR-25-260) in FortiFone (CVE-2025-47855, CVSS score: 9.3) that could allow an unauthenticated attacker to obtain device configuration via a specially crafted HTTP(S) request to the Web Portal page. It impacts the following versions of the enterprise communications platform -

* FortiFone 3.0.13 through 3.0.23 (Upgrade to 3.0.24 or above)
* FortiFone 7.0.0 through 7.0.1 (Upgrade to 7.0.2 or above)
* FortiFone 7.2 (Not affected)

Users are advised to update to the latest versions for optimal protection. As workarounds for CVE-2025-64155, Fortinet is recommending that customers limit access to the phMonitor port (7900).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[FortiFone](https://thehackernews.com/search/label/FortiFone)[Fortinet](https://thehackernews.com/search/label/Fortinet)[FortiSIEM](https://thehackernews.com/search/label/FortiSIEM)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trendi...