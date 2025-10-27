---
title: Mass Assignment leads to the victim’s account being inaccessible forever
url: https://infosecwriteups.com/mass-assignment-leads-to-the-victims-account-being-inaccessible-forever-52e48c6a8a4d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-05-05
fetch_date: 2025-10-04T11:38:52.015124
---

# Mass Assignment leads to the victim’s account being inaccessible forever

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F52e48c6a8a4d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmass-assignment-leads-to-the-victims-account-being-inaccessible-forever-52e48c6a8a4d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmass-assignment-leads-to-the-victims-account-being-inaccessible-forever-52e48c6a8a4d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-52e48c6a8a4d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-52e48c6a8a4d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Mass Assignment leads to the victim’s account being inaccessible forever

[![M7arm4n](https://miro.medium.com/v2/resize:fill:64:64/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page---byline--52e48c6a8a4d---------------------------------------)

[M7arm4n](https://m7arm4n.medium.com/?source=post_page---byline--52e48c6a8a4d---------------------------------------)

4 min read

·

May 4, 2023

--

2

Listen

Share

Hi Guys, My name is m7arm4n and today I wanna talk about one of my findings on a private program that was vulnerable to Mass Assignment leads to make victim’s accounts inaccessible. I discovered many Mass Assignment in different programs and functions but this one is my favorite and the first one.

Press enter or click to view image in full size

![]()

## **What Is Mass Assignment Vulnerability?**

Mass Assignment Vulnerability is a type of security weakness that can occur in web applications. Whereas the web application allows the user to change the object multiple times with a single request, without properly filtering or validating the input.

This vulnerability occurs because developers often use a feature in some web frameworks to automatically map incoming data to object properties. Attackers can exploit this feature by submitting specially crafted input that includes additional properties or modifying existing ones that were not intended to be modified. This may allow access to or modification of sensitive data including user account information, payment information, or other sensitive information.

For example, suppose a web application allows a user to update profile information, including name, email address, and password. If the developer does not prepare or validate the input properly, the attacker can send a request that includes additional parameters such as “isAdmin=true”, giving them administrative access to the application.

## steps to reproduce

I skipped subdomain enumeration. when I reach the website registered as a normal user and after a few minutes, I understood the website had two endpoints to update the user’s data. One of them was for an email address which required a password to update it, Other one was only for first name and last name which does not require a password to update it.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

I tried to update the email to an existing email but unfortunately, I got an error.

Press enter or click to view image in full size

![]()

I thought a little differently and opened the Edit part to update the first name and last name and captured the update request in my Burp.

Press enter or click to view image in full size

![]()

I was looking for an interesting parameter to exploit, but the response was a redirection page that did not expose any hidden parameters in the response. I tried to add some interest parameters such as isAdmin, etc.

I added an Email parameter to the body and set a new email, Surprisingly my email updated to the new email.

Press enter or click to view image in full size

![]()

But the impact of this vulnerability till now is information/P5 and we should escalate this to something impactful. And I set up an existing victim’s email then forward it. Bingo I got success 😍🤯

My email address was updated to a victim’s email address, now let’s take check the victim’s account. On the victim side, I tried to log in with valid credentials but I got the error, tried to forget password? Nope, I got the same error.

Press enter or click to view image in full size

![]()

### **What Happened**

We set the same email for 2 accounts. and when functions ask the database for email, the database does not return anything or returns two accounts which mean functions do not work correctly. Now, The victim's account is inaccessible forever :D

Thank you for following me here, Don’t forget to follow me for more write-ups.

[Twitter](https://twitter.com/M7arm4n) 🐦

[Infosec](https://medium.com/tag/infosec?source=post_page-----52e48c6a8a4d---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----52e48c6a8a4d---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----52e48c6a8a4d---------------------------------------)

[Bugs](https://medium.com/tag/bugs?source=post_page-----52e48c6a8a4d---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----52e48c6a8a4d---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--52e48c6a8a4d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--52e48c6a8a4d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--52e48c6a8a4d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--52e48c6a8a4d---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--52e48c6a8a4d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![M7arm4n](https://miro.medium.com/v2/re...