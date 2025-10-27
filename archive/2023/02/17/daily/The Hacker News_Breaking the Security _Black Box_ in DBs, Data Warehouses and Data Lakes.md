---
title: Breaking the Security "Black Box" in DBs, Data Warehouses and Data Lakes
url: https://thehackernews.com/2023/02/breaking-security-black-box-in-dbs-data.html
source: The Hacker News
date: 2023-02-17
fetch_date: 2025-10-04T07:17:13.964303
---

# Breaking the Security "Black Box" in DBs, Data Warehouses and Data Lakes

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

# [Breaking the Security "Black Box" in DBs, Data Warehouses and Data Lakes](https://thehackernews.com/2023/02/breaking-security-black-box-in-dbs-data.html)

**Feb 16, 2023**The Hacker NewsData Security / Compliance

[![Satori automated data security platform](data:image/png;base64... "Satori automated data security platform")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiV4eq3SJl4OOpTa9q7WTntkbDIGWMB3_oVmQSGLBftDvoecLflnzXU6uyJZCfSOwrkmIQ5uzJ0ZDMK7ULjGEn9ECPBnHDy6yil0YKIv8NsAMG-JjzJT-xmKSuJ10-Yyoqr3rYU9ijgFt1Tw0vCE8DiK6gpOZVmkMvAPNdln-Ok3bv0mdvxwhbZ80qE/s790-rw-e365/main.png)

Security teams typically have great visibility over most areas, for example, the corporate network, endpoints, servers, and cloud infrastructure. They use this visibility to enforce the necessary security and compliance requirements. However, this is not the case when it comes to sensitive data sitting in production or analytic databases, data warehouses or data lakes.

Security teams have to rely on data teams to locate sensitive data and enforce access controls and security policies. This is a huge headache for both the security and data teams. It weakens the business's security and compliance putting it at risk of exposing sensitive data, large fines, reputational damages, and more. Also, in many cases, it slows down the business's ability to scale up data operations.

This article examines how Satori, a data security platform, gives control of the sensitive data in databases, data warehouses and data lakes to the security teams.

Satori's [**automated data security platform**](https://satoricyber.com/) provides a simple and easy way to meet security and compliance requirements while reducing risk exposure.

## Why is Securing Data Stores Hard?

Security teams don't have good visibility and enforcement of policies regarding access to DBs, data warehouses or data lakes. Take a look at an example.

Nick is a security engineering manager at ACME organization. He is responsible for keeping up with changing security and compliance regulations such as HIPAA, SOC2, and ISO. This is a difficult task since security and compliance regulations are always changing and evolving. Nick is good at his job and can wade through the complexities of the different regulations and determine the necessary security measures to ensure that ACME remains in compliance. This is important so that ACME doesn't fail an audit, expose sensitive data, receive fines or worse.

Then, one day, Nick is suddenly tasked with meeting security and compliance requirements across all of ACME's analytic and production data.

Nick faces a problem. Although he has done his job and determined the necessary steps to ensure security and compliance it is very difficult to actually carry out these steps and implement the security policies. There are several reasons why Nick's job is difficult and frustrating that are explored in more detail below.

### Visibility Over Sensitive Data and Logs

Nick's lack of visibility limits his ability to implement and manage security policies and compliance requirements. Three main sources impede his visibility.

#### 1 — Different logs from different sources are "buried."

Since ACME has sensitive data spread across multiple databases, data lakes and data warehouses; there are a wide variety of audit logs from all of these different sources. Furthermore, Nick has to correlate the log data with known locations of sensitive data (if he has them).

#### 2 — Changes to the configuration and processes to enable visibility.

It is important to ensure that all sensitive data access is accurately monitored. Nick may want to examine why a user was accessing sensitive information in a region outside their service area and prevent this type of access from occurring in the future. He needs to change the configuration and make sure that the change control processes are effective. However, this is not as simple as it seems. The lack of visibility means that Nick cannot verify that these changes are made in real-time.

#### 3 — Knowing the type and location of sensitive data.

Nick doesn't have the ability to continuously seek out sensitive data. His lack of visibility coupled with the fact that he is not the owner of these data stores means that he is not able to search the multiple data stores for sensitive data. Instead, he has to rely on the engineering team.

The majority of companies use manual processes to scan and discover sensitive data. The manual scanning of data, when Nick can get the data engineers to stop their projects and undertake this task, is slow and error-prone. This means that Nick is often anxious about getting the data engineers to continuously scan the data to find sensitive information and identity information.

### Enforcement of Security Policies

ACME has sensitive data that is spread across a number of diverse databases, data lakes and data warehouses. Nick is a very good security engineer but it is unlikely that he has the knowledge to understand SQL and the inner workings of the databases, data warehouses and lakes that comprise the ACME data stack. Since he does not have the ability to actually code the necessary changes to the security policies he has to rely on the data engineers to carry out his tasks.

Even though data engineers typically prefer to work on their own projects instead of implementing Nick's security policies, it is unlikely that they would allow Nick to implement them himself, even if he knew how. The engineers who own the data stores probably do not want Nick to meddle with things like creating objects or changing configurations on their data stores. So even if he wanted to, and could, it is unlikely that Nick has the access to apply and implement the necessary security policies, instead, he needs to rely on the data engineers to do this for him.

## Using a Data Security Platform

An overview of using [**Satori's automated data security platform**](https://satoricyber.com/), to overcome such challenges follows.
...