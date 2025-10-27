---
title: New OpenSSH Flaws Enable Man-in-the-Middle and DoS Attacks — Patch Now
url: https://thehackernews.com/2025/02/new-openssh-flaws-enable-man-in-middle.html
source: The Hacker News
date: 2025-02-19
fetch_date: 2025-10-06T20:49:29.719176
---

# New OpenSSH Flaws Enable Man-in-the-Middle and DoS Attacks — Patch Now

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

# [New OpenSSH Flaws Enable Man-in-the-Middle and DoS Attacks — Patch Now](https://thehackernews.com/2025/02/new-openssh-flaws-enable-man-in-middle.html)

**Feb 18, 2025**Ravie LakshmananVulnerability / Network Security

[![OpenSSH](data:image/png;base64... "OpenSSH")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhE70jiODdSyQ2yUz6vu1Nxs_xJ9WUOpw1IqiOiUH0-dgosq8JJbjCS3JJGMhl2PjNp2ZwrSYZE_iWapWN2tpd_z6PMC__mxw4QsLYESE6cma7gge5S6Oyn552CgolPzFnVqgWid9Bbl3l-XLYJUue7lu2YswJxXTnduNVxBNi9DbKRIaFhXo6_L_AjgnbE/s790-rw-e365/ssh.png)

Two security vulnerabilities have been discovered in the OpenSSH secure networking utility suite that, if successfully exploited, could result in an active machine-in-the-middle (MitM) and a denial-of-service (DoS) attack, respectively, under certain conditions.

The vulnerabilities, [detailed](https://blog.qualys.com/vulnerabilities-threat-research/2025/02/18/qualys-tru-discovers-two-vulnerabilities-in-openssh-cve-2025-26465-cve-2025-26466) by the Qualys Threat Research Unit (TRU), are [listed](https://www.qualys.com/2025/02/18/openssh-mitm-dos.txt) below -

* **CVE-2025-26465 (CVSS score: 6.8)** - The OpenSSH client contains a logic error between versions 6.8p1 to 9.9p1 (inclusive) that makes it vulnerable to an active MitM attack if the VerifyHostKeyDNS option is enabled, allowing a malicious interloper to impersonate a legitimate server when a client attempts to connect to it (Introduced in December 2014)
* **CVE-2025-26466 (CVSS score: 5.9)** - The OpenSSH client and server are vulnerable to a pre-authentication DoS attack between versions 9.5p1 to 9.9p1 (inclusive) that causes memory and CPU consumption (Introduced in August 2023)

"If an attacker can perform a man-in-the-middle attack via CVE-2025-26465, the client may accept the attacker's key instead of the legitimate server's key," Saeed Abbasi, manager of product at Qualys TRU, said.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"This would break the integrity of the SSH connection, enabling potential interception or tampering with the session before the user even realizes it."

In other words, a successful exploitation could permit malicious actors to compromise and hijack SSH sessions, and gain unauthorized access to sensitive data. It's worth noting that the VerifyHostKeyDNS option is disabled by default.

That said, the option was enabled by default on FreeBSD from September 2013 until March 2023, thereby potentially exposing machines running the Unix-like operating system to potential risks.

Repeated exploitation of CVE-2025-26466, on the other hand, can result in availability issues, preventing administrators from managing servers and locking legitimate users out, effectively crippling routine operations.

Both the vulnerabilities have been [addressed](https://www.openssh.com/releasenotes.html) in version OpenSSH 9.9p2 released today by OpenSSH maintainers.

The disclosure comes over seven months after Qualys shed light on another OpenSSH flaw dubbed [regreSSHion](https://thehackernews.com/2024/07/new-openssh-vulnerability-could-lead-to.html) (CVE-2024-6387, CVSS score: 8.1) that could have resulted in unauthenticated remote code execution with root privileges in glibc-based Linux systems.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Denial-of-Service](https://thehackernews.com/search/label/Denial-of-Service)[linux](https://thehackernews.com/search/label/linux)[man-in-the-middle attack](https://thehackernews.com/search/label/man-in-the-middle%20attack)[network security](https://thehackernews.com/search/label/network%20security)[OpenSSH](https://thehackernews.com/search/label/OpenSSH)[software security](https://thehackernews.com/search/label/software%20security)[SSH](https://thehackernews.com/search/label/SSH)[System Administration](https://thehackernews.com/search/label/System%20Administration)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:imag...