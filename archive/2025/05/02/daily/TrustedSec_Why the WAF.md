---
title: Why the WAF
url: https://trustedsec.com/blog/why-the-waf
source: TrustedSec
date: 2025-05-02
fetch_date: 2025-10-06T22:31:13.765631
---

# Why the WAF

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
* [Why the WAF](https://trustedsec.com/blog/why-the-waf)

May 01, 2025

# Why the WAF

Written by
Brian Berg

Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WhyTheWAF_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1745515466&s=142d05e10656546bdaf71f8b8c072e4c)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#d7e8a4a2b5bdb2b4a3ea94bfb2b4bcf2e5e7b8a2a3f2e5e7a3bfbea4f2e5e7b6a5a3beb4bbb2f2e5e7b1a5b8baf2e5e783a5a2a4a3b2b384b2b4f2e5e6f1b6baa7ecb5b8b3aeea80bfaef2e5e7a3bfb2f2e5e7809691f2e496f2e5e7bfa3a3a7a4f2e496f2e591f2e591a3a5a2a4a3b2b3a4b2b4f9b4b8baf2e591b5bbb8b0f2e591a0bfaefaa3bfb2faa0b6b1 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhy-the-waf "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Why%20the%20WAF%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhy-the-waf "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwhy-the-waf&mini=true "Share on LinkedIn")

In my experience, most organizations are prepared to discuss the scope of penetration tests when preparing for an External or Internal Penetration Test, but when it comes time to discuss specifics about a web application assessment, there’s often some confusion. One particular area of confusion is whether or not a web application firewall (WAF), or intrusion prevention system (IPS) is in place and if it would be possible to test without it in place for a specific IP address.

When asked if a WAF is in place, a fair number of clients will say they don’t know. So, let’s clear up that up first. A WAF inspects the content of web traffic for potentially malicious requests and drops them before they get to a web server. This is different from a traditional network firewall that primarily works on different levels of the protocol stack and can’t inspect the raw http contents of a packet outside of the packet header. In short, a WAF will see when someone attempts to issue a login request with the username of *' or '1' = '1'--* and drop the request, but a firewall will let the request through.

Now that that’s cleared up, some may think testing without the WAF is cheating, but the reality is, security assessments are only allotted so much time. Performing a portion of testing with some defenses disabled helps get better coverage of the application and helps identify if some of the application’s natural defenses, such as input and output encoding, are effectively utilized. In the event that a flaw such as XSS or SQLi is discovered, it’s fairly trivial for the person performing the assessment to change to an IP address that has not been allowlisted to see if the WAF properly defends against the attack or not. Unless the goal of the assessment is to gain an overall picture of the deployment environment, the primary goal of an application assessment should be to test the application and not just the security control in front of it. Another way to think of it is that allowlisting an IP address through a WAF is the most economical strategy for an assessment because the application’s inherent defenses are tested in an efficient manner, then the security appliance is tested to see how effective it is at blocking attacks.

Much like any other technology, WAFs are far from perfect, and bypasses are discovered fairly frequently. After a quick GitHub search, hundreds of resources, including automated tooling to attempt WAF bypasses, are presented. One particular technique that I have been getting a lot of mileage out of is essentially a buffer overflow that fills up the WAF’s ability to check the request. The WAF only sees junk data at the start of a request and then passes the request to the web server. The web server ignores the junk data and processes the malicious payload. This should further drive home the fact that testing without a WAF in place is a worthwhile endeavor since the WAF may have some security gaps of its own and applying a bypass to each request can cost a lot of valuable time during an assessment.

Even though it may be possible to bypass a WAF, I still feel like a WAF is a worthwhile addition to the security posture of an application environment. Note that I said “addition” because it should be part of a defense-in-depth approach to application security. It should not be used as a patch to try and cover up underlying issues with the application’s code. Technology is forever changing, and new issues are constantly being uncovered. Because of this undeniable...