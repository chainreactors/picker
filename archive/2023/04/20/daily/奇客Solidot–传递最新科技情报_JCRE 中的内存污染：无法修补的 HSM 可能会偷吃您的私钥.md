---
title: JCRE 中的内存污染：无法修补的 HSM 可能会偷吃您的私钥
url: https://www.solidot.org/story?sid=74706
source: 奇客Solidot–传递最新科技情报
date: 2023-04-20
fetch_date: 2025-10-04T11:34:36.935074
---

# JCRE 中的内存污染：无法修补的 HSM 可能会偷吃您的私钥

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

**本文已被查看 7493 次**

## JCRE 中的内存污染：无法修补的 HSM 可能会偷吃您的私钥

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Edwards](/~Edwards) (42866)发表于 2023年04月19日 12时56分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=74706&appkey=1370085986&title=JCRE%20%E4%B8%AD%E7%9A%84%E5%86%85%E5%AD%98%E6%B1%A1%E6%9F%93%EF%BC%9A%E6%97%A0%E6%B3%95%E4%BF%AE%E8%A1%A5%E7%9A%84%20HSM%20%E5%8F%AF%E8%83%BD%E4%BC%9A%E5%81%B7%E5%90%83%E6%82%A8%E7%9A%84%E7%A7%81%E9%92%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自消失吧！书本**

Shawn the R0ck 写道：*私钥一直是安全保护的核心目标。由于密钥槽的限制，大多数加密货币硬件钱包使用 MCU 芯片（如 STM32F205RE）进行实现，以便能使用secure element存储和支持更广泛的加密货币种类，然而，那些对保护私钥有更高安全要求的人通常会对 Java 卡感兴趣，因为Java Card基本上是具有加密算法硬件实现的智能卡。私钥或对称密钥无法从中提取。用户只能从 Java 卡获得加密操作的结果，另外一点是已经使用通信参数初始化但尚未加载应用程序（applet）的 Java 卡是可由用户编程的，而且有一些以 Java 卡 applet 形式实现的各种功能的自由开源软件项目。即使Java Card作为HSM（硬件安全模块）的安全性高于常见加密货币硬件钱包的实现，但依然有安全风险，HardenedVault介绍了两个典型的漏洞，这些漏洞位于更底层的JCRE（Java Card运行时环境），虽然不会导致私钥被泄露，但会导致应用程序陷入无法恢复的错误。一旦出现这种问题，卡中的私钥就可能会丢失。智能卡作为 HSM 的实现比基于 MCU 的解决方案（几乎所有硬件钱包都采用了这种方案）更加安全，但仍存在某些安全风险。甚至获得 EAL 5+ 认证的硬件钱包也有被攻击的记录。因此，在系统安全方面，我们仍需要坚持纵深防御的策略。另一方面，透明度很重要，开源是确保 HSM 的整个运行环境能够得到适当审计的唯一途径。对于 Java 卡，我们希望未来能够拥有一个自由开源且可更新的 JCRE。或者某种功能上类似于 Java 卡但可以用 C 语言编程的 HSM（对不起，我们不想使用 Rust，因为我们已经有了现代的缓解和检测器，Rust 对此来说有些生锈了，不是吗？），甚至可以直接使用通用计算（如可信计算、运行时保护、攻击面缩小等）实现。*
https://hardenedvault.net/blog/2023-04-18-java-card-runtime-memory-corruption/

﻿

会玩的人才会学

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