---
title: Windows 收集用户计算机安装的编程智能体和开发工具
url: https://www.solidot.org/story?sid=85908
source: 奇客Solidot–传递最新科技情报
date: 2026-11-17
fetch_date: 2026-11-18T09:22:16.824100
---

# Windows 收集用户计算机安装的编程智能体和开发工具

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261117)
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

**本文已被查看 3799 次**

## Windows 收集用户计算机安装的编程智能体和开发工具

[![隐私](https://icon.solidot.org/images/topics/topic隐私.png?123)](/search?tid=133 "隐私")

[Edwards](/~Edwards) (42866)发表于 2026年11月17日 14时50分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85908&appkey=1370085986&title=Windows%20%E6%94%B6%E9%9B%86%E7%94%A8%E6%88%B7%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%AE%89%E8%A3%85%E7%9A%84%E7%BC%96%E7%A8%8B%E6%99%BA%E8%83%BD%E4%BD%93%E5%92%8C%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自苍穹微石**

一位开发者利用 AI 工具寻找 Windows 未记录的功能，结果发现了一个 DLL 文件记录了用户使用的编程智能体如 codex.exe、claude.exe、copilot.exe 和 cursor.exe 等，以及开发者工具如 python.exe、dotnet.exe、 gcc.exe 和 code.exe 等。该 DLL 文件是 MissionControlAggregator.dll，是一个运行中的 Windows 组件，它会将记录的信息保存在本地，报告给 Windows 诊断系统。除非用户选择退出诊断数据收集（默认启用），那么这些数据最终会发送给微软。MissionControlAggregator.dll 通过字符串比较操作检查一系列 AI 智能体和开发者工具。
https://xusheng.dev/posts/windows-coding-agent-telemetry/

[回复](/comments?sid=85908&op=reply&type=story)

﻿

你不问我，我就不会说谎话。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261117)
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