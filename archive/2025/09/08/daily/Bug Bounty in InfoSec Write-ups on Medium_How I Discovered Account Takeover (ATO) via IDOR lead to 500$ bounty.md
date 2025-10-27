---
title: How I Discovered Account Takeover (ATO) via IDOR lead to 500$ bounty
url: https://infosecwriteups.com/how-i-discovered-account-takeover-ato-via-idor-lead-to-500-bounty-537bc7ff10b8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-08
fetch_date: 2025-10-02T19:48:30.611213
---

# How I Discovered Account Takeover (ATO) via IDOR lead to 500$ bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F537bc7ff10b8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-account-takeover-ato-via-idor-lead-to-500-bounty-537bc7ff10b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-discovered-account-takeover-ato-via-idor-lead-to-500-bounty-537bc7ff10b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-537bc7ff10b8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-537bc7ff10b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Discovered Account Takeover (ATO) via IDOR lead to 500$ bounty

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--537bc7ff10b8---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--537bc7ff10b8---------------------------------------)

3 min read

·

Sep 7, 2025

--

8

Listen

Share

Hello Everyone,

Today, I want to share my experience of discovering an account takeover (ATO) vulnerability through IDOR. Let’s dive right in!

So, hunting starts with a random program selection let call it `example.xyz`

I started hunting with enumerating subdomain and checking if there is any possible subdomain takeover but there is nothing found.

I use my waybackurls to grab previous url’s from the `example.xyz`and started hunting manually. I visited the signup page and started the registration process while the burp suite is on backend I register myself with Just confirming my mail and phone number While I notice a `POST` is sent to server with my mail and the following information with zero Authentication Header or cookies just like I am not logged in

```
{
  "id": "67274f46-b5d8-4826-bf29-d1584a195cfa",
  "email": "jeetpal2007@gmail.com",
  "phase": "phone_number",
  "country_code": "91",
  "phone_number": "123456789",
  "verification_id": "46ab8b35-0722-4652-a76c-e3c3b2642df0"
}
```

Then I created my second account and took the ID from that particular account and changed the field of the ID parameter in request to second account. After verifying a valid mail and number, I got surprised the server accept other number and mail without verification. the server validates the information without checking it. so, I just change the Email and phone of second user to my own and here the tricks come. I just go to forget password page and enter mail verify the mail got you to set new password. I just created that but after that there is a phone verification which also bypass since the server is not validating the phone number while change from request I go OTP too on my phone.

Press enter or click to view image in full size

![]()

So, I just reported the Issue after 5 Days I got the reply from the team a bounty for Low

Press enter or click to view image in full size

![]()

I asked the reason for Low for a zero click they said

Press enter or click to view image in full size

![]()

Thank you for reading if you enjoy it clap 50 times

New articles Dropping soon

**Connect with me**
**Linkedin**: <https://www.linkedin.com/in/jeet-pal-22601a290/>
**Instagram:** <https://www.instagram.com/jeetpal.2007/>
**X/Twitter:** <https://x.com/Mr_mars_hacker>

## And here’s something special for you! 🚨

Join a community of **2,800+ security researchers** on our **Discord server**, where we discuss **Web3 vulnerabilities, audits, and much more!** 🚀
👉 **Join the server here!:** <https://discord.gg/Y467qAFM4X>

Note: I just republish it with more information to share

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----537bc7ff10b8---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----537bc7ff10b8---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----537bc7ff10b8---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----537bc7ff10b8---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----537bc7ff10b8---------------------------------------)

--

--

8

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--537bc7ff10b8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--537bc7ff10b8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--537bc7ff10b8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--537bc7ff10b8---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--537bc7ff10b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--537bc7ff10b8---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*WCsSJbdkMUH6Kkj_7j8Ewg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--537bc7ff10b8---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_page---post_author_info--537bc7ff10b8---------------------------------------)

[2.3K followers](https://jeetpal2007.medium.com/followers?source=post_page---post_author_info--537bc7ff10b8---------------------------------------)

·[3 following](https://medium.com/%40jeetpal2007/following?source=post_page---post_author_info--537bc7ff10b8---------------------------------------)

A security researcher,Auditor Web3 & Developer Connect me on social media via <https://linktr.ee/jeetpal2007> query:jeetpal2007@gmail.com...