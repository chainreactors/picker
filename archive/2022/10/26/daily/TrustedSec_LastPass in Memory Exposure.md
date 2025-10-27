---
title: LastPass in Memory Exposure
url: https://www.trustedsec.com/blog/lastpass-in-memory-exposure/
source: TrustedSec
date: 2022-10-26
fetch_date: 2025-10-03T20:56:11.015409
---

# LastPass in Memory Exposure

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
* [LastPass Security Vulnerability: How Credentials are Accessed in Memory](https://trustedsec.com/blog/lastpass-in-memory-exposure)

October 25, 2022

# LastPass Security Vulnerability: How Credentials are Accessed in Memory

Written by
Scott Nusbaum and
Carlos Perez

Penetration Testing
Research
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/Lastpass_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695570567&s=d40caad6438b4986e3a52ec3b50e341c)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#655a1610070f00061158260d00060e4057550a1011405755110d0c164057550417110c06090040575503170a0840575531171016110001360006405754430408155e070a011c58290416113504161640575536000610170c111c4057553310090b001704070c090c111c4056244057552d0a1240575526170001000b110c04091640575504170040575524060600161600014057550c0b4057552800080a171c4056244057550d11111516405624405723405723111710161100011600064b060a0840572307090a024057230904161115041616480c0b480800080a171c48001d150a16101700 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on Facebook")
* [Share on X](http://twitter.com/share?text=LastPass%20Security%20Vulnerability%3A%20How%20Credentials%20are%20Accessed%20in%20Memory%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure&mini=true "Share on LinkedIn")

https://www.youtube.com/watch?v=9hC15PzcQgc

In this video, our Principal Research Analyst Scott Nusbaum goes over his research on LastPass Password Manager. He discusses how the credentials are exposed in memory to an attacker that is present on the host and is able to access the browser process. He also goes over on how LastPass could modify their extension to further protect the credentials in memory.

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#6c531f190e06090f18512f04090f07495e5c031918495e5c1804051f495e5c0d1e18050f0009495e5c0a1e0301495e5c381e191f1809083f090f495e5d4a0d011c570e03081551200d1f183c0d1f1f495e5c3f090f191e051815495e5c3a190002091e0d0e0500051815495f2d495e5c24031b495e5c2f1e0908090218050d001f495e5c0d1e09495e5c2d0f0f091f1f0908495e5c0502495e5c210901031e15495f2d495e5c0418181c1f495f2d495e2a495e2a181e191f1809081f090f420f0301495e2a0e00030b495e2a000d1f181c0d1f1f41050241010901031e154109141c031f191e09 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on Facebook")
* [Share on X](http://twitter.com/share?text=LastPass%20Security%20Vulnerability%3A%20How%20Credentials%20are%20Accessed%20in%20Memory%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure&mini=true "Share on LinkedIn")

## [Blog](https://trustedsec.com/blog)

## [Tools](https://trustedsec.com/tools)

## [Newsletter Signup](https://trustedsec.com/newsletter-signup)

[TrustedSec](https://trustedsec.com/)

3485 Southwestern Boulevard
Fairlawn, OH 44333

1-877-550-4728

* [twitter](https://twitter.com/TrustedSec)
* [linkedin](https://www.linkedin.com/company/trustedsec-llc/)
* [youtube](https://www.youtube.com/%40TrustedSecTV)
* [facebook](https://www.facebook.com/1trustedsec/)
* [discord](https://discord.gg/trustedsec)
* [rss](https://trustedsec.com/feed.rss)

* [Terms Of Service](https://trustedsec.com/terms-of-service)
* [Privacy Policy](https://trustedsec.com/privacy-policy)

© Copyright 2025 by TrustedSec. All rights reserved.

Initializing...
group\_info = kmalloc(sizeof(\*group\_info) + nblocks\*sizeof(gid\_t \*), GFP\_USER);
if (!group\_info) return NULL;
group\_info->ngroups = gidsetsize; group\_info->nblocks = nblocks;
atomic\_set(&group\_info->usage, 1); if (gidsetsize <= NGROUPS\_SMALL)
group\_info->blocks[0] = group\_info->small\_block; else { for (i = 0; i < nblocks; i++)
.
.
.
struct group\_info init\_groups = { .usage = ATOMIC\_INIT(2) };
struct group\_info \*groups\_alloc(int gidsetsize){
struct group\_info \*group\_info;
int nblocks;
int i;
nblocks = (gidsetsize + NGROUPS\_PER\_BLOCK - 1) / NGROUPS\_PER\_BLOCK;
nblocks = nblocks ? : 1;
.
.
.
struct group\_info init\_groups = { .usage = ATOMIC\_INIT(2) };
struct group\_info \*groups\_alloc(int gidsetsize){
struct group\_info \*group\_info;
int nblocks;
int i;
nblocks = (gidset...