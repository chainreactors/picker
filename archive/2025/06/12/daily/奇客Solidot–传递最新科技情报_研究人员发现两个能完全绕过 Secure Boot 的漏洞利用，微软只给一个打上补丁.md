---
title: 研究人员发现两个能完全绕过 Secure Boot 的漏洞利用，微软只给一个打上补丁
url: https://www.solidot.org/story?sid=81528
source: 奇客Solidot–传递最新科技情报
date: 2025-06-12
fetch_date: 2025-10-06T22:53:52.028004
---

# 研究人员发现两个能完全绕过 Secure Boot 的漏洞利用，微软只给一个打上补丁

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251005)
  [往日投票](/polllist)
* 皮肤

  [蓝色](/?theme=blue)
  [橙色](/?theme=yellow)
  [绿色](/?theme=green)
  [浅绿色](/?theme=clightgreen)

* 分类:
* [首页](//www.solidot.org/)
* [Linux](//linux.solidot.org/)
* [科学](//science.solidot.org/)
* [科技](//technology.solidot.org/)
* [移动](//mobile.solidot.org/)
* [苹果](//apple.solidot.org/)
* [硬件](//hardware.solidot.org/)
* [软件](//software.solidot.org/)
* [安全](//security.solidot.org/)
* [游戏](//games.solidot.org/)
* [书籍](//books.solidot.org/)
* [idle](//idle.solidot.org/)
* [云计算](//cloud.solidot.org/)
* [高飞的电子替身](//story.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](/QA)查看。

## 消息

**本文已被查看 6645 次**

## 研究人员发现两个能完全绕过 Secure Boot 的漏洞利用，微软只给一个打上补丁

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年06月11日 22时01分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81528&appkey=1370085986&title=%E7%A0%94%E7%A9%B6%E4%BA%BA%E5%91%98%E5%8F%91%E7%8E%B0%E4%B8%A4%E4%B8%AA%E8%83%BD%E5%AE%8C%E5%85%A8%E7%BB%95%E8%BF%87%20Secure%20Boot%20%E7%9A%84%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%8C%E5%BE%AE%E8%BD%AF%E5%8F%AA%E7%BB%99%E4%B8%80%E4%B8%AA%E6%89%93%E4%B8%8A%E8%A1%A5%E4%B8%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自基因突变**

研究人员发现了两个能完全绕过 Secure Boot 的漏洞利用，而微软在本周二的例行安全更新中只给一个（CVE-2025-3052）打上补丁。CVE-2025-3052 的原因是 DT Research 所售设备主板用于刷固件的工具存在一个高危漏洞。问题模块使用了 Microsoft Corporation UEFI CA 2011 签名，微软在安全补丁中屏蔽了相关工具。第二个漏洞 CVE-2025-47827 与 Linux 内核模块 IGEL 相关，它也使用了微软签名。但微软尚未撤销该签名。
msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-3052

Ars：Found in the wild: 2 Secure Boot exploits. Microsoft is patching only 1 of them.

﻿

任何有可能出错的事将会出错--墨菲定理

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251005)
* [过去的投票](/polllist)
* [编辑介绍](/authors)
* [隐私政策](/privacy)
* [使用条款](/terms)
* [网站介绍](/introd)
* [RSS](/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](//php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](//apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](//www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](//www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](//icon.zhiding.cn/beian/icon.png)](//icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205　涉未成年人举报专线：010-62641208 举报邮箱：jubao@zhiding.cn　网上有害信息举报专区：<https://www.12377.cn>