---
title: Zoom and Xerox Release Critical Security Updates Fixing Privilege Escalation and RCE Flaws
url: https://thehackernews.com/2025/08/zoom-and-xerox-release-critical.html
source: The Hacker News
date: 2025-08-14
fetch_date: 2025-10-07T00:50:44.531957
---

# Zoom and Xerox Release Critical Security Updates Fixing Privilege Escalation and RCE Flaws

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

# [Zoom and Xerox Release Critical Security Updates Fixing Privilege Escalation and RCE Flaws](https://thehackernews.com/2025/08/zoom-and-xerox-release-critical.html)

**Aug 13, 2025**Ravie LakshmananVulnerability / Software Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha2BURnd9EZHiBtdwvpmovsvT8uqUgGB2Wy-wafrWB8ZFmNliJ7Vvb3XQpmYQ0gCgI-gRasZ-II_tc6Bf4P39mQ9odhekagkyBKDWLezbNZfnwKTOOTKXFCxsfUFHnogGyBb_SftFiulCiCUfNQrfT95BRqZwGOKy_eBDQfWSdxdE2rO8jcoNNVLnpYQ8v/s790-rw-e365/zoom.png)

Zoom and Xerox have addressed critical security flaws in Zoom Clients for Windows and FreeFlow Core that could allow privilege escalation and remote code execution.

The vulnerability impacting Zoom Clients for Windows, tracked as **CVE-2025-49457** (CVSS score: 9.6), relates to a case of an untrusted search path that could pave the way for privilege escalation.

"Untrusted search path in certain Zoom Clients for Windows may allow an unauthenticated user to conduct an escalation of privilege via network access," Zoom [said](https://www.zoom.com/en/trust/security-bulletin/zsb-25030/) in a security bulletin on Tuesday.

The issue, reported by its own Offensive Security team, affects the following products -

* Zoom Workplace for Windows before version 6.3.10
* Zoom Workplace VDI for Windows before version 6.3.10 (except 6.1.16 and 6.2.12)
* Zoom Rooms for Windows before version 6.3.10
* Zoom Rooms Controller for Windows before version 6.3.10
* Zoom Meeting SDK for Windows before version 6.3.10

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The disclosure comes as multiple vulnerabilities have been [disclosed](https://securitydocs.business.xerox.com/wp-content/uploads/2025/08/Xerox-Security-Bulletin-025-013-for-Freeflow-Core-8.0.5.pdf) in Xerox FreeFlow Core, the most severe of which could result in remote code execution. The issues, which have been addressed in version 8.0.4, include -

* **CVE-2025-8355** (CVSS score: 7.5) - XML External Entity (XXE) injection vulnerability leading to server-side request forgery (SSRF)
* **CVE-2025-8356** (CVSS score: 9.8) - Path traversal vulnerability leading to remote code execution

"These vulnerabilities are rudimentary to exploit and if exploited, could allow an attacker to execute arbitrary commands on the affected system, steal sensitive data, or attempt to move laterally into a given corporate environment to further their attack," Horizon3.ai said.

The cybersecurity company said CVE-2025-8355 stems from the fact the binary ("jmfclient.jar") responsible for handling Job Message Format (JMF) messages, which contain commands for managing print jobs and reporting their status, included an XML parsing utility that did not sanitize or limit usage of XML External Entities. As a result, an attacker could send a specially crafted request to perform SSRF attacks.

CVE-2025-8356, on the other hand, has to do with the XML parsing routine's inadequate handling of JMF commands related to file upload and processing, opening the door for a path traversal attack. This vulnerability could be weaponized to drop a web shell in a publicly accessible location via a crafted HTTP request.

"While the service on port 4004 doesn't contain any features that would allow this file to be served, the primary web portals provide all the necessary functionality for executing and serving our malicious payload," security researcher Jimi Sebree [said](https://horizon3.ai/attack-research/attack-blogs/from-support-ticket-to-zero-day/).

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[network security](https://thehackernews.com/search/label/network%20security)[privilege escalation](https://thehackernews.com/search/label/privilege%20escalation)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[software security](https://thehackernews.com/search/label/software%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Xerox](https://thehackernews.com/search/label/Xerox)[Zoom](https://thehackernews.com/search/label/Zoom)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found ...