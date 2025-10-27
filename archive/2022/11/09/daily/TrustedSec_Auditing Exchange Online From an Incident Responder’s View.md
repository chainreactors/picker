---
title: Auditing Exchange Online From an Incident Responder’s View
url: https://www.trustedsec.com/blog/auditing-exchange-online-from-an-incident-responders-view/
source: TrustedSec
date: 2022-11-09
fetch_date: 2025-10-03T22:07:54.665131
---

# Auditing Exchange Online From an Incident Responder’s View

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Auditing Exchange Online From an Incident Responder's View](https://trustedsec.com/blog/auditing-exchange-online-from-an-incident-responders-view)

November 08, 2022

# Auditing Exchange Online From an Incident Responder's View

Written by
Steven Erwin

Application Security Assessment
Cloud Assessment
Incident Response
Office 365 Security Assessment
Organizational Training
Password Audits

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AuditingExchangeOnline_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695569394&s=34fe3626b5cf3461cd25bcd21683b163)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e2dd91978088878196dfa18a878189c7d0d28d9796c7d0d2968a8b91c7d0d28390968b818e87c7d0d284908d8fc7d0d2b6909791968786b18781c7d0d3c4838f92d9808d869bdfa397868b968b8c85c7d0d2a79a818a838c8587c7d0d2ad8c8e8b8c87c7d0d2a4908d8fc7d0d2838cc7d0d2ab8c818b86878c96c7d0d2b08791928d8c868790c7d0d591c7d0d2b48b8795c7d1a3c7d0d28a96969291c7d1a3c7d0a4c7d0a496909791968786918781cc818d8fc7d0a4808e8d85c7d0a48397868b968b8c85cf879a818a838c8587cf8d8c8e8b8c87cf84908d8fcf838ccf8b8c818b86878c96cf908791928d8c86879091cf948b8795 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fauditing-exchange-online-from-an-incident-responders-view "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Auditing%20Exchange%20Online%20From%20an%20Incident%20Responder%27s%20View%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fauditing-exchange-online-from-an-incident-responders-view "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fauditing-exchange-online-from-an-incident-responders-view&mini=true "Share on LinkedIn")

Business Email Compromise (BEC) within the Microsoft 365 environment is becoming a more common attack vector. In case you’re unfamiliar with what exactly BEC entails, it’s when an attacker or unauthorized user gains access to a business email account via social engineering. Most commonly, an attacker compromises an account, intercepts email conversation(s), and uses this account to send illegitimate communication. This usually involves changing bank account or payment information from legitimate account to accounts managed by hackers.

While investigating many of of these attacks, TrustedSec has identified a series of baseline recommendations that will help harden your Microsoft 365 environment and ensure the right data is available to facilitate Incident Response activities in the event of a breach.

## Understand Licensing

Microsoft 365 licensing alone could be the subject of an entire training class. While we won’t deep-dive into the different tiers, it’s important to understand and highlight the major differences between the tiers to understand what licensing you may need for specific employees, employee groups, or high value targets. In Incident Response, data is key. It is important to understand that *only* E3+ or E5 licenses offer advanced auditing, which includes an audit log of mail items accessed. The absence of this data makes it impossible to discern what exactly the attackers accessed in your environment. Additionally, E3+ and E5 licensing both offer a longer retention policy than lower tiers, so it’s important to act quickly when an incident is believed to have happened so that an event doesn’t fall out of the retention window.

## Enable Audit Logs

All license tiers offer some form of audit logging, but depending on when your Microsoft 365 was setup, audit logging may not be enabled by default. It is highly recommended to validate that your environment has audit logging enabled. Enabling audit logging is not retrospective and will only start logging events going forward. In the event of a breach, this means you risk losing or not capturing valuable artifacts. Reactively enabling audit logs won’t assist with an ongoing incident, so it’s important to proactively enable this.

## Enforce Multi-Factor Authentication (MFA)

MFA is perhaps the best way to prevent BEC. MFA requires a user to enter the password plus an additional factor, whether that is an SMS code, a push notification, or an authentication application supplied code.

## Disable Legacy Applications

Legacy applications, specifically IMAP and POP3, are enabled by default within the Microsoft 365 environment. Unless there is a legitimate business need that warrants leaving legacy applications enabled, all should be disabled, especially because leaving them enabled could negate the account protections offered by MFA. If you...