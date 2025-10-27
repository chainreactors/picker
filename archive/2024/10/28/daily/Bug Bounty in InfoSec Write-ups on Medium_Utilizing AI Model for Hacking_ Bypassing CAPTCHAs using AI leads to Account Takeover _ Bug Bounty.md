---
title: Utilizing AI Model for Hacking: Bypassing CAPTCHAs using AI leads to Account Takeover | Bug Bounty
url: https://infosecwriteups.com/utilizing-ai-model-for-hacking-bypassing-captchas-using-ai-leads-to-account-takeover-bug-bounty-028804b779a0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:48:20.530687
---

# Utilizing AI Model for Hacking: Bypassing CAPTCHAs using AI leads to Account Takeover | Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F028804b779a0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Futilizing-ai-model-for-hacking-bypassing-captchas-using-ai-leads-to-account-takeover-bug-bounty-028804b779a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Futilizing-ai-model-for-hacking-bypassing-captchas-using-ai-leads-to-account-takeover-bug-bounty-028804b779a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-028804b779a0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-028804b779a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Utilizing AI Model for Hacking: Bypassing CAPTCHAs using AI leads to Account Takeover | Bug Bounty

[![Ph.Hitachi](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*WZn-64UUVRL95-ov)](https://ph-hitachi.medium.com/?source=post_page---byline--028804b779a0---------------------------------------)

[Ph.Hitachi](https://ph-hitachi.medium.com/?source=post_page---byline--028804b779a0---------------------------------------)

9 min read

·

Oct 1, 2024

--

4

Listen

Share

Leveraging AI for CAPTCHA bypass opens the door to potential vulnerabilities, revealing critical flaws in web security.

Hi Guys,
so im ph-hitachi, and im Full-Stack Developer, DevOps Enginner & Security Researcher with experienced to Automation Enginnering & Bug bounty Automation, this year i commited to findings new way of attack vector focusing on how we can utilize a modern tools & technologies and how hackers can possibly take this advantage & leverage these technologies for exploitation.

## Introduction:

With the rise of automation, **AI-driven** technologies have advanced significantly, and so have their applications in cybersecurity. Recently, I encountered a situation where AI was used not to secure systems but to exploit them. This post will walk through how an AI model, specifically **Generative AI**, was used to bypass **CAPTCHA** and take over accounts in a web application.

### What is CAPTCHA?

CAPTCHA, short for **Completely Automated Public Turing test to tell Computers and Humans Apart**, is a widely-used security mechanism designed to protect online services from automated abuse such as **brute-force attacks**, **credential stuffing**, and **bot-driven activities**. Typically, CAPTCHA challenges present a task that is difficult for bots but easy for humans — such as identifying objects in images, recognizing distorted text, or solving basic math problems.

CAPTCHA’s primary function is to block **automated scripts or bots** from performing harmful actions, such as repeatedly trying combinations of usernames and passwords until they find a valid match. However, CAPTCHA-based defenses are only effective if they cannot be bypassed or solved by automated means.

## **Testing Overview**:

We used a combination of manual and automated tools to test the platform. The test involved:

1. Extracting CAPTCHA images from the server.
2. Solving CAPTCHA images using an AI-based model.
3. Testing the resilience of the login page to brute-force attacks using a cluster bomb approach.

## Overview of the Bug Discovery:

![]()

**Step 1: Identifying CORS Misconfiguration on CAPTCHA Endpoint**

The first step in discovering the vulnerability was testing the security of the `{BASE_URL}/admin-web/captcha/show` endpoint. During the test, I found that the endpoint had a **CORS misconfiguration**, allowing unauthorized origins to access sensitive resources, such as CAPTCHA images.

Press enter or click to view image in full size

![]()

By sending a simple HTTP request from an untrusted domain, I was able to retrieve the CAPTCHA image without any server-side validation of origin.

```
POST /admin-web/captcha/show HTTP/2
Host: [redacted].com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: [redacted].com
Content-Type: application/x-www-form-urlencoded
Content-Length: 10
Origin: http://attacker.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

sysId=1000
```

```
HTTP/2 200 OK
Content-Type: application/json
Date: Tue, 01 Oct 2024 01:28:11 GMT
X-Trace-Id: i100,i101001a441232779d64e6f88ea3b2040cfb43a
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Access-Control-Allow-Origin: http://attacker.com
Access-Control-Expose-Headers: Set-Cookie
Access-Control-Allow-Credentials: true
X-Cache: Miss from cloudfront

{"img":"/9j/4AAQSkZJRgABAgAAAQABAAD(truncated)...","key":"code_xxxxxxxxxxx"}
```

This exposed CAPTCHA image became the entry point for the attack, as it could be automatically retrieved and processed.

Press enter or click to view image in full size

![]()

**Step 2: Testing Authentication Flow**

Once I identified the exposed CAPTCHA, the next step was to analyze the **authentication flow**. I targeted the `{BASE_URL}/admin-web/auth/authInfo` endpoint, which is responsible for verifying user credentials. Each login request required a username, password, and the new CAPTCHA solution.

![]()

Once the request is made, the server would return a response indicating whether the login was successful.

* **loginName**: The username being tested in the brute-force attack.
* **loginPassword**: The password being tested.
* **captchaCode**: The CAPTCHA solution (CAPTCHA TEXT = 6+3=captchaCode).
* **captchaKey**: The key retrieved from the initial CAPTCHA request.

Press enter or click to view image in full size

![]()

**Step 3: CAPTCHA Solving Using AI Model**

Initially, when attempting to solve the CAPTCHA using the AI model, I noticed that the **default CAPTCHA image** returned incorrect results due to poor image quality. The CAPTCHA presented simple mathematical equations like `6 + 4`, but the AI misinterpreted the output as a string of numbers such as `"6743"` rather than solving the equation.

Press enter or click to view image in full size

![]()

To resolve this, I applied **image preprocessing techniques** to enhance the clarity of the CAPTCHA. This improved the AI’s ability to read the CAPTCHA with **100% accuracy**. The key was to convert the image to black-and-white and sharpen it using the following [command](https://mathieularose.com/decoding-captchas):

Press enter or click to view image in full size

![]()

```
$ convert captcha_image.png -gaussian-blur 0 -t...