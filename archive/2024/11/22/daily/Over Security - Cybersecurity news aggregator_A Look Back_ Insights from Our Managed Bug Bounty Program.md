---
title: A Look Back: Insights from Our Managed Bug Bounty Program
url: https://blog.compass-security.com/2024/11/a-look-back-insights-from-our-managed-bug-bounty-program/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-22
fetch_date: 2025-10-06T19:18:45.355587
---

# A Look Back: Insights from Our Managed Bug Bounty Program

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [A Look Back: Insights from Our Managed Bug Bounty Program](https://blog.compass-security.com/2024/11/a-look-back-insights-from-our-managed-bug-bounty-program/ "A Look Back: Insights from Our Managed Bug Bounty Program")

[November 21, 2024](https://blog.compass-security.com/2024/11/a-look-back-insights-from-our-managed-bug-bounty-program/ "A Look Back: Insights from Our Managed Bug Bounty Program")
 /
[Fabio Poloni](https://blog.compass-security.com/author/fpoloni/ "Posts by Fabio Poloni")
 /
[0 Comments](https://blog.compass-security.com/2024/11/a-look-back-insights-from-our-managed-bug-bounty-program/#respond)

**Introduction**

At Compass Security, we are proud to offer a fully managed bug bounty program tailored to the needs of both SMEs and larger enterprises. From scoping to payout, we manage every aspect of the process to ensure a seamless experience for our customers and valued hunters. In this blog post, we’ll take a look at our journey since the launch of our service in October 2023, highlighting key milestones, metrics and learnings gathered along the way.

We want to cut through the hype around bug bounty programs by publishing the real numbers, challenges and benefits in a transparent way.

**From October 2023 onwards**

Since October 2023, we have brought five customers on board, with more in the pipeline. Moreover, we are also eating our own dog food and running two programs, focusing on Compass Security’s infrastructure and the cyber training range developed by our sister company Hacking-Lab.

[![A screenshot of the website of Compass Security showing a list of bug bounty programs.](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_programs-1024x822.png)](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_programs.png)

Specifically, we are very proud to be running the program for the European Organization for Nuclear Research (CERN), based in Meyrin (Geneva), which is probably the largest bug bounty program in Switzerland, next to Swisscom’s immense playground.

**Let’s Talk Bounties**

In total, hunters from all over the world have discovered over 30 valid bugs so far, resulting in a total payout of roughly CHF 15’000 and averaging at about CHF 500 per bug. Thirteen hunters have received payouts so far. The highest bounty paid was CHF 2’050.

[![A bar plot of payouts in CHF per Hunter. The top hunter earned 5000CHF.](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_payouts-by-hunter.png)](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_payouts-by-hunter.png)

Figure : Payouts in CHF per Hunter

So if you are considering launching a program you will find that it is not the masses that will jump on it and go after your scope but a few very dedicated hunters who will try to skim the cream . The set of criteria that hunters use to decide which program to jump on ranges from the novelty of the program, to scope, to maximum bounty payouts. We have learnt from discussions that European and Swiss hunters in particular will rarely invest their time in programs where the maximum bounty is below CHF 10’000. And we can confirm that most of the bounties we have paid have gone outside Europe. Mainly Asia and North America.

**Key Metrics and Performance**

Our managed programs received just over 200 reports in total. Some of the most interesting findings were subdomain takeover, account takeover, and exposure of sensitive resources. While most of the vulnerabilities were of low or medium severity, we also received a few high severity issues. Our triage process still varies in speed but is generally very fast. Payouts have also been very fast, but are occasionally affected by slow bank procedures. We have already built up a small community of hunters who submit new reports and keep us going.

With so many bugs, there are also many reports that do not qualify for a bounty.

Ineligible bugs are usually some form of report that either is no issue, has no real impact, lacks relevant proof or is defined in the program’s Rules of Engagement (RoE) as not being eligible for payment.

[![A pie chart showing bugs that do not qualify for a bounty: 122 ineligible, 35 duplicate and 21 out of scope bugs](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_rejection_reasons.png)](https://blog.compass-security.com/wp-content/uploads/2024/11/compass_security_bug_bounty_rejection_reasons.png)

Duplicates, also known as collisions with Pwn2Own events, are bugs that have already been reported by another hunter and are therefore no longer eligible for a bounty. Understandably, this is one of the pain points and fears that come with bug hunting and puts pressure on hunters. Our general triage policy is to mark a report as duplicate if the same issue has already been reported and accepted for the same asset.

Most of the duplicates come from hunters smashing automated scanners at program scopes. Although we generally forbid scanning by program policy, some hunters still use it as an efficient means to perhaps grab some low hanging fruit or get an overview of the targets.

Beyond that, we sometimes get reports that are out of scope and address issues in assets that are not listed among our managed bug bounty programs, due to hunters not following the asset lists, mistakenly testing third-party services or excluded IP ranges, and for very human reasons such as typos in domain names.

**Love From the Community**

One of our hunters recently shared their positive experience with our bug bounty platform, praising our fast triage process and transparent payout system. His feedback underscores the importance of effective communication in building a respectful relationship that encourages continued collaboration.

> I wanted to take a moment to express my appreciation for your exceptional bug bounty platform. I really like your platform and the immediate response of the triage team and the payout process is so fast and transparent.
>
> So far i have been hunting on so many platforms. I find your triage to be the best out of them all with very well explained responses. I have learned a lot from you guys too while hunting. Your detailed explanations on my reports really helped me understand so many vulnerabilities that i find hard to understand. So, it is a great experience working with you guyz.
>
> Looking forward to contribute more on your platform.
> – GS

This is where we are heading. Trust, transparency, kindness and respect for those who contribute to the success of the programs we manage.

**Cost and Earnings**

For most of our programs we currently take a flat fee for every eligible bug report we handle, hand over to the customer, provide guidance on fixing and track status. We use this flat rate to cover triage efforts and continuous development of our very basic reporting platform.

Yes, we do not charge for false positives, duplicates or out of scope issues. It is our promise to keep these away from our customers.

**Bug Bounty Buyers Guide**

If you are considering starting a bug bounty program, we suggest you stick to the concept. Money for bugs. So consider free subscriptions that take a flat fee per relevant report. \*shameless plug\*

Unless you have super specific needs for huge maxi...