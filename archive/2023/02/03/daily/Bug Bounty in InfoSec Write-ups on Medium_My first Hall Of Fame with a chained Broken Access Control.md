---
title: My first Hall Of Fame with a chained Broken Access Control
url: https://infosecwriteups.com/my-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-03
fetch_date: 2025-10-04T05:34:22.123476
---

# My first Hall Of Fame with a chained Broken Access Control

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F76f9e2e0e467&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-hall-of-fame-with-a-chained-broken-access-control-76f9e2e0e467&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-76f9e2e0e467---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-76f9e2e0e467---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My first HOF: Story of a chained Broken Access Control

[![Naman Jain](https://miro.medium.com/v2/resize:fill:64:64/1*VdpO9wQ_ckzyUtkTs8s6EQ.jpeg)](https://namx05.medium.com/?source=post_page---byline--76f9e2e0e467---------------------------------------)

[Naman Jain](https://namx05.medium.com/?source=post_page---byline--76f9e2e0e467---------------------------------------)

2 min read

·

Feb 2, 2023

--

Listen

Share

This blog is about how I got my first HOF after chaining multiple bugs.

Let’s get started.

Press enter or click to view image in full size

![]()

## What is Broken Access Control

> In simple words, BAC means you are able to perform certain actions or fetch certain files which you are not authorized to.

## The Bug

Let’s name the program ***redacted.com***. After some enumeration I found a support page i.e. ***redacted.com/support*** which has a login feature. I created an account i.e. **Attacker1** and started exploring with it.

Later I found that you can create ticket in the help desk section. I simply files a test complaint and created a ticket and checked the Burp History I was a parameter named opener ID. Then I got two ideas, Rate Limit and IDOR.

Press enter or click to view image in full size

![]()

Request Captured in Burp while submitting the ticket

### Bug 1: Rate Limit

For this, capture the request in Burp while submitting the ticket > send the request to intruder > add the position > start the attack. As expected, there was not Rate Limit and I was able to create as many tickets I want.

### Bug 2: IDOR

Since I already the ID parameter in request, I created another account i.e. **Attacker2** without wasting any time.

I created a ticket with the Attacker1’s account > Captured the request > changed the ID number with Attacker2’s ID > send the request to intruder > add the position > start the attack.

And as expected, It worked. I was able to create as many tickets as I want in other users help desk portal.

## Impact

By Doing so, an attacker can create many unwanted tickets which can be a hectic for the support team to close the tickets as well as the user’s too and can also spam the user’s email.

### HOF

Press enter or click to view image in full size

![]()

## Outro

Thanks for reading this writeup. This is my first blog related to Bug Bounty, so Feedback is appreciated. And if you have any doubt, you can reach me at:

| [LinkedIn](http://linkedin.com/in/namx05) | [Twitter](http://twitter.com/namx05) |

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----76f9e2e0e467---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----76f9e2e0e467---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----76f9e2e0e467---------------------------------------)

[Info Sec Writeups](https://medium.com/tag/info-sec-writeups?source=post_page-----76f9e2e0e467---------------------------------------)

[Infosec Write Ups](https://medium.com/tag/infosec-write-ups?source=post_page-----76f9e2e0e467---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--76f9e2e0e467---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--76f9e2e0e467---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--76f9e2e0e467---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--76f9e2e0e467---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--76f9e2e0e467---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Naman Jain](https://miro.medium.com/v2/resize:fill:96:96/1*VdpO9wQ_ckzyUtkTs8s6EQ.jpeg)](https://namx05.medium.com/?source=post_page---post_author_info--76f9e2e0e467---------------------------------------)

[![Naman Jain](https://miro.medium.com/v2/resize:fill:128:128/1*VdpO9wQ_ckzyUtkTs8s6EQ.jpeg)](https://namx05.medium.com/?source=post_page---post_author_info--76f9e2e0e467---------------------------------------)

[## Written by Naman Jain](https://namx05.medium.com/?source=post_page---post_author_info--76f9e2e0e467---------------------------------------)

[93 followers](https://namx05.medium.com/followers?source=post_page---post_author_info--76f9e2e0e467---------------------------------------)

·[31 following](https://medium.com/%40namx05/following?source=post_page---post_author_info--76f9e2e0e467---------------------------------------)

Security Researcher @Credshields | Smart Contract Auditor

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----76f9e2e0e467---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----76f9e2e0e467---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----76f9e2e0e467---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----76f9e2e0e467---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----76f9e2e0e467---------------------------------------)

[Privacy](https://policy.medium.co...