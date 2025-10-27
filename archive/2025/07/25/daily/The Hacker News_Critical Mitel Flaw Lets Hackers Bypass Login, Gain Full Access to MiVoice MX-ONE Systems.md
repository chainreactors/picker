---
title: Critical Mitel Flaw Lets Hackers Bypass Login, Gain Full Access to MiVoice MX-ONE Systems
url: https://thehackernews.com/2025/07/critical-mitel-flaw-lets-hackers-bypass.html
source: The Hacker News
date: 2025-07-25
fetch_date: 2025-10-06T23:52:32.238274
---

# Critical Mitel Flaw Lets Hackers Bypass Login, Gain Full Access to MiVoice MX-ONE Systems

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

# [Critical Mitel Flaw Lets Hackers Bypass Login, Gain Full Access to MiVoice MX-ONE Systems](https://thehackernews.com/2025/07/critical-mitel-flaw-lets-hackers-bypass.html)

**Jul 24, 2025**Ravie LakshmananVulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEioFgy77Nhemnu-J7tFZrPrNWqU3YYisg8msYMStMHGEBzrWptx-dT1VQk4w73r9WhQoH54Q_hRY5EIdQmhRrim0I4e-QFEQspo1kEw27WC2b85GfuprMjxYzp38XcBb_msHql1-8EAURCMzFPKcvfkJmIDBctcKdQq2xnaxBG1tQcJ_GMFWhVv5q-Y_HuD/s790-rw-e365/phone-hack.jpg)

Mitel has released security updates to address a critical security flaw in MiVoice MX-ONE that could allow an attacker to bypass authentication protections.

"An authentication bypass vulnerability has been identified in the Provisioning Manager component of Mitel MiVoice MX-ONE, which, if successfully exploited, could allow an unauthenticated attacker to conduct an authentication bypass attack due to improper access control," the company [said](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2025-0009) in an advisory released Wednesday.

"A successful exploit of this vulnerability could allow an attacker to gain unauthorized access to user or admin accounts in the system."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The shortcoming, which is yet to be assigned a CVE identifier, carries a CVSS score of 9.4 out of a maximum of 10.0. It affects MiVoice MX-ONE versions from 7.3 (7.3.0.0.50) to 7.8 SP1 (7.8.1.0.14).

Patches for the issue have been made available in MXO-15711\_78SP0 and MXO-15711\_78SP1 for MX-ONE versions 7.8 and 7.8 SP1, respectively. Customers using MiVoice MX-ONE version 7.3 and above are recommended to submit a patch request to their authorized service partner.

As mitigations until fixes can be applied, it's advised to limit direct exposure of MX-ONE services to the public internet and ensure that they are placed within a trusted network.

Along with the authentication bypass flaw, Mitel has shipped updates to resolve a high-severity vulnerability in MiCollab (CVE-2025-52914, CVSS score: 8.8) that, if successfully exploited, could permit an authenticated attacker to carry out an SQL injection attack.

"A successful exploit could allow an attacker to access user provisioning information and execute arbitrary SQL database commands with potential impacts on the confidentiality, integrity, and availability of the system," Mitel [said](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2025-0008).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The vulnerability, which impacts MiCollab versions 10.0 (10.0.0.26) to 10.0 SP1 FP1 (10.0.1.101) and 9.8 SP3 (9.8.3.1) and earlier, has been resolved in versions 10.1 (10.1.0.10), 9.8 SP3 FP1 (9.8.3.103), and later.

With shortcomings in Mitel devices [coming under](https://thehackernews.com/2025/01/cisa-flags-critical-flaws-in-mitel-and.html) [active attacks](https://thehackernews.com/2025/01/new-aquabot-botnet-exploits-cve-2024.html) in the past, it's essential that users move quickly to update their installations as soon as possible to mitigate potential threats.

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

[Authentication](https://thehackernews.com/search/label/Authentication)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Mitel](https://thehackernews.com/search/label/Mitel)[network security](https://thehackernews.com/search/label/network%20security)[sql injection](https://thehackernews.com/search/label/sql%20injection)[System Integrity](https://thehackernews.com/search/label/System%20Integrity)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjackin...