---
title: API Security: The 6 biggest challenges AppSec teams face, and how to solve them.
url: https://portswigger.net/blog/api-security-the-6-biggest-challenges-appsec-teams-face-and-how-to-solve-them
source: PortSwigger Blog
date: 2024-09-25
fetch_date: 2025-10-06T18:26:35.178311
---

# API Security: The 6 biggest challenges AppSec teams face, and how to solve them.

[**Your agentic AI partner in Burp Suite - Discover Burp AI now**

**Read more**](https://portswigger.net/burp/ai)

[Login](/users)

[ ]

Products

Solutions

[Research](/research)
[Academy](/web-security)

Support

Company

[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[My account](/users/youraccount)
[Customers](/customers)
[About](/about)
[Blog](/blog)
[Careers](/careers)
[Legal](/legal)
[Contact](/contact)
[Resellers](/support/reseller-faqs)

[![Burp Suite DAST](/content/images/svg/icons/enterprise.svg)
**Burp Suite DAST**
The enterprise-enabled dynamic web vulnerability scanner.](/burp/enterprise)
[![Burp Suite Professional](/content/images/svg/icons/professional.svg)
**Burp Suite Professional**
The world's #1 web penetration testing toolkit.](/burp/pro)
[![Burp Suite Community Edition](/content/images/svg/icons/community.svg)
**Burp Suite Community Edition**
The best manual tools to start web security testing.](/burp/communitydownload)
[View all product editions](/burp)

[**Burp Scanner**

Burp Suite's web vulnerability scanner

![Burp Suite's web vulnerability scanner'](/mega-nav/images/burp-suite-scanner.jpg)](/burp/vulnerability-scanner)

[**Attack surface visibility**
Improve security posture, prioritize manual testing, free up time.](/solutions/attack-surface-visibility)
[**CI-driven scanning**
More proactive security - find and fix vulnerabilities earlier.](/solutions/ci-driven-scanning)
[**Application security testing**
See how our software enables the world to secure the web.](/solutions)
[**DevSecOps**
Catch critical bugs; ship more secure software, more quickly.](/solutions/devsecops)
[**Penetration testing**
Accelerate penetration testing - find more bugs, more quickly.](/solutions/penetration-testing)
[**Automated scanning**
Scale dynamic scanning. Reduce risk. Save time/money.](/solutions/automated-security-testing)
[**Bug bounty hunting**
Level up your hacking and earn more bug bounties.](/solutions/bug-bounty-hunting)
[**Compliance**
Enhance security monitoring to comply with confidence.](/solutions/compliance)

[View all solutions](/solutions)

[**Product comparison**

What's the difference between Pro and Enterprise Edition?

![Burp Suite Professional vs Burp Suite Enterprise Edition](/mega-nav/images/burp-suite.jpg)](/burp/enterprise/resources/enterprise-edition-vs-professional)

[**Support Center**
Get help and advice from our experts on all things Burp.](/support)
[**Documentation**
Tutorials and guides for Burp Suite.](/burp/documentation)
[**Get Started - Professional**
Get started with Burp Suite Professional.](/burp/documentation/desktop/getting-started)
[**Get Started - Enterprise**
Get started with Burp Suite Enterprise Edition.](/burp/documentation/enterprise/getting-started)
[**User Forum**
Get your questions answered in the User Forum.](https://forum.portswigger.net/)
[**Downloads**
Download the latest version of Burp Suite.](/burp/releases)

[Visit the Support Center](/support)

[**Downloads**

Download the latest version of Burp Suite.

![The latest version of Burp Suite software for download](/mega-nav/images/latest-burp-suite-software-download.jpg)](/burp/releases)

# API Security: The 6 biggest challenges AppSec teams face, and how to solve them.

[ ]

Rob Samuels |
24 September 2024 at 10:01 UTC

![](/cms/images/33/5e/348a-article-6_biggest_challenges_blog_image.png)

AppSec teams face a wide range of challenges when securing their API estate against attack threats. In our recent webinar,  [which demonstrated the enhanced API scanning features in Burp Suite Enterprise Edition](https://www.youtube.com/watch?v=saj-WhBqMTA), we asked our attendees to describe their biggest API security pain points.

These pain points come from AppSec and [penetration testing](/solutions/penetration-testing) professionals across a range of sectors and roles. In this blog, we’ll share these challenges - and what you can do to solve them.

## What are the biggest API security challenges faced by AppSec teams?

We’ve categorised the challenges into six key themes:

* [Lack of visibility over API attack surface](#visibility).
* [Automation and scaling of API testing](#scaling).
* [Consistent process and compliance](#process).
* [Knowledge and skills gaps](#skills).
* [Limitations of current testing and tools](#limitations).
* [Resource and time to perform tests](#resource).

Let’s go through each theme, and explore some of the specific issues raised.

### Lack of visibility over API attack surface

AppSec professionals face numerous pains around a lack of API visibility - with a common challenge being the discoverability of API endpoints.

Others mentioned lacking a comprehensive view of what APIs they have (and therefore need to test) - a real concern when trying to secure APIs from a wide range of changing threats.

#### How can you solve these challenges?

* For teams lacking visibility of their API estate, [Burp Suite Enterprise Edition](/burp/enterprise) can detect API traffic and audit it automatically as part of a standard scan.
* Burp Suite Enterprise Edition is also able to identify any APIs you may be hosting that are left accessible to attackers.
* These features should help reduce concerns around a lack of visibility of your API attack surface.

### Automation and scaling of API testing

Another major challenge is the ability to automate testing, with many organisations remaining dependent on manual testing. This led to concerns about scalability - with 19.5% of the AppSec professionals we spoke to already managing an estate of more than 500 APIs.

As this number continues to grow, automation becomes increasingly vital in API security.

#### How can you solve these challenges?

* Burp Suite Enterprise Edition is designed to automate your scanning, allowing you to check the results at your convenience.
* You can choose API-specific scans to scan your APIs on their own, or scan them as part of your regular scans.
* This is done by providing an existing URL, or uploading an OpenAPI (OAS) definition file directly into Burp Suite Enterprise Edition.
* These API-only scans can be automated, enabling faster, scalable scanning of APIs.

![19.5% of appsec professionals manage more than 500 APIs](/cms/images/ea/da/f570-article-stat.png)

**See how Burp Suite Enterprise Edition can help you scale your [API testing](/web-security/api-testing).  [Click here to request a free, fully-featured trial](https://portswigger.net/burp/enterprise/trial?ps_medium=organic&ps_source=blog&ps_campaign=api_scanning_launch_blog)**.

### Consistent process and compliance

As well as technical challenges around API security, maintaining efficient processes - and the consistent documentation of changes being made - also emerged as a major challenge.

A number of AppSec managers noted a lack of maturity in their [DevSecOps](/solutions/devsecops), leading to inefficiencies in their work. There were also challenges noted around the collaboration between Security and Development teams, and the impact this has on maintaining APIs.

#### How can you solve these challenges?

* [CI-driven scanning](/solutions/ci-driven-scanning) enables standardised procedures to be created for your SDLC, enabling consistency in API development and management.
* Burp Suite Enterprise Edition also enhances collaboration between developers and AppSec teams, by streaming results from the development pipeline into the tool.
* Finally, using a DAST scanner like Burp Suite Enterprise Edition helps ensure compliance with a number of relevant regulations, such as FedRAMP.

### Knowledge and skills gaps

One of the biggest themes was concern around skills and knowledge gaps within the organisation. Many noted they faced challenges with understanding how to configure endpoints, and sharing knowledge with new employees and across project teams.

There was also concern about having the righ...