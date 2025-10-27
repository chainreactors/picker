---
title: Google did an Oopsie: a simple IDOR worth $3,133.7
url: https://infosecwriteups.com/google-did-an-oopsie-a-simple-idor-worth-3-133-7-2abefaef954d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-05
fetch_date: 2025-10-06T20:34:46.057083
---

# Google did an Oopsie: a simple IDOR worth $3,133.7

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2abefaef954d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-did-an-oopsie-a-simple-idor-worth-3-133-7-2abefaef954d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-did-an-oopsie-a-simple-idor-worth-3-133-7-2abefaef954d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2abefaef954d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2abefaef954d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Google did an Oopsie: a simple IDOR worth $3,133.7

[![accalon](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*lfD_53qb6RrBvvrBiDyOYQ.gif)](https://medium.com/%40accalon?source=post_page---byline--2abefaef954d---------------------------------------)

[accalon](https://medium.com/%40accalon?source=post_page---byline--2abefaef954d---------------------------------------)

4 min read

·

Feb 3, 2025

--

5

Listen

Share

***Tl;dr****: Sometimes the bounty is hidden in plain sight — a simple IDOR by changing the Google Drive file ID. Blocked by login/pay wall? Read for free here : (*<https://c2a.github.io/simple-idor-on-google>*)*

…

***Pssst****…. I am now part of* [***SysBraykr***](https://sysbraykr.com)*, an offensive security company from Asia. Go check out our website if you want to meet a bunch of interesting people in the cybersecurity field (like me! :)).*

…

Back in 2019, when I had just started learning about hacking and bug bounty hunting, I had this dream of being in Google’s Hall of Fame.

I mean, their products are everywhere — billions of people use them every day — so I thought it would be awesome to be one of the recognized people who helped make it safer for everyone. Back then, there weren’t that many people doing it.

So, I randomly chose one of their products and started hunting. As expected, it wasn’t that easy. Days went by, and nothing came up. I started to think maybe I wasn’t ready for this and should go for an easier target. But then, I decided to switch to a considerably less famous product of Google : ***REDACTED.google.com***.

After reading their documentation on *developer.google.com* to understand the functionality, I began my hunt. On one occasion, I actually found an XSS vulnerability, but it triggered on a properly sandboxed domain (*\*.googleusercontent.com*), which is intended behavior and not a valid bug according to [their rules](https://bughunters.google.com/learn/invalid-reports/web-platform/xss/6619189462433792/xss-in-sandbox-domains).

That was until I stumbled upon a feature where we could import a file from Google Drive (and it worked perfectly). When I intercepted the request using my lovely Community Edition Burp Suite, I noticed that it was using the drive file ID in the post parameter ***docId*** to identify which drive file we chose.

Press enter or click to view image in full size

![]()

I noticed that the ***docId*** is present in the Google Drive file URL, something like this:

*https://drive.google.com/open?id=****18TrUTt3SI3fmKNut8SREDACTED***

It returns a JSON response with a token and the title of the file we picked. I sent it to the repeater and started to play with the request. A crazy thought suddenly crossed my mind — *what if I used someone else’s file? A private one?*

![]()

hmm…

For those who don’t know, we can make a file private on Google Drive by changing the permission settings. If other people want to access it, they have to request access from the owner.

![]()

So, I created a private file on my other account and put the ID in the ***docId*** parameter. And surprisingly, it worked! The server returned a 200 response along with the token and file name, even though the requester shouldn’t have had access to the private file.

![]()

Press enter or click to view image in full size![]()

Did i just find an IDOR?

I reported this bug straight away. The next day, they triaged the report and escalated it from P4 all the way to P2. Two days later, I got the beloved “Nice Catch!” catchphrase.

Press enter or click to view image in full size

![]()

Nice Catch!

At that time, although the bounty decision was still in discussion, my name had already been carved into their “***Honorable Mention***” page (not ***Hall of Fame***, not yet). I honestly didn’t expect to get a bounty reward, considering this was a fairly simple, low-hanging fruit bug. I needed to know the file ID to exploit it, which is a fairly unique, long, random token, ***AND*** I could only go as far as knowing the file name and file type.

But I think they take security very seriously (*or maybe they found something worse internally — who knows ¯\_(ツ)\_/¯*). Because, surprisingly, three weeks later, I got an update saying my report was worth $3,133.70. Damn, they’re crazy (in a good way, of course ❤).

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Timeline:

* ***September 8, 2019***: Vulnerability reported.
* ***September 9, 2019***: Report triaged, escalated from P4 to P2.
* ***September 12, 2019***: Nice Catch!
* ***October 1, 2019***: Update regarding bounty, and they put my name on the Hall of Fame. Nice!
* ***November 14, 2019***: $$$$ paid.

[Idor](https://medium.com/tag/idor?source=post_page-----2abefaef954d---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----2abefaef954d---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----2abefaef954d---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2abefaef954d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2abefaef954d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2abefaef954d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2abefaef954d---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=...