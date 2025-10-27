---
title: timwhitez starred DirCreate2System
url: https://buaq.net/go-144469.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:40.135974
---

# timwhitez starred DirCreate2System

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

![](https://8aqnet.cdn.bcebos.com/92113ff8c0e2884097d4ac7df0e794cb.jpg)

timwhitez starred DirCreate2System

Weaponizing to get NT AUTHORITY\SYSTEM for Privileged Directory Creation Bugs with Win
*2023-1-6 18:45:2
Author: [github.com(查看原文)](/jump-144469.htm)
阅读量:36
收藏*

---

Weaponizing to get NT AUTHORITY\SYSTEM for Privileged Directory Creation Bugs with Windows Error Reporting

### Short Description:

I've discovered **comctl32.dll** (which is missing in system dir which doesn't really exist) has been loaded by wermgr.exe via windows error reporting by running schtasks. It means if we can create a folder name as **C:\windows\system32\wermgr.exe.local** with Full permission ACL, we can hijack the **comctl32.dll** in that folders. Then, I created this poc as a Directory creation to NT AUTHORITY\SYSTEM shell method.

### **POC video**

[POC.wmv](https://github.com/binderlabs/DirCreate2System/blob/main/poc.wmv) (with backblaze's directory creation bug)

#### Remark: I've already reported to backblaze and they replied me that it's know issues. So, I made a video poc for educational purpose of this dircreate2system poc.

### For testing purposes:

(if you have a directory creation bug via service vulnerabilities, you don't need administrator access)

1. **As an administrator**, create directory `wermgr.exe.local` in `C:\Windows\System32\`
2. And then, give it access control `cacls C:\Windows\System32\wermgr.exe.local /e /g everyone:f`
3. Place `spawn.dll` file and `dircreate2system.exe` in a same directory.
4. Then, run `dircreate2system.exe`.
5. Enjoy a shell as NT AUTHORITY\SYSTEM.

[![test1](https://github.com/binderlabs/DirCreate2System/raw/main/POC1.jpg)](https://github.com/binderlabs/DirCreate2System/blob/main/POC1.jpg)

#### *Note:*

*You can also use another methods by viewing this* [dir\_create2system.txt](https://github.com/sailay1996/awesome_windows_logical_bugs/blob/master/dir_create2system.txt)

文章来源: https://github.com/binderlabs/DirCreate2System
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)