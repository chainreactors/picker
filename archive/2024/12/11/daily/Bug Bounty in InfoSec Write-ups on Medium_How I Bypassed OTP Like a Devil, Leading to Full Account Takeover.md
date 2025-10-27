---
title: How I Bypassed OTP Like a Devil, Leading to Full Account Takeover
url: https://infosecwriteups.com/how-i-bypassed-otp-like-a-devil-leading-to-full-account-takeover-7bb7a673f7a0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-11
fetch_date: 2025-10-06T19:39:28.853897
---

# How I Bypassed OTP Like a Devil, Leading to Full Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7bb7a673f7a0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-otp-like-a-devil-leading-to-full-account-takeover-7bb7a673f7a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-bypassed-otp-like-a-devil-leading-to-full-account-takeover-7bb7a673f7a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7bb7a673f7a0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7bb7a673f7a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Zero click account Takeover

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:64:64/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---byline--7bb7a673f7a0---------------------------------------)

[ZEROSEC](https://medium.com/%40Zeroo_sec?source=post_page---byline--7bb7a673f7a0---------------------------------------)

4 min read

·

Dec 10, 2024

--

3

Listen

Share

## Introduction:

Hello, hackers! Zero is back with another thrilling tale from my bug bounty adventures. This time, I went head-to-head with a seemingly impenetrable OTP system, only to uncover a devilishly simple bypass that led to a full account takeover. Sound exciting? Buckle up, because this story is a rollercoaster of curiosity, creativity, and responsible disclosure.

If you’re new to hacking, don’t worry — you’ll find this breakdown easy to follow and, hopefully, inspiring! Let’s dive in!

![]()

## How I Did It

The target site, let’s call it **radicated.com**, had a simple setup:

1. OTP-based login.
2. Email and password login.
3. Google login.

Now, when I saw the OTP login option, my inner hacker thought, *Can I bypass this and take over an account?* The challenge was on! Spoiler: **I pulled it off.** Here’s how it happened.

## Analyzing the OTP Request

After entering the OTP on the website, I intercepted the outgoing request. It looked something like this:

![]()

After submitting the wrong OTP, I intercepted the request and saw the server’s response. It simply said:

![]()

So, I decided to play around a bit — I intercepted the response and changed the status code to something like 200 OK. And guess what? Boom! NOTHING happened. Boo! It was a bit of a letdown, but hey, not every trick works on the first try!

![]()

So, I wasn’t ready to give up just yet. Instead of sulking, I thought, *“Let’s spice things up!”* I intercepted the response **again** — this time, I didn’t just tweak the status code; I decided to make some *bold moves* in the response body.

I changed the `"type"` field to `"REGISTER"`, hoping it might trigger something interesting. For a second, I felt like a mad scientist flipping random switches in a lab. *Would it work? Would it explode?* My heart was racing as I sent the modified response back to the server...

![]()

And guess what?
**BOOM!** It worked like a charm. By simply tweaking the response, I was able to **take over any account linked to a phone number**. Just like that, I could hijack anyone’s account and claim it as my own. **Hahaha!** It felt unreal — like holding the **master key to an entire digital kingdom**.

Press enter or click to view image in full size

![]()

Alright, let’s get into the juicy details!

Here’s what I actually did:
I intercepted the server’s response and decided to try something different. Instead of just messing around with the status code (like I did earlier), I made **two key changes**:

1. I changed the **response body’s** `type` **field** to `"REGISTER"`.
2. I updated the **status code** to `200 OK`.

![]()

## **Conclusion:**

And that, my fellow hackers, is how I bypassed OTP and pulled off a full account takeover. Sometimes, hacking is all about thinking outside the box and playing around with the smallest details. What may seem like an ordinary request can turn into an opportunity for full control with the right tweaks. Always remember, it’s not just about brute force, but about strategy, creativity, and testing every possible vulnerability.

So, keep learning, keep experimenting, and never forget to report responsibly. Happy hacking! Happy hunting!

**Follow me on** [***X***](https://x.com/ig_ftw) **and** [***LinkedIn***](https://www.linkedin.com/in/ranjan-yadav-82b28b249/)for more hacking adventures, tips, and tricks! Let’s stay connected and learn together. Stay curious, stay safe, and never stop hacking!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----7bb7a673f7a0---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----7bb7a673f7a0---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----7bb7a673f7a0---------------------------------------)

[Otp Bypass](https://medium.com/tag/otp-bypass?source=post_page-----7bb7a673f7a0---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----7bb7a673f7a0---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7bb7a673f7a0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7bb7a673f7a0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7bb7a673f7a0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7bb7a673f7a0---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--7bb7a673f7a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:96:96/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--7bb7a673f7a0---------------------------------------)

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:1...