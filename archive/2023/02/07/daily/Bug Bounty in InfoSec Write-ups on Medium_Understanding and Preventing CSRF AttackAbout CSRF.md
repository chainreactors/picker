---
title: Understanding and Preventing CSRF AttackAbout CSRF
url: https://infosecwriteups.com/understanding-and-preventing-csrf-attackabout-csrf-a107a5b5ddb5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-07
fetch_date: 2025-10-04T05:50:49.964071
---

# Understanding and Preventing CSRF AttackAbout CSRF

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa107a5b5ddb5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funderstanding-and-preventing-csrf-attackabout-csrf-a107a5b5ddb5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funderstanding-and-preventing-csrf-attackabout-csrf-a107a5b5ddb5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a107a5b5ddb5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a107a5b5ddb5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Understanding and Preventing CSRF Attack

## A Comprehensive Guide to Identifying, Mitigating and Protecting Your Website from Cross-Site Request Forgery

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--a107a5b5ddb5---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--a107a5b5ddb5---------------------------------------)

4 min read

·

Feb 1, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

## What is CSRF?

* CSRF is a type of attack that exploits the trust relationship between a website and its users. When a user logs into a website, their browser is often given a token that is used to authenticate subsequent requests made by the user. This token is stored in a cookie and is sent along with each request to the server.
* An attacker can use this trust relationship to their advantage by tricking a user into performing actions on a website without their knowledge.
* This can be done by creating a fake website that looks similar to the original website and including a hidden form that makes a request to the original website when the form is submitted.
* The request is made using the user’s browser, so it is authenticated using the token stored in the user’s cookie. The result is that the user has unwittingly performed a malicious action on the original website without realizing it.

## How to Find CSRF

Finding CSRF vulnerabilities can be a challenge, but there are several tools and techniques that can be used to help.

### Tools and Techniques Used to Find CSRF

1. **Manual Testing**

* Manual testing involves manually analyzing the website’s code to look for any areas that could potentially be vulnerable to CSRF.
* This can be a time-consuming process, but it is one of the most effective ways to find vulnerabilities.

**2. Automated Tools**

* There are several automated tools that can be used to find CSRF vulnerabilities.
* These tools work by automatically sending requests to the website and analyzing the responses to see if any vulnerabilities are present. Some popular tools include **OWASP ZAP, Burp Suite, and Nitko**.

**3. Pen Testing**

* Penetration testing, or pen testing for short, is a process where a team of security experts test the security of a website.
* This can be done either manually or using automated tools. Pen testing can be useful in finding CSRF vulnerabilities because it provides a comprehensive analysis of the website’s security.

## Impact of CSRF

The impact of a CSRF attack can be severe. Some of the most common consequences of a CSRF attack include:

### 1. Stealing Sensitive Information

An attacker can use CSRF to steal sensitive information, such as login credentials, credit card numbers, and other personal information.

### 2. Performing Malicious Actions

An attacker can use CSRF to perform malicious actions, such as changing a user’s password, making a purchase without their consent, or posting spam messages on a user’s behalf.

### 3. Damaging Reputation

A CSRF attack can damage a website’s reputation and cause users to lose trust in the website.

## Prevention

Preventing CSRF attacks can be a complex process, but there are several steps that can be taken to minimize the risk.

### 1. Use Anti-CSRF Tokens

* Anti-CSRF tokens are random strings that are generated by the server and sent to the client with each request.
* The client must include the token in subsequent requests, and the server will only process the request if the token is present.
* This ensures that requests can only be made by the user and not by an attacker

### 2. Use Same-Site Cookies

* Same-site cookies are a type of cookie that are only sent with requests that originate from the same website that set the cookie.
* This means that an attacker cannot use a user’s cookies to make requests to the website.

### 3. Use Captchas

* Captchas can be used to ensure that requests are made by a human and not by an automated script. This can prevent attackers from using CSRF to automate malicious actions.

### 4. Limit the Scope of Sensitive Actions

* Sensitive actions, such as changing a password or making a purchase, should be limited in scope. This means that these actions should only be possible when the user explicitly confirms the action.

## Conclusion

* CSRF is a serious web security vulnerability that can lead to sensitive information being leaked or malicious actions being performed.
* Finding CSRF vulnerabilities can be challenging, but there are several tools and techniques that can be used to help.
* To prevent CSRF attacks, websites should use anti-CSRF tokens, same-site cookies, captchas, and limit the scope of sensitive actions. By taking these precautions, websites can protect their users and maintain their reputation.

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](https://www.buymeacoffee.com/cyberw1ng)

Thank you for Reading!!

Happy Hunting ~

```
Author : karthikeyan Nagaraj ~ Cyberw1ng
```

[Csrf](https://medium.com/tag/csrf?source=post_page-----a107a5b5ddb5---------------------------------------)

[Web Security](https://medium.com/tag/web-security?source=post_page-----a107a5b5ddb5---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----a107a5b5ddb5---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----a107a5b5ddb5---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----a107a5b5ddb5---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosec...