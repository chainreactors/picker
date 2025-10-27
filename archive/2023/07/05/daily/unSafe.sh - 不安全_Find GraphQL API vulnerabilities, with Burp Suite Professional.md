---
title: Find GraphQL API vulnerabilities, with Burp Suite Professional
url: https://buaq.net/go-171194.html
source: unSafe.sh - 不安全
date: 2023-07-05
fetch_date: 2025-10-04T11:52:22.962946
---

# Find GraphQL API vulnerabilities, with Burp Suite Professional

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

![](https://8aqnet.cdn.bcebos.com/ea9c4a8b77a416ba32dc654927dfa4e0.jpg)

Find GraphQL API vulnerabilities, with Burp Suite Professional

Gareth Heyes |04 July 2023 at 13:
*2023-7-4 21:0:0
Author: [portswigger.net(查看原文)](/jump-171194.htm)
阅读量:33
收藏*

---

Gareth Heyes |
04 July 2023 at 13:00 UTC

![Showing a radar with the GraphQL logo in the middle with submarines for each GraphQL detection type such as introspection](https://portswigger.net/cms/images/a3/0c/b5bf-article-graphql-article.png)

As a penetration tester, you need your tools to find the latest vulnerabilities. [GraphQL](https://portswigger.net/web-security/graphql) APIs are widely used on today’s websites, and expose attack surface for a wide range of security issues.

Burp Scanner’s new GraphQL checks will automatically report many instances of GraphQL vulnerabilities on your penetration tests. [Get the latest version of Burp Suite Professional](https://portswigger.net/burp/releases/professional-community-2023-6), and start finding these issues today.

## GraphQL scan checks

We added support for GraphQL in Burp Suite to enable you to detect known endpoints, find hidden endpoints, detect when introspection or suggestions are enabled, and report when an endpoint does not validate the content type.

### Finding known endpoints

It can be tedious to manually trawl through a web site to determine the GraphQL endpoint. We've made this easier by getting [Burp Scanner](https://portswigger.net/burp/vulnerability-scanner) to do the work for you. We've defined some passive and active scan checks to find known endpoints automatically, allowing you to focus on finding the vulnerabilities.

### Finding hidden endpoints

Sometimes a developer will deploy a GraphQL endpoint without using it on the site - for example, if it was accidentally deployed to production. Burp Suite will look for common endpoints and find hidden GraphQL deployments even without the site using it. These endpoints could be a valuable resource for a tester, as it's likely a vulnerability will be found if it's an accidental deployment.

### Detecting introspection

Introspection allows you to run a query on the actual schema to see what queries it supports. It's often turned off in production because a site might not want to expose the inner workings of its API to the world. Burp will detect if introspection is enabled - although this isn't a vulnerability in itself, it could be useful for a tester to aid testing the site and useful for a developer to remind them to turn it off in production.

### Detecting suggestions

Some GraphQL servers like Apollo will make suggestions when you make an invalid query, to help you construct a valid one. This can be used by a tester to discover the underlying schema by using a dictionary of words and the suggestion response as an oracle, even when introspection is disabled. A tool such as [clairvoyance](https://github.com/nikitastupin/clairvoyance) can be used to construct a valid schema from a dictionary. Burp will enable you to find endpoints that have suggestions enabled and report them.

### Invalidated content type

Most GraphQL endpoints use a POST method with an application/json content type. If the content type is validated correctly, then a browser can't make this request without using [CORS](https://portswigger.net/web-security/cors) as it will be unable to send the correct content type. This makes the endpoint secure against [CSRF](https://portswigger.net/web-security/csrf). However, if a site does not validate the content type and does not implement some form of CSRF token, it could be possible to abuse the GraphQL endpoint by forging requests provided mitigations like [SameSite](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions) cookies can be bypassed or neutralized because of the SameSite None flag. Burp will report if it's possible to forge the request to the endpoint using a GET request or application/x-www-form-urlencoded POST request.

## Try it out for yourself

If you want to learn more about GraphQL - including an overview of how it works, discovery and exploitation techniques, and how GraphQL vulnerabilities can lead to information disclosure and CSRF -  take a look at the Web Security Academy. We've prepared thorough [learning materials](https://portswigger.net/web-security/graphql/) and [interactive labs](https://portswigger.net/web-security/graphql/lab-graphql-reading-private-posts) where you can practise your skills - go check them out!

![Gareth Heyes](https://portswigger.net/cms/profiles/gareth-heyes.png)

文章来源: https://portswigger.net/blog/find-graphql-api-vulnerabilities-with-burp-suite-professional
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)