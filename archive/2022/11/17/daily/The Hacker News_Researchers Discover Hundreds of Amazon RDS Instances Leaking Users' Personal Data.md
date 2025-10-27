---
title: Researchers Discover Hundreds of Amazon RDS Instances Leaking Users' Personal Data
url: https://thehackernews.com/2022/11/researchers-discover-hundreds-of-amazon.html
source: The Hacker News
date: 2022-11-17
fetch_date: 2025-10-03T23:02:37.878278
---

# Researchers Discover Hundreds of Amazon RDS Instances Leaking Users' Personal Data

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

# [Researchers Discover Hundreds of Amazon RDS Instances Leaking Users' Personal Data](https://thehackernews.com/2022/11/researchers-discover-hundreds-of-amazon.html)

**Nov 16, 2022**Ravie Lakshmanan

[![Amazon RDS Snapshots](data:image/png;base64... "Amazon RDS Snapshots")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf1eGs2cdLg0po3Zu2fVzKXa_NB-9JN0hMPKYqSbb9w_vhadWpMdgpHbnko8_aJLjhNRtkvYXufzsG93F5RJHGG62iSsU4Xqa44m4-UckEOBFdgOAoTTb5yEByhu_SWobwZoLPOoFhUmO2QMXmh1X8n1dws9mXDus1Y8XeG802QUZigjawyhdgvftM/s790-rw-e365/amazon.jpg)

Hundreds of databases on Amazon Relational Database Service (Amazon RDS) are exposing personal identifiable information (PII), new findings from Mitiga, a cloud incident response company, show.

"Leaking PII in this manner provides a potential treasure trove for threat actors – either during the reconnaissance phase of the cyber kill chain or extortionware/ransomware campaigns," researchers Ariel Szarf, Doron Karmi, and Lionel Saposnik said in a [report](https://www.mitiga.io/blog/how-mitiga-found-pii-in-exposed-amazon-rds-snapshots) shared with The Hacker News.

This includes names, email addresses, phone numbers, dates of birth, marital status, car rental information, and even company logins.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Amazon RDS is a [web service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) that makes it possible to set up relational databases in the Amazon Web Services (AWS) cloud. It offers support for different database engines such as MariaDB, MySQL, Oracle, PostgreSQL, and SQL Server.

The root cause of the leaks stems from a feature called public [RDS snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html), which allows for creating a backup of the entire database environment running in the cloud and can be accessed by all AWS accounts.

[![Amazon RDS Snapshots](data:image/png;base64... "Amazon RDS Snapshots")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitYLOcg5UTrdgsB3eBqRfURLcojxJmaJmJcS3_jb2E51-6OpptnvQyI1RaQsory35pTv0aGUhxovB76bzwmK4qXAoRSjzEbFDb49cjkGRBspxWaWR9vAfcbh1kC5-LOYjWqgUtEs6OQPh_IhwcL5_X0Zw6QpchRyH1uIlWBji-jHx_xvA2m8z0Bzbz/s790-rw-e365/data.jpg)

"Make sure when sharing a snapshot as public that none of your private information is included in the public snapshot," Amazon [cautions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html) in its documentation. "When a snapshot is shared publicly, it gives all AWS accounts permission both to copy the snapshot and to create DB instances from it."

The Israeli company, which carried out the research from September 21, 2022, to October 20, 2022, said it found 810 snapshots that were publicly shared for varying duration, starting from a few hours to weeks, making them ripe for abuse by malicious actors.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Of the 810 snapshots, over 250 of the backups were exposed for 30 days, suggesting that they were likely forgotten.

Based on the nature of the information exposed, adversaries could either steal the data for financial gain or leverage it to get a better grasp of a company's IT environment, which could then act as a stepping stone for covert intelligence gathering efforts.

It's highly recommended that RDS snapshots are not publicly accessible in order to prevent potential leak or misuse of sensitive data or any other kind of security threat. It's also advised to encrypt snapshots where applicable.

![](data:image/png;base64...)

![The Hacker News](https://www.facebook.com/tr?id=905236253725995&ev=PageView&noscript=1)

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

[amazon](https://thehackernews.com/search/label/amazon)[Amazon RDS](https://thehackernews.com/search/label/Amazon%20RDS)[Database](https://thehackernews.com/search/label/Database)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX ...