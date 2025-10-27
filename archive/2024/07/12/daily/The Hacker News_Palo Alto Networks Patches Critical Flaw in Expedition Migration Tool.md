---
title: Palo Alto Networks Patches Critical Flaw in Expedition Migration Tool
url: https://thehackernews.com/2024/07/palo-alto-networks-patches-critical.html
source: The Hacker News
date: 2024-07-12
fetch_date: 2025-10-06T17:46:09.410170
---

# Palo Alto Networks Patches Critical Flaw in Expedition Migration Tool

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

# [Palo Alto Networks Patches Critical Flaw in Expedition Migration Tool](https://thehackernews.com/2024/07/palo-alto-networks-patches-critical.html)

**Jul 11, 2024**Ravie LakshmananVulnerability / Enterprise Security

[![Palo Alto Networks](data:image/png;base64... "Palo Alto Networks")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-siVqYc98XRaBvRCGc41KIhVdA5dDNA0RKWdH_Ity3AraUc4s5Zd7rkzDgGWovHtxLQoHb-bQqZzMe_NpyWWbtNx2pMIz3e2MsTMFKAhV67qTpJZqyqAD7ki6r-sdGCxXJ8QCII_ov8hjR6MU9A12xm7CbW-M8MUekY7oH5oIP6xrTiSo7o3SUcZsfd2t/s790-rw-e365/palo.png)

Palo Alto Networks has released security updates to address [five security flaws](https://security.paloaltonetworks.com/) impacting its products, including a critical bug that could lead to an authentication bypass.

Cataloged as CVE-2024-5910 (CVSS score: 9.3), the vulnerability has been described as a case of missing authentication in its Expedition migration tool that could lead to an admin account takeover.

"Missing authentication for a critical function in Palo Alto Networks Expedition can lead to an Expedition admin account takeover for attackers with network access to Expedition," the company [said](https://security.paloaltonetworks.com/CVE-2024-5910) in an advisory. "Configuration secrets, credentials, and other data imported into Expedition is at risk due to this issue."

The flaw impacts all versions of Expedition prior to version 1.2.92, which remediates the problem. Synopsys Cybersecurity Research Center's (CyRC) Brian Hysell has been credited with discovering and reporting the issue.

While there is no evidence that the vulnerability has been exploited in the wild, users are advised to update to the latest version to secure against potential threats.

As workarounds, Palo Alto Networks is recommending that network access to Expedition is restricted to authorized users, hosts, or networks.

Also fixed by the American cybersecurity firm is a newly disclosed flaw in the RADIUS protocol called [BlastRADIUS](https://thehackernews.com/2024/07/radius-protocol-vulnerability-exposes.html) (CVE-2024-3596) that could allow a bad actor with capabilities to perform an adversary-in-the-middle (AitM) attack between Palo Alto Networks PAN-OS firewall and a RADIUS server to sidestep authentication.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The vulnerability then permits the attacker to "escalate privileges to 'superuser' when RADIUS authentication is in use and either [CHAP or PAP](https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/authentication/configure-radius-authentication) is selected in the RADIUS server profile," it [said](https://security.paloaltonetworks.com/CVE-2024-3596).

The following products are affected by the shortcomings:

* PAN-OS 11.1 (versions < 11.1.3, fixed in >= 11.1.3)
* PAN-OS 11.0 (versions < 11.0.4-h4, fixed in >= 11.0.4-h4)
* PAN-OS 10.2 (versions < 10.2.10, fixed in >= 10.2.10)
* PAN-OS 10.1 (versions < 10.1.14, fixed in >= 10.1.14)
* PAN-OS 9.1 (versions < 9.1.19, fixed in >= 9.1.19)
* Prisma Access (all versions, fix expected to be released on July 30)

It also noted that neither CHAP nor PAP should be used unless they are encapsulated by an encrypted tunnel since the authentication protocols do not offer Transport Layer Security (TLS). They are not vulnerable in cases where they are used in conjunction with a TLS tunnel.

However, it's worth noting that PAN-OS firewalls configured to use EAP-TTLS with PAP as the authentication protocol for a RADIUS server are also not susceptible to the attack.

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[enterprise security](https://thehackernews.com/search/label/enterprise%20security)[Firewall Security](https://thehackernews.com/search/label/Firewall%20Security)[network security](https://thehackernews.com/search/label/network%20security)[Software Updates](https://thehackernews.com/search/label/Software%20Updates)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-mal...