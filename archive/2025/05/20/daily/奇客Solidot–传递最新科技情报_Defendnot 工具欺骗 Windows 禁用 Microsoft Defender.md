---
title: Defendnot 工具欺骗 Windows 禁用 Microsoft Defender
url: https://www.solidot.org/story?sid=81326
source: 奇客Solidot–传递最新科技情报
date: 2025-05-20
fetch_date: 2025-10-06T22:28:03.361896
---

# Defendnot 工具欺骗 Windows 禁用 Microsoft Defender

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

**本文已被查看 4653 次**

## Defendnot 工具欺骗 Windows 禁用 Microsoft Defender

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年05月19日 15时06分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81326&appkey=1370085986&title=Defendnot%20%E5%B7%A5%E5%85%B7%E6%AC%BA%E9%AA%97%20Windows%20%E7%A6%81%E7%94%A8%20Microsoft%20Defender "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自空中城堡**

杀毒软件会使用 Windows Security Center (WSC) API 通知 Windows 已安装并执行实时保护。为避免操作系统同时运行多个安全软件导致冲突，Windows 会禁用系统自带的安全软件 Microsoft Defender。研究员 es3n1n 开发了名为 Defendnot 的工具滥用了该 API，通过注册虚假的杀毒软件去禁用 Microsoft Defender。Defendnot 是基于一个已删除的项目 no-defender，no-defender 使用了第三方杀毒软件的代码去伪造 WSC 注册，在该杀毒软件开发商递交了 DMCA 删除申请后，开发者从 GitHub 下架了 no-defender。Defendnot 利用虚假的杀毒软件 DLL 规避了版权问题。WSC API 受到 Protected Process Light (PPL)、有效数字签名和其他功能的保护。Defendnot 通过将 DLL 注入到已由微软签名并信任的系统进程 Taskmgr.exe 中绕过了这些要求。
BleepingComputer:New 'Defendnot' tool tricks Windows into disabling Microsoft Defender
github.com/es3n1n/defendnot

﻿

太阳绝不为它所做的善事后悔，也从不指望任何报酬。

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