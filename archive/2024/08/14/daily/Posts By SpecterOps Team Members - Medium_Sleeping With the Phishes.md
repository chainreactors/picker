---
title: Sleeping With the Phishes
url: https://posts.specterops.io/sleeping-with-the-phishes-7d9e4dd88054?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-14
fetch_date: 2025-10-06T18:05:51.613388
---

# Sleeping With the Phishes

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7d9e4dd88054&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fsleeping-with-the-phishes-7d9e4dd88054&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fsleeping-with-the-phishes-7d9e4dd88054&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-7d9e4dd88054---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-7d9e4dd88054---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## PHISHING SCHOOL

# Sleeping With the Phishes

## Hiding C2 With Stealthy Callback Channels

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--7d9e4dd88054---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--7d9e4dd88054---------------------------------------)

10 min read

·

Aug 13, 2024

--

Listen

Share

Write a custom command and control (C2) implant — Check ✅

Test it on your system — Check ✅

Test it in a lab against your client’s endpoint detection and response (EDR) product — Check ✅

Convince a target to download the payload — Check ✅

Get your hard earned shell… — Nada! Nil! Goose Egg! ❌

## **What happened?**

If we’ve written a custom implant, and even taken precautions to test it against the same EDR, then we can be reasonably assured that the payload executed. The only remaining explanation as to why you didn’t receive a callback is that the outbound communication must have been blocked. Your poor shell is alive and well, but it’s crying out for help and can’t find its way home.

![]()

How can we avoid such a tragedy?

## What is Stealthy, Anyway?

When it comes to network traffic, the best approach we can take to remain “stealthy” is to try to blend in with existing traffic. By far, HTTP(S) is the most popular callback method for beaconing malware for three reasons:

1. ***It’s easy to implement*** — Simple, text-based, flexible protocol with many available libraries
2. ***It’s likely to be open outbound*** — Browser-based workflows necessitate HTTP(S) outbound
3. ***There is a ton of existing traffic*** — Our traffic will be a needle in a haystack

As long as the contents of our HTTP(S) messages look similar to real web traffic (a.k.a., our “C2 profile”) then we should be able to blend in and remain “stealthy”. But, there is a catch:

*“Everything is stealthy until someone is looking for it.”* [— @tifkin\_](https://twitter.com/tifkin_)

However you chose to structure your messages, there may be telltales that could give away your particular brand of malware in the future. If you don’t write your own C2 profile and just use an open-source one, then it is likely that some security products have already fingerprinted your malware’s communication style.

In addition to fingerprinting C2 profiles, network defenders have a few more ways to block a lot of unknown malicious traffic, and cause a headache for red teams:

1. Blocking traffic to new or uncategorized domains
2. Blocking traffic to any domain that is new to the target network (first visits)
3. Only allowing traffic to a narrow set of websites required to do business (allow listing)

Bypassing block number one is easy. Just host some benign content on your domain until it is a few months old and categorized. Blocks two and three are a bit more challenging to bypass. Let’s look at a few options that will likely still work even in the case of domain allow listing and that are also somewhat “stealthy”.

## The Classic: DNS

DNS has long been the preferred choice for red teams as a long-haul C2 callback. Like HTTP(S), it is extremely likely that DNS traffic is allowed outbound. There is also a ton of existing traffic to blend in. It only comes with two caveats:

1. ***Size limits*** — We only get [253 characters max](https://devblogs.microsoft.com/oldnewthing/20120412-00/?p=7873) per request to work with
2. ***Case insensitive*** — We will need to add additional bytes to [encode](https://gist.github.com/dtmsecurity/16728513bb92fe7bdec532be426ef17a) data that isn’t lowercase alphanumeric

DNS responses can be up to 512 bytes, but that’s still a major limitation. What this means is that most DNS C2 profiles break up the call and response data into small chunks and generate a very high volume of DNS requests over short periods. In addition, most DNS C2 profiles are designed to be “efficient” and use all of the available bytes for each request, which generates requests that don’t look normal at all compared to regular DNS lookups. Keeping this in mind, here’s some tips on how to use DNS effectively, while staying stealthy:

First, I would recommend only using DNS for check-ins, or other communications that require very small data transfers. In general, try to stay well under the 253 character limit.

Second, design post-exploitation commands that require very little output. For instance, one command might simply retrieve a host name, and let you know if the implant can load a webpage on that host. Another command might then instruct the implant to call back to that host over HTTPS.

Finally, remember that DNS caching is a thing. Make sure that every DNS request from your implant has at least one random or incrementing portion so that your requests aren’t dropped early by a caching DNS server.

## The Overlooked: ICMP

ICMP is also very frequently allowed outbound. Even if the only TCP ports allowed outbound are 80 and 443, remember that ICMP is its own protocol separate from TCP. Unfortunately, each ICMP packet can only carry 32 bytes of information and is oftentimes overlooked on the stealth front. If you happen to land in an environment that isn’t monitoring ICMP at all, then the size limitation shouldn’t matter.

![]()

We can generate a huge volume of traffic while still flying under the radar. The only problem is, if defenders do set up ICMP monitoring, then flagging anomalous requests is insanely easy. That’s because normal ECHO Request (PING) and ECHO Reply messages always have a data payload of ‘abcdefghijklmnopqrstuvwabcdefghi’. Why? I have no idea. Just know that fake messages are easy to spot so ICMP tends to be all or nothing when used for C2 traffic.

## You’ve Got Mail(ware): C2 Over SMTP

One of my favorite tricks to help my implants blend in is to use [Microsoft Component Object Model](https://learn.microsoft.com/en-us/windows/win32/com/the-component-object-model)s (COMs) to drive legitimate Windows binaries to do my bidding; for example, creating a hidden instance of [Internet Explorer](https://learn.microsoft.com/en-u...