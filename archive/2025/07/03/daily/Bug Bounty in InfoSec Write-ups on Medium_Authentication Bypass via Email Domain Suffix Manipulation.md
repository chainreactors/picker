---
title: Authentication Bypass via Email Domain Suffix Manipulation
url: https://infosecwriteups.com/authentication-bypass-via-email-domain-suffix-manipulation-c866501c7b4b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-03
fetch_date: 2025-10-06T23:50:35.539535
---

# Authentication Bypass via Email Domain Suffix Manipulation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc866501c7b4b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fauthentication-bypass-via-email-domain-suffix-manipulation-c866501c7b4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fauthentication-bypass-via-email-domain-suffix-manipulation-c866501c7b4b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c866501c7b4b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c866501c7b4b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Authentication Bypass via Email Domain Suffix Manipulation

[![Bishal Shrestha](https://miro.medium.com/v2/resize:fill:64:64/1*69Ov1zWMeaoJYT9wGOKT_w.jpeg)](https://bishal0x01.medium.com/?source=post_page---byline--c866501c7b4b---------------------------------------)

[Bishal Shrestha](https://bishal0x01.medium.com/?source=post_page---byline--c866501c7b4b---------------------------------------)

3 min read

·

Jul 1, 2025

--

5

Listen

Share

## Introduction

Authentication is the process of verifying the identity of a user, system, or entity to ensure they are who they claim to be before granting access to resources. This process involves presenting credentials, like usernames and passwords, and validating them against a trusted source. Authentication is a crucial security measure, helping to protect systems, data, networks, and applications from unauthorized access and potential attacks.

However, there are multiple ways authentication can be bypassed. Sometimes, it can be due to SQL injection,SSRF, IDOR, default login credentials, access control bugs, and even blind XSS can help to bypass authentication.

## Vulnerability Discovery

In this write-up, I will explain how I found this bug in detail.

A few months ago, I found an interesting internal application via recon. Initially, I left that domain because there was a strict login enforced via the front-end, and I did not see much to test. I tried a few things like default credentials and analyzed the JavaScript files but didn’t find much.

Another day, I decided to test it again.
 I started playing with the registration and login fields and collected all the HTTP requests. Then I noticed something interesting — a prefix was added to the entered email address.

In the frontend, I entered:

Press enter or click to view image in full size

![]()

Then, I replaced the domain part to via http request using the burp suite:

Press enter or click to view image in full size

![]()

Change the email from bishal@redacted.com to **bishal0x01@bugcrowdninja.com**

Since it was checking **emailSuffix** only. Like **redacted.com** and other internal domains.

I checked my email, and to my surprise, it was successfully registered! I received the confirmation email and was able to verify the account.

Press enter or click to view image in full size

![]()

At first, there wasn’t much to see just the application field to submit an application. But after sending an application, I tried to modify it to other users’ applications.
 And… I was successfully able to access other users’ applications too!

Press enter or click to view image in full size

![]()

Additionally, after submitting an application, it was supposed to be approved by admins.
 But what if we could approve those applications ourselves?

Well, I was able to self-approve too!

Moreover, via different API endpoints, I was able to leak all internal information — users, admins, partners — including sensitive documents and more.

While using the frontend, I could only access my own application.
 However, using the API endpoints, I was able to perform full CRUD actions **as an admin** — meaning I had **full privilege** over the system.

Press enter or click to view image in full size

![]()

## Impact

* Full authentication bypass
* Unauthorized access to all users’ and admins’ sensitive data (PII exposure)
* Ability to perform CRUD operations as an admin
* Access to internal documents and applications
* Ability to self-approve critical workflows (e.g., applications)

## Key Takeaways

* Always validate and sanitize user input, even at the backend.
* Never trust only the frontend for authentication or input handling.
* Secure API endpoints separately with proper access controls.
* Regularly audit registration and authentication flows for unusual behavior.
* Small bugs like email domain mishandling can lead to major security breaches.

## Timeline:

*Reported →*17 Mar 2025 16:46:10 UTC

*Triaged →*18 Mar 2025 22:46:19 UTC

*Resolved →*15 Apr 2025 16:02:17 UTC

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c866501c7b4b---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----c866501c7b4b---------------------------------------)

[Writeup](https://medium.com/tag/writeup?source=post_page-----c866501c7b4b---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page-----c866501c7b4b---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c866501c7b4b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c866501c7b4b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c866501c7b4b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c866501c7b4b---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--c866501c7b4b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bishal Shrestha](https://miro.medium.com/v2/resize:fill:96:96/1*69Ov1zWMeaoJYT9wGOKT_w.jpeg)](https://bishal0x01.medium.com/?source=post_page---post_author_info--c866501c7b4b-----...