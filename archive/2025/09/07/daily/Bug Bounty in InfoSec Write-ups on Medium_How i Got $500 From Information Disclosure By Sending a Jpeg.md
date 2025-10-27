---
title: How i Got $500 From Information Disclosure By Sending a Jpeg
url: https://infosecwriteups.com/how-i-got-500-from-information-disclosure-by-sending-a-jpeg-e273d1b94da1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-07
fetch_date: 2025-10-02T19:47:19.694630
---

# How i Got $500 From Information Disclosure By Sending a Jpeg

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe273d1b94da1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-500-from-information-disclosure-by-sending-a-jpeg-e273d1b94da1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-500-from-information-disclosure-by-sending-a-jpeg-e273d1b94da1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e273d1b94da1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e273d1b94da1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How i Got $500 From Information Disclosure By Sending a Jpeg🔥

## Information Disclosure by Sending a Jpeg To Leak (IP Address , OS Version, Country, User-Agent, Time Zone)

[![Mado](https://miro.medium.com/v2/resize:fill:64:64/1*sG60faGcA69B4sDGL06HVg.png)](https://medium.com/%400xMado-1Tap?source=post_page---byline--e273d1b94da1---------------------------------------)

[Mado](https://medium.com/%400xMado-1Tap?source=post_page---byline--e273d1b94da1---------------------------------------)

3 min read

·

Sep 5, 2025

--

4

Listen

Share

Press enter or click to view image in full size

![]()

الحمد لله والصلاة والسلام على رسول الله وعلى آله وصحبه أما بعد

Hello Hacker

### I’m Mohamed also known as Mado, a dedicated security researcher and bug hunter

> NOTE: **The target is an external application with a disclosure program, but since I haven’t received official permission yet, I’m using** `target.com` **as a placeholder in this write-up**

## Target Overview

The target platform provides a **team workspace** where members can collaborate by creating and managing tasks. In addition, the platform offers a **built-in team chat feature** that allows users to communicate directly within the workspace

Press enter or click to view image in full size

![]()

## The Discovery

During my testing I focused on the **chat functionality** specifically the file upload feature since it allows users to share images and documents with other team members

While uploading an image I noticed that the request included a parameter called `file_url`This parameter pointed to the location of the uploaded image. Naturally I wondered: *what if I change this value to an external domain under my control*

Press enter or click to view image in full size

![]()

Original Request

I first tried replacing the URL with one of my own collaboration servers But it didn’t receive any requests To confirm the Bug I then used an IP-Logger which successfully captured

Press enter or click to view image in full size

![]()

Request After Change

**I also checked the server response to confirm whether the request returned a** `200 OK` **or a** `400 Bad Request`

Press enter or click to view image in full size

![]()

**After forwarding the request, the result was that the image showed an error when the chat was opened**

![]()

**Then I switched to the victim account opened the chat and went back to The IP logger Then BOOM**

Press enter or click to view image in full size

![]()

**I clicked on “More Info” to see more details about the victim**

Press enter or click to view image in full size

![]()

### MindSet:

Press enter or click to view image in full size

![]()

## Impact:

Black Hat Hackers can get critical information about all The Target users in Team The information obtained is very important for the privacy of the users and includes information such as IP address, OS version , city …

## The Result:

In the end I was able to prove that simply by uploading a modified JPEG in the team chat it was possible to trigger requests to an external server As a result I successfully collected sensitive information from other team members including their (**IP address, time zone, operating system version country and browser details (User-Agent)** all **without any user interaction)**

### Severity is : Medium To High

Press enter or click to view image in full size

![]()

Response From Traige

### If You Want To Reach Me All My Contact Info is Here: [Click Here](https://guns.lol/mado1)

……………Thank You For Reading And I hope This Was helpful………………

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----e273d1b94da1---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----e273d1b94da1---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----e273d1b94da1---------------------------------------)

[Information Disclosure](https://medium.com/tag/information-disclosure?source=post_page-----e273d1b94da1---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----e273d1b94da1---------------------------------------)

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e273d1b94da1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e273d1b94da1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e273d1b94da1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e273d1b94da1---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--e273d1b94da1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Mado](https://miro.medium.com/v2/resize:fill:96:96/1*sG60faGcA69B4sDGL06HVg.png)](https://medium.com/%400xMado-1Tap?source=post_page---post_author_info--e273d1b94da1---------------------------------------)

[![Mado](https://miro.medium.com/v2/resize:fill:128:128/1*sG60faGcA69B4sDGL06HVg.png)](https://medium.com/%400xMado-1Tap?source=post_page---post_author_info--e273d1b94da1---------------------------------------)

[## Written by Mado](https://medium.com/%400xMado-1Tap?source=post_page---post_au...