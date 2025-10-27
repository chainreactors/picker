---
title: timwhitez starred sleepmask_ekko_cfg
url: https://buaq.net/go-153988.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:23.375088
---

# timwhitez starred sleepmask_ekko_cfg

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

timwhitez starred sleepmask\_ekko\_cfg

A tag already exists with the provided branch name. Many Git commands accept
*2023-3-17 23:56:6
Author: [github.com(查看原文)](/jump-153988.htm)
阅读量:24
收藏*

---

Code snippets to add on top of cobalt strike sleepmask kit so that ekko can work in a CFG protected process.

All credits to [@Icebreaker](https://github.com/IcebreakerSecurity)

## Usage

1. Enable ekko sleep in sleepmask kit
2. Include cfg.c
3. Add below codes before ekko sleep

```
   PVOID NtContinue = KERNEL32$GetProcAddress(KERNEL32$GetModuleHandleA("ntdll.dll"),"NtContinue");
   //PVOID NtContinue = NTDLL$NtContinue; //<-- this should be the same as above
   if (!markCFGValid_nt(NtContinue))
    {
        return;
    }
```

4. Put cfg.c in folder
5. Append the contents in bofdefs.h
6. Compile

## Caveat

1. Sleep 0 will terminate the process, meaning that socks cannot be used (However, if interactive process is needed, its pointless to use ekko, just revert back to use original sleep)

## Reference

1. <https://github.com/IcebreakerSecurity/Ekko_CFG_Bypass>

文章来源: https://github.com/ScriptIdiot/sleepmask\_ekko\_cfg
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)