---
title: Patch Issued for Critical VMware vCenter Flaw Allowing Remote Code Execution
url: https://thehackernews.com/2024/09/patch-issued-for-critical-vmware.html
source: The Hacker News
date: 2024-09-19
fetch_date: 2025-10-06T18:29:56.902785
---

# Patch Issued for Critical VMware vCenter Flaw Allowing Remote Code Execution

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

# [Patch Issued for Critical VMware vCenter Flaw Allowing Remote Code Execution](https://thehackernews.com/2024/09/patch-issued-for-critical-vmware.html)

**Sep 18, 2024**Ravie LakshmananVirtualization / Network Security

[![VMware vCenter](data:image/png;base64... "VMware vCenter")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMC2DXqJkT9gUlSpCnH6er3vRFfu4PXM_XPALdbscs9PO53KS6LIajmxqL9OU6ASd9YqCONOEZOmQ9bysok7a3CQTA7Rbth8qQZhN-_dFZBsl6_F9WYiqcSq6zU-EK0-vVCNhOCmPYkAh-AMhndzm476610sCoREdf5GoS8OgGPxceUC7N1LU2T_rtnsuN/s790-rw-e365/vmware.png)

Broadcom on Tuesday released updates to address a critical security flaw impacting VMware vCenter Server that could pave the way for remote code execution.

The vulnerability, tracked as CVE-2024-38812 (CVSS score: 9.8), has been described as a heap-overflow vulnerability in the [DCE/RPC protocol](https://en.wikipedia.org/wiki/DCE/RPC).

"A malicious actor with network access to vCenter Server may trigger this vulnerability by sending a specially crafted network packet potentially leading to remote code execution," the virtualization services provider [said](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24968) in a bulletin.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shortcoming is similar to two other remote code execution flaws, [CVE-2024-37079 and CVE-2024-37080](https://thehackernews.com/2024/06/vmware-issues-patches-for-cloud.html) (CVSS scores: 9.8), that VMware resolved in vCenter Server in June 2024.

Also addressed by VMware is a privilege escalation flaw in the vCenter Server (CVE-2024-38813, CVSS score: 7.5) that could enable a malicious actor with network access to the instance to escalate privileges to root by sending a specially crafted network packet.

Security researchers zbl and srs of team TZL have been credited with discovering and reporting the two flaws during the [Matrix Cup](https://finance.yahoo.com/news/matrix-cup-cyber-security-competition-133500114.html) cybersecurity competition held in China back in June 2024. They have been fixed in the below versions -

* vCenter Server 8.0 (Fixed in 8.0 U3b)
* vCenter Server 7.0 (Fixed in 7.0 U3s)
* VMware Cloud Foundation 5.x (Fixed in 8.0 U3b as an asynchronous patch)
* VMware Cloud Foundation 4.x (Fixed in 7.0 U3s as an asynchronous patch)

Broadcom said it's not aware of malicious exploitation of the two vulnerabilities, but has urged customers to update their installations to the latest versions to safeguard against potential threats.

"These vulnerabilities are memory management and corruption issues which can be used against VMware vCenter services, potentially allowing remote code execution," the company [said](https://blogs.vmware.com/cloud-foundation/2024/09/17/vmsa-2024-0019-questions-answers/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The development comes as the U.S. Cybersecurity and Infrastructure Security Agency (CISA) and the Federal Bureau of Investigation (FBI) released a [joint advisory](https://thehackernews.com/2024/07/gitlab-patches-critical-flaw-allowing.html) urging organizations to work towards eliminating cross-site scripting (XSS) flaws that threat actors could exploit to breach systems.

"Cross-site scripting vulnerabilities arise when manufacturers fail to properly validate, sanitize, or escape inputs," the government bodies [said](https://www.cisa.gov/resources-tools/resources/secure-design-alert-eliminating-cross-site-scripting-vulnerabilities). "These failures allow threat actors to inject malicious scripts into web applications, exploiting them to manipulate, steal, or misuse data across different contexts."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Enterprise IT](https://thehackernews.com/search/label/Enterprise%20IT)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[virtualization](https://thehackernews.com/search/label/virtualization)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Ser...