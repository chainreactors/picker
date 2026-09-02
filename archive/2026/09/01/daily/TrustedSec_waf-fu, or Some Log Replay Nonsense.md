---
title: waf-fu, or Some Log Replay Nonsense
url: https://trustedsec.com/blog/waf-fu-or-some-log-replay-nonsense
source: TrustedSec
date: 2026-09-01
fetch_date: 2026-09-02T06:41:41.550343
---

# waf-fu, or Some Log Replay Nonsense

[Skip to Main Content](#main)

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
* [waf-fu, or Some Log Replay Nonsense](https://trustedsec.com/blog/waf-fu-or-some-log-replay-nonsense)

September 01, 2026

# waf-fu, or Some Log Replay Nonsense

Written by
Lilly Mayo

Application Security Assessment
Cloud Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WaffuYourWayToBetterCredAccess_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1787700738&s=fca029e7755ff8582ac2f60483cc4609)

Table of contents

* [1    waf-fu Your Way to Better Credential Access](#Access)
* [2    Straight From the Horse’s Docs](#Docs)
* [3    Hunting to be Repetitive](#Repetitive)
* [4    Replay With waf-fu](#Replay)
* [5    Plugging the Gaps](#Gaps)
* [6    Live, Log, (Replay), Laugh](#Laugh)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#59662a2c3b333c3a2d641a313c3a327c6b69362c2d7c6b692d31302a7c6b69382b2d303a353c7c6b693f2b36347c6b690d2b2c2a2d3c3d0a3c3a7c6b687f383429623b363d20642e383f743f2c7c6b1a7c6b69362b7c6b690a36343c7c6b6915363e7c6b690b3c293538207c6b691736372a3c372a3c7c6a187c6b69312d2d292a7c6a187c6b1f7c6b1f2d2b2c2a2d3c3d2a3c3a773a36347c6b1f3b35363e7c6b1f2e383f743f2c74362b742a36343c7435363e742b3c29353820743736372a3c372a3c "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwaf-fu-or-some-log-replay-nonsense "Share on Facebook")
* [Share on X](https://twitter.com/share?text=waf-fu%2C%20or%20Some%20Log%20Replay%20Nonsense%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwaf-fu-or-some-log-replay-nonsense "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwaf-fu-or-some-log-replay-nonsense&mini=true "Share on LinkedIn")

## 1    waf-fu Your Way to Better Credential Access

So, a gig or two ago I was reviewing CloudWatch logs to search for any credentials that I may be able to use, in order to gain additional access to the environment. Various Web Application Firewalls (WAFs) were configured so that all headers were captured in the log, which was pretty convenient!

The part that wasn’t so fun was trying to replay multiple requests across multiple WAF logs, each with their own required content, just to see if at least one may provide a way to hopefully gain additional access into the applications the WAFs were configured to protect. It’s possible to do it all manually, but I found it to be a frustrating process when reviewing dozens or hundreds of log groups or individual log entries that needed to be checked to find out which may get me where I wanted to go.

Soo, I figured that there must be a better solution to handle building AWS WAF log replay traffic more at scale and that’s what was built. Feel free to jump to [Replay With waf-fu](#Replay) if you want to see the tool that’s being released. But for everyone else, we’ll first talk about what WAF does and doesn’t capture by default.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/waf-fu_Mayo/Fig01_Mayo_waf-fu.jpg?w=320&q=90&auto=format&fit=max&dm=1787767668&s=e76d0ffc391f321fdfe53c8326b9c6ac)

Figure 1 - Surprises Abound

## 2    Straight From the Horse’s Docs

Okay, so what does an AWS WAF capture with the default configuration? [Surprisingly a lot](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html), and none of it is automatically redacted. So…good news for us. You may see some cutoff if dealing with [logs of exceptional size](https://docs.aws.amazon.com/waf/latest/developerguide/waf-oversize-request-components.html), but for most cases it’s probably the whole hog. Here’s a small table with the details to look professional about it.

| Field | Source | Details |
| --- | --- | --- |
| HTTP Method | *httpRequest.httpMethod* | Request operation, such as GET, POST, PUT, DELETE, etc. |
| URI Path | *httpRequest.uri* | Path identifying the requested resource |
| Query String | *httpRequest.args* | Query parameters and their values |
| All Headers | *httpRequest.headers[]* | Header names and values supplied with the request |
| HTTP Version | *httpRequest.httpVersion* | HTTP protocol version used for the request |
| Client IP | *httpRequest.clientIp* | IP address of the client sending the request |
| Country | *httpRequest.country* | Country associated with the request's origin or a literal ‘-‘ when AWS WAF cannot determine it |
| Timestamp | *timestamp* | Request timestamp recorded in milliseconds since the Unix epoch |

It’s a lot of neato stuff. And as seen with the CAPTCHA log example on the AWS [WAF logging examples](https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html) documentation, their examples show that logged content can certainly include session cookie data.

To be fair, some of WAFv2 documentation does recommend r...