---
title: 安全研究人员利用 Claude 成功入侵 OpenAI
url: https://www.solidot.org/story?sid=85421
source: 奇客Solidot–传递最新科技情报
date: 2026-09-18
fetch_date: 2026-09-19T07:01:19.320064
---

# 安全研究人员利用 Claude 成功入侵 OpenAI

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260918)
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

**本文已被查看 2190 次**

## 安全研究人员利用 Claude 成功入侵 OpenAI

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年09月18日 23时17分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85421&appkey=1370085986&title=%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6%E4%BA%BA%E5%91%98%E5%88%A9%E7%94%A8%20Claude%20%E6%88%90%E5%8A%9F%E5%85%A5%E4%BE%B5%20OpenAI%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自我是6号**

Hacktron 安全团队组合利用 OpenAI 的 SSO（单点登录）配置错误以及其社区论坛使用的 Discourse 软件 libheif 软件包堆缓冲区溢出漏洞，成功控制了多名 OpenAI 员工的 ChatGPT 账户。利用这些账户安全研究人员能访问 OpenAI 内部代码库，以及其他关联服务。他们向 OpenAI 和 Discourse 报告了 bug，从 OpenAI 获得了 6500 美元的赏金。安全研究人员利用了 OpenAI 竞争对手 Anthropic 的 Claude AI 工具去辅助发现 bug，以及实现远程代码执行 RCE。他们一开始使用的是较旧的模型 Opus 4.8，之后使用了新发布的 Opus 5.5。整个 AI 辅助 bug 发现和辅助攻击消耗的 token 支出不到 3000 美元，AI 智能体花费了数天时间，而研究人员投入的人工时间仅仅数小时，凸显了 AI 时代黑客攻击成本的低廉。
https://www.hacktron.ai/blog/hacking-openai

[回复](/comments?sid=85421&op=reply&type=story)

﻿

法律必须被信仰，否则形同虚设。--伯尔曼

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260918)
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