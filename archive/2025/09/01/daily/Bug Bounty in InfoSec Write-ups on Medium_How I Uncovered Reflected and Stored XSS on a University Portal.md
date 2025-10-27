---
title: How I Uncovered Reflected and Stored XSS on a University Portal
url: https://infosecwriteups.com/how-i-uncovered-reflected-and-stored-xss-on-a-university-portal-ad6c653c6a81?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:29:07.382343
---

# How I Uncovered Reflected and Stored XSS on a University Portal

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fad6c653c6a81&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-uncovered-reflected-and-stored-xss-on-a-university-portal-ad6c653c6a81&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-uncovered-reflected-and-stored-xss-on-a-university-portal-ad6c653c6a81&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ad6c653c6a81---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ad6c653c6a81---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Uncovered Reflected and Stored XSS on a University Portal

[![Avyukt Security](https://miro.medium.com/v2/resize:fill:64:64/1*5jGxXKsgQjjFNintRNHdwg.jpeg)](https://medium.com/%40avyuktsec?source=post_page---byline--ad6c653c6a81---------------------------------------)

[Avyukt Security](https://medium.com/%40avyuktsec?source=post_page---byline--ad6c653c6a81---------------------------------------)

4 min read

·

Aug 1, 2025

--

Listen

Share

Press enter or click to view image in full size

![]()

By: Kavin Jindal

Recently, while exploring the website of an educational institute, I came across a classic yet simple vulnerability of Reflected and Stored-XSS through a user-facing login page. Here’s a detailed breakdown of my methodology to find both the vulnerabilities:

## What is a Cross-Site Scripting (XSS) Vulnerability?

* Cross-site scripting, also known as XSS, is a vulnerability that enables attackers to inject malicious JavaScript code into a web application.
* These types of vulnerabilities occur mainly because a web server asks for user input and without any input sanitization or checks, it reflects that data on the page. It allows attackers to inject malicious JavaScript code into the web application which can be used to chain more complex vulnerabilities and execute attacks such as stealing cookies of a high privileged user or phishing attacks.
* I was able to discover two different types of XSS vulnerabilities on the target site:
* Reflected XSS: Reflected XSS occurs when malicious user input is reflected to that user without any input- sanitization, facilitating in execution of malicious JavaScript on the client side.
* Stored-XSS: As the name suggests, these types of vulnerabilities occur when the web server stores user input (for example, in a database) and is reflected by the user. The root cause here is that the web server doesn’t validate user input before storing it in its database or while reflecting the data on the page. These types of vulnerabilities are especially critical because they expand the attack surface, putting a larger number of website users at risk.

## My Methodology for finding both types of XSS:

## - Reflected XSS in the Student Login Form:

* I ran a very basic web directory scan using [**dirb**](https://www.kali.org/tools/dirb/)which returned several paths. I ran basic SQLi and XSS payloads on the relevant pages to look for an exploit. Unfortunately, the website had security mechanisms in place to block SQL Injection attacks but interestingly it was vulnerable to XSS payloads.
* After browsing through several pages I came across a student login page that was prone to **Reflected XSS via the GET method.**

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

* Basically after using the wrong credentials on the login form an error message popped up which was received from the URL. This seemed interesting and absurd at the same time due to which I had the idea of attempting XSS Injection here which surprisingly worked.

Press enter or click to view image in full size

![]()

* This only increased my curiosity and I looked for other instances on the website which were vulnerable to XSS and I wondered if I could get access to something more critical and interesting.

## - Stored-XSS via Student Registration Page:

* I opened up the registration page and entered fake credentials hoping that there would be no email or phone validation active. To my guess, there wasn’t and the system only checked for the email regex pattern.

Press enter or click to view image in full size

![]()

* I used the following JavaScript payload in the Name fields with an invalid phone number and email address.

```
<script>alert(2)</script>
```

* Luckily, the account was successfully registered and I got through the authentication process without any hassle.
* After the registration, I was redirected to an admission portal where students could fill in their details in an application form and make a fee payment. The website was using a secure third-party service for receiving payments hence it had no scope of exploitation. The admission form itself couldn’t be submitted without paying the fee hence that too was out of scope.
* But while browsing through the portal and clicking around on links I found an instance of stored XSS on a random page.

Press enter or click to view image in full size

![]()

* It basically was an empty page that showed a welcome message with the first name.
* Here as I used the JavaScript payload in the first name field it doesn’t display anything and instead initiates the payload. But upon checking the page source it is visible in the field as follows.

Press enter or click to view image in full size

![]()

* You can see that the XSS payload isn’t sanitized and is instead treated as a normal scripting element, hence explaining the vulnerability.

## Conclusion

* This was a very easy exploit that explored the XSS web vulnerability. It’s quite surprising to come across such a basic security loophole nowadays in user-facing features on websites. It was a fun learning experience working on this website and sharing my insights with you. I hope you found this write-up informative.

### Happy Hacking!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----ad6c653c6a81---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----ad6c653c6a81---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----ad6c653c6a81---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----ad6c653c6a81---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----ad6c653c6a81---------------------------------------)

...