---
title: From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne
url: https://infosecwriteups.com/from-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-04-19
fetch_date: 2025-10-04T11:33:37.236088
---

# From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feeff74aff422&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-payload-to-300-bounty-a-story-of-crlf-injection-and-responsible-disclosure-on-hackerone-eeff74aff422&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eeff74aff422---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eeff74aff422---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# From payload to 300$ bounty: A story of CRLF injection and responsible disclosure on HackerOne

[![Karthikeyan.V](https://miro.medium.com/v2/resize:fill:64:64/1*7Dwtch8Uu2UNSxmjHtFs8Q.png)](https://medium.com/%40karthithehacker?source=post_page---byline--eeff74aff422---------------------------------------)

[Karthikeyan.V](https://medium.com/%40karthithehacker?source=post_page---byline--eeff74aff422---------------------------------------)

3 min read

·

Apr 16, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

As a bug bounty hunter, I’m always on the lookout for security vulnerabilities that I can report to companies and earn rewards. Recently, I discovered a CRLF injection vulnerability on a popular website through the HackerOne platform, and in this blog post, I’m going to share how I found it and the impact it had.

First, let me explain what CRLF injection is. CRLF stands for “Carriage Return Line Feed”, which are special characters used to represent the end of a line in various protocols, including HTTP. An attacker can inject CRLF characters into an HTTP header, which can lead to various attacks, such as HTTP response splitting, cross-site scripting, and cookie manipulation.

During my bug bounty testing, I used my [crlfi](https://github.com/karthi-the-hacker/crlfi) tool, I created this tool for the purpose of detect the CRLF injection Bug. You can install it on your machine by running the following command: “npm install crlfi -g”. It is supported on Windows, Mac, and Linux operating systems. To learn more about how to use it, please visit my Github repository “<https://github.com/karthi-the-hacker/crlfi>”.

After a few minutes of scanning, I was able to obtain a vulnerable output with the payload.

I noticed that the location header value was not properly sanitized, and I was able to inject CRLF characters into it using a simple payload like “%0d%0a” Example [http://example.com/](http://example.com/random)%0D%0ATest-Header:karthithehacker .

This allowed me to manipulate the server’s response and inject arbitrary content into it, such as fake headers or even JavaScript code.

To demonstrate the impact of the vulnerability, I created a proof of concept that injected a fake “Set-Cookie” header into the server’s response, which could be used to steal session cookies and perform session hijacking attacks. I reported the vulnerability to the company through the HackerOne platform, and they confirmed it and rewarded me with a bounty.

> Technical Content : <https://karthithehacker.com/blogs/crlf-in-h1-poc.html>

Press enter or click to view image in full size

![]()

The lesson here is that even seemingly harmless headers can be vulnerable to CRLF injection, and it’s important to properly sanitize user input before using it in HTTP headers. As a bug bounty hunter, it’s also important to keep an eye out for these types of vulnerabilities, as they can have a significant impact on the security of a web application.

> *Tips:- Downgrade the HTTPS to HTTP and inject CRLF payloads*

POC Video :

In conclusion, CRLF injection is a powerful technique that attackers can use to manipulate HTTP headers and perform various attacks. By understanding how it works and how to prevent it, we can help make the web a safer place for everyone.

Connect with me:

Twitter: <https://twitter.com/karthithehacker>

Instagram: <https://www.instagram.com/karthithehacker/>

LinkedIn: <https://www.linkedin.com/in/karthikeyan--v/>

Website: <https://www.karthithehacker.com/>

Github : <https://github.com/karthi-the-hacker/>

npmjs: <https://www.npmjs.com/~karthithehacker>

Youtube: <https://www.youtube.com/karthithehacker>

> **Thank you**

[Karthikeyan.V](https://medium.com/u/a14784d94f2c?source=post_page---user_mention--eeff74aff422---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----eeff74aff422---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----eeff74aff422---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----eeff74aff422---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----eeff74aff422---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----eeff74aff422---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eeff74aff422---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eeff74aff422---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eeff74aff422---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--eeff74aff422---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--eeff74aff422---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan.V](https://miro.medium.com/v2/resize:fill:96:96/1*7Dwtch8Uu2UNSxmjHtFs8Q.png)](https://medium.com/%40karthithehacker?source=post_page---post_autho...