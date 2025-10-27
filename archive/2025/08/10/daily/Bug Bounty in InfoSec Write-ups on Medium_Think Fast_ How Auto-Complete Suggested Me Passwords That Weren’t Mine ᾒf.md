---
title: Think Fast: How Auto-Complete Suggested Me Passwords That Weren’t Mine ᾒf
url: https://infosecwriteups.com/think-fast-how-auto-complete-suggested-me-passwords-that-werent-mine-%E1%BE%92f-d5c26ad34a3a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-10
fetch_date: 2025-10-07T00:17:47.274967
---

# Think Fast: How Auto-Complete Suggested Me Passwords That Weren’t Mine ᾒf

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd5c26ad34a3a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthink-fast-how-auto-complete-suggested-me-passwords-that-werent-mine-%25E1%25BE%2592f-d5c26ad34a3a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthink-fast-how-auto-complete-suggested-me-passwords-that-werent-mine-%25E1%25BE%2592f-d5c26ad34a3a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d5c26ad34a3a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d5c26ad34a3a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🧠 Think Fast: How Auto-Complete Suggested Me Passwords That Weren’t Mine 🔐

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--d5c26ad34a3a---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--d5c26ad34a3a---------------------------------------)

3 min read

·

Aug 8, 2025

--

1

Share

Free [link](https://medium.com/%40iski/think-fast-how-auto-complete-suggested-me-passwords-that-werent-mine-%E1%BE%92f-d5c26ad34a3a?sk=ed2b7a9dc95f1dd6630ac5345d1942e5) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Perplexity AI

> *\_”I just wanted to book a cab. Ended up almost unlocking someone else’s account. Thanks, autofill.”\_*

You ever sit at your desk with a plate of noodles, Netflix on the second monitor, and Burp Suite humming like it knows you’re about to hit paydirt? Yeah, that was me. One hand on the fork, the other CTRL+Shift+I-ing through a bug bounty target. Little did I know, a forgotten `<input>` field would cough up passwords like an over-sharer on truth serum.

Let’s dive into how one misconfigured form, a forgotten GraphQL endpoint, and a very talkative browser nearly handed me other users’ passwords on a silver platter.

[## 📸 Picture Perfect Exploit: How Image Uploads Turned Into Shell Access 🐚

### Hey there!😁

infosecwriteups.com](/picture-perfect-exploit-how-image-uploads-turned-into-shell-access-473659d49020?source=post_page-----d5c26ad34a3a---------------------------------------)

## 🚀 The Recon Rabbit Hole Begins

It all started with a pretty simple goal: mass recon.

I used a combo of tools like:

* **Subfinder** + **Amass** for subdomain enumeration
* **httpx** for probing alive hosts

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c26ad34a3a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c26ad34a3a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d5c26ad34a3a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d5c26ad34a3a---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--d5c26ad34a3a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d5c26ad34a3a---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--d5c26ad34a3a---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--d5c26ad34a3a---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--d5c26ad34a3a---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--d5c26ad34a3a---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d5c26ad34a3a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d5c26ad34a3a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d5c26ad34a3a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d5c26ad34a3a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d5c26ad34a3a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d5c26ad34a3a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d5c26ad34a3a---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d5c26ad34a3a---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d5c26ad34a3a---------------------------------------)