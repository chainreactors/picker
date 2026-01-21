---
title: Colonel Clustered: Finding Outliers in Burp Intruder
url: https://trustedsec.com/blog/colonel-clustered-finding-outliers-in-burp-intruder
source: TrustedSec
date: 2026-01-20
fetch_date: 2026-01-21T03:32:42.807280
---

# Colonel Clustered: Finding Outliers in Burp Intruder

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
* [Colonel Clustered: Finding Outliers in Burp Intruder](https://trustedsec.com/blog/colonel-clustered-finding-outliers-in-burp-intruder)

January 20, 2026

# Colonel Clustered: Finding Outliers in Burp Intruder

Written by
Drew Kirkpatrick

Threat Hunting
Application Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ColonelClustered_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1768595994&s=6f8b35cf1d23aee63dea6e8ed69f838d)

Table of contents

* [How it Works](#How)
* [Using Colonel Clustered](#Using)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#58672b2d3a323d3b2c651b303d3b337d6a68372d2c7d6a682c30312b7d6a68392a2c313b343d7d6a683e2a37357d6a680c2a2d2b2c3d3c0b3d3b7d6a697e393528633a373c21651b373437363d347d6a681b342d2b2c3d2a3d3c7d6b197d6a681e31363c31363f7d6a68172d2c34313d2a2b7d6a6831367d6a681a2d2a287d6a6811362c2a2d3c3d2a7d6b197d6a68302c2c282b7d6b197d6a1e7d6a1e2c2a2d2b2c3d3c2b3d3b763b37357d6a1e3a34373f7d6a1e3b373437363d34753b342d2b2c3d2a3d3c753e31363c31363f75372d2c34313d2a2b753136753a2d2a287531362c2a2d3c3d2a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fcolonel-clustered-finding-outliers-in-burp-intruder "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Colonel%20Clustered%3A%20Finding%20Outliers%20in%20Burp%20Intruder%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fcolonel-clustered-finding-outliers-in-burp-intruder "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fcolonel-clustered-finding-outliers-in-burp-intruder&mini=true "Share on LinkedIn")

TL;DR, gimme the goods: <https://github.com/hoodoer/ColonelClustered>

*Extension has been submitted to the Bapp store, awaiting approval.*

This is a Burp Suite extension I’ve been meaning to write for many years, yet somehow I never seemed able to finish the project until now. The reason I’ve wanted to create a clustering feature for Burp Intruder is because I find how pentesters typically use Intruder to be intellectually unsatisfying.

When we’re using Intruder, we’re typically looking for a difference in the server responses based on our fuzzed inputs. The metrics we use to identify those differences are commonly response size, status code, content-type, and response time. None of these are good quality measures of the actual content of the server response, but they are readily available and easy to sort by.

Intruder does capture every response, but manually reviewing thousands of them for subtle content changes is impractical. If a meaningful difference occurs that doesn't trigger a change in response size or timing, it effectively becomes invisible and we could miss something important.

While we don’t have time to read all the server responses ourselves, there’s no reason we can’t have algorithms do that for us, and that’s exactly what Colonel Clustered does. It groups request/response pairs together based on similarity of response content.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/ColonelClustered_Kirkpatrick/Fig01_Kirkpatrick_ColonelClustered.jpeg?w=320&q=90&auto=format&fit=max&dm=1768595410&s=2d0004b7ef7ce431c3292322886e6928)

Figure 1 - Poor, Poor Algorithms

Algorithms for clustering text have been known for decades—the popular K-Means algorithm dates back to the 1950s. This is not fancy LLM magic, this is just old school math.

Typically, these algorithms require a lot of manual knob-turning to get useful results, but Colonel Clustered takes advantage of the 'batched' nature of Intruder results. Because we have the entire dataset available at the time of analysis, the Burp extension can autofit its own parameters. This costs a few extra CPU cycles, but it completely removes the guesswork for the user. There are no settings to tweak because the algorithm calibrates itself to the data at hand.

## How it Works

So, let’s talk about how Colonel Clustered works. The first step is tokenization of the responses. There are different tokenizers for different content types, with strategies that match the form of that server response. You can [read more details on the underpinnings of Colonel Clustered here](https://github.com/hoodoer/ColonelClustered?tab=readme-ov-file#how-it-works).

After tokenization, some pre-grouping is performed to try to minimize the number of responses to be analyzed. Then we come to the clustering algorithms.

I spent a good amount of time trying out different approaches to the problem and ultimately settled on two (...