---
title: WinRAR 0-Day 从 4 月开始就被利用
url: https://www.solidot.org/story?sid=75880
source: 奇客Solidot–传递最新科技情报
date: 2023-08-25
fetch_date: 2025-10-04T12:02:05.753493
---

# WinRAR 0-Day 从 4 月开始就被利用

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

**本文已被查看 5446 次**

## WinRAR 0-Day 从 4 月开始就被利用

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2023年08月24日 15时10分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=75880&appkey=1370085986&title=WinRAR%200-Day%20%E4%BB%8E%204%20%E6%9C%88%E5%BC%80%E5%A7%8B%E5%B0%B1%E8%A2%AB%E5%88%A9%E7%94%A8 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自火星战将**

WinRAR 上周修复了一个高危漏洞 CVE-2023-40477，该漏洞允许远程攻击者通过引诱受害者打开一个特制的 RAR 压缩文件去执行任意代码。安全公司 Group IB 周三公开了该漏洞的更多细节。该漏洞从今年四月起就开始被利用，攻击者通过证券交易论坛引诱受害者打开含有恶意代码的压缩文件，利用漏洞攻击者可以伪造文件扩展，在伪造的 .jpg 或 .txt 等文件格式中隐藏恶意脚本。当受害者打开文件，攻击者可以远程执行代码，安装 DarkMe、GuLoader 和 Remcos RAT 等系列恶意软件，然后从经纪帐户中提取出资金。Group-IB 称它跟踪到了至少 130 名受害者，但经济损失和受害者总数尚不清楚。
https://www.group-ib.com/blog/cve-2023-38831-winrar-zero-day/

﻿

宗教上最深的误解——认为坏人没有宗教。——尼采

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