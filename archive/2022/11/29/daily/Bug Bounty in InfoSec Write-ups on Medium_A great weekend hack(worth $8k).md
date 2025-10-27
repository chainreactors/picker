---
title: A great weekend hack(worth $8k)
url: https://infosecwriteups.com/a-great-weekend-hack-worth-8k-9bfda8ab65b9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-29
fetch_date: 2025-10-03T23:58:08.542844
---

# A great weekend hack(worth $8k)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F9bfda8ab65b9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-great-weekend-hack-worth-8k-9bfda8ab65b9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-great-weekend-hack-worth-8k-9bfda8ab65b9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-9bfda8ab65b9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-9bfda8ab65b9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# A great weekend hack(worth $8k)

[![Manas Harsh](https://miro.medium.com/v2/resize:fill:64:64/1*q2MIz-LpA2BqDTXNckeeKA.jpeg)](https://manasharsh.medium.com/?source=post_page---byline--9bfda8ab65b9---------------------------------------)

[Manas Harsh](https://manasharsh.medium.com/?source=post_page---byline--9bfda8ab65b9---------------------------------------)

4 min read

·

Nov 26, 2022

--

4

Listen

Share

Press enter or click to view image in full size

![]()

Source: Google images

This post is a writeup of my recent findings on Synack which got me $8k for 5 bugs, on a single day.

So, I was hacking on a program which was in QR period(QR period is a specific time defined by Synack where researchers with best reports are rewarded), and I had 7 hours left when I saw it. I submitted 6 bugs on this one, in which 5 got rewarded and 1 got rejected. I will define how did I go ahead and find them:)

These were the bugs I found:-

1. 2 SQL injections
2. 2 Stored XSS
3. 1 IDOR(read only)

**SQL injections:-** These SQL injections were error based SQL injections which I found from **MATCH & REPLACE** funtionality in Burp. In case you don’t know what is it, it looks something like this:-

Press enter or click to view image in full size

![]()

Source: Google images

Here, as you can see you can define param values and many other things to match and replace to your desired input. I added an item for **Param Value** where I had to change a param value for eg. **test > test’** and I got a result from it. When match and replace finds it for you, you would be able to see a different response on burp itself. You can read more about it [**here**](https://portswigger.net/burp/documentation/desktop/tutorials/using-match-and-replace). It looks something like this:-

Press enter or click to view image in full size

![]()

Source:- Portswigger

You can toggle between requests and it should give you the results. Later on, I sent it to SQLmap and I was able to fetch data from it. I don’t need to tell you how does it look like, if you are reading this you probably already know:)

2nd SQL injection came in the same way, I just added **test’’ instead of test’** this time and it came on another endpoint where I could escalate it further and dump data. I had to get in touch with multiple super talented SRTs for this one though. Thanks to them:)

**Stored XSS:-** I got two of them and won both! These XSS were quite simple and went straight. I just had to use this payload twice in input fields. I tried a few though, they didn’t work, but this one did. I just had to bypass a few filters seeing the JS output and it got reflected:)

**‘><input autofocus onfocus=alert(1)>**

This happened twice and it was fun to exploit them. I reckon people would’ve reported more than 30–35 XSS with same payload since its a famous one, where you use autofocus attribute to reflect JS.

**IDOR:-**

I submitted two IDORs too but somehow payout didn’t come that way. I could see the data of other folks with changing IDs, pretty simple. Found it on two places but got accepted in only one report. I wonder why I didnt win the 2nd. IDORs are pretty common and you still see them here and there. I used AutoRepeater for this one, which is a burp extension and it also has an option to match and replace things:)

So, a total payout:-

SQL injections:- $2900\*2

XSS Injection:- $880\*2

IDOR(which got accepted on an broken access Control’s payout):- $387

![]()

Tips:- Use Match and replace funtion to automate your game in bounties, and the most important one:- **Write great reports, really great ones. Include everything there. Resources, Video POCs etc. Also, screenshots with every steps in a clear way.**

As you can see, there was really nothing new here but what you can take from it is, spend time and check everything:) Error based SQLIs are still there, you might find one today/tonight:)

Until next time ❤

If you liked my work:- [Buy me a coffee!](https://buymeacoffee.com/manasjha79q)

Twitter:- @manasH4rsh

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Hacking](https://medium.com/tag/hacking?source=post_page-----9bfda8ab65b9---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----9bfda8ab65b9---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----9bfda8ab65b9---------------------------------------)

[Application Security](https://medium.com/tag/application-security?source=post_page-----9bfda8ab65b9---------------------------------------)

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9bfda8ab65b9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--9bfda8ab65b9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--9bfda8ab65b9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--9bfda8ab65b9---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--9bfda8ab65b9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest in...