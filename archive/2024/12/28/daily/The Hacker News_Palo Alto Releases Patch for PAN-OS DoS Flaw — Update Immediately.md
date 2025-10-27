---
title: Palo Alto Releases Patch for PAN-OS DoS Flaw — Update Immediately
url: https://thehackernews.com/2024/12/palo-alto-releases-patch-for-pan-os-dos.html
source: The Hacker News
date: 2024-12-28
fetch_date: 2025-10-06T19:44:02.153963
---

# Palo Alto Releases Patch for PAN-OS DoS Flaw — Update Immediately

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

# [Palo Alto Releases Patch for PAN-OS DoS Flaw — Update Immediately](https://thehackernews.com/2024/12/palo-alto-releases-patch-for-pan-os-dos.html)

**Dec 27, 2024**Ravie LakshmananFirewall Security / Vulnerability

[![PAN-OS DoS Flaw](data:image/png;base64... "PAN-OS DoS Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhFUBddpk9ocXHlSGvUq9dfD8SDNLMC8JbBs1XjmLxS2IAqkniWDoE7Yw5U5Mq45AXx5jqiGNukZ5tHaSPqVrmr4I1ZXM8zZ69nceuv1lr_v7UllOVUYAyWSM6HISGyaG_dwCy8IKNgP2JN8hzAEY_TjOT-AJGU9z7HgiDkYoRL43K18uqXM381n713dTY/s790-rw-e365/palo.png)

Palo Alto Networks has disclosed a high-severity vulnerability impacting PAN-OS software that could cause a denial-of-service (DoS) condition on susceptible devices.

The flaw, tracked as CVE-2024-3393 (CVSS score: 8.7), impacts PAN-OS versions 10.X and 11.X, as well as Prisma Access running PAN-OS versions 10.2.8 and later or prior to 11.2.3. It has been addressed in PAN-OS 10.1.14-h8, PAN-OS 10.2.10-h12, PAN-OS 11.1.5, PAN-OS 11.2.3, and all later PAN-OS versions.

"A denial-of-service vulnerability in the DNS Security feature of Palo Alto Networks PAN-OS software allows an unauthenticated attacker to send a malicious packet through the data plane of the firewall that reboots the firewall," the company [said](https://security.paloaltonetworks.com/CVE-2024-3393) in a Friday advisory.

"Repeated attempts to trigger this condition will cause the firewall to enter maintenance mode."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Palo Alto Networks said it discovered the flaw in production use, and that it's aware of customers "experiencing this denial-of-service (DoS) when their firewall blocks malicious DNS packets that trigger this issue."

The extent of the activity is presently unknown. When reached for comment, the company acknowledged that the vulnerability is being used in the wild. "We proactively released this advisory to provide transparency and equip our customers with the information needed to protect their environments," it told The Hacker News.

It's worth pointing out that firewalls that have the DNS Security logging enabled are affected by CVE-2024-3393. Furthermore, the severity of the flaw drops to a CVSS score of 7.1 when access is only provided to authenticated end users via Prisma Access.

The fixes have also been extended to other commonly deployed maintenance releases -

* PAN-OS 11.1 (11.1.2-h16, 11.1.3-h13, 11.1.4-h7, and 11.1.5)
* PAN-OS 10.2 (10.2.8-h19, 10.2.9-h19, 10.2.10-h12, 10.2.11-h10, 10.2.12-h4, 10.2.13-h2, and 10.2.14)
* PAN-OS 10.1 (10.1.14-h8 and 10.1.15)
* PAN-OS 10.2.9-h19 and 10.2.10-h12 (only applicable to Prisma Access)
* PAN-OS 11.0 (No fix owing to it reaching end-of-life status on November 17, 2024)

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

As workarounds and mitigations for unmanaged firewalls or those managed by Panorama, customers have the option of setting Log Severity to "none" for all configured DNS Security categories for each [Anti-Spyware profile](https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-profiles/security-profile-anti-spyware) by navigating to Objects > Security Profiles > Anti-spyware > (select a profile) > DNS Policies > DNS Security.

For firewalls managed by Strata Cloud Manager (SCM), users can either follow the above steps to disable DNS Security logging directly on each device, or across all of them by opening a support case. For Prisma Access tenants managed by SCM, it's recommended to open a support case to turn off logging until an upgrade is carried out.

### CVE-2024-3393 Added to CISA KEV Catalog

On December 30, 2024, the high-severity security flaw impacting Palo Alto Networks PAN-OS software was [added](https://www.cisa.gov/news-events/alerts/2024/12/30/cisa-adds-one-known-exploited-vulnerability-catalog) to the Cybersecurity and Infrastructure Security Agency's (CISA) Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patches by January 20, 2025.

*(The story was updated after publication to include a response from Palo Alto Networks and confirm reports of active exploitation in the wild.)*

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DNS Security](https://thehackernews.com/search/label/DNS%20Security)[dos attack](https://thehackernews.com/search/label/dos%20attack)[Firewall Security](https://thehackernews.com/search/label/Firewall%20Security)[Palo Alto Networks](https://thehackernews.com/search/label/Palo%20Alto%20Networks)[PAN-OS](https://thehackernews.com/search/label/PAN-OS)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-contex...