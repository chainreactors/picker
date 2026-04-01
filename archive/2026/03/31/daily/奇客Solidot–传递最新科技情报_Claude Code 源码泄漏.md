---
title: Claude Code 源码泄漏
url: https://www.solidot.org/story?sid=83926
source: 奇客Solidot–传递最新科技情报
date: 2026-03-31
fetch_date: 2026-04-01T04:45:32.401883
---

# Claude Code 源码泄漏

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260331)
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

**本文已被查看 806 次**

## Claude Code 源码泄漏

[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Edwards](/~Edwards) (42866)发表于 2026年03月31日 22时20分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83926&appkey=1370085986&title=Claude%20Code%20%E6%BA%90%E7%A0%81%E6%B3%84%E6%BC%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自丽赛的故事**

Anthropic 公司开发的 AI 编程工具 Claude Code 在发布到 npm 上时不小心通过一个映射文件泄漏了未混淆的源代码，源代码被提取出来之后被上传到了 GitHub 等平台。用户发现， Claude Code 使用了正则表达式检测用户提示词中的负面情绪。使用正则表达式去检测情绪比调用大模型要快得多也能显著节省算力。
https://github.com/chatgptprojects/claude-code
https://github.com/chatgptprojects/claude-code/blob/642c7f944bbe5f7e57c05d756ab7fa7c9c5035cc/src/utils/userPromptKeywords.ts#L8
https://news.ycombinator.com/item?id=47584540

[回复](/comments?sid=83926&op=reply&type=story)

﻿

在所有的禁欲道德里，人把自己的一部分视为神，加以崇拜，因此被迫把其他部分加以恶魔化。——尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260331)
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