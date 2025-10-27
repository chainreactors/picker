---
title: Palo Alto Advises Securing PAN-OS Interface Amid Potential RCE Threat Concerns
url: https://thehackernews.com/2024/11/palo-alto-advises-securing-pan-os.html
source: The Hacker News
date: 2024-11-10
fetch_date: 2025-10-06T19:17:02.698106
---

# Palo Alto Advises Securing PAN-OS Interface Amid Potential RCE Threat Concerns

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

# [Palo Alto Advises Securing PAN-OS Interface Amid Potential RCE Threat Concerns](https://thehackernews.com/2024/11/palo-alto-advises-securing-pan-os.html)

**Nov 09, 2024**Ravie LakshmananVulnerability / Network Security

[![Potential RCE Threat Concerns](data:image/png;base64... "Potential RCE Threat Concerns")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJm-DG3VZUcqH1JlqgTKrxODE3JpKpLwFtdu3XtuDPt1k5U58fgtLeZSivdGS2UnhanH6pcMmSovESs_1OumwYHIpSoKcieLLwt9YpzW1aeTU427FahXs3R7Sd-8yVEDEtRMiXa_8wXtZKqcCkHgsOmZVajiLpMAtX41F0sppaxBH2PywJS1KJU-vq0E8S/s790-rw-e365/palo.png)

Palo Alto Networks on Friday issued an informational advisory urging customers to ensure that access to the PAN-OS management interface is secured because of a potential remote code execution vulnerability.

"Palo Alto Networks is aware of a claim of a remote code execution vulnerability via the PAN-OS management interface," the company [said](https://security.paloaltonetworks.com/PAN-SA-2024-0015). "At this time, we do not know the specifics of the claimed vulnerability. We are actively monitoring for signs of any exploitation."

In the interim, the network security vendor has recommended that users correctly configure the management interface in line with the best practices, and make sure that access to it is possible only via trusted internal IPs to limit the attack surface.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

It goes without saying that the management interface should not be exposed to the Internet. Some of the [other guidelines](https://live.paloaltonetworks.com/t5/community-blogs/tips-amp-tricks-how-to-secure-the-management-access-of-your-palo/ba-p/464431) to reduce exposure are listed below -

* Isolate the management interface on a dedicated management VLAN
* Use jump servers to access the management IP
* Limit inbound IP addresses to the management interface to approved management devices
* Only permit secured communication such as SSH, HTTPS
* Only allow PING for testing connectivity to the interface

The development comes a day after the U.S. Cybersecurity and Infrastructure Security Agency (CISA) [added](https://thehackernews.com/2024/11/cisa-alerts-to-active-exploitation-of.html) a now-patched critical security flaw impacting Palo Alto Networks Expedition to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The vulnerability, tracked as CVE-2024-5910 (CVSS score: 9.3), relates to a case of missing authentication in the Expedition migration tool that could lead to an admin account takeover, and possibly gain access to sensitive data.

While it's currently not known how it's being exploited in the wild, federal agencies have been advised to apply the necessary fixes by November 28, 2024, to secure their networks against the threat.

### Update

Palo Alto Networks, in an update on November 15, 2024, confirmed that it "observed threat activity exploiting an unauthenticated remote command execution vulnerability against a limited number of firewall management interfaces which are exposed to the internet." For more details, [click here](https://thehackernews.com/2024/11/cisa-flags-critical-palo-alto-network.html).

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

[CISA](https://thehackernews.com/search/label/CISA)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[network security](https://thehackernews.com/search/label/network%20security)[Palo Alto Networks](https://thehackernews.com/search/label/Palo%20Alto%20Networks)[PAN-OS](https://thehackernews.com/search/label/PAN-OS)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)

[![CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief](data:image/svg+xml;base64... "CometJacking: One Click Can Turn Perplexity’s Comet AI Browser Into a Data Thief")

CometJacking: One Click Can Turn Perplexity's Comet AI Brows...