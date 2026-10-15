---
title: Linus Torvalds 用 LLM 辅助开发的补丁递交接受审查
url: https://www.solidot.org/story?sid=85612
source: 奇客Solidot–传递最新科技情报
date: 2026-10-14
fetch_date: 2026-10-15T06:44:07.951367
---

# Linus Torvalds 用 LLM 辅助开发的补丁递交接受审查

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261014)
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

**本文已被查看 2829 次**

## Linus Torvalds 用 LLM 辅助开发的补丁递交接受审查

[![Linux](https://icon.solidot.org/images/topics/topiclinux.png?123)](/search?tid=7 "Linux")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年10月14日 23时14分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85612&appkey=1370085986&title=Linus%20Torvalds%20%E7%94%A8%20LLM%20%E8%BE%85%E5%8A%A9%E5%BC%80%E5%8F%91%E7%9A%84%E8%A1%A5%E4%B8%81%E9%80%92%E4%BA%A4%E6%8E%A5%E5%8F%97%E5%AE%A1%E6%9F%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自异形：悲伤之海**

Linux 作者 Linus Torvalds 在维护者峰会上透露他在大模型帮助下开发了一系列补丁解决一个长期存在的问题。现在这组 10 个补丁已递交接受审查。这些补丁主要增强 folio 的查找机制：通过识别处于热数据状态的 folio，设置一个“延迟释放该 folio 直至 RCU 周期结束”的标志。随后利用 RCU 延迟在 RCU 保护下进行常规的 folio 查找，同时在 RCU 保护下直接进行实际的 folio 数据访问...补丁在测试中性能实现了数量级的提升，但已发现存在竞态条件，因此需要进一步完善。
https://lwn.net/Articles/1100449/

[回复](/comments?sid=85612&op=reply&type=story)

﻿

任何有可能出错的事将会出错--墨菲定理

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261014)
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