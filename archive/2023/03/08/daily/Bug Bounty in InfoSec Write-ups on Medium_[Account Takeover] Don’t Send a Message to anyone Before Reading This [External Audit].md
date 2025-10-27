---
title: [Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]
url: https://infosecwriteups.com/dont-send-a-message-to-anyone-before-reading-this-account-takeover-vulnerability-external-audit-cf584a0c983c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-08
fetch_date: 2025-10-04T08:55:05.705655
---

# [Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcf584a0c983c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdont-send-a-message-to-anyone-before-reading-this-account-takeover-vulnerability-external-audit-cf584a0c983c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdont-send-a-message-to-anyone-before-reading-this-account-takeover-vulnerability-external-audit-cf584a0c983c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cf584a0c983c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cf584a0c983c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# [Account Takeover] Don’t Send a Message to anyone Before Reading This [External Audit]

[![Vipul Sahu](https://miro.medium.com/v2/resize:fill:64:64/1*s81_1pBeT2o5kQ2pvZsB6Q.jpeg)](https://medium.com/%40vipul_sahu?source=post_page---byline--cf584a0c983c---------------------------------------)

[Vipul Sahu](https://medium.com/%40vipul_sahu?source=post_page---byline--cf584a0c983c---------------------------------------)

3 min read

·

Mar 7, 2023

--

Listen

Share

The security of a web application relies heavily on the strength and effectiveness of its authentication and authorization mechanisms. If these are not carefully designed, implemented, and maintained, the application can become vulnerable to a range of different attacks. One particularly dangerous attack vector is authentication bypass, where an attacker can gain access to the system without providing valid credentials.

During my recent penetration test, I discovered a critical account takeover vulnerability in the target system. This vulnerability can be exploited through response manipulation and requires the victim to send a message to the attacker. In the interest of protecting the target’s privacy, we will refer to it as “redacted.com” throughout this blog post.

Press enter or click to view image in full size

![]()

During my security testing, I inspected the response to a valid login request. Although the user\_id was present, which is considered sensitive information, no cookies were set. Upon realizing this, I probed for response manipulation by inputting incorrect credentials and modifying the response with the correct one. To my surprise, I was granted access for a brief moment before being immediately logged out of the dashboard. This unexpected behavior led me to believe that the application was performing additional checks.

After further investigation, I stumbled upon an endpoint named user\_login\_status.php. Utilizing the match and replace function, I modified the response by changing any instance of user\_signed\_out to user\_is\_signed\_in, thus mimicking a successful login. Although this allowed me to gain access to my account, I encountered an obstacle — I still required a user\_id to carry out the account takeover.

Press enter or click to view image in full size

![]()

user\_login\_status.php

In the redacted system, I discovered a vulnerability in the way it handles the response to a get\_message request. When a user sends a message to another user, redacted sends a get\_message request to retrieve the message. However, the response to this request not only includes the message content but also the sender\_id and sender\_email, where the sender\_id is actually the user\_id.

Press enter or click to view image in full size

![]()

Leaking user\_id and email address

By exploiting this vulnerability, I was able to intercept the response and gain access to the user’s account by using the sender\_email and a random password on the login page. By modifying the response from

> {“user\_profile”:{“sign\_in\_status”:”invalid\_password”}}

to

> {“user\_profile”:{“sign\_in\_status”:”login\_success”,”user\_id”:”<user\_id\_string>"}}

I was able to gain full access to the user’s account, allowing me to execute a complete takeover.

In conclusion, the vulnerability in redacted that allowed me to bypass authentication and take over any user’s account is a severe threat to the security of the application. To mitigate this vulnerability, the application should improve the design and implementation of its authentication and authorization mechanisms. The application can start by ensuring that responses to requests do not contain sensitive information such as user IDs or email addresses. It is also essential to validate responses properly to prevent tampering. Furthermore, implementing multi-factor authentication and session management can reduce the risk of account takeover.

**Linkedin:** <https://www.linkedin.com/in/vipul-sahu-a7a420174/>

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----cf584a0c983c---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----cf584a0c983c---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----cf584a0c983c---------------------------------------)

[Authentication Bypass](https://medium.com/tag/authentication-bypass?source=post_page-----cf584a0c983c---------------------------------------)

[Response Manipulation](https://medium.com/tag/response-manipulation?source=post_page-----cf584a0c983c---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf584a0c983c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf584a0c983c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cf584a0c983c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cf584a0c983c---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--cf584a0c983c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.inf...