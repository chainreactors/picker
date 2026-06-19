---
title: 三个安全启动证书即将过期
url: https://www.solidot.org/story?sid=84621
source: 奇客Solidot–传递最新科技情报
date: 2026-06-18
fetch_date: 2026-06-19T07:07:28.296438
---

# 三个安全启动证书即将过期

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260618)
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

**本文已被查看 1992 次**

## 三个安全启动证书即将过期

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年06月18日 19时30分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84621&appkey=1370085986&title=%E4%B8%89%E4%B8%AA%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E8%AF%81%E4%B9%A6%E5%8D%B3%E5%B0%86%E8%BF%87%E6%9C%9F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自人猿泰山之智斗恐龙**

三个微软在 2011 年颁发的安全启动 (Secure Boot) 证书将于 6 月 24 日过期。安全启动检查系统启动期间加载的所有固件的数字签名，确保其来自可信提供商。安全启动旨在设计阻止会纂改 UEFI 的恶意程序 UEFI bootkits，一旦安装此类恶意程序很难检测到，即使重装系统也没用。安全启动使用加密签名确保启动过程中加载的每个固件都受到计算机制造商的信任，它旨在建立信任链，防止攻击者用恶意固件替换预期的启动固件。但在 2023 年研究人员发现了存在于几乎所有 Windows 和 Linux 系统 UEFI 启动过程中的严重漏洞 LogoFail。该漏洞存在于启动时显示硬件制造商徽标的软件中，攻击者能利用其图像解析 bug 绕过安全启动，用恶意固件感染 UEFI。微软因此移除了三个在 2011 年颁发的旧证书，用 2023 年颁发的新证书取代。Windows 用户可通过 Windows 安全设置 > 设备安全性 > 安全启动 去检查证书是否已经更新。Linux 用户可关注名叫 shim 的程序更新。
https://arstechnica.com/security/2026/06/windows-and-linux-users-the-deadline-to-update-secure-boot-keys-is-near/
https://support.microsoft.com/zh-cn/topic/windows-%E5%AE%89%E5%85%A8%E5%90%AF%E5%8A%A8%E8%AF%81%E4%B9%A6%E8%BF%87%E6%9C%9F%E5%92%8C-ca-%E6%9B%B4%E6%96%B0-7ff40d33-95dc-4c3c-8725-a9b95457578e

[回复](/comments?sid=84621&op=reply&type=story)

﻿

任何人均有其价值

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260618)
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