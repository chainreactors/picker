---
title: Burp-Dom-Scanner - Burp Suite's Extension To Scan And Crawl Single Page Applications
url: https://buaq.net/go-167089.html
source: unSafe.sh - 不安全
date: 2023-06-04
fetch_date: 2025-10-04T11:44:27.986883
---

# Burp-Dom-Scanner - Burp Suite's Extension To Scan And Crawl Single Page Applications

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

![](https://8aqnet.cdn.bcebos.com/46e858c195d09dee5dd0c27e4b29bd21.jpg)

Burp-Dom-Scanner - Burp Suite's Extension To Scan And Crawl Single Page Applications

It's a Burp Suite's extension to allow for recursive crawling and scanning of Single Page Ap
*2023-6-3 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-167089.htm)
阅读量:44
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhtt_dhS9x6uC9XEmaqeYTJ_l8Uk5-bckUzFjcjfVBV94bsSYfpQOFinRuxOfb_YHLEhB49803ZYndVEWrUDl8jyVCsLUnk7yzPkHq002Gp7FFYS3WQ3AF1M_s1ZETb3apTrKzLZ-D57oZfgGRGgxyqO-vn0aLxiiwxokk9m9PXSikgp7eT_upTqVL1iA=w640-h404)](https://blogger.googleusercontent.com/img/a/AVvXsEhtt_dhS9x6uC9XEmaqeYTJ_l8Uk5-bckUzFjcjfVBV94bsSYfpQOFinRuxOfb_YHLEhB49803ZYndVEWrUDl8jyVCsLUnk7yzPkHq002Gp7FFYS3WQ3AF1M_s1ZETb3apTrKzLZ-D57oZfgGRGgxyqO-vn0aLxiiwxokk9m9PXSikgp7eT_upTqVL1iA)

It's a Burp Suite's extension to allow for recursive [crawling](https://www.kitploit.com/search/label/Crawling "crawling") and [scanning](https://www.kitploit.com/search/label/Scanning "scanning") of Single Page Applications.

It requires node and [DOMDig](https://github.com/fcavallarin/domdig "DOMDig").

Latest release can be downloaded [here](https://github.com/fcavallarin/burp-dom-scanner/releases/latest/download/burp-dom-scanner.jar "here")

1. Install [node](https://nodejs.org "node")
2. Install [DOMDig](https://github.com/fcavallarin/domdig "DOMDig")
3. Download and load the extension
4. Set both the path of `node`'s executable and the path of `domdig.js` in the extension's UI.

Burp DOM Scanner uses [DOMDig](https://github.com/fcavallarin/domdig "DOMDig") as the crawling and scanning engine.

## DOMDig

DOMDig is a DOM [XSS scanner](https://www.kitploit.com/search/label/XSS%20scanner "XSS scanner") that runs inside the Chromium web browser and it can scan single page applications (SPA) recursively. Unlike other scanners, DOMDig can crawl any webapplication (including gmail) by keeping track of DOM modifications and XHR/fetch/websocket requests and it can simulate a real user interaction by firing events. During this process, XSS payloads are put into input fields and their execution is tracked in order to find [injection](https://www.kitploit.com/search/label/Injection "injection") points and the related URL modifications.

## Usage and Details

Details about usage, performed checks and reported vulnerabilities, can be found at [DOMDig's page](https://github.com/fcavallarin/domdig "DOMDig's page")

Burp-Dom-Scanner - Burp Suite's Extension To Scan And Crawl Single Page Applications
![Burp-Dom-Scanner - Burp Suite's Extension To Scan And Crawl Single Page Applications](https://blogger.googleusercontent.com/img/a/AVvXsEhtt_dhS9x6uC9XEmaqeYTJ_l8Uk5-bckUzFjcjfVBV94bsSYfpQOFinRuxOfb_YHLEhB49803ZYndVEWrUDl8jyVCsLUnk7yzPkHq002Gp7FFYS3WQ3AF1M_s1ZETb3apTrKzLZ-D57oZfgGRGgxyqO-vn0aLxiiwxokk9m9PXSikgp7eT_upTqVL1iA=s72-w640-c-h404)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/burp-dom-scanner-burp-suites-extension.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)