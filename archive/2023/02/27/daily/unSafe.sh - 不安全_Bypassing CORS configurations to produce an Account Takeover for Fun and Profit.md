---
title: Bypassing CORS configurations to produce an Account Takeover for Fun and Profit
url: https://buaq.net/go-151067.html
source: unSafe.sh - 不安全
date: 2023-02-27
fetch_date: 2025-10-04T08:09:57.414753
---

# Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Bypassing CORS configurations to produce an Account Takeover for Fun and Profit

The bug that is being written about here is from an previous bug bounty engagement for a major telec
*2023-2-26 21:9:59
Author: [infosecwriteups.com(查看原文)](/jump-151067.htm)
阅读量:16
收藏*

---

The bug that is being written about here is from an previous bug bounty engagement for a major telecommunication company. This bug consists of a CORS misconfiguration that isn’t commonly a misconfiguration unless certain conditions are met. First for individuals who aren’t familiar with CORS technology, CORS stands for Cross Origin Resource Sharing and is a common method to bypass SOP for developers in order to retrieve information across multiple domains. CORS works by facilitating certain headers in the initial request and requires certain headers being available in the server response. The request specifies the Origin Header which declares the site that is making the request to the server in question. The relevant headers located on the server are the Access-Control-Allow-Origin headers and the Access-Control-Allow-Credentials header. Access-Control-Allow-Origin specifies the value that is located in the request’s Origin header and is only reflected in the server response if that Origin is allowed to make requests to the server. The Access-Control-Allow-Credentials header is in place in order to specify that the request made includes cookie values for the server in question. An CORS vulnerability occurs when two conditions are present, the first condition is that an attacker can specify the value in the Origin header and that value is accepted by the server and reflected in the Access-Control-Allow-Origin headers. The second condition being that the Access-Control-Allow-Credentials header is set to True, allowing cookies in the request to be utilized by the server. After these conditions are set an attacker can get a user of the server to go to his site and leak sensitive information from the that user’s session from the server in question.

When looking for this bug I noticed that a server was returning sensitive information in the response of an logged in user. This information included the id token, refresh token and the server authentication token. The server authentication token is the value that was being used in order to authenticate the user to the server. The server’s response also included an Access-Control-Allow-Origin and a Access-Control-Allow-Credentials header set to True. This information was being returned on every response from the server.

In this particular scenario the second condition was met, but the first condition wasn’t present. Instead of the Access-Control-Allow-Origin header being set to the value in the Origin it was permanently set to a wildcard. A wildcard in the header essentially means that any site can request information from the server cross domain, however if the Access-Control-Allow-Origin header is set to a wildcard the Access-Control-Allow-Credentials header will not be included in the server response. This was created as a security boundary to the overly permissive nature of the wildcard value. This is a problem due to the fact that the impact of a CORS vulnerability is usually a disclosure of sensitive information from a session. If the Access-Control-Allow-Credentials header isn’t available its the same as logging into an application without a session.

There is a small caveat to this rule however and it allows for this security boundary to be bypassed. If the HTTP response contains the Access-Control-Allow-Origin header with a wildcard as its value and it also doesn’t contain an Cache Control header with a value of no store, it is possible to send a request to a endpoint in question to retrieve the response from the cache instead of the website directly if a logged in user has already visited that endpoint. In this scenario, every page on this site contained the sensitive data in the HTTP response with the required headers. I selected a page that was apart of the login flow of the site to guarantee that if the user was logged in previously, that page had to be cached in the browser. The way to exploit this client side bug is utilize the fetch javascript library and change the cache option to force-cache and host the script on a malicious server.

Example POC for this bug

After a logged in user of the vulnerable site visit the site the script will fetch the response of the page from the browser along with sensitive data in the response. In this case it was the server authentication token which allowed for a full account takeover of the logged in user.

Connect with me on Twitter: @Pullerze

文章来源: https://infosecwriteups.com/bypassing-cors-configurations-to-produce-an-account-takeover-for-fun-and-profit-3e50c3f2a124?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)