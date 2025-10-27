---
title: How I Hacked an Admin Panel in Just 2 Minutes
url: https://infosecwriteups.com/how-i-hacked-an-admin-panel-in-just-2-minutes-19d145820ee7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-07
fetch_date: 2025-10-06T19:38:12.394322
---

# How I Hacked an Admin Panel in Just 2 Minutes

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F19d145820ee7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-an-admin-panel-in-just-2-minutes-19d145820ee7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-hacked-an-admin-panel-in-just-2-minutes-19d145820ee7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-19d145820ee7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-19d145820ee7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Breaking In Without Breaking Anything: Weak Admin Panel Credentials

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:64:64/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---byline--19d145820ee7---------------------------------------)

[ZEROSEC](https://medium.com/%40Zeroo_sec?source=post_page---byline--19d145820ee7---------------------------------------)

3 min read

·

Oct 8, 2024

--

2

Listen

Share

## **Introduction:**

> Hello everyone, my name is Ranjan Yadav, and I’m currently in my third year of BCA. I started my journey in cybersecurity over a year ago, and I’ve been passionate about it ever since. Bug bounty hunting and researching targets have become my favorite activities, and today, I’m excited to share how I hacked an admin panel

![]()

## **The Vulnerability:**

> This is one of the easiest vulnerabilities to exploit, even if you’re not very familiar with hacking. Don’t worry — you can find it too! The vulnerability I came across was **Weak/Default Credentials**.
>
> **Description**: The system was using default credentials, which are often publicly documented or extremely easy to guess (like “admin/admin” or “password123”).
>
> **Risk**: Attackers can easily gain unauthorized access by guessing or knowing these credentials, leading to data breaches, system compromises, and potentially unauthorized actions that could harm the entire system.

## **How I Found the Admin Panel**

Subdomain Enumeration:

Before diving into the admin panel, I needed to find all possible subdomains associated with the target. Subdomain enumeration is a critical first step in identifying hidden services, and I used **Subfinder** for this task.

**Using Subfinder**:
I ran the following command to find all subdomains for the target domain, in this case, `radicate.com`, and saved the output to a file called `subdomain.txt`:

> subfinder -d radicate.com -all -recursive -o subdomain.txt

**Filtering for Admin Panels**:
To narrow down my search for admin panels, I filtered the results for subdomains containing the word “admin”:

> cat subdomain.txt | grep “admin”

Alternatively, you can combine both steps in one command, without saving to a file:

> subfinder -d radicate.com -all -recursive | grep “admin”

This method quickly revealed several admin-related subdomains, and that’s when the real fun began!

Press enter or click to view image in full size

![]()

**Taking Screenshots with Aquatone**:
To visualize and quickly inspect all the subdomains, I used **Aquatone** to generate screenshots of the subdomains:

> cat subdomain.txt | aquatone

This process helped me quickly identify several admin-related subdomains and provided screenshots of the login pages, which made the next steps much easier!

**Accessing the Login Pages:**

After identifying the admin-related subdomains and taking screenshots using Aquatone, the next step was to visit those login pages and check for weak credentials. This is where things got interesting.

> **Testing for Default Credentials**:
> Admin panels often have weak or default credentials, which can easily be guessed. I started by testing some of the most common weak passwords:
>
> **admin/admin**
>
> **admin/password123**
>
> **admin/123456**
>
> Guest/Guest
>
> test/test

**Success!**

When I used `admin/admin` on one of the login pages... **BOOM**—I got immediate access! This simple, common combination allowed me to bypass the login page and enter the system.

![]()

Press enter or click to view image in full size

![]()

**Conclusion:**

I hope you enjoyed this story! I tried to keep the content simple and straightforward so that even beginners can understand how such vulnerabilities are exploited. This experience shows that sometimes, hacking doesn’t have to be complicated — simple issues like weak credentials can lead to serious security risks. Remember, always secure your systems with strong passwords!

> If you found this helpful, feel free to follow me on [LinkedIn](https://www.linkedin.com/in/ranjan-yadav-82b28b249/) and [Twitter](https://x.com/ig_ftw) for more insights and updates on my bug bounty journey.

Bye👋

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----19d145820ee7---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----19d145820ee7---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--19d145820ee7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--19d145820ee7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--19d145820ee7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--19d145820ee7---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--19d145820ee7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:96:96/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--19d145820ee7---------------------------------------)

[![ZEROSEC](https://miro.medium.com/v2/resize:fill:128:128/1*kcRAs3KDKoSWu6KDXpx1Dw.jpeg)](https://medium.com/%40Zeroo_sec?source=post_page---post_author_info--19d145820e...