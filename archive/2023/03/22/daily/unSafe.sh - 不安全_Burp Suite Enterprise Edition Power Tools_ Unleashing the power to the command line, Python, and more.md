---
title: Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more
url: https://buaq.net/go-154576.html
source: unSafe.sh - 不安全
date: 2023-03-22
fetch_date: 2025-10-04T10:13:47.830631
---

# Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more

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

Burp Suite Enterprise Edition Power Tools: Unleashing the power to the command line, Python, and more

Ollie Whitehouse |21 March 2023 a
*2023-3-21 22:30:0
Author: [portswigger.net(查看原文)](/jump-154576.htm)
阅读量:60
收藏*

---

Ollie Whitehouse |
21 March 2023 at 14:30 UTC

### tl;dr

We have released BSEEPT - [Burp Suite Enterprise Edition Power Tools](https://github.com/olliewuk/bseept) which:

* Is a command line tool to drive all aspects of the BSEE [GraphQL API](https://portswigger.net/burp/extensibility/enterprise/graphql-api/index.html).
* Is a Python client library to allow you to easily utilise the BSEE GraphQL API in your own code be it command line tooling, lambdas, or integration layers.
* Returns BSEE's JSON allowing you to parse on the command line with `jq` and similar.

### Backstory

In January I joined PortSwigger in a more involved capacity as Non-Executive Director++ (the ++ being I can still code whilst sitting in the boardroom). In my first month I spent time coming up to speed on the products, their features, roadmaps, and most importantly their APIs for extensibility and similar.

These first months saw me produce two extension prototypes using the [Montoya API](https://github.com/PortSwigger/burp-extensions-montoya-api). These used the [Google Safe Browsing API to identify known malicious sites in sitemaps](https://gist.github.com/olliewuk/c518e820784d72cc8b1ce6f26be7a968) and a [YAML-powered regular expression engine to identify sensitive information presence / leakage](https://gist.github.com/olliewuk/8f8e563359261cdb322852c858810f60). I then had the fortune of working with Hannah and Alex on the [TOTP Authenticate](https://github.com/Hannah-PortSwigger/TOTPAuthenticate) extension to support multi-factor authentication in [Burp Suite Enterprise Edition](https://portswigger.net/burp/enterprise).

I then turned my attention to the [Burp Suite Enterprise Edition](https://portswigger.net/burp/enterprise) GraphQL API. It struck me that we had this amazing GraphQL API, which we both use in the product, but also expose to customers. But for DevOps teams and others in the security function to really utilize this required a bit of investment.

So an objective was born ... write the power tools that teams who work with Burp Suite Enterprise Edition would find valuable.

Que A-Team building music, over 80 commits, lots of learning (I learnt to use a Mac at the same time) and out popped BSEEPT.

BSEEPT allows you to use every aspect of the GraphQL API from the command line or in your own Python code.

### Quick Demo

I have written an extensive readme on the [GitHub project](https://github.com/olliewuk/bseept) but I will give an example of how one might use it.

In this example we will run through several steps:

1. Query the run scans.
2. Then pass through `jq` to just extract the issue titles.
3. Then pass through `jq` to build a CSV of issue titles, site, and path they were found in.

All without writing any new code - just using command line tools!

So we first get the scan details:

`bseept % python3 bseept.py --getscans | jq`

Second, extract the issues for the successful scan with the scan ID of 123:

`bseept % python3 bseept.py --getscanissues 123 | jq
{
   "data": {
      "scan": {
         "issues": [
            {
               "issue_type": {
                  "name": "External service interaction (HTTP)",
                  "description_html": "<p>External service interaction arises when it is possible to induce an application to interact with an arbitrary external service, such as a web or mail server. The ability to trigger arbitrary external service interactions does not constitute a vulnerability in its own right, and in some cases might even be the intended behavior of the application.\nHowever, in many cases, it can indicate a vulnerability with serious consequences.</p>\n<p>The ability to send requests to other systems can allow the vulnerable server to be used as an attack proxy.\n By submitting suitable payloads, an attacker can cause the application server to attack other systems that it can interact with. \n This may include public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself. \n Depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers. </p>",
                  "remediation_html": "<p>You should review the purpose and intended use of the relevant application functionality, \n and determine whether the ability to trigger arbitrary external service interactions is intended behavior. \n If so, you should be aware of the types of attacks that can be performed via this behavior and take appropriate measures. \n These measures might include blocking network access from the application server to other internal systems, and hardening the application server itself to remove any services available on the local loopback adapter.</p>\n<p>If the ability to trigger arbitrary external service interactions is not intended behavior, then you should implement a whitelist of permitted services and hosts, and block any interactions that do not appear on this whitelist.</p>\n\n<p>Out-of-Band [Application Security Testing](https://portswigger.net/burp/application-security-testing) ([OAST](https://portswigger.net/burp/application-security-testing/oast)) is highly effective at uncovering high-risk features, to the point where finding the root cause of an interaction can be quite challenging. To find the source of an external service interaction, try to identify whether it is triggered by specific application functionality, or occurs indiscriminately on all requests. If it occurs on all endpoints, a front-end CDN or application firewall may be responsible, or a back-end analytics system parsing server logs. In some cases, interactions may originate from third-party systems; for example, a HTTP request may trigger a poisoned email which passes through a link-scanner on its way to the recipient.</p>",
                   "vulnerability_classifications_html": "<ul>\n<li><a href=\"https://cwe.mitre.org/data/definitions/918.html\">CWE-918: [Server-Side Request Forgery](https://portswigger.net/web-security/ssrf) ([SSRF](https://portswigger.net/web-security/ssrf))</a></li>\n<li><a href=\"https://cwe.mitre.org/data/definitions/406.html\">CWE-406: Insufficient Control of Network Message Volume (Network Amplification)</a></li>\n</ul>",
                   "references_html": "<ul>\n <li><a href=\"https://portswigger.net/blog/introducing-burp-collaborator\">Burp Collaborator</a></li>\n <li><a href=\"https://portswigger.net/burp/application-security-testing/oast\">Out-of-band application security testing (OAST)</a></li>\n <li><a href=\"https://portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface\">PortSwigger Research: Cracking the Lens</a></li>\n</ul>"
                },
                "confidence": "certain",
                "display_confidence": null,
                "serial_number": "5601616512020228096",
                "severity": "high",
                "description_html": "It is possible to induce the application to perform server-side HTTP and HTTPS requests to arbitrary domains.

The payload <b>http://s0t5stlr0i5p270b2o0hxzl1ksqlee24qzdq1f.oastify.com/</b> was submitted in the <b>Referer</b> HTTP header.

The application performed an HTTP request to the specified domain.",
                "remediation_html": null,
                "path": "/catalog",
                "ori...