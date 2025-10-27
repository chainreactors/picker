---
title: My Hall of Fame at United Nations Success Story
url: https://infosecwriteups.com/my-hall-of-fame-at-united-nations-success-story-97675232aed7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-02
fetch_date: 2025-10-03T21:31:30.735467
---

# My Hall of Fame at United Nations Success Story

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F97675232aed7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-hall-of-fame-at-united-nations-success-story-97675232aed7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmy-hall-of-fame-at-united-nations-success-story-97675232aed7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-97675232aed7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-97675232aed7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I got into United Nations Hall of Fame as an 18y/o Ethical Hacker!

[![Joshua Arulsamy](https://miro.medium.com/v2/resize:fill:64:64/1*7p4nlqZA0R7gWMFfGnQnCg.jpeg)](https://joshuaarulsamy.medium.com/?source=post_page---byline--97675232aed7---------------------------------------)

[Joshua Arulsamy](https://joshuaarulsamy.medium.com/?source=post_page---byline--97675232aed7---------------------------------------)

3 min read

·

Aug 27, 2022

--

Listen

Share

For anyone aspiring to build a career in cybersecurity, Hall of Fames play a major role, like anyone and everyone as a young aspiring ethical hacker it was my dream too and it was a surprise to me when it turned into a reality one day. Here is how I made my dream come true.

If you’re thinking Hall of Fame at United Nations is a great deal and it demands extraordinary skills to enter United Nations Hall of Fame! This is for you.

Press enter or click to view image in full size

![]()

Photo by [Jonathan Ansel Moy de Vitry](https://unsplash.com/%40jmdv?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Is it Hard to Enter United Nations HOF?

The simple answer is No.

If Entering United Nations is your goal it's not at all a great deal , go ahead and explore vulnerabilities like clickjacking which is very common in UN sites and try to increasing the severity of it and Report it to infosec@un.org , it’s just time consuming and not hard , But the real fun is doing something interesting and new that justifies your presence in the **Hall Of Fame** , Here is the Story of how I made it to United Nations Hall of Fame by Finding XSS in one of the UN owned subdomains .

Press enter or click to view image in full size

![]()

Photo by [Max Bender](https://unsplash.com/%40maxwbender?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/hacker?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

The core step in finding any vulnerability in any **domain** is **subdomain** enumeration, I personally use **amass,** **subfinder** and **sublist3r** you can use use any tool of your choice but combining the goodness of all these tools is a better idea so that you don’t miss any subdomain. If you’re an absolute beginner you can try online tools like [**DNSDumpster**](https://dnsdumpster.com/) , [**Virustotal**](https://www.virustotal.com/)or any such enumeration tool available online. On enumeration I got a lot of active subdomains, had been a while I guess something around 8000 subdomains. One domain caught my attention [**https://mdgs.un.org**](https://mdgs.un.org/query.asp) **,** I moved on to explore further and I tried brute forcing the directories.

Now I Found something amazing,

[**https://mdgs.un.org/query.asp**](https://mdgs.un.org/query.asp)

This gave me some hope that this has some juice in it!

I tried various XSS payloads on the search field there and finally one payload worked for me,

**Payload** : **x” onmouseover=alert(1) x=”**

After the successful execution of the payload, **I found an alert pop up each time the mouse cursor crosses the Search field.**

**It was a Reflected XSS!!!!!**

Press enter or click to view image in full size

![]()

Photo by [Fauzan Saari](https://unsplash.com/%40fznsr_?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/achivement?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

I reported the vulnerability to United Nations infosec@un.org , on **19th of January** and waited for almost 2 months.

On **March 16** Finally my name **Joshua Arulsamy** was added to the Hall of Fame.

![]()

[Finally, My Name was Added to the Infosec Hall of Fame](https://unite.un.org/content/hall-fame/list)

**Find my name here:** [Hall of Fame | Office of Information and Communications Technology](https://unite.un.org/content/hall-fame/list)

Thank You so much for reading, do follow me here on medium and on [LinkedIn](https://www.linkedin.com/in/joshuaarulsamy/) for more amazing content!

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----97675232aed7---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----97675232aed7---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----97675232aed7---------------------------------------)

[Technology](https://medium.com/tag/technology?source=post_page-----97675232aed7---------------------------------------)

[Achievement](https://medium.com/tag/achievement?source=post_page-----97675232aed7---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--97675232aed7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--97675232aed7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--97675232aed7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--97675232aed7---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?s...