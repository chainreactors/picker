---
title: Account Takeover Guide
url: https://infosecwriteups.com/account-takeover-guide-eaff94d4ffe8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-02
fetch_date: 2025-10-04T05:28:41.517344
---

# Account Takeover Guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feaff94d4ffe8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-guide-eaff94d4ffe8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-guide-eaff94d4ffe8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eaff94d4ffe8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eaff94d4ffe8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Account Takeover Guide

[![Dheeraj Yadav](https://miro.medium.com/v2/resize:fill:64:64/1*fsaUtmxfUu8fFlxamIPzzA.jpeg)](https://medium.com/%40dheerajydv19?source=post_page---byline--eaff94d4ffe8---------------------------------------)

[Dheeraj Yadav](https://medium.com/%40dheerajydv19?source=post_page---byline--eaff94d4ffe8---------------------------------------)

3 min read

·

Feb 1, 2023

--

Listen

Share

Hey guys, in this tutorial, I will be sharing my learning about account takeover which I have learned after reading some blogs only on account takeover.

![]()

What is Account Takeover vulnerability?

Account takeover is a type of attack that allows an unauthorized user to gain access to someone else account by exploiting any kind of vulnerabilities that exist on that website, and these vulnerabilities are called account takeover vulnerabilities.

Account takeover is also written as ATO in short.

1. Account takeover via IDOR in password reset -

When to Hunt: When user\_id is visible in the POST request.

How to: Just simply change the user\_id from yours to someone else in POST request, if there exists this vulnerability, the password of the victim (the person whose user\_id you have entered) account will get changed.

How can I increase the impact: If this vulnerability exists, try to take over the admin’s account.

Read a detailed blog on this at [https://medium.com/@swapmaurya20/a-simple-idor-to-account-takeover-88b8a1d2ec24](https://medium.com/%40swapmaurya20/a-simple-idor-to-account-takeover-88b8a1d2ec24)

2. Account Takeover via password reset poisoning -

When to hunt: No specific symptoms as per my knowledge

How to: Intercept the password reset request in burp suite, try adding the following headers one by one, and observe the link you got in the email you would have received.

> Host: [attacker.com](http://attacker.com/)
> Host: [target.com](http://target.com/)
> X-Forwarded-Host: [attacker.com](http://attacker.com/)
> Host: [target.com](http://target.com/)
> Host: [attacker.co](http://attacker.com/)m

Note — In many bug bounty programs, this bug is kept out of scope as it requires user interaction, so read the program policy carefully.

Read a detailed blog on this at <https://vbharad.medium.com/account-takeover-through-password-reset-poisoning-72989a8bb8ea>

3. Account Takeover via CSRF-

Cross-Site Request Forgery (CSRF) is a type of attack that allows an attacker to execute unwanted actions on a web application on behalf of a user. In the context of an account takeover, a CSRF attack would involve tricking a user into clicking on a link or visiting a website that is controlled by the attacker. The link or website would then make a request to the web application on the user’s behalf, such as changing the user’s password or transferring money from the user’s account.

When to Hunt: Missing anti csrf tokens(sometimes website uses other ways to protect too apart from the csrf tokens)

How to Hunt: Inter the password change request which you should do via your account and then go to the burp suite and create a csrf poc for it, and change the details like username and email to the victim’s account. If this works successfully, you will be able to reset the password using forgot password.

Read a detailed blog on this at [https://infosecwriteups.com/account-takeover-via-csrf-78add8c99526](/account-takeover-via-csrf-78add8c99526)

4. Account Takeover by broken cryptography -

When to hunt: when you get an instinct that the URL you are getting in your mail for forgot password can be decoded and altered easily.

How to Hunt: Create two account on the website, request a password for account 1 and capture the request in burpsuite and then send it to the intruder and also send it to the server. For now, you would have received an email with a password reset link, try to decode the string. Now, try to make the token for account 2, if you are able to do this, you will be able to reset the password for account 2.

Read a detailed blog on this at <https://vasuyadav0786.medium.com/weak-cryptography-to-account-takeovers-87782224ed0d>

5. Account Takeover by 0auth Misconfiguration -

When to hunt: When having multiple types of authorization

How to Hunt: Go to [https://target.com/signup/](https://badoo.com/en/signup/) and signup using the unregistered victim’s account. After the sometime victim is going to signup using the OAuth method. What happens here is, now the attacker can easily log in using the victim’s account which bypasses the verification methods.

There are some other ways too for account takeover but I have just covered the most common ones, you can read about others on google.

Account Takeover Mindmap: <https://xmind.app/m/M3WEqG/>

Follow me on Twitter -
<https://twitter.com/Dheerajydv19>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----eaff94d4ffe8---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----eaff94d4ffe8---------------------------------------)

[Wapt](https://medium.com/tag/wapt?source=post_page-----eaff94d4ffe8---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----eaff94d4ffe8---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----eaff94d4ffe8---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eaff94d4ffe8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eaff94d4ffe8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eaff94d4ffe8-------------------------...