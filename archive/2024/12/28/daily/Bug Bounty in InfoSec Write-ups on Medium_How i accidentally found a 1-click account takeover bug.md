---
title: How i accidentally found a 1-click account takeover bug
url: https://infosecwriteups.com/how-i-accidentally-found-a-1-click-account-takeover-bug-dd27a512dd22?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-28
fetch_date: 2025-10-06T19:37:09.402080
---

# How i accidentally found a 1-click account takeover bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdd27a512dd22&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-accidentally-found-a-1-click-account-takeover-bug-dd27a512dd22&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-accidentally-found-a-1-click-account-takeover-bug-dd27a512dd22&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dd27a512dd22---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dd27a512dd22---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Press enter or click to view image in full size

![]()

# How i accidentally found a 1-click account takeover bug

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--dd27a512dd22---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--dd27a512dd22---------------------------------------)

3 min read

·

Dec 27, 2024

--

5

Listen

Share

**Hello!**
I hope you’re doing well. Today, I want to share how I accidentally discovered a **1-Click Account Takeover Bug** on a self-hosted platform **redacted.com(That’s not the actual name)**. Alhamdulillah, the issue was eventually fixed, but unfortunately, I never received any feedback or acknowledgment from them. This is one of the downsides of hunting vulnerabilities on self-hosted platforms.

While testing, I signed into **redacted.com** on two devices: my laptop and my phone (using two different accounts). On my laptop, I initiated an email change request. The verification link was sent to my email, which I then opened on my phone.

Initially, I noticed my email had been changed but didn’t pay much attention because I was confused about what was happening. It wasn’t until later that I decided to test the **email change logic** more thoroughly.

I discovered a **critical vulnerability**: a user could change another user’s email address without knowing their password, potentially leading to a full account takeover.

## Steps to Reproduce the Vulnerability:

1. **Request Email Change**: User A (Gaza) initiates a request to change their account email.
2. **Receive Verification Link**: User A receives an email with a verification link to confirm the email change.
3. **Share Link with Another User**: User A shares the verification link with User B (Test), who is logged in on a separate browser session.
4. **User B Clicks the Link**: User B clicks the link, triggering the email change action. However, the system updates User B’s email address instead of User A’s.
5. **Log In Using New Email**: User A now logs in using the updated email address and selects “Forgot Password.”
6. **Reset Password**: A password reset link is sent to the new email address (controlled by User A).
7. **Account Takeover**: User A resets the password and gains full control of User B’s account.

## Impact

This vulnerability allows a malicious user to hijack another user’s account by manipulating the email change verification process. The attacker can gain full access to the victim’s account, potentially leading to data theft, identity fraud, and unauthorized access to sensitive information.

About a week and a few days later, I noticed the issue had been fixed. I waited a while before reaching out to them, but I received no response.

Here’s my perspective on why I didn’t get a response:

> **Another Hunter Reported It First**: This could explain why I didn’t get feedback, though I’m not entirely convinced.

I have a PoC video demonstrating the vulnerability. However, it contains my personal email and i’m yet to recieve a response from the team, so I cannot share it directly.

I hope you learned something from this write-up! Thank you for reading till the end. If you found it helpful, please show your support by clapping for this write-up.

> For any suggestions or Correction, Kindly reach out to me:
>
> Twitter — [callgh0st](https://twitter.com/callgh0st)

> Zohar Chamberlain Regev:
>
> [As an Israeli citizen I am deeply concerned about the violence my government is using to oppress and destroy your lives. I know that most Israelis don’t even think about the Palestinians, especially those living in the Gaza Strip as fellow human beings. The bombs when they fall on you are terrible, but the slow death with no future under continued blockade and decades long repressive occupation is much worse. I wish you strength and look forward to the day when your place as the people of this land will be fully restored.](https://aztheatre.org.uk/messages-of-love-and-support-to-the-people-of-gaza-12-may-13-may-2021/#:~:text=Zohar%20Chamberlain%20Regev,be%20fully%20restored.)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----dd27a512dd22---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----dd27a512dd22---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----dd27a512dd22---------------------------------------)

[Gaza](https://medium.com/tag/gaza?source=post_page-----dd27a512dd22---------------------------------------)

[Transparency](https://medium.com/tag/transparency?source=post_page-----dd27a512dd22---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dd27a512dd22---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dd27a512dd22---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dd27a512dd22---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dd27a512dd22---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--dd27a512dd22---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging fro...