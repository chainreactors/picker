---
title: Using RPC in BOFs
url: https://www.trustedsec.com/blog/using-rpc-in-bofs/
source: TrustedSec
date: 2023-03-29
fetch_date: 2025-10-04T11:02:18.153546
---

# Using RPC in BOFs

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
* [Using RPC in BOFs](https://trustedsec.com/blog/using-rpc-in-bofs)

March 28, 2023

# Using RPC in BOFs

Written by
Christopher Paschen

Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/RPCinBOFs_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695562486&s=90d74ac197092e165d75034d483d2236)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9ba4e8eef9f1fef8efa6d8f3fef8f0bea9abf4eeefbea9abeff3f2e8bea9abfae9eff2f8f7febea9abfde9f4f6bea9abcfe9eee8effeffc8fef8bea9aabdfaf6eba0f9f4ffe2a6cee8f2f5fcbea9abc9cbd8bea9abf2f5bea9abd9d4dde8bea8dabea9abf3efefebe8bea8dabea9ddbea9ddefe9eee8effeffe8fef8b5f8f4f6bea9ddf9f7f4fcbea9ddeee8f2f5fcb6e9ebf8b6f2f5b6f9f4fde8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fusing-rpc-in-bofs "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Using%20RPC%20in%20BOFs%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fusing-rpc-in-bofs "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fusing-rpc-in-bofs&mini=true "Share on LinkedIn")

In previous blog posts, I detailed [how a windows programmer can develop against RPC](https://trustedsec.com/blog/rpc-programming-for-the-aspiring-windows-developer) and solidified [why I feel Beacon Object Files (BOFs) have become cemented](https://trustedsec.com/blog/changes-in-the-beacon-object-file-landscape) as a usable technique for the time being. I will complete this mini-series by making the previous [RPC POC code](https://github.com/trustedsec/Windows-MS-LSAT-RPC-Example) that we had into a BOF.

## Planning

The first step of converting our BOF is to plan our end goal. First, we determine the scope of the conversion. In this case, our POC is small, so we are not stripping functionality out of a larger project; therefore, we will be converting the entire thing.

Next, we should decide if we are coding this for a specific implant’s runner or targeting a more general audience. I would at least like to be able to run whatever we output in Cobalt Strike, our internal implant, and Sliver. This means that we must code against the lowest common denominator of functionality for all functionality that we code. A couple restrictions are introduced via this combination:

1. No more than 64 unique dynamic function resolution calls can be used.
2. All defaults should be handled in the BOF, as no script logic can provide defaults.

Finally, we should decide what we want the user experience to be like. I do this as a planning step for most of the software I write. Knowing how you want a user to interact with the system you are coding can steer your development. For this case, I do not want the services being checked to be hardcoded. Instead, I want the user to be able to input any service name and receive the answer as to whether it exists on a given target. It should look something like <bofname> <target> <servicename>. I would want to code 'NT Service\' as the prefix on the BOF side, given that all checks will need to start with that string.

For this blog, I will not go through full incorporation into the named implants, as a much more reasonable implementation of these techniques would use the win32 API.

## Preparing

We have decided to convert our entire POC. Up front, that is easy enough—we would simply convert every function call to a BOF equivalent. To do this we are going to first copy all the .c files out of our existing project and paste them into a new subfolder called 'BOF'. Next, we will open each file and start removing/converting code.

Another item we need to address is a BOF consists of a singular object file. While there are ways to coax the linker to join multiple object files into a singular object file, I find it much easier to just #include our various dependent .c files together, such that the compiler will recognize them as one unit and output one object file.

We should also check to see if C++ code is used. If so, our easiest path is likely to convert to c-based equivalents. While it is possible to get C++ code to compile into a runnable BOF, it requires familiarity with numerous assumptions. Unless you have a compelling reason to keep the C++ code, it is best to avoid it with a BOF.

Our original POC included and depended on the WindowsRpcHelper library. For this library, we need to break out the used functions and include them directly, be that in our source itself, or in a frequently reused common .c file that we could include between projects. An example of such a library...