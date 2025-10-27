---
title: How I got my first $13500 bounty through Parameter Polluting (HPP)
url: https://infosecwriteups.com/how-i-got-my-first-13500-bounty-through-parameter-polluting-hpp-179666b8e8bb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-11
fetch_date: 2025-10-06T18:02:21.534842
---

# How I got my first $13500 bounty through Parameter Polluting (HPP)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F179666b8e8bb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-first-13500-bounty-through-parameter-polluting-hpp-179666b8e8bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-first-13500-bounty-through-parameter-polluting-hpp-179666b8e8bb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-179666b8e8bb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-179666b8e8bb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I got my first $13500 bounty through Parameter Polluting (HPP)

[![rAmpancist](https://miro.medium.com/v2/resize:fill:64:64/1*InjMQvPB8gvZW03UiL4VLQ.png)](https://rampancist.medium.com/?source=post_page---byline--179666b8e8bb---------------------------------------)

[rAmpancist](https://rampancist.medium.com/?source=post_page---byline--179666b8e8bb---------------------------------------)

3 min read

·

Aug 10, 2024

--

2

Listen

Share

Press enter or click to view image in full size

![]()

From Invicti

Hey, Its rAmpancist and I’m thrilled to have you join me for this post.

This write-up is about 2 IDORs and an XSS I found on a housing website. However what led me into these bugs is the point of this article.

The structure revolved around a main website which you had to create your account on, which had different privilege levels based on what you actually want to do, and then a second website which was a subdomain of the main website and included a sub-service which functioned getting help from main website.

In main website, you could’ve been a host or a customer. In this sub-service you could’ve used different functionalities depending on whether your main account is a host or a customer.

Press enter or click to view image in full size

![]()

Registration form

The registration form looked like something like this. You chose whether your main account is host or not, and then enter your ID, which then required the website to prompt a check to see whether ID is valid and retrieve information. Wonderfully enough though, the hosting section completely malfunctioned. Like no matter how valid your hosting ID was, the service told you its invalid or couldn’t retrieve information.

That’s when I knew, no hunter has successfully created a host account, and whatever lies behind, is mine.

The registration body looked something like this if you selected that you are a host:

```
IsHost=1&HostId=123&Email=test%40test.com
```

And this if you selected you are a customer:

```
IsHost=0&Email=test%40test.com
```

It wouldn’t supply a `HostId` if you selected that you’re non-host…

The way it functioned was funny :

If `HostId` exists and `IsHost=1` -> search for `hostID` and fail

If `HostId` doesn’t exist and `IsHost=0` -> user is customer and proceed

If `HostId` exists and `IsHost`=0 -> user is host but don’t search for hostID (!!!?)

That precisely means that it determined whether or not you are a host by checking if you supplied any `HostID` but processed the check only if you selected that `isHost=1` , which is a flaw and lets you create invalid host accounts.

That way I unlocked 4 features and I immediately knew they have bugs.

One of them was a form submission. The form contained confidential user both inputted directly from user and retrieved from the main website (makes the information critical).

When you submitted a form you were granted a 3 character unique ID on the URL that opened your form. Easiest way possible, the ID was public and had no protection.

This is public IDOR which means 2 things:

1- You can see other people’s stuff (of course)

2- You can achieve reflected XSS if you find an XSS on the form and pass the URL to victim

Now you might ask, well were any of the inputs not properly sanitized and vulnerable? The answer is no, they were all fine.

However this is where I chain my **OTHER** finding! Previously I found that the field name is vulnerable to XSS, but the sad thing was that my name was entirely private and only I could see it, so self-XSS.

However now we suddenly leveraged self-XSS to a reflected one, thanks to the IDOR! Since my name gets reflected in the form and outputted in the 3 character page.

So we have 2 bugs now. Ones IDOR leading to heavy leakage (Critical, Due to information being retrieved from main website) and XSS (Medium, sadly, It was not elevate-able, trust me).

Now the last one, the form contained a file upload. The file upload itself gave you **Another** link to the file which was separate from main form and was vulnerable by itself, as you could’ve seen other files.

Main IDOR $12000, File IDOR $1000, XSS $500.

I hope you’ve enjoyed reading my article.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----179666b8e8bb---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----179666b8e8bb---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----179666b8e8bb---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----179666b8e8bb---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----179666b8e8bb---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--179666b8e8bb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--179666b8e8bb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--179666b8e8bb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--179666b8e8bb---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--179666b8e8bb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter fo...