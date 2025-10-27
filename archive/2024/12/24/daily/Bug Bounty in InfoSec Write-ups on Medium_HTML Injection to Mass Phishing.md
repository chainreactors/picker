---
title: HTML Injection to Mass Phishing
url: https://infosecwriteups.com/html-injection-to-mass-phishing-5701d495cdc2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-24
fetch_date: 2025-10-06T19:37:23.621365
---

# HTML Injection to Mass Phishing

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F5701d495cdc2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhtml-injection-to-mass-phishing-5701d495cdc2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhtml-injection-to-mass-phishing-5701d495cdc2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-5701d495cdc2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-5701d495cdc2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **HTML Injection to Mass Phishing**

[![Bharat Singh](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---byline--5701d495cdc2---------------------------------------)

[Bharat Singh](https://bharat-singh.medium.com/?source=post_page---byline--5701d495cdc2---------------------------------------)

3 min read

·

Dec 19, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

### **Introduction**

Hi fellow hackers!

HTML Injection vulnerabilities may not initially appear as severe as SQL Injection or Remote Code Execution, but their potential impact can be just as devastating when exploited creatively. In this blog, I will walk you through a real-world scenario where I discovered an HTML Injection vulnerability in the “Invite User” functionality of an application. This vulnerability could be weaponized to conduct mass phishing campaigns by redirecting users to malicious websites.

### The Discovery Process

In the application I was testing, the vulnerability existed in the “Add new user” feature. Here is how the functionality worked:

>> An admin or existing user could invite new users to the application by entering their email address, username, password etc.

>> The application would send an invitation email to the entered address containing the username and the password.

I remember some blogs I had read in the past about HTML Injection so I thought why not try it here.

Quickly I went to /user/new to add a new user(Victim User).
There I have filled all the details of newly added victim user like Name, Email, Username, Password etc.

Press enter or click to view image in full size

![]()

Intercepted the request with Burp Suite and change the content of password field in the request with a HTML injection payload.

> <a href=’https://google.com’>Click Here</a>

Press enter or click to view image in full size

![]()

I sent the request and opened the added victim user’s email inbox.

Press enter or click to view image in full size

![]()

HTML Injection Payload Works!!!

As we can observe the hyperlink is created in the password field saying “Click Here”.

On clicking the link the user is successfully redirected to google.com.

Press enter or click to view image in full size

![]()

### **The Impact**

When the invited user received the email and clicked on the malicious link, they were redirected to my phishing site instead of the legitimate application. This phishing site could then capture sensitive information such as login credentials or other personal details.

Since there is no limitation on adding users, this vulnerability could lead to mass level phishing.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

If you guys like this writeup and learned something valuable then do hit the clap **👏 X 50 times.**

Feel free to connect with me on [Linkedin](https://www.linkedin.com/in/bharat-s1ngh/) and [Twitter](https://x.com/BH4R4T_S1NGH).

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----5701d495cdc2---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----5701d495cdc2---------------------------------------)

[Phishing](https://medium.com/tag/phishing?source=post_page-----5701d495cdc2---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----5701d495cdc2---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----5701d495cdc2---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5701d495cdc2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--5701d495cdc2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--5701d495cdc2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--5701d495cdc2---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--5701d495cdc2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:96:96/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--5701d495cdc2---------------------------------------)

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:128:128/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--5701d495cdc2---------------------------------------)

[## Written by Bharat Singh](https://bharat-singh.medium.com/?source=post_page---post_author_info--5701d495cdc2---------------------------------------)

[356 followers](https://bharat-singh.medium.com/followers?source=post_page---post_author_info--5701d495cdc2---------------------------------------)

·[83 following](https://medium.com/%40bharat-singh/following?source=post_page---post_author_info--5701d495cdc2---------------------------------------)

Cybersecurity enthusiast who plays CTFs and do Bug Bounty for fun. >>>><https://www.linkedin.com/in/bharat-s1ngh/><<<<

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----5701d495cdc2--------------------------------------...