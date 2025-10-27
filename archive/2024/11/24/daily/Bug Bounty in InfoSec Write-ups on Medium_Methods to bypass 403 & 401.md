---
title: Methods to bypass 403 & 401
url: https://infosecwriteups.com/methods-to-bypass-403-401-38df4cec069e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-24
fetch_date: 2025-10-06T19:14:50.840468
---

# Methods to bypass 403 & 401

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F38df4cec069e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmethods-to-bypass-403-401-38df4cec069e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmethods-to-bypass-403-401-38df4cec069e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-38df4cec069e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-38df4cec069e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Methods to bypass 403 & 401

[![cryptoshant🇮🇳](https://miro.medium.com/v2/resize:fill:64:64/1*WB_W42RWlz5rAUWNCTByiw.png)](https://medium.com/%40dsmodi484?source=post_page---byline--38df4cec069e---------------------------------------)

[cryptoshant🇮🇳](https://medium.com/%40dsmodi484?source=post_page---byline--38df4cec069e---------------------------------------)

5 min read

·

Nov 23, 2024

--

Listen

Share

Hello Hackers, today in this write-up I am going to give you all things you need to know to bypass 403 & 401 error page, some automation tools, tips and tricks, medium articles, hackerone disclosed reports all the thing so let’s get started.

Press enter or click to view image in full size

![]()

credit:copilot

**What is the difference between 403 & 401 Errors?**

**• 401 Unauthorized:** This error indicates the need for authentication. It often appears when a user isn’t logged in or lacks permission to access the resource.

**• 403 Forbidden:** This code shows that while the server understands the request, it refuses to authorize it. Even an authenticated user might encounter this error due to permissions or IP restrictions.

Now I hope you understand the difference between 403 & 401 error message :) Now let’s dive into some techniques you can use to bypass:

**Common Techniques for Bypassing 403/401 Pages**

**1)** **URL Manipulation:** To test you can see following test case to bypass this type of restrictions. Now for understanding let’s say admin panel is restricted to access so we can use following test cases to bypass this restriction.

· **/admin -> 403**

**· /Admin -> 200**

**· /AdMin -> 200**

**· /admin/ -> 200**

**· /admin/. -> 200**

**· //admin// -> 200**

**· /.;/admin -> 200**

**· /./admin/.. -> 200**

**· /admin.json -> 200**

**· /;/admin -> 200**

**· //;//admin -> 200**

**· /admi%6e -> 200 [n is url encoded to %6e]**

**· /%2e/admin -> 200**

**· /admin..;/ -> 200**

**You can also do fuzzing to this endpoints like this:**

**· /FUZZ/admin**

**· /admin/FUZZ**

**· /adminFUZZ**

Sometimes /admin is not accessible but /admin/users may be accessible so to give some times to fuzzing is also fruitful.

**2)** **Header Manipulation:** In this method you can also use param Miner tool in burp suite to guess headers in the request. You can use following test cases:

Like if our get request looks something like this:

```
GET /admin HTTP/1.1
Host: target.com => 403 Forbidden
```

Now if application supports headers like x-original-url, x-rewrite-url etc. then you can test manually in this way in burp.

```
GET /anything HTTP/1.1
Host: target.com
X-Original-URL: /admin

OR

GET /anything HTTP/1.1
Host: target.com
X-Rewrite-URL: /admin
```

There are more headers you can use something like this:

· **X-Originating-IP: 127.0.0.1**

· **X-Forwarded-For: 127.0.0.1**

· **X-Forwarded: 127.0.0.1**

· **Forwarded-For: 127.0.0.1**

· **X-Remote-IP: 127.0.0.1**

· **X-Remote-Addr: 127.0.0.1**

· **X-ProxyUser-Ip: 127.0.0.1**

· **X-Original-URL: 127.0.0.1**

· **Client-IP: 127.0.0.1**

· **True-Client-IP: 127.0.0.1**

· **Cluster-Client-IP: 127.0.0.1**

· **X-ProxyUser-Ip: 127.0.0.1**

· **Host: localhost**

**3)** **Parameter Tampering:** In this type you can clearly see parameter which are given in false you can manually true it to access the page something like if the **isAdmin=false** parameter is set to false you can simply change it to true like **isAdmin=true** to access the resources. There is one more example like if the parameter value is set to be restricted like: **?view=restricted** you can simply change it to **?view=public.** You can also remove parameters which restrict you to access the page. So this is all about parameter tampering.

**4)** **HTTP Method Switching:** If you cannot access the resource using **GET** method then try to change the method like use **HEAD, POST, PUT, TRACE, OPTIONS, DELETE, PATCH.**

Request looks something like this:

```
GET /admin HTTP/1.1
Host: target.com
```

Change method like this way:

```
POST /admin HTTP/1.1
Host: target.com
```

If the application supports method override header then you can also test like this way:

```
POST /admin HTTP/1.1
Host: target.com
X-http-method-override: GET

Or

X-http-override: GET
```

Thus you can override the method and if WAF not configured properly then you can able to bypass.

**5)** **Automation Tools:** Now let’s come with most people interested topic automation! So there are already many tools for bypass this bad 403 & 401 but here I will give some tools which are more popular and industry recognized.

· So the first tool is built in burpsuite you can simply download in burp by going to **burp extensions -> BApp store -> 403 Bypasser** see below image:

Press enter or click to view image in full size

![]()

[## GitHub - iamj0ker/bypass-403: A simple script just made for self use for bypassing 403

### A simple script just made for self use for bypassing 403 - iamj0ker/bypass-403

github.com](https://github.com/iamj0ker/bypass-403?source=post_page-----38df4cec069e---------------------------------------)

[## GitHub - Dheerajmadhukar/4-ZERO-3: 403/401 Bypass Methods + Bash Automation + Your Support ;)

### 403/401 Bypass Methods + Bash Automation + Your Support ;) - Dheerajmadhukar/4-ZERO-3

github.com](https://github.com/Dheerajmadhukar/4-ZERO-3?source=post_page-----38df4cec069e---------------------------------------)

[## GitHub - diablo-101/403-bypass

### Contribute to diablo-101/403-bypass development by creating an account on GitHub.

github.com](https://github.com/diablo-101/403-bypass?source=post_page-----38df4cec069e---------------------------------------)

**Note: My personal opinion please don’t rely on one tool use multiple tools to get better output. Because sometime one tool can’t give access but other one give you this happens so use multiple tools.**

**6) New Method:** Actually I think this write-up explain you in better way he find out this method so go and read this articl...