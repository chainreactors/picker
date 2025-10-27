---
title: 高危 WinRAR 0day 正被利用
url: https://www.solidot.org/story?sid=82017
source: 奇客Solidot–传递最新科技情报
date: 2025-08-13
fetch_date: 2025-10-07T00:47:49.918801
---

# 高危 WinRAR 0day 正被利用

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251006)
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

**本文已被查看 6436 次**

## 高危 WinRAR 0day 正被利用

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2025年08月12日 09时23分 星期二 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82017&appkey=1370085986&title=%E9%AB%98%E5%8D%B1%20WinRAR%200day%20%E6%AD%A3%E8%A2%AB%E5%88%A9%E7%94%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自忽然七日**

两个俄罗斯网络犯罪组织过去两周正通过含有恶意附件的钓鱼邮件利用一个高危 WinRAR 0day。WinRAR 是广泛使用的文件压缩工具，用户数多达 5 亿，安全公司 ESET 于 7 月 18 日首次检测到针对 WinRAR 的攻击，7 月 24 日确定利用了一个 WinRAR 0day，同一天通知 WinRAR 开发商，6 天后漏洞修复。该漏洞滥用了名为交换数据流（Alternate Data Streams，ADS）的 Windows 功能，该功能允许同一文件路径可以有不同的表示方式。漏洞利用滥用该功能触发了一个此前未知的路径遍历漏洞，导致 WinRAR 将恶意可执行文件植入攻击者选择的文件路径 %TEMP% 和 %LOCALAPPDATA%，因为能执行代码 Windows 通常禁止访问这些路径。利用该漏洞的俄罗斯黑客组织包括 RomCom 和 Paper Werewolf。
arstechnica.com/security/2025/08/high-severity-winrar-0-day-exploited-for-weeks-by-2-groups/
www.welivesecurity.com/en/eset-research/update-winrar-tools-now-romcom-and-others-exploiting-zero-day-vulnerability/

[回复](/comments?sid=82017&op=reply&type=story)

﻿

自由的保证是什么?是对自己不再感到羞耻。--尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251006)
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