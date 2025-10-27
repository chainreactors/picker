---
title: How Threat Actors Use OneNote to Deploy ASyncRAT
url: https://www.trustedsec.com/blog/how-threat-actors-use-onenote-to-deploy-asyncrat/
source: TrustedSec
date: 2023-02-02
fetch_date: 2025-10-04T05:31:00.604608
---

# How Threat Actors Use OneNote to Deploy ASyncRAT

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
* [How Threat Actors Use OneNote to Deploy ASyncRAT](https://trustedsec.com/blog/how-threat-actors-use-onenote-to-deploy-asyncrat)

February 01, 2023

# How Threat Actors Use OneNote to Deploy ASyncRAT

Written by
Carlos Perez

Incident Response
Incident Response & Forensics
Malware Analysis
Office 365 Security Assessment
Threat Hunting

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OneNoteAsyncRATMalwareVideo_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695566005&s=7f2988a0c55c76b0b2671892bd720167)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1e216d6b7c747b7d6a235d767b7d753b2c2e716b6a3b2c2e6a76776d3b2c2e7f6c6a777d727b3b2c2e786c71733b2c2e4a6c6b6d6a7b7a4d7b7d3b2c2f387f736e257c717a67235671693b2c2e4a766c7b7f6a3b2c2e5f7d6a716c6d3b2c2e4b6d7b3b2c2e51707b50716a7b3b2c2e6a713b2c2e5a7b6e7271673b2c2e5f4d67707d4c5f4a3b2d5f3b2c2e766a6a6e6d3b2d5f3b2c583b2c586a6c6b6d6a7b7a6d7b7d307d71733b2c587c7271793b2c58767169336a766c7b7f6a337f7d6a716c6d336b6d7b3371707b70716a7b336a71337a7b6e727167337f6d67707d6c7f6a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat "Share on Facebook")
* [Share on X](http://twitter.com/share?text=How%20Threat%20Actors%20Use%20OneNote%20to%20Deploy%20ASyncRAT%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat&mini=true "Share on LinkedIn")

https://youtu.be/vWDwsbNWa1E

See how Research Team Lead Carlos Perez dissects a sample of a OneNote document that was used to deploy ASyncRAT, an open-source remote admin tool, to enable phishing attacks. You’ll find out how these OneNote files are now being used by threat actors and where to find the location that ASyncRAT is being downloaded and executed.

The detection for this attack is included in the TrustedSec Sysmon Configuration and will allow you to monitor and block actions taken with this technique.
<https://github.com/trustedsec/defensive-scripts/blob/main/onenote_asyncrat_dropper.xml>

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#0f307c7a6d656a6c7b324c676a6c642a3d3f607a7b2a3d3f7b67667c2a3d3f6e7d7b666c636a2a3d3f697d60622a3d3f5b7d7a7c7b6a6b5c6a6c2a3d3e296e627f346d606b76324760782a3d3f5b677d6a6e7b2a3d3f4e6c7b607d7c2a3d3f5a7c6a2a3d3f40616a41607b6a2a3d3f7b602a3d3f4b6a7f6360762a3d3f4e5c76616c5d4e5b2a3c4e2a3d3f677b7b7f7c2a3c4e2a3d492a3d497b7d7a7c7b6a6b7c6a6c216c60622a3d496d6360682a3d49676078227b677d6a6e7b226e6c7b607d7c227a7c6a2260616a61607b6a227b60226b6a7f636076226e7c76616c7d6e7b "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat "Share on Facebook")
* [Share on X](http://twitter.com/share?text=How%20Threat%20Actors%20Use%20OneNote%20to%20Deploy%20ASyncRAT%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhow-threat-actors-use-onenote-to-deploy-asyncrat&mini=true "Share on LinkedIn")

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
nblocks = (g...