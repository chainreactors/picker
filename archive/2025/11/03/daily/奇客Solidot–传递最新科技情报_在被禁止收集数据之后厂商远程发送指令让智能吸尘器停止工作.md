---
title: 在被禁止收集数据之后厂商远程发送指令让智能吸尘器停止工作
url: https://www.solidot.org/story?sid=82701
source: 奇客Solidot–传递最新科技情报
date: 2025-11-03
fetch_date: 2025-11-04T03:10:02.315612
---

# 在被禁止收集数据之后厂商远程发送指令让智能吸尘器停止工作

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251103)
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

**本文已被查看 2108 次**

## 在被禁止收集数据之后厂商远程发送指令让智能吸尘器停止工作

[![IT](https://icon.solidot.org/images/topics/topicit.png?123)](/search?tid=9 "IT")

[Edwards](/~Edwards) (42866)发表于 2025年11月03日 15时18分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=82701&appkey=1370085986&title=%E5%9C%A8%E8%A2%AB%E7%A6%81%E6%AD%A2%E6%94%B6%E9%9B%86%E6%95%B0%E6%8D%AE%E4%B9%8B%E5%90%8E%E5%8E%82%E5%95%86%E8%BF%9C%E7%A8%8B%E5%8F%91%E9%80%81%E6%8C%87%E4%BB%A4%E8%AE%A9%E6%99%BA%E8%83%BD%E5%90%B8%E5%B0%98%E5%99%A8%E5%81%9C%E6%AD%A2%E5%B7%A5%E4%BD%9C "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自诺比与扭曲时空的项链**

工程师 Harishanka 监控了其拥有的 iLife A11 智能吸尘器的进出流量，发现吸尘器一直在向厂商（深圳智意）发送日志和遥测数据——这些行为他并没有授权。他决定屏蔽厂商遥测服务器的 IP 地址，同时继续开放固件和 OTA 服务器的访问。结果他的吸尘器很快就连开机都无法开机了。他送去维修，但都没有查出任何问题。吸尘器每次都能正常工作几天，然后停止工作。他决定拆开吸尘器查找问题根源。吸尘器使用了全志的 A33 SoC，运行 TinaLinux 操作系统，使用微控制器 GD32F103 管理传感器，测试发现硬件本身没有问题，因此他将注意力转向操作系统和软件。他在日志里发现了一个指令，其时间戳与设备停止工作时间完全吻合，这显然是一条终止指令，在他撤销该指令并重启设备后，设备恢复了正常工作。他建议不要将家里的主要 WiFi 网络连接物联网设备，将这些智能设备视为家里的陌生人。
https://codetiger.github.io/blog/the-day-my-smart-vacuum-turned-against-me/
https://yro.slashdot.org/story/25/11/02/2241201/manufacturer-remotely-bricks-smart-vacuum-after-its-owner-blocked-it-from-collecting-data

[回复](/comments?sid=82701&op=reply&type=story)

﻿

以眼还眼，世界只会更盲目。--甘地

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251103)
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