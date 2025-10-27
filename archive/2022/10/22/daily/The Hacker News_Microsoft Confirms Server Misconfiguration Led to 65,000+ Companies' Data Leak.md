---
title: Microsoft Confirms Server Misconfiguration Led to 65,000+ Companies' Data Leak
url: https://thehackernews.com/2022/10/microsoft-confirms-server.html
source: The Hacker News
date: 2022-10-22
fetch_date: 2025-10-03T20:39:28.032270
---

# Microsoft Confirms Server Misconfiguration Led to 65,000+ Companies' Data Leak

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

# [Microsoft Confirms Server Misconfiguration Led to 65,000+ Companies' Data Leak](https://thehackernews.com/2022/10/microsoft-confirms-server.html)

**Oct 21, 2022**Ravie Lakshmanan

[![Microsoft](data:image/png;base64... "Microsoft")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFBhCbNuDiuoTm0IYtSy80GbNH-a72wQ85U6BLNXWRdYd1plUZBmaaPyvWaQktBZcEt__0Wkg9ffFmu9RndZ3qFpxueYRsb_j6xJvHtbaHg9Zfa8wNeFG5R1I2VrypmCA0WCCy6Dgk7cYL37stFUDzC5I3zTMSkxVtE9orNCLD9hB3-cgRWhA11WIQ/s790-rw-e365/microsoft-hacked.jpg)

Microsoft this week confirmed that it inadvertently exposed information related to thousands of customers following a security lapse that left an endpoint publicly accessible over the internet sans any authentication.

"This misconfiguration resulted in the potential for unauthenticated access to some business transaction data corresponding to interactions between Microsoft and prospective customers, such as the planning or potential implementation and provisioning of Microsoft services," Microsoft [said](https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/) in an alert.

Microsoft also emphasized that the B2B leak was "caused by an unintentional misconfiguration on an endpoint that is not in use across the Microsoft ecosystem and was not the result of a security vulnerability."

The misconfiguration of the Azure Blob Storage was spotted on September 24, 2022, by cybersecurity company SOCRadar, which termed the leak **BlueBleed**. Microsoft said it's in the process of directly notifying impacted customers.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The Windows maker did not reveal the scale of the data leak, but according to SOCRadar, it affects more than 65,000 entities in 111 countries. The exposure amounts to 2.4 terabytes of data that consists of invoices, product orders, signed customer documents, partner ecosystem details, among others.

"The exposed data include files dated from 2017 to August 2022," SOCRadar [said](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/).

Microsoft, however, has disputed the extent of the issue, stating the data included names, email addresses, email content, company name, and phone numbers, and attached files relating to business "between a customer and Microsoft or an authorized Microsoft partner."

It also claimed in its disclosure that the threat intel company "greatly exaggerated" the scope of the problem as the data set contains "duplicate information, with multiple references to the same emails, projects, and users."

[![Microsoft](data:image/png;base64... "Microsoft")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgr8Kl0PJH1fbIwZyKNtDrzxlDAMhCWHibCbKKu6rx3-AAadNujKnlPN_bOoDar9Znmk1R8c4ozT-ZlX8j7NOzjWHeHBcYph2f7zFBLhY3t_QkmXzPtwtW1fVPJ_d0Y8eJNNlz_OwXSlcUKTZLklYUinpBax_QpjR6py19Hs3JU7n3t97vS24ZDwy6Y/s790-rw-e365/ms.jpg)

On top of that, Redmond expressed its disappointment over SOCRadar's decision to release a [public search tool](https://socradar.io/labs/bluebleed) that it said exposes customers to unnecessary security risks.

SOCRadar, in a [follow-up post](https://socradar.io/details-on-the-largest-b2b-leak-bluebleed/) on Thursday, likened the BlueBleed search engine to data breach notification service "Have I Been Pwned," describing it as a way for organizations to search if their data was exposed in a cloud data leak.

The cybersecurity vendor also said it has temporarily suspended all BlueBleed queries in the Threat Hunting module it offers to its customers as of October 19, 2022, following Microsoft's request.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Microsoft being unable (read: refusing) to tell customers what data was taken and apparently not notifying regulators – a legal requirement – has the hallmarks of a major botched response," security researcher Kevin Beaumont [tweeted](https://twitter.com/GossiTheDog/status/1582819993263099905). "I hope it isn't."

Beaumont further said the Microsoft bucket "has been publicly indexed for months" by services like [Grayhat Warfare](https://buckets.grayhatwarfare.com/) and that "it's even in search engines."

There is no evidence that the information was improperly accessed by threat actors prior to the disclosure, but such leaks could be exploited for malicious purposes such as extortion, social engineering attacks, or a quick profit.

"While some of the data that may have been accessed seems trivial, if SOCRadar is correct in what was exposed, it could include some sensitive information about the infrastructure and network configuration of potential customers," Erich Kron, security awareness advocate at KnowBe4, told The Hacker News in an email.

"This information could be valuable to potential attackers who may be looking for vulnerabilities within one of these organizations' networks."

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

[Azure](https://thehackernews.com/search/label/Azure)[data breach](https://thehackernews.com/search/label/data%20breach)[Data Leak](https://thehackernew...