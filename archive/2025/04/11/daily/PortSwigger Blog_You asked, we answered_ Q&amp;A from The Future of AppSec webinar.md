---
title: You asked, we answered: Q&amp;A from The Future of AppSec webinar
url: https://portswigger.net/blog/q-a-from-the-future-of-appsec-webinar
source: PortSwigger Blog
date: 2025-04-11
fetch_date: 2025-10-06T22:04:20.392733
---

# You asked, we answered: Q&amp;A from The Future of AppSec webinar

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

# You asked, we answered: Q&A from The Future of AppSec webinar

[ ]

Tom Ryder |
10 April 2025 at 14:33 UTC

When we wrapped up our biggest-ever webinar, [The Future of AppSec: PortSwigger’s Vision](https://portswigger.net/future-of-appsec-webinar), the conversation was far from over.

With thousands of security professionals tuning in live, the questions came thick and fast. You asked about everything from on-prem deployments of [Burp Suite DAST](https://portswigger.net/burp/documentation/enterprise), to AI models, product roadmaps, and whether AppSec is becoming “a dumpster fire”.

We reviewed hundreds of questions, identified key themes, and selected specific ones to answer that reflect the majority of what people asked.

We’ll be answering some of the standout questions you raised during the session, including topics that we didn’t get time to cover during the webinar. Whether you’re curious about how [Burp AI](https://portswigger.net/burp/ai) works behind the scenes, [Burp Suite DAST](/burp/dast) support, or just wondering what’s next for [Burp Suite](https://portswigger.net/burp), this Q&A is for you.

Thank you again for shaping the future of AppSec with us. Let’s get into the Q&A:

![](/cms/images/10/5d/3492-article-burp_suite_dast_gif.gif)

## Burp Suite DAST

### Q: When is Burp Suite DAST expected to be available for enterprise usage? Interested to get a deep dive demo.

A: You’re in luck, it already is! [Burp Suite Enterprise Edition](https://portswigger.net/burp/documentation/enterprise) is now called Burp Suite DAST. We’ve renamed it to provide greater clarity around the product’s purpose. Burp Suite DAST continues to be trusted by leading global organizations for scalable, automated security testing and rest assured, we’ll keep innovating and adding new capabilities to make it even better.

Keep an eye out for a follow-up webinar with a live demo illustrating the value of Burp Suite DAST.

### Q: If you need to follow a specific workflow in the API, could Burp Suite DAST handle it?

A: Yes. Burp Suite DAST can scan APIs defined via OpenAPI, SOAP, [Postman collections](https://portswigger.net/burp/documentation/enterprise/user-guide/scanning-apis), and more. If your API requires stateful workflows, you can use recorded login sequences or authenticated sessions.

### Q: How does this DAST tool compare to traditional DAST solutions and API security tools?

A: Burp Suite DAST delivers deep, accurate scanning of both web apps and APIs. We currently support REST and SOAP APIs, either in isolation or as part of a broader web app scan. You just need to provide a suitable [OpenAPI (Swagger) spec](https://portswigger.net/blog/api-security-the-6-biggest-challenges-appsec-teams-face-and-how-to-solve-them), WSDL, or Postman Collection.

Unlike generic tools that spread themselves thin across many areas, Burp Suite DAST focuses on delivering deep, high-quality results where it matters most. If your team is looking for a DAST solution that can also handle API security with depth and precision, not just tick a box, Burp Suite DAST is built to meet that need.

### Q: Do we have 24/7 support for Burp DAST? Or does the support team work in a specific time zone?

A: Today, our support is based in the UK during business hours, but we’re actively expanding to the USA to provide more responsive, around-the-clock coverage.

![](/cms/images/37/63/c462-article-burp-ai-q1.png)

## Burp AI

### Q: Is Burp AI a part of Burp Suite Professional or do you need to pay for it separately?

A: [Burp AI](https://portswigger.net/burp/ai) is the collective term for AI-powered features included in [Burp Suite Professional](/burp/pro), along with the trusted platform that securely manages all communication with the AI services. You don't need to pay for an extra subscription, all of the features are included in Burp Suite Professional. However, using Burp AI features relies on a built-in credits system. All users will receive 10,000 free AI credits and further credits can be purchased from within my account.

### Q: Will user data and methodology be used to train the AI model or is there privacy?

A: No, data and methodologies will not be used to train the AI models. We understand the concern and take data privacy extremely seriously. We have contractual zero-retention agreements in place with all of our AI providers. This ensures that none of your data is stored or used for model training purposes by the AI service.

### Q: Is the AI going to be able to run airgapped and offline?

A: Not at this time. The current AI features in Burp Suite Professional rely on cloud-based large language models accessed via PortSwigger’s secure AI gateway. These models require significant co...