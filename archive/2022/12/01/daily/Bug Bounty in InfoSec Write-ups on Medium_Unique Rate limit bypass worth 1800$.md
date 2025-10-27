---
title: Unique Rate limit bypass worth 1800$
url: https://infosecwriteups.com/unique-rate-limit-bypass-worth-1800-6e2947c7d972?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-01
fetch_date: 2025-10-04T00:11:35.300545
---

# Unique Rate limit bypass worth 1800$

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6e2947c7d972&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funique-rate-limit-bypass-worth-1800-6e2947c7d972&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funique-rate-limit-bypass-worth-1800-6e2947c7d972&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6e2947c7d972---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6e2947c7d972---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Unique Rate limit bypass worth 1800$

[![Manav Bankatwala](https://miro.medium.com/v2/resize:fill:64:64/1*lKKgns5f3pH7FpGgLfe27A@2x.jpeg)](https://medium.com/%40manavbankatwala29?source=post_page---byline--6e2947c7d972---------------------------------------)

[Manav Bankatwala](https://medium.com/%40manavbankatwala29?source=post_page---byline--6e2947c7d972---------------------------------------)

3 min read

·

Nov 27, 2022

--

10

Listen

Share

Hello people,

While this is my first writeup on one of my finding of bypassing Rate limit to which I was awarded 1800$. Keeping it straight and simple, Here it goes.

Since few months, I have been trying to focus on rate limits and their security mechanism. I have read lots of write-ups of bypassing rate limits and gathered all of the methodologies in my checklist.

So I got this target one day which states that rate limit is out of scope with a note that they are completely secured from any type of rate limits on any endpoint. I decided to give a try on bypassing it even if it was out of scope just to prove the company statement wrong.

## **How they implemented rate limit security mechanism?**

On any of their endpoint, there were 2 things responsible for preventing rate limit attacks.

1. X-Recaptcha-Token header
2. X-Security-Token header

Press enter or click to view image in full size

![]()

So, this X-Recaptcha-Token header consists of the **captcha token** and X-Security-Token consists of a long value, every time a new request is made, value for both of this parameter changes. So probably, we can’t even send same request more than 1 time. So if I removed the “X-Recaptcha-Token”, It showed an error that “captcha token invalid or not found”. This is how they implemented a strong rate limit security mechanism.

## **How I was able to bypass it?**

After reviewing some responses, I found that there is a header “X-Disbaled-Recaptcha: 0”. I immediately removed the previous header from request and added this “X-Disabled-Recaptcha” header with value “1”. On sending this request instead of getting an error that “Recaptcha token is invalid or not found”, it showed a different error stating “Security token is invalid or alread used.” YES, you guessed it right. We were able to bypass the recaptcha token mechanism but still the **security token** was preventing and I tried every method to bypass the security token check but nothing worked. So I just though that it is not vulnerable and there’s no way to bypass this mechanism.

After few days, again I opened up that burp file and started to observe all the endpoints. To my surprise I found an endpoint which was responsible for generation of that “Security Token” and there was no rate limit mechanism only to that particular endpoint. Now, the normal behaviour of security tokens should be that as soon as new token is generated, the old one should be expired immediately even if it is **unused**. To my surprise I manually copied 10 security tokens and sent the request with header “X-Disabled-Recaptcha: 1”. All of the requests went successfull. YES!! That’s it. We bypassed the mechanism.

## **How I exploited it?**

I created a simple script to create 1000 unique security tokens using the previously found endpoint.

Press enter or click to view image in full size

![]()

Imported this token into intruder. Added the header “X-Disabled-Recaptcha: 0” and started the attack.

Press enter or click to view image in full size

![]()

And we bypassed it on each and every endpoint.

At last, I told them that I was able to bypass their mechanism on all of their endpoints making their bold statement **wrong** to which they rewarded me 1800$ even if it was out of scope.

That’s it guys, I will surely write about some of my unique findings.

Share it guys, will share something amazing soon.

## **Follow me on:**

<https://www.linkedin.com/in/manavbankatwala/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6e2947c7d972---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----6e2947c7d972---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----6e2947c7d972---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----6e2947c7d972---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----6e2947c7d972---------------------------------------)

--

--

10

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6e2947c7d972---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6e2947c7d972---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6e2947c7d972---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6e2947c7d972---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--6e2947c7d972---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Manav Bankatwala](https://miro.medium.com/v2/resize:fill:96:96/1*lKKgns5f3pH7FpGgLfe27A@2x.jpeg)](https://medium.com/%40manavbankatwala29?source=post_page---post_author_info--6e2947c7d972----------------------...