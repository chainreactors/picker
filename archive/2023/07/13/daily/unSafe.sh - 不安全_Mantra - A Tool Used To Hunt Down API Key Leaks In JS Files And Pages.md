---
title: Mantra - A Tool Used To Hunt Down API Key Leaks In JS Files And Pages
url: https://buaq.net/go-171872.html
source: unSafe.sh - 不安全
date: 2023-07-13
fetch_date: 2025-10-04T11:52:58.848742
---

# Mantra - A Tool Used To Hunt Down API Key Leaks In JS Files And Pages

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

![](https://8aqnet.cdn.bcebos.com/fa5d91d51311b2300628b645ddd7daf9.jpg)

Mantra - A Tool Used To Hunt Down API Key Leaks In JS Files And Pages

The tool in question was created in Go and its main objective is to search for API keys in J
*2023-7-12 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171872.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhOCpN886uym5PAaH9tvz23xwiWn9ECxTJ2zMFDJO1YAlvKbx3GyUuQANk3d2x98qTX0FAFFvfLsS-S82_rWeiyTfT3bYtdOZz4H6ChmbEW8Iv4GdN3iyMyVs8gSYlJmR1fgGTRdJPuBlKIJ8ypmdX5cs-euNFy3l_Y3lEjEpItB71oipPflDWZjihbYg=w640-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEhOCpN886uym5PAaH9tvz23xwiWn9ECxTJ2zMFDJO1YAlvKbx3GyUuQANk3d2x98qTX0FAFFvfLsS-S82_rWeiyTfT3bYtdOZz4H6ChmbEW8Iv4GdN3iyMyVs8gSYlJmR1fgGTRdJPuBlKIJ8ypmdX5cs-euNFy3l_Y3lEjEpItB71oipPflDWZjihbYg)

The tool in question was created in Go and its main objective is to search for API keys in JavaScript files and HTML pages.

It works by checking the source code of web pages and script files for strings that are identical or similar to API keys. These keys are often used for [authentication](https://www.kitploit.com/search/label/Authentication "authentication") to online services such as third-party APIs and are confidential and should not be shared publicly.

By using this tool, developers can quickly identify if their API keys are leaking and take steps to fix the problem before they are compromised. Furthermore, the tool can be useful for security officers, who can use it to verify that applications and websites that use external APIs are adequately protecting their keys.

In summary, this tool is an efficient and accurate solution to help [secure](https://www.kitploit.com/search/label/Secure "secure") your API keys and prevent [sensitive information](https://www.kitploit.com/search/label/Sensitive%20Information "sensitive information") leaks.

## Help

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgFHCgZDLUp92BLszusiS4SEwOWV495vD99YxG6nfLpEcRfplXvZwpF7NlRLrUNwGQwyqrJfz8mpkcljrNhTSlniM_A2OFAT4ixOniRFKTfyCKUe-aIasKvVvUsnQ9oR1cNxUXMBAb5Td1uzFanBRVlrcoSPQX9o6E9GBdGnnrmDWx9Ehg9nFQRv3-Kgw=w640-h398)](https://blogger.googleusercontent.com/img/a/AVvXsEgFHCgZDLUp92BLszusiS4SEwOWV495vD99YxG6nfLpEcRfplXvZwpF7NlRLrUNwGQwyqrJfz8mpkcljrNhTSlniM_A2OFAT4ixOniRFKTfyCKUe-aIasKvVvUsnQ9oR1cNxUXMBAb5Td1uzFanBRVlrcoSPQX9o6E9GBdGnnrmDWx9Ehg9nFQRv3-Kgw)

## Usage

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiLSKMXgrZFfwGwmxBMO7ub8yHiLpDJtD-7AasTODb_H23Ga-gC3YJjRo9ia-WVPxi4EpL5Ca6KHuoMzbP62LuqsQ99s-wBS4wWBoEH1qh1uKzqcXUS4CQOrfMeNLfaPWVs4Zf1X1VvS-4aUtoM4RmcCcUPuYPoxm6gouuLj-SHzsWb_Ms3z_v67xyhmw=w640-h284)](https://blogger.googleusercontent.com/img/a/AVvXsEiLSKMXgrZFfwGwmxBMO7ub8yHiLpDJtD-7AasTODb_H23Ga-gC3YJjRo9ia-WVPxi4EpL5Ca6KHuoMzbP62LuqsQ99s-wBS4wWBoEH1qh1uKzqcXUS4CQOrfMeNLfaPWVs4Zf1X1VvS-4aUtoM4RmcCcUPuYPoxm6gouuLj-SHzsWb_Ms3z_v67xyhmw)

## Install

```
git clone https://github.com/MrEmpy/Mantra
```

## Buy me a coffee?

[LivePix](https://livepix.gg/mrempy "LivePix")

Mantra - A Tool Used To Hunt Down API Key Leaks In JS Files And Pages
![Mantra - A Tool Used To Hunt Down API Key Leaks In JS Files And Pages](https://blogger.googleusercontent.com/img/a/AVvXsEhOCpN886uym5PAaH9tvz23xwiWn9ECxTJ2zMFDJO1YAlvKbx3GyUuQANk3d2x98qTX0FAFFvfLsS-S82_rWeiyTfT3bYtdOZz4H6ChmbEW8Iv4GdN3iyMyVs8gSYlJmR1fgGTRdJPuBlKIJ8ypmdX5cs-euNFy3l_Y3lEjEpItB71oipPflDWZjihbYg=s72-w640-c-h320)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/07/mantra-tool-used-to-hunt-down-api-key.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)