---
title: Flagging Flaws: Micro-CMS v1
url: https://infosecwriteups.com/flagging-flaws-micro-cms-v1-26b4ac14f622?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-17
fetch_date: 2025-10-04T11:51:54.299813
---

# Flagging Flaws: Micro-CMS v1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F26b4ac14f622&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fflagging-flaws-micro-cms-v1-26b4ac14f622&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fflagging-flaws-micro-cms-v1-26b4ac14f622&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-26b4ac14f622---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-26b4ac14f622---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Flagging Flaws: Micro-CMS v1

[![ScriptKitty](https://miro.medium.com/v2/resize:fill:64:64/1*ASowRgbWQRxIKRbTO1AQmg.jpeg)](https://medium.com/%40beirutey?source=post_page---byline--26b4ac14f622---------------------------------------)

[ScriptKitty](https://medium.com/%40beirutey?source=post_page---byline--26b4ac14f622---------------------------------------)

3 min read

·

Jul 16, 2023

--

Listen

Share

Welcome to “Flagging Flaws: Hacker101 Micro-CMS v1,” where we gon find those vulnerabilities within this machine. Join me as we navigate the box Micro-CMS v1, identifying flaws and gettin those flags :)

Press enter or click to view image in full size

![]()

## Application Overview:

Micro-CMS v1 is a web application designed for content management. It features a homepage(image 1) with three anchors leading to distinct articles while showing its titles. You can access the articles(image 2) and edit them(image 3). Users can create their own articles(Image 4), filling in a title and body, and submit them for publication. However, we’ve discovered several flaws in the system that will feed us the juice.

![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

## Flagging Flaws:

### **N°0** Broken Access Control on /page/edit/5:

The URL structure of Micro-CMS v1 allows unauthorized access to editing pages. By manipulating the page ID parameter in the URL, users can access and modify existing articles without proper authorization, potentially compromising the integrity of the system.

Press enter or click to view image in full size

![]()

### **N°1** XSS on Title — Referred in a Less Protected Page:

Micro-CMS v1 suffers from an XSS vulnerability when injecting malicious scripts into the article title. This vulnerability becomes even more critical when the manipulated title is displayed in less protected areas of the system(homepage), allowing attackers to execute unauthorized actions or compromise sensitive data.
 **simple xss example:** *<script>alert(‘XSS Attack!’);</script>*

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

### **N°2** XSS when script tag is disabled//on Mousehover Alert:

An additional XSS vulnerability is found in the article body, specifically when an <a> tag with an onmouseover alert event is injected. Exploiting this vulnerability enables attackers to execute malicious scripts when unsuspecting users hover over the affected area. This can lead to potential attacks, including phishing or session hijacking.
**Simple xss without script tag:** *<a onmousehover=”alert(‘x’);”>*

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

### **N°3***SQL Injection Vulnerability* — Edit Page Indexation:

The URL indexing mechanism used in the edit page introduces a potential SQL injection vulnerability. Attackers can craft malicious SQL queries within the URL parameter, potentially gaining unauthorized access to the backend database, and manipulating data beyond the intended scope.

**Simple SQLI like attack:** *##machine##.ctf.hacker101.com/page/edit/2***' or 1=1**

Press enter or click to view image in full size

![]()

This was it for todayyy!!! Let us continue our journey of Flagging Flaws by studying vulnerabilities & reports, and exercising our problem-solving skills. LET’S GOOO!

Follow me for more !!!!!! or if you love kitties !!!!!!! or whateverrrrrr!!!!!!! :)

[Ctf](https://medium.com/tag/ctf?source=post_page-----26b4ac14f622---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----26b4ac14f622---------------------------------------)

[CMS](https://medium.com/tag/cms?source=post_page-----26b4ac14f622---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----26b4ac14f622---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----26b4ac14f622---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--26b4ac14f622---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--26b4ac14f622---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--26b4ac14f622---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--26b4ac14f622---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--26b4ac14f622---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ScriptKitty](https://miro.medium.com/v2/resize:fill:96:96/1*ASowRgbWQRxIKRbTO1AQmg.jpeg)](https://medium.com/%40beirutey?source=post_page---post_author_info--26b4ac14f622---------------------------------------)

[![ScriptKitty](https://miro.medium.com/v2/resize:fill:128:128/1*ASowRgbWQRxIKRbTO1AQmg.jpeg)](https://medium.com/%40beirutey?source=post_page---post_author_info--26b4ac14f622---------------------------------------)

[## Written by ScriptKitty](https://medium.com/%40beirutey?source=post_page---post_author_info--26b4ac14f622---------------------------------------)

[...