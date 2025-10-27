---
title: Valve 用了 15 个月才修复 Dota 2 的一个高危漏洞
url: https://www.solidot.org/story?sid=74096
source: 奇客Solidot–传递最新科技情报
date: 2023-02-11
fetch_date: 2025-10-04T06:21:04.679977
---

# Valve 用了 15 个月才修复 Dota 2 的一个高危漏洞

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

**本文已被查看 7331 次**

## Valve 用了 15 个月才修复 Dota 2 的一个高危漏洞

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年02月10日 14时56分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74096&appkey=1370085986&title=Valve%20%E7%94%A8%E4%BA%86%2015%20%E4%B8%AA%E6%9C%88%E6%89%8D%E4%BF%AE%E5%A4%8D%20Dota%202%20%E7%9A%84%E4%B8%80%E4%B8%AA%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自记忆残留**

在研究人员私下警告之后，Valve 修复了一个 Dota 2 的高危漏洞。该漏洞位于 Dota 2 使用的开源 JS 引擎 V8 中，它是在 2021 年发现的，跟踪编号 CVE-2021-38003，Google 在 2021 年 10 月修复了漏洞，但 Valve 直到上个月才修复，期间隔了 15 个月。安全公司 Avast 的研究人员发现，已经有一名黑客利用修补的拖延而发布了 4 个自定义游戏模式利用该漏洞。Dota 2 支持自定义游戏模式，用户通过一个验证流程递交自己开发的自定义模式后可以公开发布供其他玩家下载。黑客递交的第一个自定义模式显然是用于概念验证的，它的一个文件名叫 evil.lua，之后递交的三个自定义模式则更隐蔽，包含了后门，可以执行通过 HTTP 下载的任意 JS 脚本。
https://arstechnica.com/?p=1916611

﻿

百善孝为先，论心不论迹，论迹贫家无孝子；万恶淫为首，论迹不论心，论心世上少完人

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