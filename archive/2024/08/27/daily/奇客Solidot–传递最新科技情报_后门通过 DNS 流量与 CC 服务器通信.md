---
title: 后门通过 DNS 流量与 CC 服务器通信
url: https://www.solidot.org/story?sid=79075
source: 奇客Solidot–传递最新科技情报
date: 2024-08-27
fetch_date: 2025-10-06T18:06:02.903833
---

# 后门通过 DNS 流量与 CC 服务器通信

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

**本文已被查看 5553 次**

## 后门通过 DNS 流量与 CC 服务器通信

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2024年08月26日 17时00分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79075&appkey=1370085986&title=%E5%90%8E%E9%97%A8%E9%80%9A%E8%BF%87%20DNS%20%E6%B5%81%E9%87%8F%E4%B8%8E%20CC%20%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%80%9A%E4%BF%A1 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自十二魔**

赛门铁克研究人员报告了一种使用罕见技术的后门 Backdoor.Msupedge。它通过 DNS 流量与 C&C（指令控制）服务器通信。它的 DNS 隧道工具是基于公开代码的 dnscat2 工具。Msupedge 还通过 C&C 服务器（ctl.msedeapi[.]net)）域名解析到 IP 地址作为指令。解析后的 IP 地址的第三个八位组是一个开关语句，后门的行为将根据该八位组减去 7 的值而进行改变。攻击者可能是通过最近修复的 PHP 高危漏洞 CVE-2024-4577 入侵系统的，漏洞的危险评分 9.8/10，影响 Windows 系统上安装的所有版本的 PHP，成功利用漏洞允许远程执行代码。
https://symantec-enterprise-blogs.security.com/threat-intelligence/taiwan-malware-dns
https://therecord.media/hackers-malware-university-taiwan-backdoor

﻿

发现可能性的界限的唯一办法就是越过这个界限，到不可能中去。--阿瑟·克拉克

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