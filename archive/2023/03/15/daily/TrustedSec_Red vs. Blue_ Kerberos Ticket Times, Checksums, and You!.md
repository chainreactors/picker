---
title: Red vs. Blue: Kerberos Ticket Times, Checksums, and You!
url: https://www.trustedsec.com/blog/red-vs-blue-kerberos-ticket-times-checksums-and-you/
source: TrustedSec
date: 2023-03-15
fetch_date: 2025-10-04T09:40:03.244550
---

# Red vs. Blue: Kerberos Ticket Times, Checksums, and You!

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
* [Red vs. Blue: Kerberos Ticket Times, Checksums, and You!](https://trustedsec.com/blog/red-vs-blue-kerberos-ticket-times-checksums-and-you)

March 14, 2023

# Red vs. Blue: Kerberos Ticket Times, Checksums, and You!

Written by
Andrew Schwartz

Incident Response
Incident Response & Forensics
Penetration Testing
Purple Team Adversarial Detection & Countermeasures
Threat Hunting

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/RedVsBlue_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695563749&s=8338f8bf1c27fbe0b9d1a01ec7667194)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#89b6fafcebe3eceafdb4cae1eceae2acbbb9e6fcfdacbbb9fde1e0faacbbb9e8fbfde0eae5ecacbbb9effbe6e4acbbb9ddfbfcfafdeceddaeceaacbbb8afe8e4f9b2ebe6edf0b4dbecedacbbb9fffaa7acbbb9cbe5fcecacbac8acbbb9c2ecfbebecfbe6faacbbb9dde0eae2ecfdacbbb9dde0e4ecfaacbbcaacbbb9cae1eceae2fafce4faacbbcaacbbb9e8e7edacbbb9d0e6fcacbbb8acbac8acbbb9e1fdfdf9faacbac8acbbcfacbbcffdfbfcfafdecedfaeceaa7eae6e4acbbcfebe5e6eeacbbcffbeceda4fffaa4ebe5fceca4e2ecfbebecfbe6faa4fde0eae2ecfda4fde0e4ecfaa4eae1eceae2fafce4faa4e8e7eda4f0e6fc "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fred-vs-blue-kerberos-ticket-times-checksums-and-you "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Red%20vs.%20Blue%3A%20Kerberos%20Ticket%20Times%2C%20Checksums%2C%20and%20You%21%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fred-vs-blue-kerberos-ticket-times-checksums-and-you "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fred-vs-blue-kerberos-ticket-times-checksums-and-you&mini=true "Share on LinkedIn")

*This blog post was co-authored with* [*Charlie Clark*](https://twitter.com/exploitph) *of* [*Semperis*](https://www.semperis.com/)*.*

## 1    Introduction

At SANS Pen Test HackFest 2022, Charlie Clark ([@exploitph](https://twitter.com/exploitph)) and I presented our talk '[I’ve Got a Golden Twinkle in My Eye](https://www.youtube.com/watch?v=ABd0dm8MbDo)' whereby we built and demonstrated two tools that assist with more accurate detection of forged tickets being used. Although we demonstrated the tools, we stressed the message of **focusing on the technique** of decrypting tickets **rather than the tools themselves**.

As we dove into our research of building IOAs, we often found ourselves examining ticket times and checksums and were repeatedly surprised by the lack of information from both Red and Blue perspectives for the ticket times and the checksums of Kerberos tickets. As such, this post will provide a more in-depth background to explain their importance and how/why understanding them can better serve offensive *and* defensive operators.

## 2    Ticket Times

### 2.1   Background of Ticket Times

In Kerberos, each ticket contains three timestamps. These times govern the period for which the ticket is valid. The three times are:

* Start Time[[1]](#_ftn1) – The time from which the ticket becomes usable
* End Time – Calculated from the Start time and the time the ticket becomes unusable
* Renew Time – Calculated from the Start time and the duration of renewal[[2]](#_ftn2)

Both Blue and Red teams should be especially cognizant of the 'End' and 'Renew' times. The understood limits for these times are stored in the Kerberos Policy within the domain GPO. While it's true that this policy determines the max values for these times, in many situations it is the account configuration and group membership that take a higher priority. It is important to know that the times discussed in the rest of this section define or calculate the **maximum** value for the relevant time and that a ticket can always be requested for a time before the maximum.

Within the Kerberos Policy there are three settings relevant to ticket times:

* Maximum lifetime for a service ticket – the number of minutes from the Start Time that a service ticket’s End Time can be
* Maximum lifetime for a user ticket – the number of hours from the Start Time that a TGT’s End Time can be
* Maximum lifetime for user ticket renewal – the number of days from the Start Time that a TGT’s Renew Time can be

The following is a screenshot of the default values for these settings:

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Figure_1.jpg)

(The above screenshot is courtesy of [Wendy Jiang of Microsoft](https://social.technet.microsoft.com/profile/wendy%20jiang?type=forum&referrer=https://social.technet.microsoft.com/forums/en-US/cde9406a-37b6-), [answering a question o...