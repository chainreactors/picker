---
title: So… You Found AWS Access Keys (Part 1)
url: https://trustedsec.com/blog/so-you-found-aws-access-keys-part-1
source: TrustedSec
date: 2026-09-10
fetch_date: 2026-09-11T06:52:53.641618
---

# So… You Found AWS Access Keys (Part 1)

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
* [So… You Found AWS Access Keys (Part 1)](https://trustedsec.com/blog/so-you-found-aws-access-keys-part-1)

September 10, 2026

# So… You Found AWS Access Keys (Part 1)

Written by
Lilly Mayo

Cloud Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/FoundAWSAccessKeysPart1_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1788530175&s=5e2b924e07b29c603dda3685674950f2)

Table of contents

* [What To Do With the Things You Found](#Found)
* [12 Digits to Discovery](#Digits)
* [Statistically Likely AWS Configurations](#Statistically)
* [Gotta go brrrr](#brrrr)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e2dd91978088878196dfa18a878189c7d0d28d9796c7d0d2968a8b91c7d0d28390968b818e87c7d0d284908d8fc7d0d2b6909791968786b18781c7d0d3c4838f92d9808d869bdfb18dc7a7d0c7dad2c7a3d4c7d0d2bb8d97c7d0d2a48d978c86c7d0d2a3b5b1c7d0d2a38181879191c7d0d2a9879b91c7d0d2c7d0dab2839096c7d0d2d3c7d0dbc7d1a3c7d0d28a96969291c7d1a3c7d0a4c7d0a496909791968786918781cc818d8fc7d0a4808e8d85c7d0a4918dcf9b8d97cf848d978c86cf839591cf838181879191cf89879b91cf92839096cfd3 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fso-you-found-aws-access-keys-part-1 "Share on Facebook")
* [Share on X](https://twitter.com/share?text=So%E2%80%A6%20You%20Found%20AWS%20Access%20Keys%20%28Part%201%29%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fso-you-found-aws-access-keys-part-1 "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fso-you-found-aws-access-keys-part-1&mini=true "Share on LinkedIn")

Finding plaintext access keys to an AWS account during an engagement is always great thrill. What can be done with them? What do they have access to? Are they *even for* any of the accounts in scope? It can be super difficult to tell any of this just from the access key, security key, and maybe session token that you found.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AWSAccessKeys_Mayo/Fig01_Mayo_AWSAccessKeys.png?w=320&q=90&auto=format&fit=max&dm=1788530588&s=6213fd5fed477cd2b820ea14377e8f4b)

Figure 1: Tell ‘em Cap’

After all, AWS has more than 200 freaking services and products, at least based on how they tend to count things. They also don’t all necessarily authenticate in the same way or with the same looking token formats. Regardless, it can be a lot. But we’re going to walk through some of it today and see if we can get some clarity for everyone that may just be looking at the report of whatever secret scanning tool was just run and your mind is just shouting into the void, *“Great! Now what the **frak** do I do with this?!”*

### AKIA to ASIA and In-Between

The main form of AWS access that most people know about is one of two types: Long-Term Access Keys and Temporary Access Keys. These are what we’re focusing on today. Both are combinations of strings that provide the access and look like the popular “AKIA” identifier for long-term keys and “ASIA” identifier for maybe lesser known but far more utilized temporary keys.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AWSAccessKeys_Mayo/Fig02_Mayo_AWSAccessKeys.png?w=320&q=90&auto=format&fit=max&dm=1788530589&s=a6fe076e2498a4ada0a31d4cae4ecc35)

Figure 2: AKIA/ASIA Formats

* **AKIA**: Long-term access keys for an IAM user’s programmatic access.
* **ASIA**: Temporary access keys created by AWS services on your behalf, such as when a `sts:AssumeRole` or similar is used to assume an IAM role.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AWSAccessKeys_Mayo/Fig03_Mayo_AWSAccessKeys.png?w=320&q=90&auto=format&fit=max&dm=1788530590&s=45a8afc49df721ca11c7b29064b6f78a)

Figure 3: Meme Tax

### “He went to find AKIA?”

Well, what can be done with these? That’s what we’re trying to get to! Oh! And there’s more access methods than just these, but we’ll start here. We’ll get into others in later posts, but these two are kind of the queens of the realm. And we’re not authenticating to anything unless we have both in our hands.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AWSAccessKeys_Mayo/Fig04_Mayo_AWSAccessKeys.png?w=320&q=90&auto=format&fit=max&dm=1788530591&s=70b0ca5444c31b7069b458843589227d)

Figure 4: AKIAaaaa

* **AWS Access Key ID (AKIA)** is usually 20 characters that always have AKIA’ as the first four characters.
* **AWS Secret Access Key** is a 40-character alpha-numeric string made up of randomized upper, lower, digits, and some symbols characters.

Most secret scanning tools have regex patterns just for the AKIA key. If you get a ping for one, then look at the surrounding data to see if you’re lu...