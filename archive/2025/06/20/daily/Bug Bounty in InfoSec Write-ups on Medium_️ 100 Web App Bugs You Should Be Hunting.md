---
title: ️ 100 Web App Bugs You Should Be Hunting
url: https://infosecwriteups.com/100-web-app-bugs-you-should-be-hunting-6295f78d6880?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-20
fetch_date: 2025-10-06T22:51:53.523126
---

# ️ 100 Web App Bugs You Should Be Hunting

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6295f78d6880&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F100-web-app-bugs-you-should-be-hunting-6295f78d6880&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F100-web-app-bugs-you-should-be-hunting-6295f78d6880&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6295f78d6880---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6295f78d6880---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 🕷️ 100 Web App Bugs You Should Be Hunting 💥

[![Swarnim Bandekar](https://miro.medium.com/v2/resize:fill:64:64/1*tYlpUgXKa2Uzqja_qIOGqA.jpeg)](https://medium.com/%40swarnimbandekar?source=post_page---byline--6295f78d6880---------------------------------------)

[Swarnim Bandekar](https://medium.com/%40swarnimbandekar?source=post_page---byline--6295f78d6880---------------------------------------)

3 min read

·

Jun 19, 2025

--

5

Listen

Share

From IDORs to SSRFs — A Mega List to Supercharge Your Hunting

In this post, I’m sharing **100 web app exploit ideas** that you can explore during your bug bounty hunts. These are not theoretical — many of these are based on real-world bugs reported in public bug bounty programs.

## 🔓 Insecure Direct Object References (IDOR)

* IDOR on user profile update
* IDOR via email enumeration
* IDOR on subscription APIs
* Broken object-level authorization in API

## 💉 Cross-Site Scripting (XSS)

* Reflected XSS in search bar
* Stored XSS in comments
* DOM-based XSS in JS-heavy pages
* XSS via SVG upload
* XSS via malformed JSON
* HTML injection in emails

## 🎯 Open Redirects

* Open redirect via query param
* Open redirect with base64 trick
* Unsafe redirect in logout flow
* Unsafe redirect after login

## 🧠 Logic and Business Flaws

* Logic flaw in shopping cart
* Price manipulation via hidden input
* Coupon abuse
* Duplicate purchase via race condition
* Bypassing paywall via caching
* Business logic flaw in refunds
* Flawed invite/token logic

## 🐍 SSRF (Server-Side Request Forgery)

* SSRF in PDF generator
* SSRF via webhook feature
* Blind SSRF via image fetcher
* SSRF using DNS rebinding
* SSRF via Cloud metadata endpoint

## 🔐 Authentication & Session

* Broken authentication bypass
* Insecure password reset token
* Missing rate limit on login
* No lockout after failed login attempts
* JWT token `none` algorithm
* JWT with weak secret
* JWT with overly long expiration
* Broken session invalidation on logout
* Session fixation
* Default credentials active
* Bypassing email verification
* No MFA enforced for admin

## 🧾 OAuth & SAML Issues

* OAuth misconfiguration (open redirect)
* OAuth token leakage via Referer
* OAuth scope escalation
* SAML signature bypass

## 🎯 CSRF (Cross-Site Request Forgery)

* CSRF on profile update
* CSRF on account deletion

## 🌀 CORS & Misconfigurations

* CORS misconfiguration (wildcard with credentials)
* Overly permissive CORS policy
* Improper cookie flags (missing `HttpOnly`/`Secure`)
* Content-Security-Policy misconfigured

## 🔨 Upload & File Handling

* Unsafe file upload (no content-type check)
* MIME type confusion on uploads
* Directory traversal in file viewer
* Uploading polyglot files
* File inclusion via upload & access
* Null byte injection in file path
* Command injection via filename

## ⚙️ Deserialization & Injection

* Unsafe deserialization (PHP, Java)
* SQL injection on rare parameter
* GraphQL injection
* HTTP parameter pollution
* Using CRLF to inject headers
* Using Unicode to bypass filters

## ⚡ GraphQL & API Exploits

* GraphQL introspection enabled
* GraphQL injection
* GraphQL rate limit missing
* Mass assignment in REST API
* API allows deleting arbitrary users
* Missing access control on internal docs
* API key reuse across environments

## 🧱 Rate Limits & Brute Force

* Missing rate limit on login
* Credential stuffing on forgotten endpoints
* No lockout after failed login attempts
* Rate-limit bypass using `X-Forwarded-For`
* GraphQL rate limit missing

## 🧪 Miscellaneous & Creative Angles

* Authentication bypass with null bytes
* Host header injection
* Abuse of debug endpoints
* Replay attack on payment endpoint
* Leaked credentials in JavaScript
* Leaked API keys in mobile app
* Token leakage via JavaScript `var`
* Fuzzing params to find debug info
* Using alternative HTTP methods (PUT, DELETE)
* Cache poisoning via Host header
* Cache deception via file extension
* Hidden admin functionality in frontend
* Mobile app with hardcoded secrets

## 📂 Sensitive Info Disclosure

* Debugging info in error messages
* Server reveals stack traces
* Leak of internal IP in error message
* Leaking sensitive info in analytics scripts
* Misconfigured `.git` exposed
* Accessible `.env` file
* Backup file accessible (.bak)
* Open database exposed (MongoDB, Redis)

## 🔍 Clickjacking & UI Issues

* Clickjacking vulnerability
* Lack of brute-force protection
* Open WebSocket with no auth
* Insecure image proxy

Press enter or click to view image in full size

![]()

> Ready to hit the hunting grounds again.
> If you found this helpful, drop a 👏 and share it with your fellow hackers.
> Stay curious. Stay ethical.
>  — Swarnim Bandekar

Credits: [Wesley Thijs](https://www.linkedin.com/in/wesley-thijs-8b384828a?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAEY_fwcBVfLJI1Ig_-A5EBJvfQJ-PNYwHCc)

### Connect with me:

[## Swarnim Bandekar

### Personal portfolio of Swarnim Bandekar

www.swarnim.live](https://www.swarnim.live/?source=post_page-----6295f78d6880---------------------------------------)

Linkedin:
[https://www.linkedin.com/in/swarnimbandekar](https://www.linkedin.com/in/swarnimbandekar/)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----6295f78d6880---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----6295f78d6880---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----6295f78d6880---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----6295f78d6880---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----6295f78d6880---------------------------------------)

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_inf...