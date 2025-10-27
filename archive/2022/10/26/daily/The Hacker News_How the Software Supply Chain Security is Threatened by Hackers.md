---
title: How the Software Supply Chain Security is Threatened by Hackers
url: https://thehackernews.com/2022/10/how-software-supply-chain-security-is.html
source: The Hacker News
date: 2022-10-26
fetch_date: 2025-10-03T20:56:24.504166
---

# How the Software Supply Chain Security is Threatened by Hackers

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

# [How the Software Supply Chain Security is Threatened by Hackers](https://thehackernews.com/2022/10/how-software-supply-chain-security-is.html)

**Oct 25, 2022**The Hacker News

[![Software Supply Chain Security](data:image/png;base64... "Software Supply Chain Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFX6PMHRCffiaj2cKQUB_2gZG9a6SMly2w522SbSSkW37TDdDfLSi3zLVi-UMYJapGfvXq3GEJ6-05zeEHsgeGGfMX1yT74oyP_D_noyx7wnvhUIGmLMWBM4DCqS0zGE5VB1RAtonHDIob8_5MgDgHNm-93GLMLYot_2h9bTg02TIn2QOHV90yemL2/s790-rw-e365/software-supply-chain.jpg)

## Introduction

In many ways, the software supply chain is similar to that of manufactured goods, which we all know has been largely impacted by a global pandemic and shortages of raw materials.

However, in the IT world, it is not shortages or pandemics that have been the main obstacles to overcome in recent years, but rather attacks aimed at using them to harm hundreds or even thousands of victims simultaneously. If you've heard of a cyber attack between 2020 and today, it's likely that the software supply chain played a role.

When we talk about an attack on the software supply chain, we are actually referring to two successive attacks: one that targets a supplier, and one that targets one or more downstream users in the chain, using the first as a vehicle.

In this article, we will dive into the mechanisms and risks of the software supply chain by looking at a typical vulnerability of the modern development cycle: the presence of personal identifying information, or "secrets", in the digital assets of companies. We will also see how companies are adapting to this new situation by taking advantage of continuous improvement cycles.

## The supply chain, at the heart of the IT development cycle

####

#### What is the supply chain?

Today, it is extremely rare to see companies producing software 100% in-house. Whether it's open source libraries, developer tools, on-premise or cloud-based deployment and delivery systems, or *software-as-a-service* (SaaS) services, these building blocks have become essential in the modern software factory.

Each of these "bricks" is itself the product of a long supply chain, making the software supply chain a concept that encompasses every facet of IT: from hardware, to source code written by developers, to third-party tools and platforms, but also data storage and all the infrastructures put in place to develop, test and distribute the software.

The supply chain is a layered structure that allows companies to implement highly flexible software factories, which are the engine of their digital transformation.

The mass reuse of open-source components and libraries has dramatically accelerated the development cycle and the ability to deliver functionality according to customer expectations. But the counterpart to this impressive gain has been a loss of control over the origin of the code that goes into the companies' products. This chain of dependencies exposes organizations and their customers to vulnerabilities introduced by changes outside their direct control.

This is obviously a major cybersecurity issue, and one that is only increasing as the supply chain becomes more and more complex year over year. So it's no surprise that large-scale cyber attacks have been able to exploit it to their advantage recently.

#### The risk of the weak link

For hackers, the software supply chain of companies represents an interesting target for several reasons. First of all, because of its complexity and the number of interacting "bricks" at the heart of the software factory, its attack surface is very large. Secondly, application security, which was historically focused on securing the application in production (i.e. exposed to the public), often lacks the visibility and tools to effectively secure internal *build* servers and other parts of the CI/CD pipeline.

In addition, it's important to understand that the development chain today is continuously evolving, adding new tools constantly. This is one of the defining characteristics of the DevOps movement, which has blurred the line between development and operations enormously, leaving developers free to deliver features for their customers as quickly as possible.

These choices though are often implemented without oversight and can be very different from one team to another, even within the same department. The accumulation of slightly different tools, libraries and platforms makes it very difficult to create accurate inventories which are the cornerstone of effective security management.

Finally, by exploiting the supply chain, hackers find ways to maximize the impact, and therefore the yield, of an attack. To understand this, we must consider that the products and services of a software services company's supply chain are the building blocks of other supply chains. An attacker who has successfully infiltrated one link in a chain can compromise the entire user base, which can have disastrous consequences.

#### The rise of supply chain attacks

In the SolarWinds attack, between March and June 2020, approximately 18,000 Orion platform customers, including a number of U.S. government agencies, downloaded updates with malicious code injected into them. This code granted hackers unauthorized backdoor access to systems and private networks of nearly 100 entities. SolarWinds did not discover the breach until December 2020. An international scandal ensued.

A few weeks later, in January 2021, an attacker obtained credentials used in Docker image creation involving Codecov software, due to an error in the build process. These credentials allowed the attacker to hijack Codecov, a software for testing developers' code coverage, and turn it into a real Trojan horse: since the software is used in continuous integration (CI) environments, it has access to the secret credentials of the build processes (we'll come back to this).

The attacker was thus able to siphon off hundreds of credentials from Codecov users, ...