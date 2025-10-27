---
title: JWT authentication bypass via unverified signature — Portswigger Simple Solution Writeup | 2023
url: https://infosecwriteups.com/jwt-authentication-bypass-via-unverified-signature-portswigger-simple-solution-writeup-2023-c306bdf7ce1b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-19
fetch_date: 2025-10-04T04:17:21.709927
---

# JWT authentication bypass via unverified signature — Portswigger Simple Solution Writeup | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc306bdf7ce1b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjwt-authentication-bypass-via-unverified-signature-portswigger-simple-solution-writeup-2023-c306bdf7ce1b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjwt-authentication-bypass-via-unverified-signature-portswigger-simple-solution-writeup-2023-c306bdf7ce1b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c306bdf7ce1b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c306bdf7ce1b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# JWT authentication bypass via unverified signature — Portswigger Simple Solution Writeup | 2023

## Portswigger Lab Solution — JWT Authentication Bypass by Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--c306bdf7ce1b---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--c306bdf7ce1b---------------------------------------)

3 min read

·

Jan 15, 2023

--

Listen

Share

[![]()](https://portswigger.net/web-security/jwt)

### Lab Link:

[## JWT attacks | Web Security Academy

### In this section, we’ll look at how design issues and flawed handling of JSON web tokens (JWTs) can leave websites…

portswigger.net](https://portswigger.net/web-security/jwt?source=post_page-----c306bdf7ce1b---------------------------------------)

### Lab Description:

This lab uses a JWT-based mechanism for handling sessions. Due to implementation flaws, the server doesn’t verify the signature of any JWTs that it receives.

To solve the lab, modify your session token to gain access to the admin panel at `/admin`, then delete the user `carlos`.

You can log in to your own account using the following credentials: `wiener:peter`

### What is JWT?

JWT refers to JSON Web Tokens

JSON Web Token is a proposed Internet standard for creating data with optional signature and/or optional encryption whose payload holds JSON that asserts some number of claims.

The tokens are signed either using a private secret or a public/private key

### Analysis:

1. Login with`wiener:peter`

![]()

2. Now Look at the Cookie using`Cookie Editor` or by`Intercepting the Traffic`

![]()

```
eyJraWQiOiJlMWYyMzczMC00NDUxLTRjMTMtYWViZi04M2Y2MmMxYmYzOGEiLCJhbGciOiJSUzI1N
iJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6IndpZW5lciIsImV4cCI6MTY3MzgwMTUxNH0.
NpgK9DOlKKauq0iI255qe5HbYVyEv8Ze9ODe6VfKdh6VkJ9fOMOL5o_rpwvtxxHsakeZPXN8ktG1S
L5y9I-D2zfHhLMI3hWGXXdXVXyw0GGbOkfCmJJWyDDljPrQYvcqJbB2uPvsDs7IkVhyklK89-Q2wo
AGQU4KVAiXBa7tM-pWIgsqn8w9Dl1jNc1cfMJ0yVjfmo5qEOIaFMlIkNvzfYuihsdjTZDOA00ZgD
j9K3eryQn1zPJh7hMp6on1mwK1ieQ_aO-dIWZ_x3bXYootpX08ijfdmL12VKr9_RKv9ppQiDbqXv
YsTC36482Wlc5LRfCOx_XE_VaQu62a0Q10hA
```

It Looks like they have used Jwt for Authentication

3. Let’s Decrypt the token using [jwt.io](https://jwt.io/)

[## JWT.IO

### JSON Web Token (JWT) is a compact URL-safe means of representing claims to be transferred between two parties. The…

jwt.io](https://jwt.io/?source=post_page-----c306bdf7ce1b---------------------------------------)

Press enter or click to view image in full size

![]()

![]()

From this, we can able to understand that the`sub` value defines the user who is logged in.

If we changed the sub-value to the name of another person, then we can access their account with the Privilege of that user, such as admin

4. Change the Value`wiener` to`administrator`

Press enter or click to view image in full size

![]()

As long as you change the value the token also gets changed

```
eyJraWQiOiJlMWYyMzczMC00NDUxLTRjMTMtYWViZi04M2Y2MmMxYmYzOGEiLCJhbGciOiJSUz
I1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6ImFkbWluaXN0cmF0b3IiLCJleHAiOjE
2NzM4MDE1MTR9.PEWC1x0JyP2oADxuxvfj_rNI-wZqxjvkyPsFvDK5_jVCXg9kb-00OHg9b7GR
cugRVLokInxsb0IpDunxIgvD362TbQBI4ONACpou0nmBH11a9nkCrQ7qxkFMYgb6cKM7JQjX2g
n5IvArWmUPOvSQUZv9hKBautpLijRAn8xn6z4-Y6UOYtfdqUnQrj0S-4oetIMPP29soB9x6yQ8
0YPk81dHi7OanX5TR1izRmCIXn_7RA2WiTHSnNsB2ARDuzXsVzel97g4-pFUdInybgGizMIRp5
942G3JU352hzjIw3XXw_3x1InT0DJPdFR7iaF4q3KY0O_WkJirodni-uf2eA
```

The Above token’s value is set to administrator

5. Copy the token, and paste it into the session using the`Cookie editor`

6. Then try to Access the`/admin` page

7. Now you will have the access to delete users, delete Carlos to solve the lab

Watch the below gif!!

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

[## Cyberw1ng

### Learn Cyber Security and Create Awareness ~ cyberwing Stay tuned with me, Subscribe, and Like the Videos… Ask Doubts…

www.youtube.com](https://www.youtube.com/channel/UCBg0UIT0319Xc-cw4QK8bqA?sub_confirmation=1&source=post_page-----c306bdf7ce1b---------------------------------------)

Github for Resources:

[## Cyberw1ng — Overview

### Security Researcher and Bug Hunter. Cyberw1ng has 8 repositories available. Follow their code on GitHub.

github.com](https://github.com/cyberw1ng?source=post_page-----c306bdf7ce1b---------------------------------------)

Telegram Channel for Free Ethical Hacking Dumps

[## Ethical Hacking Dumps — CEH, OSCP, Comptia

### Materials and Books for Ethical Hacking Exams like CEH v12, OSCP, Comptia Pentest+, Comptia Security+, Comptia Network+…

t.me](https://t.me/ethicalhackingessentials?source=post_page-----c306bdf7ce1b---------------------------------------)

Thank you for Reading!

Happy Ethical Hacking ~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

[![]()](http://buymeacoffee.com/cyberw1ng)

[Jwt](https://medium.com/tag/jwt?source=post_page-----c306bdf7ce1b---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c306bdf7ce1b---------------------------------------)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----c306bdf7ce1b---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----c306bdf7ce1b---------------------------------------)

[Programming](https://medium.com/tag/programming?source=post_page-----c306bdf7ce1b---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?sou...