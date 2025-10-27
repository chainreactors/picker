---
title: Shells in Plain Sight – Storing Payloads in the Cloud
url: https://www.trustedsec.com/blog/shells-in-plain-sight-storing-payloads-in-the-cloud/
source: TrustedSec
date: 2023-03-17
fetch_date: 2025-10-04T09:52:06.052164
---

# Shells in Plain Sight – Storing Payloads in the Cloud

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
* [Shells in Plain Sight - Storing Payloads in the Cloud](https://trustedsec.com/blog/shells-in-plain-sight-storing-payloads-in-the-cloud)

March 16, 2023

# Shells in Plain Sight - Storing Payloads in the Cloud

Written by
TrustedSec

Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HidingShellsInPlainSight_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695563516&s=71e38e9d993f584c4e1aaec4602d62f4)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#68571b1d0a020d0b1c552b000d0b034d5a58071d1c4d5a581c00011b4d5a58091a1c010b040d4d5a580e1a07054d5a583c1a1d1b1c0d0c3b0d0b4d5a594e090518530a070c11553b000d04041b4d5a5801064d5a5838040901064d5a583b010f001c4d5a58454d5a583b1c071a01060f4d5a583809110407090c1b4d5a5801064d5a581c000d4d5a582b04071d0c4d5b294d5a58001c1c181b4d5b294d5a2e4d5a2e1c1a1d1b1c0d0c1b0d0b460b07054d5a2e0a04070f4d5a2e1b000d04041b450106451804090106451b010f001c451b1c071a01060f451809110407090c1b450106451c000d450b04071d0c "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshells-in-plain-sight-storing-payloads-in-the-cloud "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Shells%20in%20Plain%20Sight%20-%20Storing%20Payloads%20in%20the%20Cloud%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshells-in-plain-sight-storing-payloads-in-the-cloud "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshells-in-plain-sight-storing-payloads-in-the-cloud&mini=true "Share on LinkedIn")

THIS POST WAS WRITTEN BY [@NYXGEEK](https://twitter.com/nyxgeek?lang=en)

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Burkeland_1.png)

I stumbled upon an old side project the other day -- it was a tool to get payloads through web content filters by hiding PowerShell in images on public sites. For example, this tweet from 2018 contains a bind shell encoded in the image, [hosted by Twitter](https://twitter.com/nyxgeek/status/956201229499191297).

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Burkeland_fig1.png)

Figure 1 - Tweet Containing Shell

While I don't regularly use this technique, and I'm not the first to use it by any means, I think it's a lot of fun and worth sharing.

TL;DR: Encode payload in image file, host it publicly, and nobody's the wiser.

## Intro

Today, we are going to be exploring storing our shells in "the cloud" by encoding them in images in publicly accessible locations.

This idea isn't new. Steganography has existed since the early days of computing. I remember a news article a few years back where hacker organizations had used social media posts on Instagram to [control malware botnets](https://www.bleepingcomputer.com/news/security/russian-state-hackers-use-britney-spears-instagram-posts-to-control-malware/) (This story is neat, and the hackers actually used a comment on the post with some Unicode delimiters to craft a URL).

Lastly, before we start: caveat emptor. Just know that while this should, in theory, be hard to notice, if somebody knew where to look, it would be trivial to extract the shell. If you're using a reverse shell or storing data, you probably don't want to leave it out anywhere long-term.

## The Concept

There are a few ways we could do this. To start, let's think about what an image file is. An image is really just a series of pixels of different colors. Each pixel's data is encoded as RGB (Red, Green, and Blue). However, some formats such as PNG store their data with an additional dimension: Alpha, aka transparency. This results in a modified set, with RGBa values (Red, Green, Blue, Alpha). For this exercise, we'll look at encoding our shell into the RGBa data.

![](https://www.trustedsec.com/wp-content/uploads/2023/03/Burkeland_fig2.png)

Figure 2 - RGB Values

To encode our data, we will need to overwrite some RGB values. Now, modifying any of the values (R, G, B, A) is probably okay. We could store our data in any of those values. However, one of these values stands out as a "better" option. That is the Alpha channel, aka the transparency channel. While R, G, and B control the actual color output, the alpha channel is generally less noticeable.

So now we just have to figure out: how can we store our code in the alpha channel (Or the Red, Green, or Blue channels)? Well, here is where some knowledge about ASCII comes in handy. ASCII has character codes from 0 - 127.

These character codes are the decimal representation of all the printable (A-Z, a-z, 0-9, etc.), and non-printable (Return, Newline, NULL,...