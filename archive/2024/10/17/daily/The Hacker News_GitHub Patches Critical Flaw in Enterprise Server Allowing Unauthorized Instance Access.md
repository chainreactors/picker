---
title: GitHub Patches Critical Flaw in Enterprise Server Allowing Unauthorized Instance Access
url: https://thehackernews.com/2024/10/github-patches-critical-flaw-in.html
source: The Hacker News
date: 2024-10-17
fetch_date: 2025-10-06T18:59:38.042580
---

# GitHub Patches Critical Flaw in Enterprise Server Allowing Unauthorized Instance Access

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

# [GitHub Patches Critical Flaw in Enterprise Server Allowing Unauthorized Instance Access](https://thehackernews.com/2024/10/github-patches-critical-flaw-in.html)

**Oct 16, 2024**Ravie LakshmananEnterprise Security / Vulnerability

[![Enterprise Server](data:image/png;base64... "Enterprise Server")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgO4E-cqezCI79n7lQJVudzuTFuuUVJUX_at66iKQBhm3qef1iPirSBFJOfZnI44dUXxRV2_ADl44RUI0m2SNu-1mb2ajtVd-5YKxHfpnOXA7NOBKuPJRBbvmLSkY9cQUr1LjiE5KqPpsJ3l_ByjRf4fPUIQKYtD0tzVA9zqnCHJSnEQ5CLRM7dJ1H2JrBC/s790-rw-e365/github.png)

GitHub has [released](https://docs.github.com/en/enterprise-server%403.14/admin/all-releases) security updates for Enterprise Server (GHES) to address multiple issues, including a critical bug that could allow unauthorized access to an instance.

The vulnerability, tracked as CVE-2024-9487, carries a CVS score of 9.5 out of a maximum of 10.0

"An attacker could bypass SAML single sign-on (SSO) authentication with the optional encrypted assertions feature, allowing unauthorized provisioning of users and access to the instance, by exploiting an improper verification of cryptographic signatures vulnerability in GitHub Enterprise Server," GitHub [said](https://docs.github.com/en/enterprise-server%403.14/admin/release-notes) in an alert.

The Microsoft-owned company characterized the flaw as a regression that was introduced as part of follow-up remediation from [CVE-2024-4985](https://thehackernews.com/2024/05/critical-github-enterprise-server-flaw.html) (CVSS score: 10.0), a maximum severity vulnerability that was patched back in May 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Also fixed by GitHub are two other shortcomings -

* CVE-2024-9539 (CVSS score: 5.7) - An information disclosure vulnerability that could enable an attacker to retrieve metadata belonging to a victim user upon clicking malicious URLs for SVG assets

* A sensitive data exposure in HTML forms in the management console (no CVE)

All three security vulnerabilities have been addressed in Enterprise Server versions 3.14.2, 3.13.5, 3.12.10, and 3.11.16.

Back in August, GitHub also [patched](https://thehackernews.com/2024/08/github-patches-critical-security-flaw.html) a critical security defect (CVE-2024-6800, CVSS score: 9.5) that could be abused to gain site administrator privileges.

Organizations that are running a vulnerable self-hosted version of GHES are highly advised to update to the latest version to safeguard against potential security threats.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[GitHub](https://thehackernews.com/search/label/GitHub)[Identity Management](https://thehackernews.com/search/label/Identity%20Management)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Browser Into a Data Thief](https://thehackernews.com/2025/10/cometjacking-one-click-can-turn.html)

[![Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](data:image/svg+xml;base64... "Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day")

Scanning Activity on Palo Alto Networks Portals Jump 500% in One Day](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)

[![Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL](data:image/svg+xml;base64... "Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL")

Researchers Warn of Self-Spreading WhatsApp Malware Named SORVEPOTEL](https://thehackernews.com/2025/10/researchers-warn-of-self-spreading.html)

[![ThreatsDay Bulletin: CarPlay Exploit, BYOVD Tactics, SQL C2 Attacks, iCloud Backdoo...