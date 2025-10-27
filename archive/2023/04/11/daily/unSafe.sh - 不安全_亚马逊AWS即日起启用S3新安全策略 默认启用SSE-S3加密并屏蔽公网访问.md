---
title: 亚马逊AWS即日起启用S3新安全策略 默认启用SSE-S3加密并屏蔽公网访问
url: https://buaq.net/go-157949.html
source: unSafe.sh - 不安全
date: 2023-04-11
fetch_date: 2025-10-04T11:29:35.215402
---

# 亚马逊AWS即日起启用S3新安全策略 默认启用SSE-S3加密并屏蔽公网访问

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

![](https://8aqnet.cdn.bcebos.com/2356fa89f6d219d1ef4cffb514fe4c1e.jpg)

亚马逊AWS即日起启用S3新安全策略 默认启用SSE-S3加密并屏蔽公网访问

亚马逊AWS提供的S3云存储是目前使用最广泛的云存储之一，不过这些年AWS S3发生过多次数据泄露事件。数据泄露倒不是亚马逊的问题，而是客户在使用存储桶时并不知道如何配置权限导致默认情
*2023-4-10 22:23:8
Author: [www.landiannews.com(查看原文)](/jump-157949.htm)
阅读量:26
收藏*

---

亚马逊AWS提供的S3云存储是目前使用最广泛的云存储之一，不过这些年AWS S3发生过多次数据泄露事件。

数据泄露倒不是亚马逊的问题，而是客户在使用存储桶时并不知道如何配置权限导致默认情况下被公开访问。

从初创企业到美国联邦政府的重要机构都出现过配置问题导致数据泄露，最终亚马逊决定默认禁用公网访问。

同时亚马逊还决定所有AWS S3存储都默认启用SSE-S3加密策略，该策略使用AES-256算法确保不会被破解。

[![亚马逊AWS即日起启用S3新安全策略 默认启用SSE-S3加密并屏蔽公网访问](https://img.lancdn.com/landian/2019/12/67564.png)](https://img.lancdn.com/landian/2019/12/67564.png)

**新策略一：新S3默认禁止ACL列表**

因为配置问题导致的公网访问引起太多问题，其实之前亚马逊对存储桶配置的权限就是禁止公网访问但不够。

有些客户会使用访问控制列表进行操作，但访问控制列表配置可能有一定的门槛，导致部分客户配置有问题。

新默认政策是自动启用存储桶屏蔽公网访问且禁用所有新存储桶配置访问控制列表，无论使用何种方式创建。

自此之后如果客户确实要对外开放存储桶访问权限，必须更小心的进行配置，避免无法访问或权限超出预料。

该政策适用于亚马逊AWS所有可用区域，包括但不限于 AWS GovCloud (政府云) 和亚马逊云科技中国区域。

**新策略二：默认启用SSE-S3加密**

作为服务提供商和平台方亚马逊修改安全策略属于重大事件，因为大多数客户都会采用默认选项不会自己改。

所以早在2011年亚马逊就提供SSE-S3 但客户使用率并不高，亚马逊在过去这些年并未默认启用存储桶加密。

同样是因为采用默认配置很多包含机密数据的存储桶被设置公开状态，这个问题已经导致多次严重泄密事件。

现在亚马逊免费且默认启用存储桶加密是个重要的举措，亚马逊称这种级别的保护可以大幅度提升数据安全。

改成默认还有个好处是客户无需自己使用工具或客户端进行配置，这对于一路点下一步的客户来说省事很多。

区域支持方面AWS全球区域/AWS中国区即亚马逊云科技全部默认采用加密，所以中国区客户也无需手动改。

版权声明：感谢您的阅读，除非文中已注明来源网站名称或链接，否则均为蓝点网原创内容。转载时请务必注明：来源于蓝点网、标注作者及[本文完整链接](https://www.landiannews.com/archives/98244.html)，谢谢理解。

文章来源: https://www.landiannews.com/archives/98244.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)