---
title: API based IDOR to leaking Private IP address of 6000 businesses
url: https://infosecwriteups.com/api-based-idor-to-leaking-private-ip-address-of-6000-businesses-6bc085ac6a6f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-16
fetch_date: 2025-10-04T03:59:45.374846
---

# API based IDOR to leaking Private IP address of 6000 businesses

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6bc085ac6a6f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fapi-based-idor-to-leaking-private-ip-address-of-6000-businesses-6bc085ac6a6f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fapi-based-idor-to-leaking-private-ip-address-of-6000-businesses-6bc085ac6a6f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6bc085ac6a6f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6bc085ac6a6f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# API based IDOR to leaking Private IP address of 6000 businesses

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---byline--6bc085ac6a6f---------------------------------------)

[Rafi Ahamed (Leonidas D. Ace)](https://rafi-ahamed.medium.com/?source=post_page---byline--6bc085ac6a6f---------------------------------------)

3 min read

·

Jan 1, 2021

--

1

Listen

Share

Hello fellow researchers,

Myself, **Rafi Ahamed**. I am a Cyber Security Researcher from Bangladesh. I love to break security. Anyway, without further ado let’s get to today’s topic.

Before I start, I wanna thank [**Katie Paxton**](https://twitter.com/InsiderPhD)for her videos. I learned a lot about IDORs from her videos. I actually earned my whole year’s bounty target just form IDORs that I learned from her videos.

## What is IDOR?

> *Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly.*

## What is an API?

> API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

So, I was testing a **NDA (*Non-disclosure Agreement*)** program and I noticed that the Web Application had an option to view the access logs of the users. Seems so simple right?

![]()

I have a bad habit of turning on **Interception** and see every request that the browser sends to the server while browsing an web application. When I visited the same page again, I noticed that **my** **access-logs** were not being displayed even though other contents of the page already has load already. Then I noticed that the my Interception was on and there was an API request intercepted which was trying to fetch the access-logs of the users.

Press enter or click to view image in full size

![]()

The intercepted request

If you take a closer at the POST data, you will see that it has a **UserID** in it.

Press enter or click to view image in full size

![]()

User ID request

Then I sent the request to Intruder and **Brute-forced** the **UserID** and I got the ***access-logs of 6000 businesses***.

![]()

The Dev’s reaction

I quickly reported the bug and the company fixed the bug within 48hours. I got a nice **$4digit bounty** for the bug.

![]()

Hope you guys enjoyed this one . PM me at [**Facebook**](https://www.facebook.com/rafiahamed.rupak.3)[**, LinkedIn**](https://www.linkedin.com/in/rafi-ahamed) or [**Twitter**](https://twitter.com/L3onid1s) anytime if you have any questions.

[Infosec](https://medium.com/tag/infosec?source=post_page-----6bc085ac6a6f---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6bc085ac6a6f---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----6bc085ac6a6f---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----6bc085ac6a6f---------------------------------------)

[Red Teaming](https://medium.com/tag/red-teaming?source=post_page-----6bc085ac6a6f---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6bc085ac6a6f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6bc085ac6a6f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6bc085ac6a6f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6bc085ac6a6f---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--6bc085ac6a6f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/resize:fill:96:96/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--6bc085ac6a6f---------------------------------------)

[![Rafi Ahamed (Leonidas D. Ace)](https://miro.medium.com/v2/resize:fill:128:128/0*ApKwr-CMeaPrvOU0)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--6bc085ac6a6f---------------------------------------)

[## Written by Rafi Ahamed (Leonidas D. Ace)](https://rafi-ahamed.medium.com/?source=post_page---post_author_info--6bc085ac6a6f---------------------------------------)

[277 followers](https://rafi-ahamed.medium.com/followers?source=post_page---post_author_info--6bc085ac6a6f---------------------------------------)

·[3 following](https://medium.com/%40rafi-ahamed/following?source=post_page---post_author_info--6bc085ac6a6f---------------------------------------)

Pentester/Bug Bounty Hunter & A typical Business Undergraduate. (<https://www.facebook.com/rafiahamed.rupak.3>)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6bc085ac6a6f---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6bc085ac6a6f---------------------------------------)

[About](h...