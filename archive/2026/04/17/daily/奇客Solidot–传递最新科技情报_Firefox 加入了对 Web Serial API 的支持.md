---
title: Firefox 加入了对 Web Serial API 的支持
url: https://www.solidot.org/story?sid=84075
source: 奇客Solidot–传递最新科技情报
date: 2026-04-17
fetch_date: 2026-04-18T04:32:02.022704
---

# Firefox 加入了对 Web Serial API 的支持

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20260417)
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

**本文已被查看 1260 次**

## Firefox 加入了对 Web Serial API 的支持

[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")

[Edwards](/~Edwards) (42866)发表于 2026年04月17日 23时24分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=84075&appkey=1370085986&title=Firefox%20%E5%8A%A0%E5%85%A5%E4%BA%86%E5%AF%B9%20Web%20Serial%20API%20%E7%9A%84%E6%94%AF%E6%8C%81 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自风暴之墙**

Firefox Nightly 版加入了对 Web Serial API 的支持，而六年前 Mozilla 以不安全为由反对支持该 API。Web Serial API 允许浏览器与通过串行端口通信的设备交互，此类设备包括 3D 打印机，微控制器如 Arduino 和 ESP32，智能家居面板如 ESPHome，以及通过 USB 或蓝牙模拟串行端口的设备通信。Google Chrome 自 2021 年起加入了对 Web Serial API 的支持，基于 Chromium 的浏览器如 Edge、Opera 和 Vivaldi 也都支持该 API。Mozilla 杰出工程师 Martin Thomso 在 2020 年表示，对于如此强大的功能，无法为用户提供充分的保护，即使用户同意。串行端口是物理连接赋予高度信任的时代的遗物，许多设备允许通过该接口连接的设备在没有任何身份验证的情况下获得管理权限，这一权限甚至超过了 root。两年后 Mozilla 被要求重新考虑其立场，Firefox CTO Bobby Holley 表示 Mozilla 愿意采用和 WebMIDI 相同的附加组件守门机制（add-on-gating mechanism）支持 WebSerial API。Mozilla 目前仍然反对 WebUSB 和 WebHID，而苹果 WebKit 团队仍然对 WebSerial、WebUSB 和 WebHID 持反对态度。
https://www.theregister.com/2026/04/14/firefox\_nightly\_web\_serial/?td=rt-3a

[回复](/comments?sid=84075&op=reply&type=story)

﻿

罗马帝国灭亡的其中一个主要原因是他们没有0 - 这样他们就没法给自己的C程序指明成功退出的路--Robert Firth

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20260417)
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