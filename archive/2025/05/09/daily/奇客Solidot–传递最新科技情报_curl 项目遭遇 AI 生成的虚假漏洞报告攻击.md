---
title: curl 项目遭遇 AI 生成的虚假漏洞报告攻击
url: https://www.solidot.org/story?sid=81237
source: 奇客Solidot–传递最新科技情报
date: 2025-05-09
fetch_date: 2025-10-06T22:28:53.099708
---

# curl 项目遭遇 AI 生成的虚假漏洞报告攻击

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

**本文已被查看 6544 次**

## curl 项目遭遇 AI 生成的虚假漏洞报告攻击

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![人工智能](https://icon.solidot.org/images/topics/topicAI.png?123)](/search?tid=151 "人工智能")

[Wilson](/~Wilson) (42865)发表于 2025年05月08日 13时45分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81237&appkey=1370085986&title=curl%20%E9%A1%B9%E7%9B%AE%E9%81%AD%E9%81%87%20AI%20%E7%94%9F%E6%88%90%E7%9A%84%E8%99%9A%E5%81%87%E6%BC%8F%E6%B4%9E%E6%8A%A5%E5%91%8A%E6%94%BB%E5%87%BB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自银色金属恋人**

curl 项目正与大量由 AI 生成的虚假漏洞报告作斗争，curl 作者 Daniel Stenberg 认为这是针对该项目的 DDoS 攻击。Stenberg 称至今没有看到一份 AI 帮助下完成的漏洞报告是有效的。5 月 4 日的一份安全报告令 Stenberg 倍感崩溃，因为报告引用了不存在的函数，而且不适用于当前版本。甚至还有安全报告包含了 AI 提示命令。Stenberg 希望管理漏洞报告的平台 HackerOne 能使用更多工具打击 AI 生成的漏洞报告，他计划封禁递交此类报告的用户。
Ars:Open source project curl is sick of users submitting “AI slop” vulnerabilities

﻿

计算机没什么用。他们只会告诉你答案。--毕加索

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