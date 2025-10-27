---
title: Chaining Bugs to get my First Bug Bounty
url: https://infosecwriteups.com/chaining-bugs-to-get-my-first-bug-bounty-7e94afb704e7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-09
fetch_date: 2025-10-04T06:06:39.438427
---

# Chaining Bugs to get my First Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7e94afb704e7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-bugs-to-get-my-first-bug-bounty-7e94afb704e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fchaining-bugs-to-get-my-first-bug-bounty-7e94afb704e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7e94afb704e7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7e94afb704e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

## First Bug Bounty

# Chaining Bugs to get my First Bug Bounty

[![ag3n7](https://miro.medium.com/v2/resize:fill:64:64/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---byline--7e94afb704e7---------------------------------------)

[ag3n7](https://ag3n7.medium.com/?source=post_page---byline--7e94afb704e7---------------------------------------)

4 min read

·

Feb 8, 2023

--

2

Listen

Share

Openredirection + clickjacking + csrf -> Account Takeover

Press enter or click to view image in full size

![]()

Bounty

Hola Hackers,

This writeup is about my first bug bounty in which the submission was duplicate, even though they rewarded me for chaining the bugs and reported it with an effective approach of a real-life attack scenario.

Let’s Start

First we will discuss about the bugs which I chained together.

> **Open Redirection**Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain.
>
> **Clickjacking**
> Clickjacking is an interface-based attack in which a user is tricked into clicking on actionable content on a hidden website by clicking on some other content in a decoy website
>
> **CSRF**Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.

*source:* [*https://portswigger.net/*](https://portswigger.net/)

Now we can go to the target website, we can call it *example.com* by respecting their privacy.

While browsing through the website using burp suite, I found some open-redirection vulnerabilities, pages vulnerable to clickjacking, page without csrf token and also some other related things.

Most of the vulnerabilities I found on the website were out of scope, so I tried again. The csrf vulnerable page was a password reset page, when I saw it first I thought I can exploit it directly but when I checked the required inputs it requires current password also. After some discussions, I found that if there is password confirmation, then we can’t exploit the csrf directly. So I tried to find other methods to exploit it.

I checked the login page which is vulnerable to clickjacking, and I already have some openredirection also. So I tried to chain it together to a real-life attack scenario.

The summary of the attack was that we redirected to the clickjacking vulnerable login page via openredirection and then the user enters their username and password, it directly passed to the password reset form using javascript which successfully changes the password of the victim to the attacker’s password.

Press enter or click to view image in full size

![]()

fake login page creation

Here we used *example.com,* we can use the original login page here and host it somewhere and redirect it through their own website.

Press enter or click to view image in full size

![]()

fake login page

*source:* [*https://github.com/shifa123/clickjackingpoc*](https://github.com/shifa123/clickjackingpoc)

And when the user enters the credentials, it is directly sent to the password reset form via javascript. We can use the csrf poc generated from burp suite while performing a password reset here and combining it with the page makes everything simple and the password reset will happen at one click after entering the credentials

Program flow:

* First goto *https://www.example.com/?option=oauthredirect&redirect\_url=https://example.com* here this redirect to example.com
* If we host a fake login page using clickjacking on the login page, we will get the email and current password

![]()

login

* Then we can sent this to password change form, *https://www.example.com/etcetc?etc=abcd&Target=PasswordResetForm&params=test* which is vulnerable to csrf attack
* When the victim enters email and current password and then click on login, the password will get resetted to attacker given password

Press enter or click to view image in full size

![]()

Fake webpage and auto-submitting code snippet

![]()

successful

* Password Changed Successfully

![]()

password reset form

If I left that csrf and clickjacking vulnerabilities when I saw it is out of scope and reported the openredirect only, will not make me satisfied.

So that thought helped me to do this.

## Lessons Learnt:

* Stay Motivated
* Don’t rush yourself
* Try to understand things
* Don’t Leave Too Early

> “Like people says, taste the success once… tongue want more.” — Kapil Dev, 83

:D

Thank You For Reading ….

### Happy Hacking and Hunt More !!

Team [InitCrew](https://twitter.com/in1tcr3w) ❤

## Follow me on :

Twitter: <https://twitter.com/ag3n7apk>

Linkedin: <https://www.linkedin.com/in/abhijith-pk-ag3n7/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----7e94afb704e7---------------------------------------)

[Csrf](https://medium.com/tag/csrf?source=post_page-----7e94afb704e7---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----7e94afb704e7---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----7e94afb704e7---------------------------------------)

[Bug Chaining](https://medium.com/tag/bug-chaining?source=post_page-----7e94afb704e7---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7e94afb704e7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)]...