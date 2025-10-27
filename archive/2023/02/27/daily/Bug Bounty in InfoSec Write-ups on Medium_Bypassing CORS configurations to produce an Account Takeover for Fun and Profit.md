---
title: Bypassing CORS configurations to produce an Account Takeover for Fun and Profit
url: https://infosecwriteups.com/bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit-3e50c3f2a124?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-27
fetch_date: 2025-10-04T08:10:41.919535
---

# Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3e50c3f2a124&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit-3e50c3f2a124&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit-3e50c3f2a124&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3e50c3f2a124---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3e50c3f2a124---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

[![Josh Fam](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)](https://pullerjsecu.medium.com/?source=post_page---byline--3e50c3f2a124---------------------------------------)

[Josh Fam](https://pullerjsecu.medium.com/?source=post_page---byline--3e50c3f2a124---------------------------------------)

4 min read

·

Feb 13, 2023

--

1

Listen

Share

![]()

The bug that is being written about here is from an previous bug bounty engagement for a major telecommunication company. This bug consists of a CORS misconfiguration that isn’t commonly a misconfiguration unless certain conditions are met. First for individuals who aren’t familiar with CORS technology, CORS stands for Cross Origin Resource Sharing and is a common method to bypass SOP for developers in order to retrieve information across multiple domains. CORS works by facilitating certain headers in the initial request and requires certain headers being available in the server response. The request specifies the Origin Header which declares the site that is making the request to the server in question. The relevant headers located on the server are the Access-Control-Allow-Origin headers and the Access-Control-Allow-Credentials header. Access-Control-Allow-Origin specifies the value that is located in the request’s Origin header and is only reflected in the server response if that Origin is allowed to make requests to the server. The Access-Control-Allow-Credentials header is in place in order to specify that the request made includes cookie values for the server in question. An CORS vulnerability occurs when two conditions are present, the first condition is that an attacker can specify the value in the Origin header and that value is accepted by the server and reflected in the Access-Control-Allow-Origin headers. The second condition being that the Access-Control-Allow-Credentials header is set to True, allowing cookies in the request to be utilized by the server. After these conditions are set an attacker can get a user of the server to go to his site and leak sensitive information from the that user’s session from the server in question.

Press enter or click to view image in full size

![]()

When looking for this bug I noticed that a server was returning sensitive information in the response of an logged in user. This information included the id token, refresh token and the server authentication token. The server authentication token is the value that was being used in order to authenticate the user to the server. The server’s response also included an Access-Control-Allow-Origin and a Access-Control-Allow-Credentials header set to True. This information was being returned on every response from the server.

In this particular scenario the second condition was met, but the first condition wasn’t present. Instead of the Access-Control-Allow-Origin header being set to the value in the Origin it was permanently set to a wildcard. A wildcard in the header essentially means that any site can request information from the server cross domain, however if the Access-Control-Allow-Origin header is set to a wildcard the Access-Control-Allow-Credentials header will not be included in the server response. This was created as a security boundary to the overly permissive nature of the wildcard value. This is a problem due to the fact that the impact of a CORS vulnerability is usually a disclosure of sensitive information from a session. If the Access-Control-Allow-Credentials header isn’t available its the same as logging into an application without a session.

There is a small caveat to this rule however and it allows for this security boundary to be bypassed. If the HTTP response contains the Access-Control-Allow-Origin header with a wildcard as its value and it also doesn’t contain an Cache Control header with a value of no store, it is possible to send a request to a endpoint in question to retrieve the response from the cache instead of the website directly if a logged in user has already visited that endpoint. In this scenario, every page on this site contained the sensitive data in the HTTP response with the required headers. I selected a page that was apart of the login flow of the site to guarantee that if the user was logged in previously, that page had to be cached in the browser. The way to exploit this client side bug is utilize the fetch javascript library and change the cache option to force-cache and host the script on a malicious server.

Press enter or click to view image in full size

![]()

Example POC for this bug

After a logged in user of the vulnerable site visit the site the script will fetch the response of the page from the browser along with sensitive data in the response. In this case it was the server authentication token which allowed for a full account takeover of the logged in user.

Connect with me on Twitter: @Pullerze

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----3e50c3f2a124---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----3e50c3f2a124---------------------------------------)

[Web Application Security](https://medium.com/tag/web-application-security?source=post_page-----3e50c3f2a124---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----3e50c3f2a124---------------------------------------)

[Cors](https://medium.com/tag/cors?source=post_page-----3e50c3f2a124---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3e50c3f2a124---------------------------------------)

[![InfoSec Write-ups](https://miro....