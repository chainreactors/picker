---
title: dizqueTV 1.5.3 Remote Code Execution
url: https://buaq.net/go-265679.html
source: unSafe.sh - 不安全
date: 2024-10-06
fetch_date: 2025-10-06T18:48:40.443394
---

# dizqueTV 1.5.3 Remote Code Execution

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

dizqueTV 1.5.3 Remote Code Execution

# Exploit Title: dizqueTV 1.5.3 - Remote Code Execution (RCE)# Date: 9/21/2024# Exploit Author: Ah
*2024-10-5 22:36:14
Author: [cxsecurity.com(查看原文)](/jump-265679.htm)
阅读量:17
收藏*

---

# Exploit Title: dizqueTV 1.5.3 - Remote Code Execution (RCE)
# Date: 9/21/2024
# Exploit Author: Ahmed Said Saud Al-Busaidi
# Vendor Homepage: https://github.com/vexorian/dizquetv
# Version: 1.5.3
# Tested on: linux
POC:
## Vulnerability Description
dizqueTV 1.5.3 is vulnerable to unauthorized remote code execution from attackers.
## STEPS TO REPRODUCE
1. go to http://localhost/#!/settings
2. now go to ffmpeg settings and change the FFMPEG Executable Path to: "; cat /etc/passwd && echo 'poc'"
3. click on update
4. now visit http://localhost/#!/version or click on version and you should see the content of /etc/passwd

文章来源: https://cxsecurity.com/issue/WLB-2024100011
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)