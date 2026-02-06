---
title: 俄罗斯黑客快速利用微软紧急修复的 Office 高危漏洞
url: https://www.solidot.org/story?sid=83486
source: 奇客Solidot–传递最新科技情报
date: 2026-02-05
fetch_date: 2026-02-06T04:08:56.971624
---

# 俄罗斯黑客快速利用微软紧急修复的 Office 高危漏洞

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260205)
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

**本文已被查看 1830 次**

## 俄罗斯黑客快速利用微软紧急修复的 Office 高危漏洞

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2026年02月05日 16时12分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=83486&appkey=1370085986&title=%E4%BF%84%E7%BD%97%E6%96%AF%E9%BB%91%E5%AE%A2%E5%BF%AB%E9%80%9F%E5%88%A9%E7%94%A8%E5%BE%AE%E8%BD%AF%E7%B4%A7%E6%80%A5%E4%BF%AE%E5%A4%8D%E7%9A%84%20Office%20%E9%AB%98%E5%8D%B1%E6%BC%8F%E6%B4%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自去月球**

微软在 1 月 26 日释出紧急更新修复 Office 高危漏洞 CVE-2026-21509，不到 48 小时俄罗斯黑客组织就对补丁进行了逆向工程，开始利用该漏洞发动大规模钓鱼攻击，入侵多个国家的外交、海事和交通机构。安全公司 Trellix 的研究人员发现，钓鱼攻击持续了 72 小时，被称为 APT28 aka Fancy Bear、Sednit、Forest Blizzard 和 Sofacy 的黑客组织向主要位于东欧的 9 个国家发送了至少 29 封恶意电邮。被攻击的国家包括了波兰、斯洛文尼亚、土耳其、希腊、阿联酋、乌克兰、罗马尼亚和玻利维亚，目标组织包括国防部（40%）、运输/物流运营商（35%）和外交机构（25%）。攻击者利用尚未修复的漏洞安装了两种新后门程序 BeardShell 或 NotDoor。BeardShell 主要用于侦察，运行在内存中不会在硬盘上留下痕迹，NotDoor 则是监控电子邮件文件夹的 VBA 宏。
https://arstechnica.com/security/2026/02/russian-state-hackers-exploit-office-vulnerability-to-infect-computers/
https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21509
https://www.trellix.com/blogs/research/apt28-stealthy-campaign-leveraging-cve-2026-21509-cloud-c2/

[回复](/comments?sid=83486&op=reply&type=story)

﻿

自由的保证是什么?是对自己不再感到羞耻。--尼采

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260205)
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