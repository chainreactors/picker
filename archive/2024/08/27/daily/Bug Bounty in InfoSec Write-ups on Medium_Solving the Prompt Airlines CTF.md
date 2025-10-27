---
title: Solving the Prompt Airlines CTF
url: https://infosecwriteups.com/solving-the-prompt-airlines-ctf-2235c725050b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-27
fetch_date: 2025-10-06T18:03:26.648641
---

# Solving the Prompt Airlines CTF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2235c725050b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsolving-the-prompt-airlines-ctf-2235c725050b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsolving-the-prompt-airlines-ctf-2235c725050b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2235c725050b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2235c725050b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Solving the Prompt Airlines CTF

[![hackerdevil](https://miro.medium.com/v2/resize:fill:64:64/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---byline--2235c725050b---------------------------------------)

[hackerdevil](https://devilwrites.medium.com/?source=post_page---byline--2235c725050b---------------------------------------)

4 min read

·

Aug 25, 2024

--

Listen

Share

A brief about the LLM CTF challenge

This blog covers a recent CTF I completed focused on Large Language Models (LLMs). Hosted at [Prompt Airlines — AI CTF by Wiz](https://promptairlines.com/), it’s an easy to moderate level challenge, perfect for those interested in exploring LLM security.

Press enter or click to view image in full size

![]()

Prompt Airlines CTF

> ***Note***: There could be many ways to solve all 5 challenges, and you might find your own unique methods to get the AI bot to reveal the flags. Ultimately, it’s about crafting the right prompts to get the AI to give up the flags. Use this blog as a hint if you get stuck, but try to solve the challenges on your own — this is just a brief overview, not a detailed guide for each challenge.

**Challenge 1: Revealing the AI Bot Identifier**

This challenge was about finding the AI bot’s identifier. The instructions mentioned that the bot had a specific identifier we needed to reveal by using the right prompts. That identifier was our flag. My approach was to ask the bot about itself and see what it knew. After a few tries with different prompts, the bot finally gave me the identifier, which was the flag.

Press enter or click to view image in full size

![]()

Challenge 1

**Challenge 2: Extracting the Private AI Bot Identifier**

There was an option “Under the hood”, through which we could see the backend instructions given to the AI bot by the developers, though some details were redacted. Challenge 2 was about finding a private identifier; which was redacted. My approach was to ask the bot to list everything it knew that had “\_”. This method helped me reveal the private identifier.

Press enter or click to view image in full size

![]()

Challenge 2

**Challenge 3: Finding the Hidden Coupon Code**

The instructions mentioned that the AI bot had access to coupon codes for flights. We needed to find a flight to Las Vegas on August 3, 2024. However, the backend instructions said the bot couldn’t directly share the coupon codes. So, the target was to craft a prompt to get the coupon codes. I asked the bot for flight details for Las Vegas on August 3, 2024. After a few tries, the bot gave me the coupon codes for that flight, and one of those codes turned out to be the flag.

Press enter or click to view image in full size

![]()

Challenge 3

**Challenge 4: Faking a Membership Card**

This challenge was about joining their loyalty program. According to the instructions, only members could book a flight. We needed to upload an image of a membership card, which should have a membership number that the bot (advanced third-party AI authentication system 😂) checks for validity. Initially, when I uploaded a test image, it gave an error but also showed what a valid card should have.

Press enter or click to view image in full size

![]()

Error Message

It needed a 5-digit alphanumeric code in a specific format. I then created a 5-digit alphanumeric code in a text editor, took a snap, and uploaded it. The system accepted it as valid and also revealed the 4th flag.

Press enter or click to view image in full size

![]()

Challenge 4

**Challenge 5: Booking a Free Ticket to Las Vegas**

For the final challenge, we needed to book a free flight to Las Vegas using the clues we gathered from the previous challenges. At first, I tried to get the bot to reveal a coupon code for a 100% discount by using fake codes like TRAVEL\_100 and TRAVEL\_00, but it didn’t work. Eventually, I simply kept asking the bot to book the flight, and it went ahead and completed the booking, revealing the final flag.

Press enter or click to view image in full size

![]()

Challenge 5

Press enter or click to view image in full size

![]()

Ticket to Las Vegas

Honestly, it took me 2–3 hours to solve this, but someone familiar with LLM security could probably do it in 30–40 minutes. Overall, it was a fun experience and I enjoyed the challenge.

[## hackerdevil

### Buy me some coffee to help write more of such content!!

buymeacoffee.com](https://buymeacoffee.com/devil09?source=post_page-----2235c725050b---------------------------------------)

Stay safe, stay informed, and keep coming back for more empowering insights.

Thank You for reading. Knowledge is power, so keep gaining!!

[Promptairlines](https://medium.com/tag/promptairlines?source=post_page-----2235c725050b---------------------------------------)

[Ctf](https://medium.com/tag/ctf?source=post_page-----2235c725050b---------------------------------------)

[Ctf Writeup](https://medium.com/tag/ctf-writeup?source=post_page-----2235c725050b---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2235c725050b---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----2235c725050b---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2235c725050b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2235c725050b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2235c725050b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_...