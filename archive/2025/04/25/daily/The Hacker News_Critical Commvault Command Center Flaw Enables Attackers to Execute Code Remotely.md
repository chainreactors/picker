---
title: Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely
url: https://thehackernews.com/2025/04/critical-commvault-command-center-flaw.html
source: The Hacker News
date: 2025-04-25
fetch_date: 2025-10-06T22:07:37.821106
---

# Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely

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

# [Critical Commvault Command Center Flaw Enables Attackers to Execute Code Remotely](https://thehackernews.com/2025/04/critical-commvault-command-center-flaw.html)

**Apr 24, 2025**Ravie LakshmananData Breach / Vulnerability

[![Commvault Command Center Flaw](data:image/png;base64... "Commvault Command Center Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDLr1rAcgXFZ49b0Sw8CA4kpnhJhoGkn9phfeRTrJhIU1mqsqUJqP7ogZ1QOgCE8VQ_nIXbML8YL45eS3nm6YSHYF4GCrMiQM7ym6PinTrALJ03qHGtgl0o4pYrwdFbqul3rh1Fin1WW7m-Q6mTDSbjCMw7FuTbBGPyHloxjBtK2kxVfX-wvWKIkN1qw7b/s790-rw-e365/exploit-watch.jpg)

A critical security flaw has been disclosed in the Commvault Command Center that could allow arbitrary code execution on affected installations.

The vulnerability, tracked as **CVE-2025-34028**, carries a CVSS score of 9.0 out of a maximum of 10.0.

"A critical security vulnerability has been identified in the Command Center installation, allowing remote attackers to execute arbitrary code without authentication," Commvault [said](https://documentation.commvault.com/securityadvisories/CV_2025_04_1.html) in an advisory published on April 17, 2025. "This vulnerability could lead to a complete compromise of the Command Center environment."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It impacts the 11.38 Innovation Release, from versions 11.38.0 through 11.38.19, and has been resolved in the following versions -

* 11.38.20
* 11.38.25

watchTowr Labs researcher Sonny Macdonald, who has been credited with discovering and reporting the flaw on April 7, 2025, [said](https://labs.watchtowr.com/fire-in-the-hole-were-breaching-the-vault-commvault-remote-code-execution-cve-2025-34028) in a report shared with The Hacker News that it could be exploited to achieve pre-authenticated remote code execution.

Specifically, the issue is rooted in an endpoint called "deployWebpackage.do," triggering what's called a pre-authenticated Server-Side Request Forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)) owing to the fact that there is "no filtering as to what hosts can be communicated with."

To make matters worse, the SSRF flaw could then be escalated to achieve code execution by making use of a ZIP archive file containing a malicious .JSP file. The entire sequence of events is as follows -

* Send an HTTP request to /commandcenter/deployWebpackage.do, causing the Commvault instance to retrieve a ZIP file from an external server
* Contents of the ZIP file get unzipped into a .tmp directory under the attacker's control
* Use the servicePack parameter to traverse the .tmp directory into a pre-authenticated facing directory on the server, such as ../../Reports/MetricsUpload/shell
* Execute the SSRF via /commandcenter/deployWebpackage.do
* Execute the shell from /reports/MetricsUpload/shell/.tmp/dist-cc/dist-cc/shell.jsp

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

watchTowr has also created a [Detection Artefact Generator](https://github.com/watchtowrlabs/watchTowr-vs-Commvault-PreAuth-RCE-CVE-2025-34028) that organizations can use to determine if their instance is vulnerable to the vulnerability.

With vulnerabilities in backup and replication software like [Veeam](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html) and [NAKIVO](https://thehackernews.com/2025/03/cisa-adds-nakivo-vulnerability-to-kev.html) coming under active exploitation in the wild, it's essential that users apply necessary mitigations to safeguard against potential threats.

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

[Backup software](https://thehackernews.com/search/label/Backup%20software)[Commvault](https://thehackernews.com/search/label/Commvault)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[SSRF](https://thehackernews.com/search/label/SSRF)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Post...