---
title: 微软花费 12 万美元 token 将 Copilot 运行时移植到 Rust 语言
url: https://www.solidot.org/story?sid=85433
source: 奇客Solidot–传递最新科技情报
date: 2026-09-20
fetch_date: 2026-09-21T07:26:39.517832
---

# 微软花费 12 万美元 token 将 Copilot 运行时移植到 Rust 语言

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260920)
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

**本文已被查看 2526 次**

## 微软花费 12 万美元 token 将 Copilot 运行时移植到 Rust 语言

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年09月20日 23时09分 星期日 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85433&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E8%8A%B1%E8%B4%B9%2012%20%E4%B8%87%E7%BE%8E%E5%85%83%20token%20%E5%B0%86%20Copilot%20%E8%BF%90%E8%A1%8C%E6%97%B6%E7%A7%BB%E6%A4%8D%E5%88%B0%20Rust%20%E8%AF%AD%E8%A8%80 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自白玫瑰**

微软利用使用 GPT-5.6 Sol 和 Claude Opus 4.8 的 AI 智能体、历时 14.5 周，花费 12 万美元 token 将 Copilot 运行时从 TypeScript 语言移植到 Rust 语言。该项目采用逐个更新运行时模块的方式执行，共进行了 135 次发布，平均每天提交约 1.3 个 Pull Request，最终将 43 万行 TypeScript 代码转换为 80 万行可用于生产的 Rust 代码。测试显示，原 TypeScript 代码每秒能完成 7.55 个生命周期（one-turn session lifecycles），而 Rust 代码每秒 120 个——意味着在特定工作负载下速度提升了 15.9 倍。包含 10 个客户端的智能体在 TypeScript 语言下消耗了 1383 MB 内存，而 Rust 语言版本仅消耗了 126 MB。Rust 版本将任务保持在进程内执行，无需像 TypeScript 版本那样启动外部后台进程完成任务。
https://www.theregister.com/devops/2026/09/18/microsoft-agentically-ports-copilot-runtime-to-rust-for-120k/5297549

[回复](/comments?sid=85433&op=reply&type=story)

﻿

首先他们无视于你，而后是嘲笑你，接着是批斗你，再来就是你的胜利之日。--甘地

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260920)
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