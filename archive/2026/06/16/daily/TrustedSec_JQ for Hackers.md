---
title: JQ for Hackers
url: https://trustedsec.com/blog/jq-for-hackers
source: TrustedSec
date: 2026-06-16
fetch_date: 2026-06-17T07:03:41.971161
---

# JQ for Hackers

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
* [JQ for Hackers](https://trustedsec.com/blog/jq-for-hackers)

June 16, 2026

# JQ for Hackers

Written by
Justin Bollinger

Penetration Testing
Training

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/JQForHackers_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1780930236&s=cbd58bc301e6bb347f39acbdd32ff8f2)

Table of contents

* [Some JSON to Play With](#Play)
* [Pretty Printing With jq](#Printing)
* [A Quick JSON Primer](#Quick)
* [Extracting Specific Fields](#Extracting)
* [Filtering With select](#select)
* [A Real-World Example: Parsing ldapdomaindump Output](#Example)
* [The Mental Model](#Model)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e8d79b9d8a828d8b9cd5ab808d8b83cddad8879d9ccddad89c80819bcddad8899a9c818b848dcddad88e9a8785cddad8bc9a9d9b9c8d8cbb8d8bcddad9ce898598d38a878c91d5a2b9cddad88e879acddad8a0898b838d9a9bcddba9cddad8809c9c989bcddba9cddaaecddaae9c9a9d9b9c8d8c9b8d8bc68b8785cddaae8a84878fcddaae8299c58e879ac580898b838d9a9b "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjq-for-hackers "Share on Facebook")
* [Share on X](https://twitter.com/share?text=JQ%20for%20Hackers%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjq-for-hackers "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fjq-for-hackers&mini=true "Share on LinkedIn")

When I was first introduced to ***jq***, it was overwhelming and confusing. I tried to just wing it, not realizing it was a very complex and powerful program. With more and more tools outputting JSON, I figured it was time to actually learn it. Turns out, it's pretty easy once you get the hang of it.

This blog is for the hackers, sysadmins, and anyone who wasn't forced to learn JavaScript by some sadistic college professor. It's an attempt to convince you, the grey-bearded hacker, to stop using CSV files and `cut` and embrace JSON.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JQforHackers_Bollinger/Fig01_Bollinger_JQjackers.png?w=320&q=90&auto=format&fit=max&dm=1780000007&s=96970836764c4dd381bf0fd645441570)

If you're familiar with Python dictionaries, this should come naturally.

## Some JSON to Play With

Lucky for us, ***httpx*** from ProjectDiscovery is a perfect tool to use as a simple example. Run the following to get a JSON object back:

```
echo www.trustedsec.com | httpx -j
```

The output will look something like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JQforHackers_Bollinger/FigA_Bollinger_JQjackers.png?w=320&q=90&auto=format&fit=max&dm=1780946479&s=4fd53cdf4cc9afa7d3d096eecf038135)

That's hard to read ‚ it's a lot of data, and it's all on a single line. Without word wrap, you wouldn't even be able to see the whole thing. You also can't ***grep*** cleanly through it.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JQforHackers_Bollinger/Fig02_Bollinger_JQjackers.png?w=320&q=90&auto=format&fit=max&dm=1780000009&s=2f1cd6321d39f7e4ffbb46a77808978e)

## Pretty Printing With jq

Pipe the same command to `jq` . and the output becomes legible:

```
echo www.trustedsec.com | httpx -j | jq .
{
  "timestamp": "2025-03-14T17:19:03.813358-04:00",
  "cdn_name": "cloudflare",
  "cdn_type": "waf",
  "port": "443",
  "url": "https://www.trustedsec.com",
  "input": "https://www.trustedsec.com",
  "title": "TrustedSec | Your Trusted Cybersecurity Partner | Protecting What‚Ä¶",
  "scheme": "https",
  "webserver": "cloudflare",
  "content_type": "text/html",
  "method": "GET",
  "host": "172.67.70.133",
  "path": "/",
  "time": "762.046417ms",
  "a": [
    "172.67.70.133",
    "104.26.15.63",
    "104.26.14.63"
  ],
  "aaaa": [
    "2606:4700:20::ac43:4685",
    "2606:4700:20::681a:f3f",
    "2606:4700:20::681a:e3f"
  ],
  "tech": [
    "Alpine.js",
    "Cloudflare",
    "Craft CMS",
    "Google Tag Manager",
    "HSTS",
    "SEOmatic"
  ],
  "words": 22245,
  "lines": 779,
  "status_code": 200,
  "content_length": 258423,
  "failed": false,
  "cdn": true,
  "knowledgebase": {
    "PageType": "other",
    "pHash": 0
  },
  "resolvers": [
    "8.8.4.4:53",
    "1.1.1.1:53"
  ]
}
```

That's better, but it's still a lot of information that I don’t need right now. How do I use jq to limit the output?

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/JQforHackers_Bollinger/Fig03_Bollinger_JQjackers.png?w=320&q=90&auto=format&fit=max&dm=1780000010&s=78956359604ea2d795e068d8c12fa7ff)

## A Quick JSON Primer

Before we go further, you need to understand a little bit about JSON. If you want the full spec, see the [JSON Schema: core definitions and terminology](https://json-schema.org/draft-04/draft-zyp...