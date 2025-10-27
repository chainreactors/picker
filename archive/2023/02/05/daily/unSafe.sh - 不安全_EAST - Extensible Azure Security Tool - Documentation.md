---
title: EAST - Extensible Azure Security Tool - Documentation
url: https://buaq.net/go-147947.html
source: unSafe.sh - 不安全
date: 2023-02-05
fetch_date: 2025-10-04T05:44:57.508498
---

# EAST - Extensible Azure Security Tool - Documentation

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

![](https://8aqnet.cdn.bcebos.com/2ba3fddfab040cbd7ef9042eda9f1e06.jpg)

EAST - Extensible Azure Security Tool - Documentation

Extensible Azure Security Tool (Later referred as E.A.S.T) is tool for assessing Azure and t
*2023-2-4 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-147947.htm)
阅读量:29
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-Pl1O1HnRx2ODYup-qhBPvpEff5QIwlQBaloCIfzIWRftGgjdQCTTdum83fvsyiWs2pX7UQcccQG6woD4w71Y4AZbltjw7PamPenJ1u8EnfKD-HGImv9ECdkCtzqfOz_Si9r4j99GdbJ6l5jTbr9mLciOx6FQZWBVLYPLnKMSUaVSHEHCYB5c7wxL8A/w640-h226/EAST_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-Pl1O1HnRx2ODYup-qhBPvpEff5QIwlQBaloCIfzIWRftGgjdQCTTdum83fvsyiWs2pX7UQcccQG6woD4w71Y4AZbltjw7PamPenJ1u8EnfKD-HGImv9ECdkCtzqfOz_Si9r4j99GdbJ6l5jTbr9mLciOx6FQZWBVLYPLnKMSUaVSHEHCYB5c7wxL8A/s638/EAST_2.png)

Extensible Azure Security Tool (Later referred as E.A.S.T) is tool for assessing Azure and to some extent Azure AD security controls. Primary use case of EAST is Security data collection for evaluation in Azure Assessments. This information (JSON content) can then be used in various reporting tools, which we use to further correlate and investigate the data.

This tool is licensed under [MIT license](https://github.com/jsa2/EAST/blob/public/LICENSE "MIT license").

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2sng9X7Sd_ASeKGGeH8w_LA5_S0CWO2kwRq03sNBYXzqmpFSPGpRHjJpgMu37WdK9mo7oGSu--ZLJ1SXEQXcDWqvoJ27xpIu-wqrasukTO-AWir_7sn8QZwUvB09hMDDpndJddjAb5WsGA05nffwlbb3rXra8kOqguHJRyCw4lPu-Q6tFHFE7qjNPEQ/w640-h390/EAST_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2sng9X7Sd_ASeKGGeH8w_LA5_S0CWO2kwRq03sNBYXzqmpFSPGpRHjJpgMu37WdK9mo7oGSu--ZLJ1SXEQXcDWqvoJ27xpIu-wqrasukTO-AWir_7sn8QZwUvB09hMDDpndJddjAb5WsGA05nffwlbb3rXra8kOqguHJRyCw4lPu-Q6tFHFE7qjNPEQ/s1136/EAST_1.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyKX_cJDBcX_ZMAIF5KeT7d4A5_XnvlH6Gx7-oy_15Baqa2PrEP3qQF7ZHFTzSogMhDtmCqHXA8C0oWrvg34LamuOLoXHCzuuY8YGbBzV_BsdIMXFg62A4zXMB5Pqc1fm7Uau3Tbty0bri3WC1XJ5t9PlzhPEX2yDyn2JVOYVnFgBMBknPLCcGXwI49w/w640-h226/EAST_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyKX_cJDBcX_ZMAIF5KeT7d4A5_XnvlH6Gx7-oy_15Baqa2PrEP3qQF7ZHFTzSogMhDtmCqHXA8C0oWrvg34LamuOLoXHCzuuY8YGbBzV_BsdIMXFg62A4zXMB5Pqc1fm7Uau3Tbty0bri3WC1XJ5t9PlzhPEX2yDyn2JVOYVnFgBMBknPLCcGXwI49w/s638/EAST_2.png)

* [Yours truly](https://www.linkedin.com/in/joosua-santasalo-00552922/ "Yours truly")
* [Nixu](https://www.nixu.com/ "Nixu") Cloud Security Team

* Preview branch introduced

  Changes:

  + Installation now accounts for use of Azure Cloud Shell's updated version in regards to depedencies (Cloud Shell has now Node.JS v 16 version installed)
  + Checking of Databricks cluster types as per [advisory](https://www.databricks.com/blog/2022/10/10/admin-isolation-shared-clusters.html "advisory")

    - Audits Databricks clusters for potential privilege elevation - This control requires typically permissions on the databricks cluster"
  + Content.json is has now key and content based sorting. This enables doing delta checks with `git diff HEAD^1` ¹ as content.json has predetermined order of results

    [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlLTr8khXWfULOso2mIlLFy8kAeHkAr95FFFpyLM9iiDgagJNKW0hUNspqrUwb9YsfKqUz0n6V57Ftkem0h9qX_eMfZWzmRgX1AggsgCyvF1x1DANHmkomtT2WH0VBG3-aXfG5YFmpGBYCHS1a2GnYdotR3PHp4BACShLx8tasBe3RUS2yEvA0wgq70Q/w640-h234/EAST_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlLTr8khXWfULOso2mIlLFy8kAeHkAr95FFFpyLM9iiDgagJNKW0hUNspqrUwb9YsfKqUz0n6V57Ftkem0h9qX_eMfZWzmRgX1AggsgCyvF1x1DANHmkomtT2WH0VBG3-aXfG5YFmpGBYCHS1a2GnYdotR3PHp4BACShLx8tasBe3RUS2yEvA0wgq70Q/s791/EAST_3.png)
  > ¹Word of caution, if want to check deltas of content.json, then content.json will need to be "unignored" from [`.gitignore`](https://github.com/jsa2/EAST/blob/public/.gitignore "Extensible Azure Security Tool - Documentation (36)") exposing results to any upstream you might have configured.
  >
  > > Use this feature with caution, and ensure you don't have public upstream set for the branch you are using this feature for
* Change of programming patterns to avoid possible race conditions with larger datasets. This is mostly changes of using `var` to `let` in  `for await` -style loops

---

EAST - Extensible Azure Security Tool - Documentation
![EAST - Extensible Azure Security Tool - Documentation](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-Pl1O1HnRx2ODYup-qhBPvpEff5QIwlQBaloCIfzIWRftGgjdQCTTdum83fvsyiWs2pX7UQcccQG6woD4w71Y4AZbltjw7PamPenJ1u8EnfKD-HGImv9ECdkCtzqfOz_Si9r4j99GdbJ6l5jTbr9mLciOx6FQZWBVLYPLnKMSUaVSHEHCYB5c7wxL8A/s72-w640-c-h226/EAST_2.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/east-extensible-azure-security-tool.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)