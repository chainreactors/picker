---
title: Approaching Login,Signup Pages and Change Password Instances for Bug Bounty Hunting
url: https://infosecwriteups.com/approaching-login-signup-pages-and-change-password-instances-for-bug-bounty-hunting-99819b24e258?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-08
fetch_date: 2025-10-04T08:55:01.116751
---

# Approaching Login,Signup Pages and Change Password Instances for Bug Bounty Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F99819b24e258&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fapproaching-login-signup-pages-and-change-password-instances-for-bug-bounty-hunting-99819b24e258&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fapproaching-login-signup-pages-and-change-password-instances-for-bug-bounty-hunting-99819b24e258&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-99819b24e258---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-99819b24e258---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Approaching Login, Signup Pages and Password Reset Instances for Bug Bounty Hunting

[![Thee Eclipse](https://miro.medium.com/v2/resize:fill:64:64/1*QPGkCrXe0vC8iTg4lnR4Cg.png)](https://medium.com/%40TheeEclipse?source=post_page---byline--99819b24e258---------------------------------------)

[Thee Eclipse](https://medium.com/%40TheeEclipse?source=post_page---byline--99819b24e258---------------------------------------)

9 min read

·

Feb 23, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Bug Bounty

> Hello Security World, In this blog we analyze the detailed approach to bug bounty hunting on login and sign up pages as well as change password instances and pages.
>
> We are not detailing the full exploitation tutorials for each but we point the arrow to the bulls eye .
>
> But are they really low-hanging fruits always? Maybe not. Let us dig right in!!

But why should one go for the login and sign up pages? Well as a beginner in bug bounty the very first attack endpoints include these pages and as professionals in the industry you can start from the login or password resets and dig your way up to critical bugs and all from a simple sign up

What makes the pages and easy to go after target? Because doesn’t matter the technology used because maybe someone is intimidated by web3 technologies but again all the technologies whether too old or futuristic the sign up and login pages are all vulnerable to quite similar bug trends and well, all allow user inputs and that makes it even more interesting.

Let us look and the bugs or issues approach for bug bounty or just web application security as a developer.

## **1. Captcha Bypass and Missing Captcha**

The very first thing organizations and developers have mastered recently over the years is the use of captcha(*Completely Automated Public Turing test to tell Computers and Humans Apart*) to verify requests and avoid bots on their platforms and this includes the famous google captcha for : “*verify you are not a robot*” .

But well ,someone might say it does not really have anything on security or rather does not attract attention to bug bounty hunters but honestly you should look it up as the first targets to login and sign up pages.

The captcha exist to: prevent automated bots from performing malicious activities such as creating multiple accounts, spamming, scraping data, or carrying out brute-force attacks to crack passwords and as well to avoid fake clicks on revenue accounts and private click programs.

> What if you bypassed the captcha set to carry out unrestricted brute-force, spamming, scrap data and even exhaust server resources for DOS or DDOS? That becomes a security issue and thus the presence of a CAPTCHA on webpages should always attract a bug bounty hunter to exploit the bugs / scenarios listed(but not limited to): creating multiple accounts, spamming, scraping data, DOS,DDOS , locking users out of their accounts or carrying out brute-force attacks to crack passwords

More on captcha bypass: <https://book.hacktricks.xyz/pentesting-web/captcha-bypass>

## **2. Improper password validation**

The next easy to note bug is the incorrect password validation which comes hand in hand with error validations that can cause security issues like displaying sensitive information to the user or allowing attackers to gain information about the website’s architecture . This typically involves the regex ( Regular Expressions ) used in the password validation while creating an account and this validation is the one that alerts you with errors like: Well for a regex like(*^(?=.\*\d)(?=.\*[a-zA-Z])(?=.\*[A-Z])(?=.\*[-\#\$\.\%\&\\*])(?=.\*[a-zA-Z]).{8,16}$*)

The password must match:

* At least 8–16 characters,
* must contain at least 1 uppercase letter,
* must contain at least 1 lowercase letter,
* and 1 number
* Can contain any of this special characters $ % # \* & — .

> But some sites will not properly validate this and allows for any password length and patterns including breached passwords and as well give suggestive error messages like: “Password 1 for user admin is invalid”

Well , the error messages should not freely give details that allows for username enumerations by brute-force or scrapping by automations like selenium or just basic linux tools . The password regex should despite limiting the password patterns to specific requirements have atleast a specific set length for inputs .

> This is because having unlimited length for password input even if by decryption in the database, the server will use up too much resources rendering the logins or sign ups for the specified user which well , could potentially lead to DOS .
>
> The password regex should be easy to comply to but again secure from attacks by wordlists made from leaked password databases of common simple patterns . That keeps accounts safe .

As a bug bounty hunter or developer, the password regex and validations should be an area to check.

More on password validation and regex: <https://gist.github.com/rogers0404/36762d5e2e60fc6bedc3a2a33c7b1310>

## **3. Email validation**

Ever signed up on a site with a fake email or a temporary one? Well , what did that imply or why did you do that instead of using your real email? Well, for different reasons obviously but why is this a security issue if out of control?

The use of fake emails and temporary emails allows for fake users and sometimes even accounts using other peoples emails and the accounts made can be used for malicious reasons like cyber bullying, spam, malicious access to services or just a threat actor rendering an organizations statistics inaccurate.

Email validation is done using email codes and sometimes even email links on sign up but well, temporary emails are not caught in the net. To filter out temporary emails there is several options including:

> Blocking popular ...