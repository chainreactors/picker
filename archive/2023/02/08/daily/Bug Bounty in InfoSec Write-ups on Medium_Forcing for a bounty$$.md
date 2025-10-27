---
title: Forcing for a bounty$$
url: https://infosecwriteups.com/forcing-for-a-bounty-b637c468d7bd?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:44.752852
---

# Forcing for a bounty$$

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb637c468d7bd&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fforcing-for-a-bounty-b637c468d7bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fforcing-for-a-bounty-b637c468d7bd&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b637c468d7bd---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b637c468d7bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Forcing for a bounty$$

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---byline--b637c468d7bd---------------------------------------)

[Rafi Ahamed (Leonidas D. Ace)](https://rafi-ahamed.medium.com/?source=post_page---byline--b637c468d7bd---------------------------------------)

2 min read

·

Nov 3, 2020

--

1

Listen

Share

**Hola fellow researchers,**

Myself, **Rafi Ahamed**. I am a Cyber Security Researcher from Bangladesh. I am a currently doing my BBA from University of Dhaka. But I do love nerdy stuffs. Let’s not waste any time & get down to our topic.

First of all, don’t get confused with the title. By forcing I actually meant Forced Browsing.

## **What is Forced Browsing?**

F**orced browsing** is an attack where the attacker aim to enumerate and access resources that are not referenced by the application, but are still accessible.

## **How did I find the bug?**

Recently I was testing a private site in **HackerOne** and the site was selling educational videos. So, they allow an user a preview of the video without payment. But the preview was for only 15 seconds or less. Well, who cares about that right?

**Actually, that’s where the $$$ lies.**

As usual I turned on **Interception** using **Burp Suite** & noticed endpoints like below:

Press enter or click to view image in full size

![]()

But the endpoint was on another subdomain. By looking at the subdomain name it was understood that the organization uses this subdomain to store all it’s videos & other stuffs. So, I quickly visited the endpoint to see if I can find anything.

Press enter or click to view image in full size

![]()

**The endpoint**

But I got nothing. Got the same preview with the same duration.

![]()

Then I noticed that the endpoint has something like this

Press enter or click to view image in full size

![]()

I thought why not remove it & see what happens. I was surprised that I got the full video. Now I can watch any paid video without payment.

![]()

> I quickly reported the bug to HackerOne & got a nice **$500** bounty.

**Reported:** Sep 27th.

**Triaged:** Sep 28th.

**Resolved:** Oct 18th.

Hope you guys enjoyed this one . PM me at [**Facebook**](https://www.facebook.com/rafiahamed.rupak.3)or [**LinkedIn**](https://www.linkedin.com/in/rafi-ahamed) anytime if you have any questions .

***#Eat\_sleep\_hack\_repeat
#Hack’em all***

[Infosec](https://medium.com/tag/infosec?source=post_page-----b637c468d7bd---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----b637c468d7bd---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----b637c468d7bd---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b637c468d7bd---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----b637c468d7bd---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b637c468d7bd---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b637c468d7bd---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b637c468d7bd---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b637c468d7bd---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--b637c468d7bd---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/resize:fill:96:96/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--b637c468d7bd---------------------------------------)

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/resize:fill:128:128/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--b637c468d7bd---------------------------------------)

[## Written by Rafi Ahamed (Leonidas D. Ace)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--b637c468d7bd---------------------------------------)

[277 followers](https://rafi-ahamed.medium.com/followers?source=post_page---post_author_info--b637c468d7bd---------------------------------------)

·[3 following](https://medium.com/%40rafi-ahamed/following?source=post_page---post_author_info--b637c468d7bd---------------------------------------)

Pentester/Bug Bounty Hunter & A typical Business Undergraduate. (<https://www.facebook.com/rafiahamed.rupak.3>)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----b637c468d7bd---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b637c468d7bd---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b637c468d7bd---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b637c468d7bd---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b637c468d7bd---------------------------------------)

[Privacy](https://p...