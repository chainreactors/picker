---
title: How I hacked into a government e-learning website
url: https://infosecwriteups.com/how-i-hacked-into-a-government-e-learning-website-ce8da8fb4ccc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-29
fetch_date: 2025-10-03T23:58:11.228435
---

# How I hacked into a government e-learning website

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fce8da8fb4ccc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-into-a-government-e-learning-website-ce8da8fb4ccc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-into-a-government-e-learning-website-ce8da8fb4ccc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ce8da8fb4ccc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ce8da8fb4ccc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I hacked into a government e-learning website

## DATE: 07/11/2022

[![iamgk808](https://miro.medium.com/v2/resize:fill:64:64/1*ZqU9IXcLelUzaqmhY4IXvw.jpeg)](https://iamgk808.medium.com/?source=post_page---byline--ce8da8fb4ccc---------------------------------------)

[iamgk808](https://iamgk808.medium.com/?source=post_page---byline--ce8da8fb4ccc---------------------------------------)

4 min read

·

Nov 26, 2022

--

1

Listen

Share

### **WHOAMI**

My name is Ganesh Kumar AKA iamgk808, a cybersecurity enthusiast and bug hunter. Handles — [Twitter](https://twitter.com/iamgk808), [Linkedin](https://www.linkedin.com/in/iamgk808/)

### **LET THE STORY BEGINS**

One Day my father asked me to log in to a government e-learning website to finish some tasks, that all teachers are required to complete within two days, so I log into my father's account & finished the tasks.

Later my father's friend also wants to finish the task so he gave me the e-mail ID and the password I tried to log in with the credential but it showed “enter the correct credential” then I asked him if the credential is correct or not and he told me that he did not create the account someone else has created the account for him with the wrong information.

So I have to find a way to log in to the account !!!

### GOAL: Log into the government e-learning website and finish the task

> **father’s friend given details :**
> email id - ######@gmail.com
> password - ###### (wrong)
> mobile no- ######## (wrong)
> UDISE Code- #########

## Attempt -1

### Login

With the given email id and password tried to log in, and the UI shows “**enter the correct credential**”

Press enter or click to view image in full size

![]()

The burp suite response shows “user not found”, I thought both the email id & password is incorrect, so this attempt is failed

![]()

## Attempt -2

### Password reset

So I tried to reset the password but it asks a mobile number, not an email id, then I entered the mobile number and the UI shows “oops something went wrong”.

Press enter or click to view image in full size

![]()

The burp suite response shows “user not found”, Thus the mobile number is also incorrect, so this attempt also failed

![]()

## Attempt -3

### REGISTER

Asks for a UDISE Code (a code given to schools to register an account), entered the code and the UI shows “Another Teacher is already registered in the given School”.

![]()

Fortunately, they have given the correct code. The burp suite response shows the full details like email, user id, mobile number, etc...

Press enter or click to view image in full size

![]()

From this attempt 3, we got useful information like email, mobile number, and user id.

With this mobile number, I tried Attempt -2 (password reset), and the OTP has sent successfully, I asked my father’s friend whether he got the OTP, and he said he did not get the OTP so I asked does the mobile number belongs to you he said it is someone else number and not his number.

so the only way here is to call the unknown number and ask for the OTP but it is not practically possible.

## Attempt -4

An idea struck my mind, so I log in with my father's valid credentials and check for any functionality or request to change a password.

Luckily I found a password reset request that only requires a valid user id and does not check the old password, From Attempt -3 I already got the user id so I changed the password successfully.

**NOTE**: If anyone knows what encryption is used to encode the password comment below.

Press enter or click to view image in full size

![]()

## Goal reached :)

Finally, I logged into the account and finished the task.

### Bugs found during this process:

1. IDOR — able to change anyone's password (Critical)
2. IDOR — able to see other teacher's P1 information by simply changing the id value (Critical)
3. IDOR — able to see other student's P1 information by simply changing the id value (Critical)

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Infosec](https://medium.com/tag/infosec?source=post_page-----ce8da8fb4ccc---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----ce8da8fb4ccc---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----ce8da8fb4ccc---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----ce8da8fb4ccc---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ce8da8fb4ccc---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ce8da8fb4ccc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ce8da8fb4ccc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ce8da8fb4ccc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ce8da8fb4ccc---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--ce8da8fb4ccc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges...