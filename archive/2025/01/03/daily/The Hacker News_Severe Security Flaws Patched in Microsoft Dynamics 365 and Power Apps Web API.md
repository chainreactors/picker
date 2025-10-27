---
title: Severe Security Flaws Patched in Microsoft Dynamics 365 and Power Apps Web API
url: https://thehackernews.com/2025/01/severe-security-flaws-patched-in.html
source: The Hacker News
date: 2025-01-03
fetch_date: 2025-10-06T20:13:09.676054
---

# Severe Security Flaws Patched in Microsoft Dynamics 365 and Power Apps Web API

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

# [Severe Security Flaws Patched in Microsoft Dynamics 365 and Power Apps Web API](https://thehackernews.com/2025/01/severe-security-flaws-patched-in.html)

**Jan 02, 2025**Ravie LakshmananVulnerability / Data Protection

[![Microsoft Dynamics 365 and Power Apps Web API](data:image/png;base64... "Microsoft Dynamics 365 and Power Apps Web API")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6YctML2Y_FznR8D44mD_aL96mHLac5JzYNO0oUaRakb03ym-tDPcDj6aDWKPqL86zUsqV6DoDgjb5VV2aQd0qo2GkuAGh87b-kiWuijzJ6_OSXmsKgxMryg0DwnWjDo_zb50MMuCGjEAvgqeKj0fKyc4PzLuVkS77LbWNz2yoO1q1lURgS5Rs_-rD-_C3/s790-rw-e365/powe.png)

Details have emerged about three now-patched security vulnerabilities in Dynamics 365 and Power Apps Web API that could result in data exposure.

The flaws, [discovered](https://www.stratussecurity.com/post/critical-microsoft-365-vulnerability) by Melbourne-based cybersecurity company Stratus Security, have been addressed as of May 2024. Two of the three shortcomings reside in Power Platform's [OData Web API Filter](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query/overview), while the third vulnerability is rooted in the [FetchXML API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/fetchxml/overview).

The root cause of the first vulnerability is the lack of access control on the OData Web API Filter, thereby allowing access to the [contacts table](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/customer-entities-account-contact) that holds [sensitive information](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/contact) such as full names, phone numbers, addresses, financial data, and password hashes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A threat actor could then weaponize the flaw to perform a boolean-based search to extract the complete hash by guessing each character of the hash sequentially until the correct value is identified.

"For example, we start by sending startswith(adx\_identity\_passwordhash, 'a') then startswith([adx\_identity\_passwordhash](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/contact#BKMK_adx_identity_passwordhash) , 'aa') then startswith(adx\_identity\_passwordhash , 'ab') and so on until it returns results that start with ab," Stratus Security said.

"We continue this process until the query returns results that start with 'ab'. Eventually, when no further characters return a valid result, we know we have obtained the complete value."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghzF2f9eR1a1EA_B5tbC_oJOFADI2gkmJGbG1GoN7r5Jv1__jJ5MIQW6-C86xfshURXp0N1kKr2gj59uNjB5k8AtxaNh1_1uBGciUaAGALrosPhQGrLglZSCRgrRZIc1SM1elTtJmim0galZrkgEg0nnN8pKLZPvGFATJeI8QfoFDRBSoXLkL_0hVvWdZX/s790-rw-e365/response.png)

The second vulnerability, on the other hand, lies in using the orderby clause in the same API to obtain the data from the necessary database table column (e.g., [EMailAddress1](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/reference/entities/contact#BKMK_EMailAddress1), which refers to the primary email address for the contact).

Lastly, Stratus Security also found that the FetchXML API could be exploited in conjunction with the contacts table to access restricted columns using an orderby query.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"When utilizing the FetchXML API, an attacker can craft an orderby query on any column, completely bypassing the existing access controls," it said. "Unlike the previous vulnerabilities, this method does not necessitate the orderby to be in descending order, adding a layer of flexibility to the attack."

An attacker weaponizing these flaws could, therefore, compile a list of password hashes and emails, then crack the passwords or sell the data.

"The discovery of vulnerabilities in the Dynamics 365 and Power Apps API underscores a critical reminder: cybersecurity requires constant vigilance, especially for large companies that hold so much data like Microsoft," Stratus Security said.

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

[Access Control](https://thehackernews.com/search/label/Access%20Control)[API Security](https://thehackernews.com/search/label/API%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data protection](https://thehackernews.com/search/label/data%20protection)[Microsoft](https://thehackernews.com/search/label/Microsoft)[password security](https://thehackernews.com/search/label/password%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterp...