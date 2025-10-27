---
title: Would you mind to tell me what your bank balance is? No? Okay, I’ll hack it.
url: https://infosecwriteups.com/would-you-mind-to-tell-me-what-your-bank-balance-is-no-okay-ill-hack-it-b3f49810cfe2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-11
fetch_date: 2025-10-06T18:26:40.428782
---

# Would you mind to tell me what your bank balance is? No? Okay, I’ll hack it.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb3f49810cfe2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwould-you-mind-to-tell-me-what-your-bank-balance-is-no-okay-ill-hack-it-b3f49810cfe2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwould-you-mind-to-tell-me-what-your-bank-balance-is-no-okay-ill-hack-it-b3f49810cfe2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b3f49810cfe2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b3f49810cfe2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Would you mind to tell me what your bank balance is? No? Okay, I’ll hack it.

[![Manav Bankatwala](https://miro.medium.com/v2/resize:fill:64:64/1*lKKgns5f3pH7FpGgLfe27A@2x.jpeg)](https://medium.com/%40manavbankatwala29?source=post_page---byline--b3f49810cfe2---------------------------------------)

[Manav Bankatwala](https://medium.com/%40manavbankatwala29?source=post_page---byline--b3f49810cfe2---------------------------------------)

3 min read

·

Sep 10, 2024

--

7

Listen

Share

IDOR x Bank = Exposed bank balance.

Alright people, let’s do this one last time.

I’m Manav Bankatwala, and I’m a security researcher. I’m not sure what kind of radioactive spider bit me, but it gave me the power to see security vulnerabilities everywhere.

## Summary:

The vulnerability I am describing in this writeup is quite old, which I found way back when I was active in bug bounty. Imagine you are asking for money back from your friend, and he/she says, I am broke. But you found out that he/she is lying because you can hack into and see the actual bank balance of your friend. Ahaa, you got him.

It’s a very simple vulnerability, but due to the impact I feel to write about it. So, the vulnerability here we are talking about is an IDOR ([Insecure Direct Object Reference](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)). I found this vulnerability in one of India’s fastest-growing digital banks. With this IDOR, I was able to see the actual **bank balance** of any user using their bank account number. Yes, you heard that right. Maybe I saw your bank balance? Haha😉

## Background:

So, every month I download my bank statements to see the expenses and manage them. One afternoon, after hunting on a bug bounty program, I thought to log into my bank account and download my statement. But after completing the whole statement download thing, I realized that I forgot to turn off the interception proxy. Due to this, all the requests were captured. I thought to just let it go, but it made me curious and think if I could find any security vulnerability, and I did find it.

## Methodology:

I didn’t want to do much aggressive testing and things like that, so just to keep it simple, I decided to look for IDORs in all the API requests that have account numbers as a parameter.

1. Opened the burp suite search tab.
2. I entered my own account number, which gave me a list of endpoints where my account number was provided as a parameter.
3. Out of all, I found an API endpoint at **/api/account/v1/m-balance.**
4. It was a post request, and the JSON body was having my account number.

Press enter or click to view image in full size

![]()

Request

5. I sent this request to repeater and changed the last two digits of my account number. Upon sending, instead of an error, it gave me the balance of another user bank account number.

Press enter or click to view image in full size

![]()

Response

To further test this, I simply sent the request to the intruder and iterated a list of bank account numbers. And ya, I got the bank balance of all the users with just one click. Without wasting time, I made a report and submitted it to the authorities.

But guess what? Banks don’t think that account balance is a sensitive thing to get exposed to. The replied, “***Through an API, an authenticated user can only enumerate the balance of an account number; no other customer details are exposed through an API. After analyzing the issue, we have categorized it as of ‘Low’ severity.”***

## Conclusion:

Do you think that bank balance exposure is really not a concern? It’s like posting your bank balance on a notice board. Are you okay if your bank balance is listed on that notice board where anyone can see it? Let me know what are your views on this and in what more this could have been exploited. Until that, adiós

## Follow me to get latest updates:

<https://www.linkedin.com/in/manavbankatwala/>

<https://www.instagram.com/manav.bug/>

<https://twitter.com/manavbankatwala>

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----b3f49810cfe2---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b3f49810cfe2---------------------------------------)

[Idor](https://medium.com/tag/idor?source=post_page-----b3f49810cfe2---------------------------------------)

[Bank Hack](https://medium.com/tag/bank-hack?source=post_page-----b3f49810cfe2---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----b3f49810cfe2---------------------------------------)

--

--

7

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b3f49810cfe2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b3f49810cfe2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b3f49810cfe2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b3f49810cfe2---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b3f49810cfe2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Manav Bankatwala](https://miro.medium.com/v2/resiz...