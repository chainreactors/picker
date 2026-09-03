---
title: AI 时代 Linux 7.x 系列每个版本修复的漏洞数接近 2000 个
url: https://www.solidot.org/story?sid=85265
source: 奇客Solidot–传递最新科技情报
date: 2026-09-02
fetch_date: 2026-09-03T06:39:16.524034
---

# AI 时代 Linux 7.x 系列每个版本修复的漏洞数接近 2000 个

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260902)
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

**本文已被查看 2490 次**

## AI 时代 Linux 7.x 系列每个版本修复的漏洞数接近 2000 个

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年09月03日 00时06分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85265&appkey=1370085986&title=AI%20%E6%97%B6%E4%BB%A3%20Linux%207.x%20%E7%B3%BB%E5%88%97%E6%AF%8F%E4%B8%AA%E7%89%88%E6%9C%AC%E4%BF%AE%E5%A4%8D%E7%9A%84%E6%BC%8F%E6%B4%9E%E6%95%B0%E6%8E%A5%E8%BF%91%202000%20%E4%B8%AA "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自夜袭动物园**

根据稳定版内核维护者 Greg Kroah-Hartman 制作的幻灯片，Linux 7.x 系列的 CVE 数量已从 7.1 的逾千增加到 7.2 的逾 1500，按照这一趋势，下个版本 7.3 将会超过 2000。这一切并非是因为 Linux 内核安全性变差，而是因为 AI 辅助安全检测工具对内核源代码的自动扫描发现了大量 bug，大部分 bug 并不严重属于低危级别。AI 工具产生了大量报告，而要从这些报告中发现有用的信息需要维护者耗费大量精力和时间。内核网络系统的维护者 Jakub Kicinski 表示他们有点不堪重负了。为了减少旧代码的 bug 报告，内核维护者们开始移除大量基本上无人使用的驱动代码。Linux 7.3 移除了旧的 SGI 和 IBM 驱动代码，此举旨在减少维护成本，因为这些历史悠久的代码被 AI 工具发现了大量 bug，而维护者有义务调查和修复这些 bug。
https://www.tomshardware.com/software/linux/linux-kernel-nears-2-000-cves-per-release-as-ai-bug-hunters-scour-40-million-lines-of-code-maintainers-say-they-are-completely-overwhelmed

[PEC 2026 AI创新者大会暨第三届提示工程峰会邀您参会](https://jinshuju.com/f/QMxIGi?x_field_1=solidot)
[回复](/comments?sid=85265&op=reply&type=story)

﻿

别向医生和律师提供错误的消息。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260902)
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