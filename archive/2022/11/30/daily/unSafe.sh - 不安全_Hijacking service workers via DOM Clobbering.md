---
title: Hijacking service workers via DOM Clobbering
url: https://buaq.net/go-137773.html
source: unSafe.sh - 不安全
date: 2022-11-30
fetch_date: 2025-10-04T00:02:56.168925
---

# Hijacking service workers via DOM Clobbering

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

![](https://8aqnet.cdn.bcebos.com/512ba572b34b98baa56fb0b8f97c889d.jpg)

Hijacking service workers via DOM Clobbering

Published: 29 November 2022 at 14:00 UTC
*2022-11-29 22:0:2
Author: [portswigger.net(查看原文)](/jump-137773.htm)
阅读量:56
收藏*

---

![Gareth Heyes](https://portswigger.net/content/images/profiles/callout_gareth_heyes_114px.png)

* **Published:** 29 November 2022 at 14:00 UTC
* **Updated:** 29 November 2022 at 14:00 UTC

![An illustration showing a service worker with a stop sign and a car rushing past with a skull on the door.](https://portswigger.net/cms/images/31/1a/f7eb-article-service-workers_blog-article.png)

In this post, we'll briefly review how service worker hijacking works, then introduce a variant that can be triggered via DOM clobbering thanks to a quirk in `document.getElementById()`.

### Understanding service workers

Many websites use service workers (SWs) to provide caching and offline capabilities. Web pages often pass information to service workers using query parameters, as SWs don't have access to the parent page's DOM. If these parameters are handled insecurely, this can lead to malicious JavaScript execution inside the SW as noted by the ["Security Study of Service Worker Cross-Site Scripting"](https://dl.acm.org/doi/fullHtml/10.1145/3427228.3427290) paper. Although rare, this vulnerability has a much higher impact than typical XSS as it enables permanent client-side site takeover.

### Hijacking service workers

This technique to hijack a service worker enables three key outcomes:

* HTML filter evasion
* Bypassing [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy)
* Escalating XSS

The `importScripts()` function lies at the heart of this vulnerability - it allows a SW to retrieve JavaScript from a different domain. In the example below an attacker can control the host query parameter, which can then lead to full control over the script that gets imported and therefore full control over the website responses.

In order to exploit these types of vulnerabilities, you need two components:

* One - control over a query string parameter that is passed to the SW.
* Two - an `importScripts()` function call inside the SW that can be influenced by the query string parameter.

index.html:

`<script>`

sw.js:

`const searchParams = new URLSearchParams(location.search);
let host = searchParams.get('host');
self.importScripts(host + "/sw_extra.js");
//host can be controllable by an attacker`

Using this knowledge we went hunting for bugs using Puppeteer and [DOM Invader](https://portswigger.net/blog/introducing-dom-invader)

We scanned multiple bug bounty sites and found one site using a SW inside an iframe - they were passing URL parameters to the SW from the framed document. DOM Invader immediately flagged this behaviour but, thankfully for the site they did not allow you to inject the SW from the top-level window. The code looked like this:

`navigator.serviceWorker.register('https://redacted&_flasher_manifest_=https://redacted/@xconfig/flasher_classic/manifestysvoy7p7location.href')`

DOM Invader generated a random token inside the location.href source which was then passed to `serviceWorker.register()` sink. This behaviour was then reported in the augmented DOM. We had configured DOM Invader to automatically inject the canary into all sources, but this didn't yield many results. So we decided to take another approach - what if we looked for all service worker registrations that used query parameters instead? This would identify potentially vulnerable SWs, but would require further investigation to see if they were exploitable - this led to an interesting discovery ...

### Service worker clobbering

We found that a major website was using <div> elements to pass information to a SW script. They were doing this by using the `innerText` of a `<div>` element with an id of "cdnDomain":

`<div style="display: none;" id="cdnDomain">example.com</div>`

This is bad because if you can use [DOM Clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering)  to clobber the variable, you could then get control over the SW domain. In fact, this is slightly different to a normal DOM Clobbering attack since the code was using `document.getElementById()` and `innerText`. If you could inject a HTML element before the `<div>` element then you could control the CDN domain - this would mean you could control the contents of the SW script. This could result in full control over the website's responses whilst bypassing a HTML filter, or evading CSP and escalating a [reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected). Here's what the code looked like:

Later the SW register method was used passing this domain:

/sw?cdnDomain=example.com

Then the SW itself was using the domain to load some scripts:

`` importScripts(`${n}/versionless/workbox-v${s.e}/workbox-sw.js`) ``

At first we thought you would require an element before the cdnDomain div in order to exploit it, however we discovered that's not necessarily the case. You can clobber the results of a `document.getElementById()` call if you inject a `<html>` or `<body>` tag with the same id attribute. Here's an example:

`<div style=display:none id=cdnDomain>test</div>
<p>
<html id="cdnDomain">clobbered</html>
<script>
alert(document.getElementById('cdnDomain').innerText);//clobbbered
</script>`

What's also interesting is that you can hide elements from `innerText`, so if you inject a HTML/body tag you can use styles to hide it from `innerText` to prevent other text from interfering with your attack:

`<div style=display:none id=cdnDomain>test</div>
<p>existing text</p>
<html id="cdnDomain">clobbered</html>
<style>
p{display:none;}
</style>
<script>
alert(document.getElementById('cdnDomain').innerText);//clobbbered
</script>`

We looked at SVG too and it's possible to use the `<body>` tag there:

`<div style=display:none id=cdnDomain>example.com</div>
<svg><body id=cdnDomain>clobbered</body></svg>
<script>
alert(document.getElementById('cdnDomain').innerText)//clobbered
</script>`

You need a `<foreignobject>` tag in order to use the HTML tag inside SVG on both Chrome and Firefox:

`<div style=display:none id=cdnDomain>example.com</div>
<svg>
<foreignobject>
<html id=cdnDomain>clobbered</html>
</foreignobject>
</svg>
<script>
alert(document.getElementById('cdnDomain').innerText)//clobbered
</script>`

### Finding service worker injection with DOM Invader

In order to find SW injection you simply need to place the canary in the query string, or configure DOM Invader to [inject the canary into all sources](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/configuration/general#inject-canary-into-all-sources). Then DOM Invader will show the new sink called "serviceWorker.register" if it finds a vulnerable function call:

![Screenshot showing the augmented DOM](https://portswigger.net/cms/images/06/f6/9f47-article-service-worker-augmented-dom.png)

We've created a [test case](https://portswigger-labs.net/dom-invader/testcases/augmented-dom-import-scripts/) which demonstrates this issue. Note that this is only flagging that the query string is being passed to the SW, further investigation is required to see if this query string is parsed and then used with something like `importScripts()` inside the SW.

DOM Invader can help you find SW injection by manipulating the query string. However, in more complex cases or bug chains, you might want to configure DOM Invader to only show you SW registrations and have a blank canary to see all calls to it. You can...