---
title: HTTP/3 connection contamination: an upcoming threat?
url: https://buaq.net/go-131703.html
source: unSafe.sh - 不安全
date: 2022-10-20
fetch_date: 2025-10-03T20:21:02.672611
---

# HTTP/3 connection contamination: an upcoming threat?

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

![](https://8aqnet.cdn.bcebos.com/54d9e6d2bb81413af9c61f22bf59b8a5.jpg)

HTTP/3 connection contamination: an upcoming threat?

Published: 19 October 2022 at 13:28 UTC
*2022-10-19 21:28:9
Author: [portswigger.net(查看原文)](/jump-131703.htm)
阅读量:41
收藏*

---

![James Kettle](https://portswigger.net/content/images/profiles/callout_james_kettle_112px.png)

* **Published:** 19 October 2022 at 13:28 UTC
* **Updated:** 19 October 2022 at 13:28 UTC

![](https://portswigger.net/cms/images/e3/83/565c-article-http_3_connection_contamination__article.png)

I [recently documented](https://portswigger.net/research/browser-powered-desync-attacks#anomalies) a dangerous reverse-proxy behaviour called first-request routing, which enables [host-header attacks](https://portswigger.net/web-security/host-header) on back-end systems. In this post, I'll show how first-request routing also enables a client-side, browser-based attack called HTTP connection contamination. This technique works on systems running HTTP/2, and is likely to become a greater threat with the advent of HTTP/3.

Web browsers have a shiny feature called [connection coalescing](https://daniel.haxx.se/blog/2016/08/18/http2-connection-coalescing), which lets them reuse a single HTTP/2+ connection for requests going to different websites, provided that the sites resolve to the same IP address and use a TLS certificate valid for both hostnames.

First-request routing is a dangerous reverse-proxy behaviour where the proxy analyses the first request on a connection to work out which back-end end to route it to, and then sends all subsequent requests on that connection to the same back-end.

Connection coalescing and first-request routing do not play well together. For example, imagine secure.example.com and wordpress.example.com are both sat behind a reverse proxy using a certificate valid for \*.example.com:

`$ nslookup wordpress.example.com
52.16.179.7 // reverse proxy that supports HTTP/2 and does first-request routing

$ nslookup secure.example.com
52.16.179.7 // same reverse proxy

$ openssl s_client -connect x.portswigger-labs.net:443
subject=/CN=*.example.com // wildcard TLS certificate`

If a browser tries to send a request to wordpress.example.com followed by secure.example.com, browser connection coalescing will force both requests down a single connection to the front-end. First-request routing will result in the  request to secure.example.com incorrectly being routed to the WordPress back-end. This means that if you find [XSS](https://portswigger.net/web-security/cross-site-scripting) on wordpress.example.com, you can use it to compromise secure.example.com!

`// create HTTP/2+ connection
fetch('https://wordpress.example.com/', {credentials: 'include'})

// connection coalescing will force this down the same connection...
// ...leading to the front-end misrouting it to WordPress
// the browser thinks our injected JS is coming from secure.example.com
// exposing saved passwords, cookies, etc.
location='https://secure.example.com/plugin/x?q=<script>stealPasswords()'`

You can explore connection coalescing for yourself by using the Timing graph under the Network tab in Chrome's developer tools (or using WireShark if you're a masochist). Issue request pairs using fetch() and see if the graph shows time spent on 'Initial connection' for the second request, and if the Connection ID column matches:

`fetch('//sub1.hackxor.net/', {mode: 'no-cors', credentials: 'include'}).then(()=>{ fetch('//sub2.hackxor.net/', {mode: 'no-cors', credentials: 'include'}) })`

![](https://portswigger.net/cms/images/d7/ca/b7cf-article-screenshot_2022-10-17_at_15.17.28.png)

I haven't invested the time required to explore this threat in depth or scan for it in the wild as I believe it's currently rare for two reasons. Firstly, first-request routing is relatively uncommon and HTTP/2's implementation complexity means there's only a small pool of unique HTTP/2 servers relative to HTTP/1.1. Secondly, connection coalescing means HTTP/2 servers performing first-request routing may intermittently break for genuine visitors, so the owners may end up fixing the vulnerability without attacker encouragement.

That said, it's not all bad news for attackers. HTTP/3 proposes [removing the requirement for an IP address match](https://www.rfc-editor.org/rfc/rfc9114.html#name-connection-reuse), which will expose everyone with a front-end that uses first-request routing and has a certificate valid for multiple hosts.

This also creates a second risk which isn't related to first-request routing - it means a compromised server with a wildcard certificate no longer requires an MITM to exploit. In effect, this greatly increases the pool of malicious actors who could profit from it.

To avoid these risks before they become a reality, ensure your reverse proxies don't perform first-request routing. You can test for this manually in Repeater by enabling HTTP/1 and HTTP/2 connection reuse, and also scan for it using the 'Connection-State' attack in [HTTP Request Smuggler](https://github.com/PortSwigger/http-request-smuggler). Also, be aware that while wildcard TLS certificates have never been ideal, HTTP/3 means a compromised server with a wildcard certificate can now be used to attack sibling domains without an active MITM.

These new threats continue the ongoing trend of web infrastructure descending into a heavily intertwined mess where a weakness in any individual site has numerous non-obvious knock-on effects on the security of the overall system. It'll be interesting to see how these risks play out in practice.

[Back to all articles](https://portswigger.net/research/articles)

文章来源: https://portswigger.net/research/http-3-connection-contamination
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)