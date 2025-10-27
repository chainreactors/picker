---
title: 恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码
url: https://www.solidot.org/story?sid=74164
source: 奇客Solidot–传递最新科技情报
date: 2023-02-18
fetch_date: 2025-10-04T07:23:04.111148
---

# 恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251003)
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

**本文已被查看 7141 次**

## 恶意程序滥用微软 IIS 功能在 Windows 上执行恶意代码

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年02月17日 18时12分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74164&appkey=1370085986&title=%E6%81%B6%E6%84%8F%E7%A8%8B%E5%BA%8F%E6%BB%A5%E7%94%A8%E5%BE%AE%E8%BD%AF%20IIS%20%E5%8A%9F%E8%83%BD%E5%9C%A8%20Windows%20%E4%B8%8A%E6%89%A7%E8%A1%8C%E6%81%B6%E6%84%8F%E4%BB%A3%E7%A0%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自头号书迷**

安全公司赛门铁克的研究人员发现一种恶意程序滥用微软 IIS 的一项功能隐蔽的渗出数据和执行恶意代码。微软 IIS（Internet Information Services）是广泛使用的 Web 服务器，它的一项功能叫 Failed Request Event Buffering（FREB），旨在帮助管理员诊断错误，FREB 能从缓存中将部分错误相关的请求写入磁盘。黑客找到了滥用该功能的方法，攻击者首先需要入侵运行 IIS 的 Windows 系统，启用 FREB，通过将恶意代码注入 IIS 进程内存劫持执行，它随后就能拦截所有 HTTP 请求，寻找特殊格式的请求，这种特殊的请求能以隐蔽的方式执行远程代码，系统上没有可疑文件或进程在运行。研究人员将这种恶意程序命名为 Frebniis。
https://arstechnica.com/?p=1918304

﻿

没有一个人的记性，好到可以作个成功的说谎者——林肯

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251003)
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