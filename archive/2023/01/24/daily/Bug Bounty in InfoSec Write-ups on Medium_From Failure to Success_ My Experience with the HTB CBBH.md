---
title: From Failure to Success: My Experience with the HTB CBBH
url: https://infosecwriteups.com/from-failure-to-success-my-experience-with-the-htb-cbbh-49f2bfd41582?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-24
fetch_date: 2025-10-04T04:38:36.971795
---

# From Failure to Success: My Experience with the HTB CBBH

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F49f2bfd41582&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-failure-to-success-my-experience-with-the-htb-cbbh-49f2bfd41582&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-failure-to-success-my-experience-with-the-htb-cbbh-49f2bfd41582&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-49f2bfd41582---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-49f2bfd41582---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From Failure to Success: My Experience with the HTB CBBH

[![hac#](https://miro.medium.com/v2/resize:fill:64:64/1*3yfN8D4a4488vlJ232jr4Q.jpeg)](https://hac10101.medium.com/?source=post_page---byline--49f2bfd41582---------------------------------------)

[hac#](https://hac10101.medium.com/?source=post_page---byline--49f2bfd41582---------------------------------------)

5 min read

·

Jan 23, 2023

--

3

Listen

Share

Press enter or click to view image in full size

![]()

*Hello everyone, my name is Hac and in this post, I will be sharing my experience with the HTB CBBH exam, which is a practical web application pentesting exam. I will be discussing my preparation, the exam format, and my overall experience. I hope this will provide insight for anyone considering taking the exam in the future.*

**Hey readers I have made a you-tube video on this topic** [**https://youtu.be/XGBUXGeEy4s**](https://youtu.be/XGBUXGeEy4s)

## So let’s talk about the pricing

The cost of the Bug Bounty Hunter (BBH) certification exam from Hack The Box (HTB) is $210, inclusive of taxes. In order to take the certification exam, individuals are required to purchase the accompanying training program. For students, the cost of the training program is $8 per month. However, for non-students, the training program costs $145. It is important to note that the cost of the training program is separate from the cost of the certification exam.

## Let’s start with their training

The Bug Bounty Hunter (BBH) training program offered by Hack The Box (HTB) is a comprehensive curriculum that encompasses a wide range of topics related to web security. The program is divided into 20 different modules, each covering a different aspect of web security, from fundamental concepts such as web requests and the use of web proxies to advanced topics like Server-Side Request Forgery (SSRF), Local File Inclusion (LFI), and vulnerabilities specific to Application Programming Interfaces (APIs). The goal of this training program is to provide participants with a thorough understanding of web security and the various techniques and tools used by BBHs to identify and exploit vulnerabilities in real-world scenarios.

## Let’s talk about the exam

The Bug Bounty Hunter (BBH) certification exam from Hack The Box (HTB) is a highly practical and realistic web application penetration testing exam, lasting for 7 days. Due to the sensitive nature of the exam, specific details cannot be shared. However, it can be thought of as a simulated real-world scenario, where various aspects of web security are interconnected and must be considered in order to identify and exploit vulnerabilities. This format allows for a comprehensive assessment of an individual’s proficiency in web application penetration testing, mimicking the challenges and complexities that a BBH would encounter in actual engagements. It is important to note that passing the exam requires not only a deep understanding of the different vulnerabilities taught in the BBH training program, but also the ability to think outside the box and come up with creative solutions to exploit the exam’s scenarios. In order to pass the exam, participants must attain a minimum score of 85 points and also present a professional penetration testing report.

## Any prerequisites for CBBH exam?

While there are no formal prerequisites for taking the Bug Bounty Hunter (BBH) certification exam from Hack The Box (HTB), the organization recommends that participants have a solid understanding of web application, web service, and API penetration testing concepts. Additionally, HTB suggests that individuals have a good comprehension of the letter of engagement, which outlines the scope and objectives of a penetration testing engagement. Having these intermediate-level skills and knowledge will help individuals to better understand the challenges and complexities of the exam, and increase their chances of success.

## Can a newbie take this exam?

The Bug Bounty Hunter (BBH) certification exam from Hack The Box (HTB) is a challenging and comprehensive assessment of one’s skills and knowledge in web application, web service, and API penetration testing. While passing the exam does not necessarily require a significant amount of prior experience in the field, it does require a thorough understanding of these concepts. It is important to note that the exam can be difficult, especially for those new to the field of cybersecurity, or with limited experience. However, if an individual is confident in their abilities and is willing to put in the necessary effort to prepare, they should not be discouraged from attempting the exam.

## Preparing for the exam

After completing the Bug Bounty Hunter (BBH) training, it’s essential to practice and apply your knowledge on real-world scenarios. One of the best ways to do this is by utilizing Hack The Box’s Academy X HTB labs feature, which offers a wide range of labs to test your skills. Additionally, you can also take on web security challenges from PortSwigger’s Web Academy to further hone your skills and solidify your understanding of web security concepts. By combining both of these resources, you can gain the practical experience needed to excel on the BBH certification exam.

Some challenges which might be helpful are:

1. OWASP-top 10 track on Hackthebox <https://app.hackthebox.com/tracks/OWASP-Top-10>
2. Akvera fortress from hackthebox <https://app.hackthebox.com/fortresses/2>
3. You can also do some boxes like [BountyHunter](https://app.hackthebox.com/machines/BountyHunter) , [Horizontall](https://app.hackthebox.com/machines/Horizontall) , [Academy](https://app.hackthebox.com/machines/Academy) , [Meta](https://app.hackthebox.com/machines/Meta) , [Forge](https://app.hackthebox.com/machines/Forge) , [Nineveh](https://app.hackthebox.com/machines/54) .
4. And try to do all the labs on [portswigger](https://portswigger.net/web-secu...