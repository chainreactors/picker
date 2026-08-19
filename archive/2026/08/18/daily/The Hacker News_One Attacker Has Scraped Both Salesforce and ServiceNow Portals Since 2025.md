---
title: One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025
url: https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:29.230555
---

# One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [One Attacker Has Scraped Both Salesforce and ServiceNow Portals Since 2025](https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html)

**The Hacker News**Aug 18, 2026SaaS Security / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijGpzrXApP6QuAgCJDVSMHyi1nEVE7liFsNRwcNTWzkwbjmzqv8vGi8qalq_aWVgtgrD2CC_ZT-qXCsj_Bkj8njgIFQExo0gg5PG_dVIQfo9-wW6lIBh6OLp6z4nBeephIQACe1GX_KOP6nzqe10CM4H8p7EwRIlWGImwXgXjsSIYKCCVlSB7Oe1LWAIQ/s1700-e365/reco.gif)

A single piece of infrastructure has been pulling records out of Salesforce and ServiceNow customer portals across multiple industries for more than a year, according to research published this week by agent security platform Reco.

The activity, which Reco has named the City Forum campaign after a domain tied to the attacker's IP address, traces back to one server: 158.220.87.79, hosted on a commodity VPS through the German provider Contabo. Every request from that server carries the same fingerprint, the default user agent of Go's net/http library, which tells researchers the tool behind it is a compiled, purpose built program rather than anything run from a browser. Passive DNS shows the same domain pointed at that IP as far back as March 2025, and the server has not moved since. Targets identified so far span telecoms, banks and other financial services firms, enterprise software vendors including security and data privacy companies, and public sector portals, though Reco has not named individual organizations.

What sets this campaign apart from prior Salesforce guest access abuse, including the widely reported activity attributed to ShinyHunters, is the range of surfaces it touches. Most known attackers in this space lean on Salesforce's older Aura framework, sending high volumes of guest requests to enumerate objects and page through records. This actor does that too, and Aura still accounts for the bulk of the traffic Reco observed, with one target logging over 560,000 events from the same IP. But the tool also reaches Salesforce's newer Lightning Web Runtime sites through the UI-API, a data layer that has no public write ups or known scanning tools associated with it, walking through API versions v56.0 through v66.0 in sequence. On top of that, the same server hammers a native ServiceNow Service Portal search endpoint, POST /api/now/sp/search, that carries almost no public documentation of its own.

According to Reco's writeup, the common thread across every technique is the same underlying issue: a guest identity that was granted more access than the site actually needed to serve the public. Salesforce Experience Cloud sites and ServiceNow portals both maintain a persistent guest user that unauthenticated visitors execute as, and that user cannot be deleted, only restricted. If the guest profile can read a record, the record is effectively public, whether or not the site requires login to view it in a browser.

The research lays out concrete detection steps for security and IT teams on both platforms. On Salesforce, defenders with Event Monitoring or Shield can pull AuraRequest and Sites log events and look for the Go-http-client user agent, the specific IP, and request paths containing /webruntime/api/services/data, alongside spikes in self registration attempts at /SiteRegister and /CommunitiesSelfReg. On ServiceNow, the transaction log table syslog\_transaction can be filtered by source IP and by URLs starting with /api/now/sp/search, with guest created rows and unusual output length flagged as the clearest signal of a live sweep.

Remediation, per the research, centers on tightening the guest profile rather than the endpoints themselves, since both the UI-API and the ServiceNow search endpoint are working as designed. On Salesforce, that means reviewing guest sharing rules, stripping unnecessary object and field level access from the guest profile, disabling self registration where it is not required, and turning off the Experience Builder setting that allows guest users to reach public APIs. On ServiceNow, the fix is mapping which search sources are exposed to public facing portals and auditing the Knowledge Base read criteria that decide what an anonymous search actually returns.

Reco says the infrastructure behind the campaign is still active and the volume is climbing, and the firm has not attributed the activity to a specific named group.

The full technical breakdown, including request signatures, sample queries, and a closer look at how the Service Portal search endpoint decides what to hand back to an anonymous caller, is available in [Reco's writeup of the City Forum campaign](https://www.reco.ai/blog/city-forum-campaign-salesforce-servicenow?utm_source=hackernews).

Security leaders weighing how much of their budget to put toward this kind of app exposure, versus other priorities competing for the same dollars, can find a planning framework in [Reco's guide to AI security investment](https://www.reco.ai/cisos-guide-to-ai-security-investment?utm_source=hackernews), which covers how to size budget, evaluate vendors, and build a business case for the board.

![](data:image/png;base64...)

Found this article interesting? This article is a contributed piece from one of our valued partners. Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

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
[![Faceb...