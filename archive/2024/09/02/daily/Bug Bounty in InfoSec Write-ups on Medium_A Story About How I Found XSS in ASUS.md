---
title: A Story About How I Found XSS in ASUS
url: https://infosecwriteups.com/a-story-about-how-i-found-xss-in-asus-cb233ce3bb9c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-09-02
fetch_date: 2025-10-06T18:24:49.132986
---

# A Story About How I Found XSS in ASUS

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcb233ce3bb9c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-story-about-how-i-found-xss-in-asus-cb233ce3bb9c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-story-about-how-i-found-xss-in-asus-cb233ce3bb9c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cb233ce3bb9c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cb233ce3bb9c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# A Story About How I Found XSS in ASUS

[![Karthikeyan.V](https://miro.medium.com/v2/resize:fill:64:64/1*7Dwtch8Uu2UNSxmjHtFs8Q.png)](https://medium.com/%40karthithehacker?source=post_page---byline--cb233ce3bb9c---------------------------------------)

[Karthikeyan.V](https://medium.com/%40karthithehacker?source=post_page---byline--cb233ce3bb9c---------------------------------------)

2 min read

·

Sep 1, 2024

--

1

Listen

Share

A few months ago, during a routine security assessment, I uncovered a significant cross-site scripting (XSS) vulnerability in the ASUS Laravel Ignition debugging tool. This vulnerability, identified as R-XSS, posed a high risk due to the potential for unauthorized script execution in users’ browsers. Here’s how I discovered and explored this vulnerability.

Press enter or click to view image in full size

![]()

## The Discovery

While examining the target, I noticed that the Laravel Ignition debug mode was enabled on `adam.asus.com`, and the endpoint was vulnerable to XSS. The vulnerability was exposed through the following URL:

* **Vulnerable URL:** `[http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E](http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload%3Dalert%28%27cappriciosec.com%27%29%3E)`

When accessing this URL, the embedded script was executed in the user’s browser, confirming the presence of an XSS vulnerability.

## Understanding the Vulnerability

* **Bug Name:** R-XSS
* **Bug Priority:** High
* **Vulnerable URL:** `[http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E](http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload%3Dalert%28%27cappriciosec.com%27%29%3E)`

## Impact

The impact of this XSS vulnerability depends on the application’s context and the privileges of the compromised user. For example:

* **Minimal Impact:** In applications with public information, the impact might be negligible.
* **Serious Impact:** In applications handling sensitive data, such as financial transactions or healthcare records, the impact could be severe, allowing unauthorized access to private information.
* **Critical Impact:** If a user with elevated privileges is compromised, the attacker could gain full control of the application, affecting all users and data.

## Steps to Reproduce

To confirm the vulnerability, follow these steps:

1. **Access the Vulnerable URL:** Open the URL in your browser: `[http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E](http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload%3Dalert%28%27cappriciosec.com%27%29%3E)`
2. **Observe the Script Execution:** The script will execute in your browser, displaying an alert with the text `cappriciosec.com`.

## Automating the Hunt

To streamline the process, I built a Python tool specifically for detecting this vulnerability. You can install it using pip and automate your testing:

**ToolPOC:** [laravel-ignition-rxss **on github**](https://pypi.org/project/laravel-ignition-rxss/)

```
pip install laravel-ignition-rxss
laravel-ignition-rxss --chatid <YourTelegramChatID>
```

* **To Check a Single URL:**

```
laravel-ignition-rxss -u http://mytargetprogram.com
```

* **To Check a List of URLs:**

```
laravel-ignition-rxss -i urls.txt
```

## Remediation

To mitigate this vulnerability, it is essential to disable debug mode by setting `APP_DEBUG` to `false` in the environment configuration. This will prevent unauthorized script execution and protect users from potential XSS attacks.

POC by: [@karthithehacker](http://twitter.com/karthithehacker)
Mail: contact@karthithehacker.com
Website: <https://www.karthithehacker.com/>

If you’re interested in our VAPT service, contact us at ceo@cappriciosec.com or contact@cappriciosec.com.

For enrolling my cybersecurity and Bugbounty course,

WhatsApp +91 82709 13635.

## Connect with me:

Twitter: <https://twitter.com/karthithehacker>

Instagram: <https://www.instagram.com/karthithehacker/>

LinkedIn: <https://www.linkedin.com/in/karthikeyan--v/>

Website: <https://www.karthithehacker.com/>

Github : <https://github.com/karthi-the-hacker/>

npmjs: <https://www.npmjs.com/~karthithehacker>

Youtube: [https://www.youtube.com/@karthi\_the\_hacker](https://www.youtube.com/%40karthi_the_hacker)

> ***Thank you***

[Karthikeyan.V](https://medium.com/u/a14784d94f2c)

[Bugbounty Poc](https://medium.com/tag/bugbounty-poc?source=post_page-----cb233ce3bb9c---------------------------------------)

[Bugbounty](https://medium.com/tag/bugbounty?source=post_page-----cb233ce3bb9c---------------------------------------)

[Bugbounty Tips](https://medium.com/tag/bugbounty-tips?source=post_page-----cb233ce3bb9c---------------------------------------)

[Bugbounty Writeup](https://medium.com/tag/bugbounty-writeup?source=post_page-----cb233ce3bb9c---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----cb233ce3bb9c---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cb233ce3bb9c---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cb233ce3bb9c---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cb233ce3bb9c---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cb233ce3bb9c---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--cb233ce3bb9c---------------------------------------)

A collection of write-ups from the best hackers in the wo...