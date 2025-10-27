---
title: CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?
url: https://buaq.net/go-141294.html
source: unSafe.sh - 不安全
date: 2022-12-26
fetch_date: 2025-10-04T02:30:48.484502
---

# CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?

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

CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?

I recently discovered a CRLF injection vulnerability on a popular website. In this blog post, I will
*2022-12-25 01:14:46
Author: [infosecwriteups.com(查看原文)](/jump-141294.htm)
阅读量:49
收藏*

---

I recently discovered a CRLF injection vulnerability on a popular website. In this blog post, I will describe the vulnerability and the attack scenarios that I was able to demonstrate. I will also discuss the potential impacts of CRLF injection vulnerabilities.

## What is CRLF?

CRLF (Carriage Return and Line Feed) is a sequence of two special characters that’s used to represent the end of a line of text in many computing contexts. In the context of cybersecurity, CRLF attacks can be used by attackers to inject malicious content into websites. To protect against these attacks, web developers need to properly handle CRLF sequences and sanitize user-generated content.

CRLF Injection attack has two most important use cases:

* **Log Splitting:** The attacker inserts an end of line character and an extra line to falsify the log file entries in order to deceive the system administrators by hiding other attacks.
* **HTTP Response Splitting:** CRLF injection is used to add HTTP headers to the HTTP response and, for example, perform an XSS attack that leads to information disclosure.

## How I was able to find the CRLF?

I used the crlfuzz tool, available at <https://github.com/dwisiswant0/crlfuzz>, to find the CRLF injection vulnerability on the website. The crlfuzz tool is a command-line tool that allows users to test for CRLF injection vulnerabilities by injecting CRLF sequences into HTTP headers.

To use the crlfuzz tool, I first had to clone the repository and install the necessary dependencies. Then, I ran the tool with the target URL and the desired payload as arguments. The tool injected the payload into the HTTP headers and sent the request to the target website.

```
▶ crlfuzz -u "http://target"
```

If the website was vulnerable to CRLF injection, the tool would receive a response indicating the injected payload had been successfully executed.

Using the crlfuzz tool, I was able to quickly and easily test for CRLF injection vulnerabilities on the website. This tool is a valuable resource for bug bounty hunters looking to find and report CRLF injection vulnerabilities.

## Cookie bomb

In the first attack scenario, I injected a cookie bomb into the website. A cookie bomb is a type of attack that aims to overwhelm a website’s server by injecting a large number of cookies into the user’s browser. This can cause the website to become slow or unresponsive for the affected user.

For example, the following payload could be used to create a cookie bomb:

```
Set-Cookie: bomb=1
```

This payload would inject 10000 cookies into the user’s browser, potentially causing the website to become slow or unresponsive. It is important for website developers to take steps to protect against cookie bombs and other types of injection attacks.

## Cloudflare WAF block

In the second scenario, I set a cookie and triggered a Cloudflare WAF block. Cloudflare WAF (Web Application Firewall) is a security measure that protects websites from a variety of cyber threats, including injection attacks. When a WAF block is triggered, it means that the website’s server has detected potentially malicious activity and is blocking access to the website in order to protect it.

For example, the following payload could be used to trigger a Cloudflare WAF block:

```
Set-Cookie: crlf=attack
```

This payload sets a cookie with a value of “attack”, which may be detected as malicious by the website’s server and trigger a Cloudflare WAF block. It is important for website developers to ensure that their WAF is configured correctly and is able to effectively protect against potential attacks.

*Submitted*: 16 Nov, 2021

*Accepted*: 17 Nov, 2021

*Triaged*: 17 Nov, 2021

Needs more info: 13 Dec, 2021 -> I gave more infos

*Triaged again*: 19 Aug, 2022 -> Bounty 500$

*Resolved / Closed*: — -

The impact of CRLF injection is diverse and also includes everything from cross-site scripting to information disclosure. It can also disable certain security restrictions such as XSS filters and the Same Origin Policy in victims’ browsers, leaving them vulnerable to malicious attacks. With the attack scenario I described, I was able to show how quickly you can render the site unusable for a single user.

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/crlf-injection-xxx-how-was-it-possible-for-me-to-earn-a-bounty-with-the-cloudflare-waf-f581506f97f5?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)