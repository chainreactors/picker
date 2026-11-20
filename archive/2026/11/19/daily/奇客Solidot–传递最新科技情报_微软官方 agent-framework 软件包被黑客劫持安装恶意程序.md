---
title: 微软官方 agent-framework 软件包被黑客劫持安装恶意程序
url: https://www.solidot.org/story?sid=85931
source: 奇客Solidot–传递最新科技情报
date: 2026-11-19
fetch_date: 2026-11-20T09:22:17.167190
---

# 微软官方 agent-framework 软件包被黑客劫持安装恶意程序

* 至顶科技：
* [至顶网](https://www.zhiding.cn/ "至顶网")
* [科技行者](https://www.techwalker.com/ "科技行者")
* [Solidot](https://www.solidot.org/ "Solidot")

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20261119)
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

**本文已被查看 4004 次**

## 微软官方 agent-framework 软件包被黑客劫持安装恶意程序

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年11月19日 16时24分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=85931&appkey=1370085986&title=%E5%BE%AE%E8%BD%AF%E5%AE%98%E6%96%B9%20agent-framework%20%E8%BD%AF%E4%BB%B6%E5%8C%85%E8%A2%AB%E9%BB%91%E5%AE%A2%E5%8A%AB%E6%8C%81%E5%AE%89%E8%A3%85%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自火星战将**

微软托管在 PyPI 上的 agent-framework 软件包被黑客劫持安装窃取信息的恶意程序。agent-framework 每月下载量近 20 万次，主要用于构建和部署 AI 智能体。受影响的版本是 v1.26.1 和 1.26.2，会窃取开发者在 Azure、Git、Docker、Hugging Face 等服务上的环境变量、凭据文件以及其它敏感信息。更糟糕的是软件包无需被导入，只要安装该软件包的 Python 解释器启动，恶意代码便会运行。微软发言人在一份声明中表示在调查期间它将部分软件包项目设为私有。
https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858

[回复](/comments?sid=85931&op=reply&type=story)

﻿

渴求美德而非奖赏。

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20261119)
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