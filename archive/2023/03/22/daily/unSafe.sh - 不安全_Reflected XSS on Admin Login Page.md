---
title: Reflected XSS on Admin Login Page
url: https://buaq.net/go-154587.html
source: unSafe.sh - 不安全
date: 2023-03-22
fetch_date: 2025-10-04T10:13:43.851381
---

# Reflected XSS on Admin Login Page

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

Reflected XSS on Admin Login Page

Hi! I’m Aswin,security researcher and a penetration tester.Here we are discussing reflected XSS in a
*2023-3-21 23:52:59
Author: [infosecwriteups.com(查看原文)](/jump-154587.htm)
阅读量:19
收藏*

---

Hi! I’m Aswin,security researcher and a penetration tester.Here we are discussing reflected XSS in a private bug bounty program.

On the website [https://xyz.redacted.com/a6,](https://xyz.redacted.com/a6%2C) when you attempt to access secret sections,The URL on the parameter “win” redirects you to a login page with values from the URL mirrored in the DOM.

Reflect XSS- Admin Login page

> A cross-site scripting attack might be launched against the application since there is no adequate handle for the data reflected, making it susceptible.

Reflected Cross-Site Scripting occurs when the injected script is mirrored off the website, such as an error message, search result, or other response.

To launch a successful Reflected XSS attack, an attacker looks for instances where user input is utilised directly to create a response.
This frequently includes the inclusion of event attributes such as onload and onmouseover to elements that are not supposed to host scripts, such as image tags (img>).

When you visit the current URL, an alert with your cookie will appear on the screen.

[https://xyz.redacted.com/a6/shared/popupLogin.jsp?win=%22%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E](https://td.intelliresponse.com/a6/shared/popupLogin.jsp?win=%22%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E)

1. Navigate to [https://xyz.redacted.com/a6](https://td.intelliresponse.com/a6)
2. Now that you’ve been forwarded to the login page, look for the win parameter on the URL and replace it with some payload beginning with “>” and some text or script in front.
3. See the completed payload on your screen.

POC

Remediation for XSS often entails cleaning data input (to ensure that no code is present), escaping all output (to ensure that data is not shown as code), and re-structuring applications such that code is loaded from well-defined destinations.

* Accessing sensitive data, or even gaining control of user accounts
* An attacker may create a payload to extract a user’s admin credentials or steal his session.

Happy Hacking..

文章来源: https://infosecwriteups.com/reflected-xss-on-admin-login-page-94960596ec88?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)