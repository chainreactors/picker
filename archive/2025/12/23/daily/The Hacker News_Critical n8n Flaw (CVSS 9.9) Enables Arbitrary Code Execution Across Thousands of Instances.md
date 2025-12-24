---
title: Critical n8n Flaw (CVSS 9.9) Enables Arbitrary Code Execution Across Thousands of Instances
url: https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html
source: The Hacker News
date: 2025-12-23
fetch_date: 2025-12-24T03:23:16.501216
---

# Critical n8n Flaw (CVSS 9.9) Enables Arbitrary Code Execution Across Thousands of Instances

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Critical n8n Flaw (CVSS 9.9) Enables Arbitrary Code Execution Across Thousands of Instances](https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html)

**Dec 23, 2025**Ravie LakshmananVulnerability / Workflow Automation

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgBiYnSQwGn-M1HD3JnvekqTc6yRC-xmKXBpGn1C-amAc8WPnk-PSGRPabQbJogN7oijKSF8v_3u00bGvP3BUcKToSIRc4W0V5xuXlWCR1Cv3jbqnMF4oZPr9r4j4bDNabp3j5AYeaE7EQQTVqMC-1ZIUbJvA5C6HeHcnb8coA_WISNeq5xj5MIA0bUx3Q4/s790-rw-e365/n8n.jpg)

A critical security vulnerability has been disclosed in the [n8n](https://www.npmjs.com/package/n8n) workflow automation platform that, if successfully exploited, could result in arbitrary code execution under certain circumstances.

The vulnerability, tracked as **[CVE-2025-68613](https://nvd.nist.gov/vuln/detail/CVE-2025-68613)**, carries a CVSS score of 9.9 out of a maximum of 10.0. The package has about 57,000 weekly downloads, according to statistics on npm.

"Under certain conditions, expressions supplied by authenticated users during workflow configuration may be evaluated in an execution context that is not sufficiently isolated from the underlying runtime," the maintainers of the npm package [said](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/filefix-d)

"An authenticated attacker could abuse this behavior to execute arbitrary code with the privileges of the n8n process. Successful exploitation may lead to full compromise of the affected instance, including unauthorized access to sensitive data, modification of workflows, and execution of system-level operations."

The issue, which affects all versions including and higher than 0.211.0 and below 1.120.4, has been patched in 1.120.4, 1.121.1, and 1.122.0. Per the attack surface management platform Censys, there are [103,476 potentially vulnerable instances](https://censys.com/advisory/cve-2025-68613) as of December 22, 2025. A majority of the instances are located in the U.S., Germany, France, Brazil, and Singapore.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPMOk7FX8XAERxrsKBXytAtwmUIGqawuLSbnUcrlqdqWz0bcTSJN3nlQQ7uYs7qwcnPu2WsmAUQ2lOKnoNzz3PDLl2PkoxQlKx7l3aFVU5yUcb8zeXryliqOlBouAhIGuZvqeuotqa8IrDq2MBXsgIII6Ey_Shz5UcpmLeeVeYfptYDrOVk9P1t_FAyesN/s790-rw-e365/data.png)

In light of the criticality of the flaw, users are advised to apply the updates as soon as possible. If immediate patching is not an option, it's advised to limit workflow creation and editing permissions to trusted users and deploy n8n in a hardened environment with restricted operating system privileges and network access to mitigate the risk.

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

[Attack Surface](https://thehackernews.com/search/label/Attack%20Surface)[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[NPM](https://thehackernews.com/search/label/NPM)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Patch Management](https://thehackernews.com/search/label/Patch%20Management)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Workflow Automation](https://thehackernews.com/search/label/Workflow%20Automation)

Trending News

[![Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](data:image/svg+xml;base64... "Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats")

Featured Chrome Browser Extension Caught Intercepting Millions of Users' AI Chats](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)

[![Google to Shut Down Dark Web Monitoring Tool in February 2026](data:image/svg+xml;base64... "Google to Shut Down Dark Web Monitoring Tool in February 2026")

Google to Shut Down Dark Web Monitoring Tool in February 2026](https://thehackernews.com/2025/12/google-to-shut-down-dark-web-monitoring.html)

[![React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors](data:image/svg+xml;base64... "React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors")

React2Shell Vulnerability Actively Exploited to Deploy Linux Backdoors](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html)

[![Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass](data:image/svg+xml;base64... "Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass")

Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass](https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html)

[![Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign](data:image/svg+xml;base64... "Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign")

Compromised IAM Credentials Power a Large AWS Crypto Mining Campaign](https://thehackernews.com/2025/12/compromised-iam-credentials-power-large.html)

[![GhostPoster Malware Found in 17 Firefox Add-ons with 50,000+ Downl...