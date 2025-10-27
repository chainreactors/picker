---
title: You Can Still Use a Pager in 2022
url: https://debugger.medium.com/howto-using-a-pager-in-the-21st-century-6a57454ecde8
source: Over Security - Cybersecurity news aggregator
date: 2023-01-23
fetch_date: 2025-10-04T04:36:10.995566
---

# You Can Still Use a Pager in 2022

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6a57454ecde8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdebugger.medium.com%2Fhowto-using-a-pager-in-the-21st-century-6a57454ecde8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdebugger.medium.com%2Fhowto-using-a-pager-in-the-21st-century-6a57454ecde8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Debugger](https://debugger.medium.com/?source=post_page---publication_nav-193b68bd4fba-6a57454ecde8---------------------------------------)

·

[![Debugger](https://miro.medium.com/v2/resize:fill:76:76/1*p88dLF6W89KEG54e8BGG4A.png)](https://debugger.medium.com/?source=post_page---post_publication_sidebar-193b68bd4fba-6a57454ecde8---------------------------------------)

Debugger is a former publication from Medium about consumer technology and gadgets. Currently inactive and not taking submissions.

Member-only story

# You Can Still Use a Pager in 2025

## How a Raspberry Pi will help you resurrect this classic communications device

[![Dmitrii Eliuseev](https://miro.medium.com/v2/resize:fill:64:64/1*nHcZLMpYQYClk1OQRhfL1A.jpeg)](https://dmitryelj.medium.com/?source=post_page---byline--6a57454ecde8---------------------------------------)

[Dmitrii Eliuseev](https://dmitryelj.medium.com/?source=post_page---byline--6a57454ecde8---------------------------------------)

12 min read

·

May 2, 2021

--

8

Share

Press enter or click to view image in full size

![]()

Pagers were popular many years ago, and some people may still have one at home. Is it possible to test the pager now? Absolutely, and I will show you how to do it.

Let’s get started.

## POCSAG — The Messaging Protocol

In the 90s, I was a student, and the pager for me was something like a Star Trek Communicator, a piece of cutting-edge technology. It is fun to remember it because now I know that, technologically, the paging protocol is straightforward. From the encoding perspective, the pager is not too different from the wireless doorbells that are available for 5$ in Aliexpress.

Let’s say we want to send the message “TEST” to the number “1234”. The message in a binary form will look something like this:

```
10101010101010101010101010101010 - Preamble
01111100110100100001010111011000 - Frame Synchronization Code
01111010100010011100000110010111 - Idle codeword
00000000000100110101111000111111 - Address + Function Bits + CRC
10010101101000111001001111111100 - T E S (7 bit/symbol)
11001010100000000000001111100011 - T . .
01111010100010011100000110010111 - Idle codeword
```

--

--

8

[![Debugger](https://miro.medium.com/v2/resize:fill:96:96/1*p88dLF6W89KEG54e8BGG4A.png)](https://debugger.medium.com/?source=post_page---post_publication_info--6a57454ecde8---------------------------------------)

[![Debugger](https://miro.medium.com/v2/resize:fill:128:128/1*p88dLF6W89KEG54e8BGG4A.png)](https://debugger.medium.com/?source=post_page---post_publication_info--6a57454ecde8---------------------------------------)

[## Published in Debugger](https://debugger.medium.com/?source=post_page---post_publication_info--6a57454ecde8---------------------------------------)

[17.6K followers](/followers?source=post_page---post_publication_info--6a57454ecde8---------------------------------------)

·[Last published Apr 19, 2022](/the-2022-apple-watch-probably-wont-measure-blood-pressure-and-that-s-a-good-thing-be248961a5ca?source=post_page---post_publication_info--6a57454ecde8---------------------------------------)

Debugger is a former publication from Medium about consumer technology and gadgets. Currently inactive and not taking submissions.

[![Dmitrii Eliuseev](https://miro.medium.com/v2/resize:fill:96:96/1*nHcZLMpYQYClk1OQRhfL1A.jpeg)](https://dmitryelj.medium.com/?source=post_page---post_author_info--6a57454ecde8---------------------------------------)

[![Dmitrii Eliuseev](https://miro.medium.com/v2/resize:fill:128:128/1*nHcZLMpYQYClk1OQRhfL1A.jpeg)](https://dmitryelj.medium.com/?source=post_page---post_author_info--6a57454ecde8---------------------------------------)

[## Written by Dmitrii Eliuseev](https://dmitryelj.medium.com/?source=post_page---post_author_info--6a57454ecde8---------------------------------------)

[4.3K followers](https://dmitryelj.medium.com/followers?source=post_page---post_author_info--6a57454ecde8---------------------------------------)

·[10 following](https://medium.com/%40dmitryelj/following?source=post_page---post_author_info--6a57454ecde8---------------------------------------)

Python/IoT developer and data engineer, data science and electronics enthusiast

## Responses (8)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6a57454ecde8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6a57454ecde8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6a57454ecde8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6a57454ecde8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6a57454ecde8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6a57454ecde8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6a57454ecde8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6a57454ecde8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6a57454ecde8---------------------------------------)