---
title: EKUwu: Not just another AD CS ESC
url: https://trustedsec.com/blog/ekuwu-not-just-another-ad-cs-esc
source: TrustedSec
date: 2024-10-09
fetch_date: 2025-10-06T18:54:38.202031
---

# EKUwu: Not just another AD CS ESC

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
* [EKUwu: Not just another AD CS ESC](https://trustedsec.com/blog/ekuwu-not-just-another-ad-cs-esc)

November 13, 2024

# EKUwu: Not just another AD CS ESC

Written by
Justin Bollinger

Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ESC15_WebHero_2.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1731516130&s=7b0b00ccbc4197007bd51fd00ae9f5d6)

Table of contents

* [Story Time](#Story)
* [AD CS Template Version History Lesson](#Template)
* [EKU and Application Policies](#Policies)
* [What Can be Done?](#What)
* [Special Thanks](#Thanks)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e6d99593848c838592dba58e83858dc3d4d6899392c3d4d6928e8f95c3d4d68794928f858a83c3d4d68094898bc3d4d6b2949395928382b58385c3d4d7c0878b96dd8489829fdba3adb39193c3d5a7c3d4d6a88992c3d4d68c939592c3d4d6878889928e8394c3d4d6a7a2c3d4d6a5b5c3d4d6a3b5a5c3d5a7c3d4d68e92929695c3d5a7c3d4a0c3d4a092949395928382958385c885898bc3d4a0848a8981c3d4a0838d939193cb888992cb8c939592cb878889928e8394cb8782cb8595cb839585 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fekuwu-not-just-another-ad-cs-esc "Share on Facebook")
* [Share on X](http://twitter.com/share?text=EKUwu%3A%20Not%20just%20another%20AD%20CS%20ESC%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fekuwu-not-just-another-ad-cs-esc "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fekuwu-not-just-another-ad-cs-esc&mini=true "Share on LinkedIn")

**Update November 12, 2024** - This vulnerability has been patched. <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-49019>

*This post was originally published on October 8, 2024.*

**TL;DR** - Using built-in default version 1 certificate templates, an attacker can craft a CSR to include application policies that are preferred over the configured Extended Key Usage attributes specified in the template. The only requirement is enrollment rights, and it can be used to generate client authentication, certificate request agent, and codesigning certificates using the ***WebServer*** template.

In 2021, researchers Will Schroeder and Lee Christensen from SpecterOps released a [whitepaper](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) detailing eight (8) escalation techniques against Active Directory Certificate Services (AD CS), which they dubbed ESC1 - ESC8. If you have not read that whitepaper, please go do that first; it will make the rest of this easier to follow. Their original research led to additional research in AD CS and, over the next couple years, additional escalation techniques were identified (ESC9 - ESC14).

## Story Time

It's 4:30AM and the testing window ends at 6:00AM. We've got a foothold, but only administrative access to one (1) system. I remote into the server using RDP and start poking around in the MMC. Since I have administrative access to the system, I can also see the system certificates. I decided to check to see if there were any templates that maybe I missed with the automated scanning for ESC1.

Then I noticed something. This kind of looks like ESC1 because it allows you to supply the subject. I'm pretty sure that the ***WebServer*** certificate template wouldn’t have the Client Authentication EKU configured, which is a requirement for ESC1, but I decided to click on ***More information is required to enroll this certificate. Click here to configure settings***.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/EKUwu-Not-just-another-AD-CS-ESC/Figure-1-MMC.exe-Certificate-Request.png?w=320&q=90&auto=format&fit=max&dm=1728407254&s=2b2ccc5e6408e345d51872c8fd701a02)

Figure 1 - MMC.exe Certificate Request

I filled out the subject and UPN fields to match the **Administrator** account just like the ESC1 attack.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/EKUwu-Not-just-another-AD-CS-ESC/Figure-2-Manual-ESC1-Attack.png?w=320&q=90&auto=format&fit=max&dm=1728407255&s=b929464c2f683f7241c45aa5ee1dfd39)

Figure 2 - Manual ESC1 Attack

I went to double check that the Key Usage was configured as ***Server Authentication,*** like it should have been set by the template, and I realized that the GUI wasn’t greyed out. I thought that was weird, and so I tried to remove the ***Server Authentication,*** added ***Client Authentication*** to the EKUs, and requested the certificate.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/EKUwu-Not-just-another-AD-CS-ESC...