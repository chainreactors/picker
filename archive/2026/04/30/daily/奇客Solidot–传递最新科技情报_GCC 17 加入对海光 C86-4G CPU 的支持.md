---
title: GCC 17 加入对海光 C86-4G CPU 的支持
url: https://www.solidot.org/story?sid=84188
source: 奇客Solidot–传递最新科技情报
date: 2026-04-30
fetch_date: 2026-05-01T05:38:47.408597
---

# GCC 17 加入对海光 C86-4G CPU 的支持

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260430)
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

**本文已被查看 2049 次**

## GCC 17 加入对海光 C86-4G CPU 的支持

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![长城](https://icon.solidot.org/images/topics/topicGreat Wall.png?123)](/search?tid=148 "长城")

[Edwards](/~Edwards) (42866)发表于 2026年04月30日 13时54分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84188&appkey=1370085986&title=GCC%2017%20%E5%8A%A0%E5%85%A5%E5%AF%B9%E6%B5%B7%E5%85%89%20C86-4G%20CPU%20%E7%9A%84%E6%94%AF%E6%8C%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自智者之惧**

GCC 编译器项目合并了支持海光 C86-4G CPU 的补丁。海光最早是与 AMD 合作的半导体企业，授权提供 AMD Zen 1 CPU的本地化版本，其产品仅供国内市场使用。海光去年五月宣布与中科曙光合并，但年底宣布合并计划终止。
C86-4G 为 16 核/32 线程处理器，其性能接近英特尔的 Raptor Lake CPU，支持 DDR5 和 PCIe Gen 5。海光声称 C86-4G 利用了自主研发的新微架构，但仅从 GCC 补丁看它仍然与 AMD Zen 有许多相似之处。C86-4G 包括了 C86-4G-M4 / C86-4G-M6 / C86-4G-M7 系列，其中 C86-4G-M7 支持 AVX-512 指令集。
https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=2a64a63d982584618af1de1b5d5f1f1c3ec03502
https://www.phoronix.com/news/Hygon-C86-4G-CPU-GCC-17
https://www.stcn.com/article/detail/3532998.html

[回复](/comments?sid=84188&op=reply&type=story)

﻿

什么都比不上厄运更能磨练人的德性。——莎士比亚

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260430)
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