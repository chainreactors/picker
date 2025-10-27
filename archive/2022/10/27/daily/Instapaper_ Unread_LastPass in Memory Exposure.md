---
title: LastPass in Memory Exposure
url: https://www.trustedsec.com/blog/lastpass-in-memory-exposure/
source: Instapaper: Unread
date: 2022-10-27
fetch_date: 2025-10-03T21:03:49.157521
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
* [Share via Email](/cdn-cgi/l/email-protection#d4eba7a1b6beb1b7a0e997bcb1b7bff1e6e4bba1a0f1e6e4a0bcbda7f1e6e4b5a6a0bdb7b8b1f1e6e4b2a6bbb9f1e6e480a6a1a7a0b1b087b1b7f1e6e5f2b5b9a4efb6bbb0ade998b5a7a084b5a7a7f1e6e487b1b7a1a6bda0adf1e6e482a1b8bab1a6b5b6bdb8bda0adf1e795f1e6e49cbba3f1e6e497a6b1b0b1baa0bdb5b8a7f1e6e4b5a6b1f1e6e495b7b7b1a7a7b1b0f1e6e4bdbaf1e6e499b1b9bba6adf1e795f1e6e4bca0a0a4a7f1e795f1e692f1e692a0a6a1a7a0b1b0a7b1b7fab7bbb9f1e692b6b8bbb3f1e692b8b5a7a0a4b5a7a7f9bdbaf9b9b1b9bba6adf9b1aca4bba7a1a6b1 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on Facebook")
* [Share on X](http://twitter.com/share?text=LastPass%20Security%20Vulnerability%3A%20How%20Credentials%20are%20Accessed%20in%20Memory%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flastpass-in-memory-exposure&mini=true "Share on LinkedIn")

https://www.youtube.com/watch?v=9hC15PzcQgc

In this video, our Principal Research Analyst Scott Nusbaum goes over his research on LastPass Password Manager. He discusses how the credentials are exposed in memory to an attacker that is present on the host and is able to access the browser process. He also goes over on how LastPass could modify their extension to further protect the credentials in memory.

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#8eb1fdfbece4ebedfab3cde6ebede5abbcbee1fbfaabbcbefae6e7fdabbcbeeffcfae7ede2ebabbcbee8fce1e3abbcbedafcfbfdfaebeaddebedabbcbfa8efe3feb5ece1eaf7b3c2effdfadeeffdfdabbcbeddebedfbfce7faf7abbcbed8fbe2e0ebfcefece7e2e7faf7abbdcfabbcbec6e1f9abbcbecdfcebeaebe0fae7efe2fdabbcbeeffcebabbcbecfededebfdfdebeaabbcbee7e0abbcbec3ebe3e1fcf7abbdcfabbcbee6fafafefdabbdcfabbcc8abbcc8fafcfbfdfaebeafdebeda0ede1e3abbcc8ece2e1e9abbcc8e2effdfafeeffdfda3e7e0a3e3ebe3e1fcf7a3ebf6fee1fdfbfceb "Share via Email")
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