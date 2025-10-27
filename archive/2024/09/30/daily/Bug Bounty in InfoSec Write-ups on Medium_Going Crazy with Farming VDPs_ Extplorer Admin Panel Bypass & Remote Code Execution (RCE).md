---
title: Going Crazy with Farming VDPs: Extplorer Admin Panel Bypass & Remote Code Execution (RCE)
url: https://infosecwriteups.com/going-crazy-with-farming-vdps-extplorer-admin-panel-bypass-remote-code-execution-rce-ed6ae27bbce9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-30
fetch_date: 2025-10-06T18:24:05.413623
---

# Going Crazy with Farming VDPs: Extplorer Admin Panel Bypass & Remote Code Execution (RCE)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fed6ae27bbce9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoing-crazy-with-farming-vdps-extplorer-admin-panel-bypass-remote-code-execution-rce-ed6ae27bbce9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoing-crazy-with-farming-vdps-extplorer-admin-panel-bypass-remote-code-execution-rce-ed6ae27bbce9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ed6ae27bbce9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ed6ae27bbce9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Going Crazy with Farming VDPs: **Extplorer Admin Panel Bypass** & Remote Code Execution (RCE)

## Hi Kings & Queens, I’m YoungVanda and in this write-up, I’ll talk about a very simple CVE which led to over +20 high—critical vulnerabilities in a couple of hours and over +500 reputation. Yeah buddy, lightweight baby.

[![YoungVanda](https://miro.medium.com/v2/resize:fill:64:64/1*xJCKzxgEb-2Ao40zUAJY9Q.jpeg)](https://youngvanda.medium.com/?source=post_page---byline--ed6ae27bbce9---------------------------------------)

[YoungVanda](https://youngvanda.medium.com/?source=post_page---byline--ed6ae27bbce9---------------------------------------)

4 min read

·

Sep 24, 2024

--

Listen

Share

### *In the Name of the One Who Gives Glory*

> If you only want to read the technical part, please start reading from the Technical Part Header.

## Some Hunting Vibes

Since I was a little boy, I always wanted to be a Gangster. Sorry, I meant a farmer. 🧑🏽‍🌾🧑🏽‍🌾🧑🏽‍🌾🧑🏽‍🌾 😂😂😂

Like World War II soldiers’ dreams, like Western movies.

Press enter or click to view image in full size

![]()

After all the war and fights, I just wanted a peaceful life. Buying a land on the edge of the world, marrying to the desired one and making babies.

So I said why not!!! f♥♥k yeah. I’m in. Let’s farm some VDPs honey.

I hit up my friend [@TheM@sterOfDisaster](https://x.com/TheMsterDoctor1) , the most dangerous doctor in the world.

Just kidding 😅😁

> Thank God this is where we ended up.

## Technical Part

After some recon, we decided to work on a program with this scope.

> **https://app.redacted.com**

I love forcing things, you know 🤔😜. Especially when there is no WAF, that’s when I get violent. So basically the first thing we did was **FUZZING**.

> **ffuf -u https://app.redacted.com/FUZZ -w wordlsit.txt -c -r**

We got a hit with this endpoint **/file\_manager/** . Then, the first thing we saw was this Admin Panel.

Press enter or click to view image in full size

![]()

This is what Extplorer panel looks like. Take a mental screenshot for the next time 😂😂😂

From old to new resources, from ancient times 😂😂😂, we’ve been told to look for CVES when we face a third-party panel or admin panel. Therefore, nowadays every hunter does the same thing. Right? OK. That’s what we did. 😐😂

We came across this reference from Exploit-DB:

> <https://www.exploit-db.com/exploits/51067>

We did a bit of reading, playing around with the target, like Cannibals, and after a couple of minutes, we realised that it’s vulnerable to Authentication Bypass. `eXtplorer<= 2.1.14 - Authentication Bypass`

We put admin:admin and then captured the request, removed the entire password field and finally sent the request.

Press enter or click to view image in full size

![]()

Just random admin:admin

Press enter or click to view image in full size

![]()

Original Body Request

![]()

Edited one — Removed password filed — &password=admin

Press enter or click to view image in full size

![]()

This is what it looked like

The Explorer panel **allows you to view and manage files in your test directory**. The panel shows the directory’s content as a tree of subdirectories, files, and tests. Long story short, we could read the source code and extract **unauthenticated endpoints** with **parameters**. Since we had access to the source code we could see what vulnerabilities each endpoint had. You can guess the rest of it. Since they were all unauthenticated endpoints and not same-root/same-cause/anything you say😘, they were all accepted.

### Just being honest and some words

Well, the key to this discovery, for us, was doing structured Wide Recon and I’m sure if I gave that application to any hunter they could find the same discoveries more or less. So, we can conclude that we were the first hunters working on that application.

This is how I see it:

> Simple Techniques + Good Wide Recon Methodology = Success — Bug

By Simple techniques I mean, it could be a simple fuzzing, running a simple nuclei command, a simple active crawling, a simple Google Dorking, and so on.

### A little Me

I’ve been a bit inactive the last couple of months. But God is with us guys. I hope very soon I can have a strong comeback.

If you somehow liked my write-up, you can like it and follow me on social media.
I don’t know man. It was nice to write something again and share some knowledge.

My Twitter Account: [@young\_vanda\_](https://twitter.com/young_vanda_)

My Super Dope Friend: [@TheM@sterOfDisaster](https://x.com/TheMsterDoctor1)

Let’s gooo. Yeah buddy, light weight baby. Lightweight baby, light weight.

### Resources

* <https://www.exploit-db.com/exploits/51067>
* You can do further studies by this Shodan Dork — http.title:”extplorer”

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ed6ae27bbce9---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----ed6ae27bbce9---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----ed6ae27bbce9---------------------------------------)

[Technology](https://medium.com/tag/technology?source=post_page-----ed6ae27bbce9---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----ed6ae27bbce9---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ed6ae27bbce9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ed6ae27bbce9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page...