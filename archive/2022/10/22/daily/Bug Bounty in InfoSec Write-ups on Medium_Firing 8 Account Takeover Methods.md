---
title: Firing 8 Account Takeover Methods
url: https://infosecwriteups.com/firing-8-account-takeover-methods-77e892099050?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-22
fetch_date: 2025-10-03T20:36:03.421739
---

# Firing 8 Account Takeover Methods

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F77e892099050&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffiring-8-account-takeover-methods-77e892099050&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffiring-8-account-takeover-methods-77e892099050&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-77e892099050---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-77e892099050---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Firing 8 Account Takeover Methods

[![Md Maruf Hosan (0xMaruf)](https://miro.medium.com/v2/resize:fill:64:64/1*jDIZ3f3n8yYDWXhYkiBS6Q.jpeg)](https://0xmaruf.medium.com/?source=post_page---byline--77e892099050---------------------------------------)

[Md Maruf Hosan (0xMaruf)](https://0xmaruf.medium.com/?source=post_page---byline--77e892099050---------------------------------------)

2 min read

·

Oct 19, 2022

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Photo by [Arget](https://unsplash.com/%40arget?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Hello! this is Md Maruf Hosan a bug bounty hunter from Bangladesh.
I am gonna be firing some account takeover methods

1. **Unicode Normalization Issue** 1. victim account `victim@gmail.com`
   2. create an account using Unicode
   example: vićtim@gmail.com
   here is ć is an Unicode character
2. list of Unicode character: <https://en.wikipedia.org/wiki/List_of_Unicode_characters>
   Note: check where verification doesn’t require
3. **Authorization Issue**
   1. change email of Account `A` and put email `B`
   2. check confirmation mail in account `B`
   3. open the confirmation mail from account `C`
   Taken over Account `C`
4. **Reusing Reset Token** if target allows you to reuse the reset link then hunt for more reset link via `gau` ,`wayback` or url`scan.io`
5. **Pre Account Takeover**
   1. signup using normal signup form as a hacker but hacker has no verification link.
   2. then if victim signs up using oauth .
   3. Verification bypass now attacker can login the victim account without verification link with the password he entered while registering.
6. **CORS Misconfiguration to Account Takeover**
   1. check api , any endpoint has access `access token/session/secret/fingerprint`
   2. if yes check for CORS misconfiguration does it allow us to fetch data from target?
   3. make a payload to fetch data and replace headers and boom
7. **Csrf to Account Takeover**if profile modification in cookie based authentication doesn’t generate any token
   1. open Account `A` change&Put email that you own click save intercept the request and generate a csrf poc.
   2. if fully cookie based auth then you dont have to modify anything send the csrf file to victim.
   3. if it requires UUID/UserID or unique token it becomes hard to do that but that doesn't mean it is secure , just start playing with target
   hint: password reset page helps many times for UUID/GUID and UserID
8. **Host Header Injection**
   well in this case there are 4 ways do that.
   1. click reset password change `host` header.
   2. or change proxy header ex: `X-Forwarded-For: attacker.com`
   3. or change `host`, `referrer`, `origin` headers at once as `attacker.com`
   4. click reset then click resend mail and do all 3 methods above
9. **Response Manipulation**1. code manipulation \* to `200 OK`
   2. code and body manipulation
   code \* to `200 OK`
   body \* to `{"success":true}` or `{}`
   it works when json is being used to transfer and receive data.

kick me on twitter: [@0xmaruf](https://twitter.com/0xmaruf)

Share this on twitter:

<https://twitter.com/0xMaruf/status/1582586936136384512?t=_oWdTwpqf1SpEurmIXWbpA&s=19>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Infosec](https://medium.com/tag/infosec?source=post_page-----77e892099050---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----77e892099050---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----77e892099050---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----77e892099050---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77e892099050---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--77e892099050---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--77e892099050---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--77e892099050---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--77e892099050---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Md Maruf Hosan (0xMaruf)](https://miro.medium.com/v2/resize:fill:96:96/1*jDIZ3f3n8yYDWXhYkiBS6Q.jpeg)](https://0xmaruf.medium.com/?source=post_page---post_author_info--77e892099050---------------------------------------)

[![Md Maruf Hosan (0xMaruf)](https://miro.medium.com/v2/resize:fill:128:128/1*jDIZ3f3n8yYDWXhYkiBS6Q.jpeg)](https://0xmaruf.medium.com/?source=post_page---post_author_info--77e892099050---------------------------------------)

[## Written by Md Maruf Hosan (0xMaruf)](https://0xmaruf.medium.com/?source=post_page---post_author_info--77e892099050---------------------------------------)

[177 followers](https://0xmaruf.medium.com/follower...