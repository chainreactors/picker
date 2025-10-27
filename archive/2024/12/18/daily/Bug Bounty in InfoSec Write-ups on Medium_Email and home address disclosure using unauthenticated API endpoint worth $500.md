---
title: Email and home address disclosure using unauthenticated API endpoint worth $500
url: https://infosecwriteups.com/email-and-home-address-disclosure-using-unauthenticated-api-endpoint-worth-500-4a497ff0678c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-18
fetch_date: 2025-10-06T19:41:49.249536
---

# Email and home address disclosure using unauthenticated API endpoint worth $500

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4a497ff0678c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Femail-and-home-address-disclosure-using-unauthenticated-api-endpoint-worth-500-4a497ff0678c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Femail-and-home-address-disclosure-using-unauthenticated-api-endpoint-worth-500-4a497ff0678c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4a497ff0678c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4a497ff0678c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Email and home address disclosure using unauthenticated API endpoint worth $500**

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:64:64/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---byline--4a497ff0678c---------------------------------------)

[the\_unlucky\_guy](https://vijetareigns.medium.com/?source=post_page---byline--4a497ff0678c---------------------------------------)

3 min read

·

Dec 10, 2024

--

6

Listen

Share

Namaste hackers, I am back with a new bug bounty write-up. In this blog, I am going to show how a unauthenticated endpoint reveals email and home address of users. The company is having a public bug bounty program on Hackerone. I will be using **redacted.com** as the main domain.

The company is a technology platform through which customers book different types of services.

[**www.redacted.com**](http://www.redacted.com) and **api.redacted.com** are in scope. As usual, I fired up my burp suite and started capturing every request in the proxy tool burp suite. **redacted.com** is the main domain but all the traffic routes through **api.redacted.com**. I used the company in the past to book some services so I have some bookings in my account.

There is an option on the platform that allows you to use the **SOS** feature during your bookings if something goes wrong. The **SOS** feature is only active during your booking time and is disabled afterward. I opened one of my bookings and clicked on **SOS**, and I received a response stating that the **Emergency Helpline will be available during your service delivery**.

Press enter or click to view image in full size

![]()

I reviewed the request for this call in Burp Suite. A **POST** request is sent to the endpoint `https://api.redacted.com/api/v2/help-recovery/gethelp/getHelpFlow` with the body:
`{"user_type":"customer","flow_type":"request","request_id":"booking_id","group_key":"customer_sos_group","mode":"published"}`. In the response, the email address, home address, and service details of users are being disclosed. I replayed the same request without an authentication token and was still able to view the email address, home address, and service details in the response.

Press enter or click to view image in full size

![]()

The main problem is with the impact because the `request_id` is a randomly and uniquely generated hashed string. So, brute-forcing the `request_id` is not feasible. I explored the application but could not find any API endpoint that would allow me to fetch the multiple `request_id` of the other users.

Press enter or click to view image in full size

![]()

I started looking for `request_id` values in Wayback URLs and on the Internet Archive. To my surprise, I found approximately 100 `request_id` values on the Internet Archive. Now, I have around 100 `request_id` values that can be used to fetch user’s email addresses, home addresses, and service details by using the vulnerable API endpoint `https://api.redacted.com/api/v2/help-recovery/gethelp/getHelpFlow.`

I quickly write a nice report to the security team through Hackerone. The Company fixed the issue and rewarded a bounty of **$500**.

![]()

**Timeline:**

*November 20, 2024 — Reported*

*November 20, 2024 — Triaged*

*November 25, 2024 — Fixed*

*December 02, 2024 — $500 Bounty awarded.*

Thanks for reading, hope you learned something new. Do clap and share if you like. Sayonara and Happy Hacking!

*Twitter:* [*7he\_unlucky\_guy*](https://twitter.com/7he_unlucky_guy) *Linkedin:* [Vijeta](https://www.linkedin.com/in/vijeta-reigns/)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----4a497ff0678c---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4a497ff0678c---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----4a497ff0678c---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----4a497ff0678c---------------------------------------)

[Application Security](https://medium.com/tag/application-security?source=post_page-----4a497ff0678c---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4a497ff0678c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4a497ff0678c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4a497ff0678c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4a497ff0678c---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--4a497ff0678c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:96:96/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---post_author_info--4a497ff0678c---------------------------------------)

[![the_unlucky_guy](https://miro.medium.com/v2/resize:fill:128:128/1*6WsUIHpOpn943C_P_cdWng.jpeg)](https://vijetareigns.medium.com/?source=post_page---post_author_info--4a497ff0678c---------------------------------------)

[## Written by th...