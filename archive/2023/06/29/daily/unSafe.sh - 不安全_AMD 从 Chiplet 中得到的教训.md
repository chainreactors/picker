---
title: AMD 从 Chiplet 中得到的教训
url: https://buaq.net/go-170726.html
source: unSafe.sh - 不安全
date: 2023-06-29
fetch_date: 2025-10-04T11:46:41.268337
---

# AMD 从 Chiplet 中得到的教训

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

AMD 从 Chiplet 中得到的教训

登录 注册
*2023-6-28 18:42:2
Author: [www.solidot.org(查看原文)](/jump-170726.htm)
阅读量:17
收藏*

---

[登录](https://www.solidot.org/login) [注册](https://www.solidot.org/register)

* 文章

  [往日文章](https://www.solidot.org/?issue=20230627)
  [往日投票](https://www.solidot.org/polllist)
* 皮肤

  [蓝色](https://www.solidot.org/?theme=blue)
  [橙色](https://www.solidot.org/?theme=yellow)
  [绿色](https://www.solidot.org/?theme=green)
  [浅绿色](https://www.solidot.org/?theme=clightgreen)

* 分类:
* [首页](https://www.solidot.org/)
* [Linux](https://linux.solidot.org/)
* [科学](https://science.solidot.org/)
* [科技](https://technology.solidot.org/)
* [移动](https://mobile.solidot.org/)
* [苹果](https://apple.solidot.org/)
* [硬件](https://hardware.solidot.org/)
* [软件](https://software.solidot.org/)
* [安全](https://security.solidot.org/)
* [游戏](https://games.solidot.org/)
* [书籍](https://books.solidot.org/)
* [idle](https://idle.solidot.org/)
* [云计算](https://cloud.solidot.org/)

## 关注我们：

solidot新版网站常见问题，请点击[这里](https://www.solidot.org/QA)查看。

## 消息

**本文已被查看 473 次**

## AMD 从 Chiplet 中得到的教训

[![AMD](https://icon.solidot.org/images/topics/topicamd.png)](https://www.solidot.org/search?tid=22 "AMD")

[Wilson](https://www.solidot.org/~Wilson) (42865)发表于 2023年06月28日 18时42分 星期三

过去五年处理器从单个硅片转变成小芯片（Chiplet）集，小芯片们像大芯片一样集体行动。这种方法意味着芯片的不同功能块能用最适合的技术构建，有利于降低成本。AMD 产品技术架构师 Sam Naffziger 是小芯片方法的早期推动者，他接受采访谈论 AMD 从中得到的教训。他说小芯片架构的目的之一是对软件完全透明，因为软件很难改变。AMD 第二代 EPYC CPU 由一个位于中心位置的 I/O 小芯片和周围环绕的计算芯片构成。这种布局减少了内存延迟，消除了第一代芯片遭遇的软件挑战。AMD 最新的 MI300 加速器集成了 CPU 芯片和 GPU 芯片，对软件而言意味着可以共享内存地址空间，软件不再需要管理内存，降低了编程难度。

https://spectrum.ieee.org/chiplet

[回复](https://www.solidot.org/comments?sid=75365&op=reply&type=story)

﻿

如果你想走到高处，就要使用自己的两条腿！不要让别人把你抬到高处；不要坐在别人的背上和头上。 --尼采·F.W.

* [首页](https://www.solidot.org/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](https://www.solidot.org/?issume=20230627)
* [过去的投票](https://www.solidot.org/polllist)
* [编辑介绍](https://www.solidot.org/authors)
* [隐私政策](https://www.solidot.org/privacy)
* [使用条款](https://www.solidot.org/terms)
* [网站介绍](https://www.solidot.org/introd)
* [RSS](https://www.solidot.org/index.rss)

本站提到的所有注册商标属于他们各自的所有人所有，评论属于其发表者所有，其余内容版权属于 solidot.org(2009-) 所有 。

[![php](https://icon.solidot.org/images/btn/php.gif)](https://php.net/ "PHP 服务器")
[![apache](https://icon.solidot.org/images/btn/apache.gif)](https://apache.org/ "Apache 服务器")
[![mysql](https://icon.solidot.org/images/btn/mysql.gif)](https://www.mysql.com/ "MySQL")

[![](https://icon.solidot.org/images/btn/solidot-s.gif)](https://www.solidot.org "solidot.org")

京ICP证161336号    [京ICP备15039648号-15](http://beian.miit.gov.cn) 北京市公安局海淀分局备案号：11010802021500 [![](https://icon.zhiding.cn/beian/icon.png)](https://icp.valu.cn/search/domain/solidot.org?verifyCode=pu7c4)

举报电话：010-62641205-5060　涉未成年人举报专线：010-62641208 举报邮箱：[[email protected]](https://www.solidot.org/cdn-cgi/l/email-protection)　网上有害信息举报专区：<https://www.12377.cn>

文章来源: https://www.solidot.org/story?sid=75365
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)