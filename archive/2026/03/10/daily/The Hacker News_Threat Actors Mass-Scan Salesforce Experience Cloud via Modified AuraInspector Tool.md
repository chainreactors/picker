---
title: Threat Actors Mass-Scan Salesforce Experience Cloud via Modified AuraInspector Tool
url: https://thehackernews.com/2026/03/threat-actors-mass-scan-salesforce.html
source: The Hacker News
date: 2026-03-10
fetch_date: 2026-03-11T04:05:31.834736
---

# Threat Actors Mass-Scan Salesforce Experience Cloud via Modified AuraInspector Tool

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Threat Actors Mass-Scan Salesforce Experience Cloud via Modified AuraInspector Tool](https://thehackernews.com/2026/03/threat-actors-mass-scan-salesforce.html)

**Ravie Lakshmanan**Mar 10, 2026Cloud Security / API Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhg3WBGF42HjwJCk1bkljwrz8qAZRBc_WKGgu7SuNluRZBhSEGh3JelP6R_I9w64bbi9soVTwDerZux7tknJmttdOS024pbnsAG8a16SYaBubeRlhDIYboq-SBO53ARQ77uWWAUGX6yTZ8AaeWOQMydWFRP-nbunFtTDsmCpqcUvgFBsTpxHYqSi050MtYl/s1700-e365/salesforce.jpg)

Salesforce has warned of an increase in threat actor activity that's aimed at exploiting misconfigurations in publicly accessible Experience Cloud sites by making use of a customized version of an open-source tool called AuraInspector.

The activity, per the company, involves the exploitation of customers' [overly permissive Experience Cloud guest user configurations](https://www.salesforce.com/blog/misconfiguration-mistakes/) to obtain access to sensitive data.

"Evidence indicates the threat actor is leveraging a modified version of the open-source tool AuraInspector [...] to perform mass scanning of public-facing Experience Cloud sites," Salesforce [said](https://www.salesforce.com/blog/protecting-your-data-essential-actions-to-secure-experience-cloud-guest-user-access/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"While the original AuraInspector is limited to identifying vulnerable objects by probing API endpoints that these sites expose (specifically the /s/sfsites/aura endpoint), the actor has developed a custom version of the tool capable of going beyond identification to actually extract data — exploiting overly permissive guest user settings."

[AuraInspector](https://thehackernews.com/2026/01/threatsday-bulletin-ai-voice-cloning.html#salesforce-audit-tool) refers to an open-source tool designed to help security teams identify and audit access control misconfigurations within the Salesforce Aura framework. It was released by Google-owned Mandiant in January 2026.

Publicly accessible Salesforce sites use a dedicated guest user profile that enables an unauthenticated user to access landing pages, FAQs, and knowledge articles. However, if this profile is misconfigured with excessive permissions, it can potentially grant unauthenticated users access to more data than intended.

As a result, an attacker could exploit this security weakness to directly query Salesforce CRM objects without logging in. For this attack to work, two conditions have to be satisfied by Experience Cloud customers: they are using the guest user profile and have not adhered to Salesforce's recommended configuration guidance.

"At this time, we have not identified any vulnerability inherent to the Salesforce platform associated with this activity," Salesforce [said](https://status.salesforce.com/generalmessages/20000244?locale=en-US). "These attempts are focused on customer configuration settings that, if not properly secured, may increase exposure."

The company attributed the campaign to a known threat actor group without taking its name, raising the possibility that it could be the work of ShinyHunters (aka UNC6240), which has a history of targeting Salesforce environments via third-party applications from [Salesloft](https://thehackernews.com/2025/09/github-account-compromise-led-to.html) and [Gainsight](https://thehackernews.com/2025/11/gainsight-expands-impacted-customer.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fs-report-d)

Salesforce is recommending customers review their Experience Cloud guest user settings, ensure the Default External Access for all objects is set to Private, disable guest users' access to public APIs, restrict visibility settings to prevent guest users from enumerating internal organization members, disable self-registration if not required, and monitor logs for unusual queries.

"This threat actor activity reflects a broader trend of '[identity-based](https://www.salesforce.com/blog/protecting-salesforce-data-after-an-identity-compromise/)' targeting," it added. "Data harvested in these scans, such as names and phone numbers – is often used to build follow-on targeted social engineering and 'vishing' (voice phishing) campaigns."

### Update

According to screenshots [shared](https://x.com/DarkWebInformer/status/2031054614733201823) by Dark Web Informer on X, ShinyHunters has claimed to have breached "several hundred" companies as part of the Salesforce Aura Campaign.

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [CRM Security](https://thehackernews.com/search/label/CRM%20Security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Identity Security](https://thehackernews.com/search/label/Identity%20Security), [Salesforce](https://thehackernews.com/search/label/Salesforce), [social engineering](https://thehackernews.com/search/label/social%20engineering)

Trending News

[![ClawJacked Flaw Lets Mali...