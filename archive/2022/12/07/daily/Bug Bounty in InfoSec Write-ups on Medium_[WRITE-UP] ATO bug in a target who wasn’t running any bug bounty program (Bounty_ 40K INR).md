---
title: [WRITE-UP] ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)
url: https://infosecwriteups.com/my-first-bug-bounty-write-up-about-my-first-valid-finding-a-very-simple-ato-bug-in-a-target-who-1b8259f531d6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:40.233422
---

# [WRITE-UP] ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1b8259f531d6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-bug-bounty-write-up-about-my-first-valid-finding-a-very-simple-ato-bug-in-a-target-who-1b8259f531d6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-first-bug-bounty-write-up-about-my-first-valid-finding-a-very-simple-ato-bug-in-a-target-who-1b8259f531d6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1b8259f531d6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1b8259f531d6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# My first bug bounty write-up about my first valid finding | A very simple ATO bug in a target who wasn’t running any bug bounty program (Bounty: 40K INR)

## It’s my first bug bounty write-up about my first valid bug which could have allowed a malicious user to take over any account on that target site

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:64:64/1*YJZ3Ns7NJ_u8GA9ad3G3-A.png)](https://theshubh77.medium.com/?source=post_page---byline--1b8259f531d6---------------------------------------)

[Shubham Bhamare](https://theshubh77.medium.com/?source=post_page---byline--1b8259f531d6---------------------------------------)

3 min read

·

Dec 25, 2020

--

2

Listen

Share

Press enter or click to view image in full size

![]()

Hi guys, I’m **Shubham Bhamare** from Maharashtra, India. It’s my first bug bounty write-up about my first valid bug which could have allowed a malicious user to take over any account on that target site.

So let's start! 👉

===

**Target:**

As I can’t disclose the name of the company, let’s call it “Target”. While using their website, I found that there should be something unintended.

But unfortunately, they weren’t running any bug bounty program. But due to the severity of this bug and the vast number of their users, I decided to contact them via email and ask them whether they’re running any bug bounty program or not. TBH, I just wanted to bring this issue to their attention, didn’t expect any reward from them. Just wanted to get this bug fixed as I also was a user of their service(s).

So the next day, they replied that they're not running any bug bounty program currently but can give a bounty based on the severity of a bug.

So with their consent, I proceed further.

===

**Setup:**

2 accounts of that target i.e. Attacker and Victim.

===

**Reproduction steps/scenario:**

1) Target has a login option. Users can log in with both by entering a password or OTP.

2) Assume that the attacker and victim have created their accounts on that target.

3) Now from the attacker's perspective, try to login to the victim's account with OTP by entering the victim's phone or username.

4) A 6-digit code will be sent to the victim.

5) After 60 seconds, click the 'Resend' button and capture the request.

6) Modify the *"phone"* parameter with the attacker's phone (where the attacker can receive messages).

7) Forward the request.

8) Now the attacker will receive the OTP and after entering it, he'll successfully log in to the victim's account.

![]()

My reaction that time 😂

> **Here, the target wasn't authenticating the phone number while resending OTPs.**

===

**Bypass:**

When the team fixed this issue, I found another similar vector that also could be abused.

It was asking OTP if the user requested to delete the account. So this endpoint was also vulnerable.

===

**Bounty:**

40K INR for both bugs.

===

**Takeaway(s):**

1) Although the company doesn't have a bug bounty program and you believe that there's something unintended in their infrastructure that should be fixed, contact them for their consent to test it further. Because securing something from bad guys is always a good practice.

2) Don't hunt on that programs/features where everyone's hunting already. Find your own programs/hidden features/techniques.

3) Always try to find a bypass.

===

Thank you for reading! Also, I’m going to publish all my [**Facebook bug bounty** **write-ups**](https://theshubh77.medium.com/list/cyber-security-61eba2e38485) very soon. So don’t forget to follow me on [**Medium**](http://medium.com/%40theshubh77). 😊

===

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----1b8259f531d6---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----1b8259f531d6---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----1b8259f531d6---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----1b8259f531d6---------------------------------------)

[Facebook Bug Bounty](https://medium.com/tag/facebook-bug-bounty?source=post_page-----1b8259f531d6---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1b8259f531d6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--1b8259f531d6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--1b8259f531d6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--1b8259f531d6---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--1b8259f531d6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Shubham Bhamare](https://miro.medium.com/v2/resize:fill:...