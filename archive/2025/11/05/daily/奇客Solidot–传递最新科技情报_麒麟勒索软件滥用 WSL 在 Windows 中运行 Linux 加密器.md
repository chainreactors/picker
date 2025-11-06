---
title: 麒麟勒索软件滥用 WSL 在 Windows 中运行 Linux 加密器
url: https://www.solidot.org/story?sid=82723
source: 奇客Solidot–传递最新科技情报
date: 2025-11-05
fetch_date: 2025-11-06T03:14:33.989210
---

# 麒麟勒索软件滥用 WSL 在 Windows 中运行 Linux 加密器

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251105)
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

**本文已被查看 1922 次**

## 麒麟勒索软件滥用 WSL 在 Windows 中运行 Linux 加密器

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年11月05日 14时09分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82723&appkey=1370085986&title=%E9%BA%92%E9%BA%9F%E5%8B%92%E7%B4%A2%E8%BD%AF%E4%BB%B6%E6%BB%A5%E7%94%A8%20WSL%20%E5%9C%A8%20Windows%20%E4%B8%AD%E8%BF%90%E8%A1%8C%20Linux%20%E5%8A%A0%E5%AF%86%E5%99%A8%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自蒲公英王朝2：风暴之墙**

麒麟（Qilin）勒索软件被发现滥用 Windows Subsystem for Linux(WSL)在 Windows 操作系统中执行 Linux 加密器以逃避传统安全工具的检测。麒麟勒索软件最初的名字叫 Agenda，2022 年 9 月改名为麒麟，沿用至今，它是目前最活跃的勒索软件之一。安全公司趋势科技和思科 Talos 报告，麒麟勒索软件组织今年至今攻击了 62 个国家的逾 700 名受害者，2025 年下半年每月新增受害者逾 40。趋势科技的安全研究员报告，麒麟勒索软件组织利用 WinSCP 将 Linux ELF 加密器传输到入侵的设备，然后通过 Splashtop 远程管理软件 (SRManager.exe) 直接在 Windows 系统中启动加密器。该加密器无法直接在 Windows 中运行，必须通过 WSL 子系统。WSL 允许用户直接在 Windows 系统中安装和运行 Linux 发行版，攻击者在获得设备的访问权限之后，会启用或安装 WSL，然后执行加密器，绕过传统的 Windows 安全软件。
https://www.bleepingcomputer.com/news/security/qilin-ransomware-abuses-wsl-to-run-linux-encryptors-in-windows/

[回复](/comments?sid=82723&op=reply&type=story)

﻿

疑人先自疑，律人先律己

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251105)
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