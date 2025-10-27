---
title: Forgotten Subdomain = $1000 “AWS Breach” Bounty
url: https://infosecwriteups.com/finding-needle-in-the-haystack-how-a-forgotten-subdomain-led-to-complete-aws-infrastructure-328571e88496?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:28:48.370447
---

# Forgotten Subdomain = $1000 “AWS Breach” Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F328571e88496&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-needle-in-the-haystack-how-a-forgotten-subdomain-led-to-complete-aws-infrastructure-328571e88496&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-needle-in-the-haystack-how-a-forgotten-subdomain-led-to-complete-aws-infrastructure-328571e88496&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-328571e88496---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-328571e88496---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Forgotten Subdomain = $1000 “AWS Breach” Bounty

[![Akash Singh](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*DBhqJwY0g4vorOe3)](https://medium.com/%400xakash.singh?source=post_page---byline--328571e88496---------------------------------------)

[Akash Singh](https://medium.com/%400xakash.singh?source=post_page---byline--328571e88496---------------------------------------)

7 min read

·

Aug 24, 2025

--

2

Share

## **Finding Needle in The Haystack!**

Free Article Link: [Click Here!](https://medium.com/bugbountywriteup/finding-needle-in-the-haystack-how-a-forgotten-subdomain-led-to-complete-aws-infrastructure-328571e88496?sk=07394f9022a2fae64c6e7dc2cbc99d97)

## The Hunt Begins

Every security researcher knows the feeling, staring at a target domain, wondering where the vulnerabilities hide. Sometimes the most devastating findings come not from the main application, but from the forgotten corners of an organization’s digital infrastructure. This is the story of how a wildcard subdomain led me down a rabbit hole that ended with access to an entire company’s AWS infrastructure and the personal data of millions of users.

Press enter or click to view image in full size

![]()

Subdomain Enumeration using tools like crt.sh can help in mapping out a target

## Chapter 1: The Wildcard in the Wild

It started like any other recon. Subdomain enumeration on `redacted.com` was returning the usual suspects – www, mail, blog. But then something interesting caught my eye: `*.corp.redacted.com`. A wildcard subdomain. In the security world, wildcards are like unmarked doors in a long hallway, you never know what's behind them until you try the handle.

I spun up my brute-forcing tools, feeding them a carefully crafted wordlist of common corporate services:

* jenkins.corp.redacted.com
* gitlab.corp.redacted.com
* jira.corp.redacted.com

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--328571e88496---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--328571e88496---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--328571e88496---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--328571e88496---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--328571e88496---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Akash Singh](https://miro.medium.com/v2/resize:fill:96:96/0*DBhqJwY0g4vorOe3)](https://medium.com/%400xakash.singh?source=post_page---post_author_info--328571e88496---------------------------------------)

[![Akash Singh](https://miro.medium.com/v2/resize:fill:128:128/0*DBhqJwY0g4vorOe3)](https://medium.com/%400xakash.singh?source=post_page---post_author_info--328571e88496---------------------------------------)

[## Written by Akash Singh](https://medium.com/%400xakash.singh?source=post_page---post_author_info--328571e88496---------------------------------------)

[91 followers](https://medium.com/%400xakash.singh/followers?source=post_page---post_author_info--328571e88496---------------------------------------)

·[3 following](https://medium.com/%400xakash.singh/following?source=post_page---post_author_info--328571e88496---------------------------------------)

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----328571e88496---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----328571e88496---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----328571e88496---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----328571e88496---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----328571e88496---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----328571e88496---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----328571e88496---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----328571e88496---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----328571e88496---------------------------------------)