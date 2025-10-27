---
title: Google to Block Entrust Certificates in Chrome Starting November 2024
url: https://buaq.net/go-247933.html
source: unSafe.sh - 不安全
date: 2024-06-30
fetch_date: 2025-10-06T16:54:42.007991
---

# Google to Block Entrust Certificates in Chrome Starting November 2024

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

![](https://8aqnet.cdn.bcebos.com/1b0d8e7edd0a40de2e3ef166f3a4919b.jpg)

Google to Block Entrust Certificates in Chrome Starting November 2024

Cybersecurity / Website SecurityGoogle has announced that it's going to start blocking websites th
*2024-6-29 22:44:0
Author: [thehackernews.com(查看原文)](/jump-247933.htm)
阅读量:9
收藏*

---

Cybersecurity / Website Security

[![Entrust Certificates](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlMAsddqUjGX7TfV6NLi0fcMXLazmyyxR-Z6bogM2rj73p_wbsGDzWp7mQxPlzpUMhBIhRpqC1mLlYCUSsT8aBEZuPP-wwR8qvAstyWU2NIUNWcWa4RqJYgVNbuO4wvebfKB5LvpjGJvFHh8z3FHSZIIN7QdENWbHmHHrdZ47px7V0hvUjIdPC4pqGjiBx/s728-rw-e365/dv.png "Entrust Certificates")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlMAsddqUjGX7TfV6NLi0fcMXLazmyyxR-Z6bogM2rj73p_wbsGDzWp7mQxPlzpUMhBIhRpqC1mLlYCUSsT8aBEZuPP-wwR8qvAstyWU2NIUNWcWa4RqJYgVNbuO4wvebfKB5LvpjGJvFHh8z3FHSZIIN7QdENWbHmHHrdZ47px7V0hvUjIdPC4pqGjiBx/s728-rw-e365/dv.png)

Google has announced that it's going to start blocking websites that use certificates from Entrust starting around November 1, 2024, in its Chrome browser, citing compliance failures and the certificate authority's inability to address security issues in a timely manner.

"Over the past several years, publicly disclosed [incident reports](https://bugzilla.mozilla.org/buglist.cgi?o2=greaterthaneq&short_desc_type=casesubstring&o1=notequals&v1=Graveyard&classification=Client%20Software&classification=Developer%20Infrastructure&classification=Components&classification=Server%20Software&classification=Other&classification=Graveyard&v2=2015-11-01&f1=classification&bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&short_desc=Entrust&f2=creation_ts&component=CA%20Certificate%20Compliance&query_format=advanced&list_id=17064895) highlighted a [pattern of concerning behaviors](https://wiki.mozilla.org/CA/Entrust_Issues) by Entrust that fall short of the above expectations, and has eroded confidence in their competence, reliability, and integrity as a publicly-trusted [[certificate authority](https://en.wikipedia.org/wiki/Certificate_authority)] owner," Google's Chrome security team [said](https://security.googleblog.com/2024/06/sustaining-digital-certificate-security.html).

To that end, the tech giant said it intends to no longer trust TLS server authentication certificates from Entrust starting with Chrome browser versions 127 and higher by default. However, it said that these settings can be overridden by Chrome users and enterprise customers should they wish to do so.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPFFLXZHfTA0FUmsAJ30SeqiM34x3Qes8BjBSTnhm4zHUJUal87CZLGZFJ7f5vxdaZIyNeTzf7fA-8s0CQhiG9ltxRFReWpgvmp2VfSMbjmN8i0yCv_74a3h7HaGxNlFqr5LEyPghIcxNNfXkksw3nQvKsqKKAU4wsl5Ll9UKu2hv6fbtXy4PHGNBW8SxC/s1200/a_d.png)](https://thehackernews.uk/auditboard-it-risk-now "Cybersecurity")

Google further noted that certificate authorities play a privileged and trusted role in ensuring encrypted connections between browsers and websites, and that Entrust's lack of progress when it comes to publicly disclosed incident reports and unrealized improvement commitments poses risks to the internet ecosystem.

The blocking action is expected to cover Windows, macOS, ChromeOS, Android, and Linux versions of the browser. The notable exception is Chrome for iOS and iPadOS, due to Apple's policies that don't permit the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md) from being used.

As a result, users navigating to a website that serves a certificate issued by Entrust or AffirmTrust will be greeted by an [interstitial message](https://untrusted-root.badssl.com/) that warns them that their connection is not secure and isn't private.

Affected website operators are urged to move to a publicly-trusted certificate authority owner to minimize disruption by October 31, 2024. According to Entrust's website, its solutions are used by Microsoft, Mastercard, VISA, and VMware, among others.

"While website operators could delay the impact of blocking action by choosing to collect and install a new TLS certificate issued from Entrust before Chrome's blocking action begins on November 1, 2024, website operators will inevitably need to collect and install a new TLS certificate from one of the many other CAs included in the Chrome Root Store," Google said.

Found this article interesting? Follow us on [Twitter **](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

文章来源: https://thehackernews.com/2024/06/google-to-block-entrust-certificates-in.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)