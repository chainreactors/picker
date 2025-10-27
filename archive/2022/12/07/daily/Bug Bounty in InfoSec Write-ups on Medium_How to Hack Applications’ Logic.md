---
title: How to Hack Applications’ Logic
url: https://infosecwriteups.com/how-to-hack-applications-logic-6b0219f0dd04?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:37.467583
---

# How to Hack Applications’ Logic

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6b0219f0dd04&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-hack-applications-logic-6b0219f0dd04&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-hack-applications-logic-6b0219f0dd04&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6b0219f0dd04---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6b0219f0dd04---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How to Hack Applications’ Logic

[![zer0dac](https://miro.medium.com/v2/resize:fill:64:64/1*V6Cy8uVkjlwN0BHVP-cKgg.jpeg)](https://zer0dac.medium.com/?source=post_page---byline--6b0219f0dd04---------------------------------------)

[zer0dac](https://zer0dac.medium.com/?source=post_page---byline--6b0219f0dd04---------------------------------------)

7 min read

·

Dec 5, 2022

--

1

Listen

Share

Hi everyone, I decided to write a guide about finding logical bugs on applications like the web, mobile, and desktop. Actually, this write-up will not only be about breaking logic, if you understand well, it will guide you to think like a hacker, and with that, you may also find a lot of different kind of vulnerabilities.

![]()

**Who Am I?**

First of all, who am I? I will not talk about my past, however, right now, I’m working for a company that is about financial things and I’m doing internal, and external penetration tests, mostly for applications. I can say that in 3 months I have found almost 30 critical logical vulnerabilities in different companies. So, I will try to show you how I found all of them. How I found that vulnerabilities cost millions for companies.

![]()

**Why Logical Vulnerabilities are Important?**

In my opinion, finding vulnerabilities are about style, and I think a pentester who is looking only at his company should leave from there in 2–3 years. Why? Because almost every hacker has their own style to check vulnerabilities. And after 2 years, that eyes found all vulnerabilities of his style and you should look further with another. The second reason is we are in 2022 and I think working for 10 years in the same company is outmoded. The most important reason is, always different applications, systems, and persons will teach you different things and you have to exit from your comfort zone. Of course, you can work with yourself to improve yourself but always real zones will push you to learn further.

There is a style that is looking for applications' logic and how to break them.

The reason why logical vulnerabilities are valuable and you should look for them is that there is no automated tool to check logical bugs because machine learning didn’t learn to learn yet. So that’s why you have to learn what application does and why you shouldn’t be an automized robot. ;)

**From Which Window am I looking?**

Press enter or click to view image in full size

![]()

So as I talked about, I hate to do hacking randomly. What I mean, I hate trying XSS, SQL payloads, or something like that without any understanding of the application. I know you heard that enumeration is the key. But it is not only for certification exams or boxes. In the real life, if you want to know what you are hacking, you should learn what the application does.

I’m not using any roadmap to enumerate applications or network systems. However, I can suggest the below link for peoples which are new in this area. Before you have your own style, you need to follow people's way to learn.

[## 80,443 - Pentesting Web Methodology

### known vulnerabilities for the server , : version that is running. TheHTTP headers and cookies of the response could be…

book.hacktricks.xyz](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web?source=post_page-----6b0219f0dd04---------------------------------------#step-by-step-web-application-discovery)

*In the future, I will publish my notes on gitbook, So do not forget to check here if I edited.*

**How do Developers Think When Building Applications?**

There is a funny story that I experienced and I want to tell you that. With that, I think you will understand the main difference between hackers and developers.

Last year, I have found a critical IDOR in an online shopping application and I contacted one of the developers who build it in order to fix that together. The funny thing at the meeting was that.

> ~Developer thinking via pseudo-code~
>
> if the customer id is 1234,
>
> GET 1234's information,
>
> if the customer id is 5678,
>
> GET 5678’s information.

It is not looking like a buggy, right? At least not for the developer. Because he thinks there is a problem when we get via 1234 id and the application sends 5678 information.

Press enter or click to view image in full size

![]()

But the developer didn’t think about one thing. We are getting 5678’s information using 1234’s session. And the problem starts there...

**Where do Logical Bugs Start and How to Find Them?**

As far as I talked, all about why you should learn application logic. Now we will come to breaking them. If you understand the logic of the application, you should think about how can we break its logic to use it for what we want.

![]()

Let’s say there is a login panel and the panel has some forgot password link.

You should create accounts to test it. Don’t forget, first we should understand them, and then we should break them!

We looked the login was clear however when we check the forgot password part we have seen that when we click the forgot password, it says please enter your dog’s name or whatever the unique thing they want.

You should examine the response and request in order to understand how they control the variables and if we can manipulate them.

If you understand it is JSON or it is SQLite, and you shouldn’t find anything, you should research hacking and bypass techniques on google and on payload all the things.(<https://github.com/swisskyrepo/PayloadsAllTheThings>)

However, most research should be about the understanding application. Hacking is %90 understanding it and %10 exploiting it. Google is our best friend, never forget to research with it.

![]()

Let’s turn back to our example, we examine the request and response and there is a control parameter that checks the dog’s name. We should understand what response is ok and what is not. If the application sends something not unique or the hacker can find it, there is a logical account takeover vulnerability. Becau...