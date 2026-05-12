---
title: Mythos 发现了一个 curl 漏洞
url: https://www.solidot.org/story?sid=84269
source: 奇客Solidot–传递最新科技情报
date: 2026-05-11
fetch_date: 2026-05-12T05:37:50.840519
---

# Mythos 发现了一个 curl 漏洞

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260511)
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

**本文已被查看 1888 次**

## Mythos 发现了一个 curl 漏洞

[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")
[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年05月11日 21时20分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84269&appkey=1370085986&title=Mythos%20%E5%8F%91%E7%8E%B0%E4%BA%86%E4%B8%80%E4%B8%AA%20curl%20%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自诺比、龙和意识星云**

Anthropic 上个月宣布的新 AI 模型 Mythos 引发了媒体的广泛关注，它宣传 Mythos 能极其精确的发现源代码中的安全漏洞。它的识别能力如此强大以至于 Anthropic 暂不向公众发布该模型，而是先提供给少数几家公司，以便于它们能优先解决其发现的安全漏洞。curl 维护者 Daniel Stenberg 认为这是一次极其成功的营销噱头。curl 是广泛使用的开源项目，因此他获得了 Mythos 的访问权限。curl 目前包含了 17.6 万行 C 代码，共 66 万个单词。Mythos 最终返回了一份安全报告，声称确认了五个安全漏洞。但 curl 的安全团队在仔细检查后发现其中 3 个是误报，1 个是 Bug，还有 1 个是低危级别的安全漏洞，将会在下个月释出的版本中修复。安全报告还详细纪录了约 20 个 bug，基本上都是正确的。Stenberg 表示他没有看到任何证据表明 Mythos 在发现安全漏洞上比之前的其它工具更胜一筹，Mythos 可能略好一点，但不足以对代码分析产生显著影响。
https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/

[回复](/comments?sid=84269&op=reply&type=story)

﻿

什么都比不上厄运更能磨练人的德性。——莎士比亚

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260511)
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