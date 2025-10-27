---
title: The Fundamentals of Cloud Security Stress Testing
url: https://thehackernews.com/2024/05/the-fundamentals-of-cloud-security.html
source: The Hacker News
date: 2024-05-09
fetch_date: 2025-10-06T17:30:07.912542
---

# The Fundamentals of Cloud Security Stress Testing

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

# [The Fundamentals of Cloud Security Stress Testing](https://thehackernews.com/2024/05/the-fundamentals-of-cloud-security.html)

**May 08, 2024**The Hacker NewsPenetration Testing / Cloud Security

[![Cloud Security Stress Testing](data:image/png;base64... "Cloud Security Stress Testing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9g0_5hh9yyfiqTDAJeGldQ363-xqM83qZitESxMRryqG8TxZrN0XEBeKwwJvWIzoV_MgNFQSFwlYIw6D-9kvBsLkEQ4x-jwm0W1f2mBfmESM1hyMmnQ1s9rQFzu_5aSyLIrguF0hROMma0LFvJuIr3zsyNyuzWLcR88ebXEzdLdbGffcUxTPy4-Ltzi4/s790-rw-e365/pen.png)

״Defenders think in lists, attackers think in graphs," said John Lambert from Microsoft, distilling the fundamental difference in mindset between those who defend IT systems and those who try to compromise them.

The traditional approach for defenders is to list security gaps directly related to their assets in the network and eliminate as many as possible, starting with the most critical. Adversaries, in contrast, start with the end goal in mind and focus on charting the path toward a breach. They will generally look for the weakest link in the security chain to break in and progress the attack from there all the way to the crown jewels.

Security teams must embrace the attacker's perspective to ensure their organization's cybersecurity defenses are adequate. Drawing an analogy to a daily life example, the standard way to defend our house from intrusion is to ensure all the doors are locked. But to validate that your house is protected requires testing your security like a burglar: attempting to pick the locks, climb through windows, and looking for places where house keys might be "safely" stored.

Penetration testing serves this need precisely: it provides an attacker's view into what can be compromised. The practice of penetration testing has been around for decades, helping to reveal how resilient our networks are against malicious attacks. However, with modern enterprises increasing their usage of cloud services, it is just as necessary to apply the concept of traditional penetration testing to the cloud.

## The Cloud's Not a Safe Haven - Know What You Need to Protect

Cloud architectures comprise resources, identities, and configurations that are defined programmatically and change at a rapid pace. As a result, the cloud can be a pandora's box of added cybersecurity complexity. While the leading cloud service providers implement rigorous security practices, this may generate a false sense of security for organizations, who may not be aware of their responsibility for securing their cloud assets, as defined by the [cloud shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). For these reasons, pentesting in the cloud is just as important as traditional network penetration testing - in some cases, even more so.

In this blog post, we explore the basic cloud pentesting building blocks, focusing on how attackers look for and exploit security gaps in your cloud.

## What Your Cloud Pentest Should Cover

Depending on your chosen cloud services' delivery model, the bounds of your responsibility for security may vary. In general terms, the cloud service providers' responsibility ends where your responsibility starts. The cloud provider is responsible for securing the hardware and the underlying software that enables its services. You are responsible for protecting everything you create in the cloud - your data, keys, assets, services, applications, and configurations. Consider an example of using Lambda functions to develop cloud-native applications in Amazon Web Services (AWS). While AWS addresses security for the compute and storage infrastructure and the Lambda service itself, it is your responsibility to ensure that access to your organization's code and resources is secure. So it's up to you to ensure that your developers are not storing credentials in the functions' code or environment variables that could be used to compromise sensitive data or laterally move in the network if intercepted by malicious actors.

To prepare for various breach scenarios, penetration tests should use different starting points:

* Black Box - the tester has no initial access within the cloud environment.
* Gray Box - the tester has the credentials of a selected user or role as initial input to show the potential impact (aka "blast radius") if an identity is compromised.

For organizations with hybrid cloud and on-premises networks, a complete and accurate understanding of risk exposure can only be achieved with the ability to test attack paths that cross between these environments. For example, an On-Prem machine is compromised, and the attacker runs an RCE to harvest credentials from the machine. Using browser password extraction, the attacker gains the credentials of a developer with privileges on an Azure VM. From there, the road to breach the cloud is paved, and this process is repeated on different machines until the attacker gets a hold of the highest privileges in the environment and can leverage any resource at will. Therefore, cloud penetration tests should cover scenarios where initial access on-premises could lead an attacker to compromise cloud resources and vice-versa.

Here are five key building blocks for cloud penetration testing:

### 1. Reconnaissance & Discovery

This first step entails mapping all the assets within your organization's cloud environment; workloads, storage, databases, and identities. The information gathered in this phase provides the scope of assets that can be used or targeted within a test and a baseline for initiating attack actions.

In traditional network pentesting, the test scope is typically defined by the IP addresses of the endpoints to be included in the test. Cloud resources, in contrast, are identified by unique identifiers, and access to them is enabled via APIs. Therefore, the typical approach for reconnaissance in cloud pentests is to gather the asset information at the beginning of a test by connec...