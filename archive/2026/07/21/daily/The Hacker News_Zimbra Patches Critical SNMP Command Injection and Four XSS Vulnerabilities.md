---
title: Zimbra Patches Critical SNMP Command Injection and Four XSS Vulnerabilities
url: https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html
source: The Hacker News
date: 2026-07-21
fetch_date: 2026-07-22T05:04:26.797903
---

# Zimbra Patches Critical SNMP Command Injection and Four XSS Vulnerabilities

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Zimbra Patches Critical SNMP Command Injection and Four XSS Vulnerabilities](https://thehackernews.com/2026/07/zimbra-patches-critical-snmp-command.html)

**Ravie Lakshmanan**Jul 21, 2026Email Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEih_Q67gFWBtG5q7zVuyna7iJj3lSm-UQRoMsami8jaf-WYMCXqQlVprQ_ifyXx-PqJg2chDHN3KrFppnZSvejTvSco4kN-P_S4U3vKQHNtvZ48g5wftlSILrMulX1WUMOeeybU4apJ5Iv8BM6ipceEVGSJucR7yRJZguIrfTUaCbbHqefGt6o2BkHrJqV0/s1700-e365/zimbra.jpg)

Zimbra has [rolled out fixes](https://blog.zimbra.com/2026/07/patch-release-update-zimbra-10-1-20/) to address multiple critical security issues, including a command injection flaw in the Simple Network Management Protocol (SNMP) monitoring component.

As many as nine security vulnerabilities have been patched in [Zimbra 10.1.20](https://wiki.zimbra.com/wiki/Zimbra_Releases/10.1.20). Topping the list is a command injection vulnerability in the SNMP monitoring component when SNMP notifications are enabled.

Also patched are four cross-site scripting (XSS) flaws in the Classic Web Client -

* A stored cross-site scripting (XSS) vulnerability that could allow malicious attachment filenames to execute script under specific conditions.
* An XSS vulnerability where crafted fields could execute a malicious script under specific conditions.
* An XSS vulnerability where a crafted field could execute a malicious script when rendered.
* An XSS vulnerability where crafted attachments could execute a malicious script when rendered.

Separately, fixes have been released for a mail forwarding restriction bypass (CVE-2026-50055) that could allow authenticated users to exfiltrate email despite mail forwarding restrictions being enabled. Rapid7 security researcher Jonah Burgess has been credited with discovering and reporting the flaw.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The company did not share any additional specifics, stating "in line with industry best practices, information disclosure is limited for security vulnerability fixes."

The release comes a little over a week after Zimbra [patched](https://thehackernews.com/2026/07/critical-zimbra-flaw-could-let-crafted_0483473395.html) a critical stored XSS flaw in the Classic Web Client that could result in arbitrary code execution.

Although none of the identified vulnerabilities have been flagged as actively exploited, XSS bugs in the email software have been repeatedly exploited by bad actors in the past, making it crucial that customers apply the updates to keep the environment secure.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [Command Injection](https://thehackernews.com/search/label/Command%20Injection), [Cross-site Scripting](https://thehackernews.com/search/label/Cross-site%20Scripting), [email security](https://thehackernews.com/search/label/email%20security), [enterprise security](https://thehackernews.com/search/label/enterprise%20security), [network security](https://thehackernews.com/search/label/network%20security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat](data:image/svg+xml;base64... "URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat")

URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat](https://thehackernews.com/2026/07/urgent-progress-tells-sharefile.html)

[![Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365](data:image/svg+xml;base64... "Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365")

Misconfigured Server Reveals Three Evilginx Phishing Operations Targeting Microsoft 365](https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html)

[![Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling](data:image/svg+xml;base64... "Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling")

Meta Files Patent for AI That Can Listen All Day and Track How You're Feeling](https://thehackernews.com/2026/07/meta-files-patent-for-ai-that-can.html)

[![New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email](data:image/svg+xml;base64... "New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email")

New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email](https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html)

[![Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity](data:image/svg+xml;base64... "Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity")

Microsoft Maps Three Salesforce Attack Paths Tied to a Year of ShinyHunters Activity](https://thehackernews.com/2026/07/m...