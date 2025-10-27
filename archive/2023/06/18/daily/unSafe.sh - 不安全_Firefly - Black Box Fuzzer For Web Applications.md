---
title: Firefly - Black Box Fuzzer For Web Applications
url: https://buaq.net/go-169182.html
source: unSafe.sh - 不安全
date: 2023-06-18
fetch_date: 2025-10-04T11:44:36.532172
---

# Firefly - Black Box Fuzzer For Web Applications

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

Firefly - Black Box Fuzzer For Web Applications

Firefly is an advanced black-box fuzzer and not just a standard asset discovery tool. Firefl
*2023-6-17 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-169182.htm)
阅读量:58
收藏*

---

Firefly is an advanced black-box fuzzer and not just a standard [asset discovery](https://www.kitploit.com/search/label/Asset%20Discovery "asset discovery") tool. Firefly provides the advantage of testing a target with a large number of built-in checks to detect behaviors in the target.

**Note:**

> Firefly is in a very new stage (v1.0) but works well for now, if the target does not contain too much dynamic content. Firefly still detects and filters dynamic changes, but not yet perfectly.

* Hevy use of gorutines and internal hardware for great preformance
* Built-in engine that handles each task for "x" response results inductively
* Highly cusomized to handle more complex fuzzing
* Filter options and request verifications to avoid junk results
* Friendly error and debug output
* Build in payloads (default list are mixed with the wordlist from [seclists](https://github.com/danielmiessler/SecLists "seclists"))
* Payload tampering and [encoding](https://www.kitploit.com/search/label/Encoding "encoding") functionality

If the above install method do not work try the following:

```
git clone https://github.com/Brum3ns/firefly.git
```

### Simple

```
firefly -u 'http://example.com/?query=FUZZ'
```

---

Firefly - Black Box Fuzzer For Web Applications
![Firefly - Black Box Fuzzer For Web Applications](https://blogger.googleusercontent.com/img/a/AVvXsEjsx3rOr6wPr2Wv7RBML1CS5kSIvfyvivKt-F0AszVt8EEfdgphNX2r4ZgLaAGn2kOEG9ui7FFyzVK0I5PZdxIhgAjFt5RWM4WScpDn-92ihpJQwEYxbUOwjD1s4hXf3DHW3npCnnlPIqn9B-jexV4GrBccwfhsWiA3GBOXitDO1RONOpDZty1VaEDjDw=s72-w464-c-h640)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/firefly-black-box-fuzzer-for-web.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)