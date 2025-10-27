---
title: Dealing With Unmarked and Mismarked CUI
url: https://trustedsec.com/blog/dealing-with-unmarked-and-mismarked-cui
source: TrustedSec
date: 2025-08-13
fetch_date: 2025-10-07T00:48:11.006340
---

# Dealing With Unmarked and Mismarked CUI

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
* [Dealing With Unmarked and Mismarked CUI](https://trustedsec.com/blog/dealing-with-unmarked-and-mismarked-cui)

August 12, 2025

# Dealing With Unmarked and Mismarked CUI

Written by
Chris Camejo

CMMC
Information Security Compliance

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/UnmarkedMismarkedCUI_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1754658023&s=cb556f430fadc36e1d3311867d1f99d9)

Table of contents

* [Correct CUI Markings](#Markings)
* [Who Marks CUI?](#Who)
* [CUI Marking Errors](#Errors)
* [Addressing Mismarked CUI](#Addressing)
* [What’s Next?](#Next)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#ffc08c8a9d959a9c8bc2bc979a9c94dacdcf908a8bdacdcf8b97968cdacdcf9e8d8b969c939adacdcf998d9092dacdcfab8d8a8c8b9a9bac9a9cdacdced99e928fc49d909b86c2bb9a9e93969198dacdcfa8968b97dacdcfaa91929e8d949a9bdacdcf9e919bdacdcfb2968c929e8d949a9bdacdcfbcaab6daccbedacdcf978b8b8f8cdaccbedacdb9dacdb98b8d8a8c8b9a9b8c9a9cd19c9092dacdb99d939098dacdb99b9a9e93969198d288968b97d28a91929e8d949a9bd29e919bd292968c929e8d949a9bd29c8a96 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdealing-with-unmarked-and-mismarked-cui "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Dealing%20With%20Unmarked%20and%20Mismarked%20CUI%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdealing-with-unmarked-and-mismarked-cui "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdealing-with-unmarked-and-mismarked-cui&mini=true "Share on LinkedIn")

Implementing CMMC and other Controlled Unclassified Information (CUI) protection obligations depends on the accurate identification of CUI, and in some cases also depends on the identification of the CUI categories and limited dissemination controls applicable to each document.

Identification of CUI should be easy, because government agencies are required to mark all CUI before sending it to a contractor, but many contractors do not understand what proper CUI markings look like. This can be further complicated by documents that are mismarked or unnecessarily marked by other contractors. This post will help contractors identify CUI and understand what to do when marking errors are suspected.

## Correct CUI Markings

Understanding what a real CUI marking looks like will help identify when documents have been mismarked and prevent confusing other markings with CUI markings.

The National Archives and Records Administration (NARA) is in charge of the government-wide CUI program, including the CUI marking standard. The NARA [CUI Marking Guide](https://www.archives.gov/files/cui/documents/20161206-cui-marking-handbook-v1-1-20190524.pdf) provides detailed information on the standard markings. At a minimum each document that contains CUI must contain:

* A banner at the top of each page that says either “CUI” or “CONTROLLED”
* The name of the agency that designated the information as CUI (agency letterhead is acceptable for this purpose).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/MismarkedCUI_Camejo/Fig01_Camejo_MismarkedCUI.png?w=320&q=90&auto=format&fit=max&dm=1754922076&s=1e58847ee0bbaf8c5cd264f7606c034a)

Figure 1 - Example Document With NARA Standard CUI Markings

The CUI banner will contain extra information when CUI falls into certain categories that require extra safeguards and/or when the CUI is subject to limited dissemination controls. For example, a document marked with the banner “CUI//SP-AIV/SP-CHRI//FEDCON” contains CUI in both the Accident Investigation (SP-AIV) and Criminal History Records Information (SP-CHRI) categories that can only be disseminated to federal employees and contractors (FEDCON).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/MismarkedCUI_Camejo/Fig02_Camejo_MismarkedCUI.png?w=320&q=90&auto=format&fit=max&dm=1754922188&s=f517ddbf4a73180793cb4edfa1d5d3ac)

Figure 2 - NARA CUI Banner Format

A standardized [CUI coversheet](https://www.gsa.gov/system/files/SF901-18a.pdf) can be used to indicate the document is CUI in lieu of the banner marking on each page. The coversheet would contain the applicable CUI category and limited dissemination control markings.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/MismarkedCUI_Camejo/Fig02_Camejo_MismarkedCUI.jpg?w=320&q=90&auto=format&fit=max&dm=1754922221&s=46fd6362c3a1376e7aaad6be65834852)

Figure 3 - CUI Coversheet Template

Although this technically violates the NARA CUI marking ...