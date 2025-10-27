---
title: 【安全通报】Oracle 一月更新多个高危漏洞
url: https://buaq.net/go-146038.html
source: unSafe.sh - 不安全
date: 2023-01-19
fetch_date: 2025-10-04T04:14:56.382826
---

# 【安全通报】Oracle 一月更新多个高危漏洞

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

![](https://8aqnet.cdn.bcebos.com/b6cf01f1f6ea0a3776a770dde31a31f7.jpg)

【安全通报】Oracle 一月更新多个高危漏洞

近日，Oracle官方 发布了 2023 年 1 月份的安全更新。涉及旗下产品（Weblogic Server、Database Server、Java SE、MySQL
*2023-1-18 20:26:28
Author: [nosec.org(查看原文)](/jump-146038.htm)
阅读量:35
收藏*

---

![Image](https://nosec.org/avatar/uploads/attach/image/0020d39d11bf8c80ac757f5ebbf3c8e4/Snipaste_2022-01-19_10-16-43.png)

近日，Oracle官方 发布了 2023 年 1 月份的安全更新。涉及旗下产品（Weblogic Server、Database Server、Java SE、MySQL等）的 327 个漏洞。此次修复的漏洞中包括 10 个和 Weblogic 相关的漏洞，均无需身份验证和用户交互即可通过网络进行远程利用。

## FOFA 查询

[app="BEA-WebLogic-Server" || app="Weblogic\_interface\_7001"](https://fofa.info/result?qbase64=YXBwPSJCRUEtV2ViTG9naWMtU2VydmVyIiB8fCAgYXBwPSJXZWJsb2dpY19pbnRlcmZhY2VfNzAwMSI%3D)

## 影响范围

```
CVE-2023-21839
Weblogic Server 12.2.1.3.0
Weblogic Server 12.2.1.4.0
Weblogic Server 14.1.1.0.0
```

根据目前FOFA系统最新数据（一年内数据），显示全球范围内（app="BEA-WebLogic-Server" || app="Weblogic\_interface\_7001"）共有 124,386 个相关服务对外开放。中国使用数量最多，共有 43,848 个；美国第二，共有 27,307 个；日本第三，共有 4,524 个；德国第四，共有 4,043 个；印度第五，共有 3,891 个。

![2023-01-17-21-54-37-image.png](https://nosec.org/avatar/uploads/attach/image/4091ac8d341d33d6586cb787dee5b7e4/2023-01-17-21-54-37-image.png)

中国大陆地区北京使用数量最多，共有 9,947 个；浙江第二，共有 6,791 个；上海第三，共有 4,437 个；广东第四，共有 3,695 个；山东第五，共有 3,220 个。

![2023-01-17-21-55-36-image.png](https://nosec.org/avatar/uploads/attach/image/04f51f549d48212c2421455bcb55db00/2023-01-17-21-55-36-image.png)

## 修复方案

**通用修补建议**

参考Oracle官方更新的补丁，及时进行更新：<https://www.oracle.com/security-alerts/cpujan2023.html>

## 参考

[1] <https://www.oracle.com/security-alerts/cpujan2023.html>

白帽汇安全研究院从事信息安全，专注于安全大数据、企业威胁情报。

公司产品：FOFA-网络空间安全搜索引擎、FOEYE-网络空间检索系统、NOSEC-安全讯息平台。

为您提供：网络空间测绘、企业资产收集、企业威胁情报、应急响应服务。

文章来源: https://nosec.org/home/detail/5062.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)