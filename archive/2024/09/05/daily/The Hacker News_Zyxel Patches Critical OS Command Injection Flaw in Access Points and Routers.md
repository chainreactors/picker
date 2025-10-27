---
title: Zyxel Patches Critical OS Command Injection Flaw in Access Points and Routers
url: https://thehackernews.com/2024/09/zyxel-patches-critical-os-command.html
source: The Hacker News
date: 2024-09-05
fetch_date: 2025-10-06T18:30:40.120202
---

# Zyxel Patches Critical OS Command Injection Flaw in Access Points and Routers

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

# [Zyxel Patches Critical OS Command Injection Flaw in Access Points and Routers](https://thehackernews.com/2024/09/zyxel-patches-critical-os-command.html)

**Sep 04, 2024**Ravie LakshmananVulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiK_r3anov1AcRNGaTL9V8GV4bafj49gjKYHWEuFc0aUkdnEpQBtelQp-iSCtB2duIyQOkLXMt5nlW1m-W6Zy-5cawC8Zl07vmiQLw_TQNkKg6NCNv7bKcKtPJ-VTm-HW6XwOsxiUp9V6YlclABSJoDa_uWt5SktpPTRU0nH1Ln9J-5R571G-F7R9ZNcxqP/s790-rw-e365/router.jpg)

Zyxel has released software updates to address a critical security flaw impacting certain access point (AP) and security router versions that could result in the execution of unauthorized commands.

Tracked as CVE-2024-7261 (CVSS score: 9.8), the vulnerability has been described as a case of operating system (OS) command injection.

"The improper neutralization of special elements in the parameter 'host' in the CGI program of some AP and security router versions could allow an unauthenticated attacker to execute OS commands by sending a crafted cookie to a vulnerable device," Zyxel [said](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-os-command-injection-vulnerability-in-aps-and-security-router-devices-09-03-2024) in an advisory.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Chengchao Ai from the ROIS team of Fuzhou University has been credited with discovering and reporting the flaw.

Zyxel has also [shipped](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-buffer-overflow-vulnerability-in-some-5g-nr-cpe-dsl-ethernet-cpe-fiber-ont-wifi-extender-and-security-router-devices-09-03-2024) [updates](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-vulnerabilities-in-firewalls-09-03-2024) for eight vulnerabilities in its routers and firewalls, including few that are high in severity, that could result in OS command execution, a denial-of-service (DoS), or access browser-based information -

* CVE-2024-5412 (CVSS score: 7.5) - A buffer overflow vulnerability in the "libclinkc" library that could allow an unauthenticated attacker to cause DoS conditions by means of a specially crafted HTTP request

* CVE-2024-6343 (CVSS score: 4.9) - A buffer overflow vulnerability that could allow an authenticated attacker with administrator privileges to trigger DoS conditions by means of a specially crafted HTTP request

* CVE-2024-7203 (CVSS score: 7.2) - A post-authentication command injection vulnerability that could allow an authenticated attacker with administrator privileges to execute OS commands

* CVE-2024-42057 (CVSS score: 8.1) - A command injection vulnerability in the IPSec VPN feature that could allow an unauthenticated attacker to execute some OS commands

* CVE-2024-42058 (CVSS score: 7.5) - A null pointer dereference vulnerability that could allow an unauthenticated attacker to cause DoS conditions by sending crafted packets

* CVE-2024-42059 (CVSS score: 7.2) - A post-authentication command injection vulnerability that could allow an authenticated attacker with administrator privileges to execute some OS commands by uploading a crafted compressed language file via FTP

* CVE-2024-42060 (CVSS score: 7.2) - A post-authentication command injection vulnerability in some firewall versions could allow an authenticated attacker with administrator privileges to execute some OS commands

* CVE-2024-42061 (CVSS score: 6.1) - A reflected cross-site scripting (XSS) vulnerability in the CGI program "dynamic\_script.cgi" that could allow an attacker to trick a user into visiting a crafted URL with the XSS payload and obtain browser-based information

The development comes as D-Link [said](https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10411) four security vulnerabilities affecting its DIR-846 router, counting two critical remote command execution vulnerabilities (CVE-2024-44342, CVSS score: 9.8) will not be patched owing to the products reaching end-of-life (EoL) status of February 2020, urging customers to replace them with support versions.

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

[Command Injection](https://thehackernews.com/search/label/Command%20Injection)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos](https://thehackernews.com/search/label/ddos)[Firewalls](https://thehackernews.com/search/label/Firewalls)[firmware](https://thehackernews.com/search/label/firmware)[network security](https://thehackernews.com/search/label/network%20security)[Patches](https://thehackernews.com/search/label/Patches)[Routers](https://thehackernews.com/search/label/Routers)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/...