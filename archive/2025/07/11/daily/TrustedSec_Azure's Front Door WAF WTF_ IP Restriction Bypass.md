---
title: Azure's Front Door WAF WTF: IP Restriction Bypass
url: https://trustedsec.com/blog/azures-front-door-waf-wtf-ip-restriction-bypass
source: TrustedSec
date: 2025-07-11
fetch_date: 2025-10-06T23:28:46.740368
---

# Azure's Front Door WAF WTF: IP Restriction Bypass

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
* [Azure's Front Door WAF WTF: IP Restriction Bypass](https://trustedsec.com/blog/azures-front-door-waf-wtf-ip-restriction-bypass)

July 10, 2025

# Azure's Front Door WAF WTF: IP Restriction Bypass

Written by
@ nyxgeek

Cloud Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AzureFrontDoorWAFWTF_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1751940096&s=d3dbf822740500a00b8f726c2e8e130f)

Table of contents

* [Background](#Background)
* [You Know What Happens When You Assume…](#Assume)
* [It's a Feature, not a Bug](#Feature)
* [Testing Setup](#Setup)
* [Verification of Blocking Rule](#Rule)
* [Identifying Front Door WAF](#Identifying)
* [Bypassing IP Restriction](#Bypassing)
* [BONUS POWERUP!](#POWERUP)
* [Detection](#Detection)
* [Remediation](#Remediation)
* [Conclusion](#Conclusion)
* [Reference](#Reference)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e5da9690878f808691d8a68d80868ec0d7d58a9091c0d7d5918d8c96c0d7d58497918c868980c0d7d583978a88c0d7d5b1979096918081b68086c0d7d4c3848895de878a819cd8a49f909780c0d7d296c0d7d5a3978a8b91c0d7d5a18a8a97c0d7d5b2a4a3c0d7d5b2b1a3c0d6a4c0d7d5acb5c0d7d5b7809691978c86918c8a8bc0d7d5a79c95849696c0d6a4c0d7d58d91919596c0d6a4c0d7a3c0d7a391979096918081968086cb868a88c0d7a387898a82c0d7a3849f90978096c883978a8b91c8818a8a97c8928483c8929183c88c95c897809691978c86918c8a8bc8879c95849696 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazures-front-door-waf-wtf-ip-restriction-bypass "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Azure%27s%20Front%20Door%20WAF%20WTF%3A%20IP%20Restriction%20Bypass%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazures-front-door-waf-wtf-ip-restriction-bypass "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fazures-front-door-waf-wtf-ip-restriction-bypass&mini=true "Share on LinkedIn")

The Azure Front Door Web Application Firewall (WAF) has an "IP restriction" option that can be bypassed with the inclusion of an HTTP header.

What's worse? This is actually expected behavior.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AzureFrontDoorWAFWTF_nyxgeek/Fig01_nyxgeek_AzureWAF.jpg?w=320&q=90&auto=format&fit=max&dm=1751983548&s=6dfb5194f7ef3c08fa0b55204c26f3c5)

Figure 1 - WHY???

## Background

There are two (2) WAFs available within Azure—Front Door WAF and the Application Gateway WAF. The Front Door WAF is Azure's Global WAF and the Application Gateway WAF is the Regional WAF.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AzureFrontDoorWAFWTF_nyxgeek/Fig02_nyxgeek_AzureWAF.png?w=320&q=90&auto=format&fit=max&dm=1752085849&s=1215a68b0b93b7cac7dd33a05d3de382)

Figure 2 - Create a WAF Policy in Azure

This particular IP restriction bypass only works in the Front Door WAF. Within the Front Door WAF, if you choose to restrict access by IP address, the default choice is a variable called ***RemoteAddr***.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AzureFrontDoorWAFWTF_nyxgeek/Fig03_nyxgeek_AzureWAF.png?w=320&q=90&auto=format&fit=max&dm=1751983551&s=c21f87e36b3c4d3b346ad5a4525d522a)

Figure 3 - Front Door WAF Policy

If the 'Match Variable' drop-down is selected, we can see our options: ***RemoteAddr*** or ***SocketAddr***.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AzureFrontDoorWAFWTF_nyxgeek/Fig04_nyxgeek_AzureWAF.png?w=320&q=90&auto=format&fit=max&dm=1751983552&s=7b05a3989e1b0a044f8187ee4d151d17)

Figure 4 - Choose Wisely

We have two (2) ambiguously named variables to match against. So, what's the difference?

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AzureFrontDoorWAFWTF_nyxgeek/Fig05_nyxgeek_AzureWAF.png?w=320&q=90&auto=format&fit=max&dm=1751983553&s=74448eb1d63316fa0c528b03c3de2b42)

Figure 5 - What Could go Wrong?

Well, within the [Front Door WAF documentation](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/waf-front-door-configure-ip-restriction), Microsoft lays it out plainly: the ***RemoteAddr*** variable matches the original client's IP address, and it does this by respecting the ***X-Forwarded-For*** HTTP header, if set. The ***SocketAddr*** variable, on the other hand, is the IP address that the WAF sees, i.e., the *real* IP address. This is what any sane person would expect the filtering to take place on.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/A...