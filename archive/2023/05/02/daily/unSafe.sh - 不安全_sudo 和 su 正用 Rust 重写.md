---
title: sudo 和 su 正用 Rust 重写
url: https://buaq.net/go-161295.html
source: unSafe.sh - 不安全
date: 2023-05-02
fetch_date: 2025-10-04T11:38:31.426252
---

# sudo 和 su 正用 Rust 重写

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

sudo 和 su 正用 Rust 重写

登录 注册
*2023-5-1 21:55:6
Author: [www.solidot.org(查看原文)](/jump-161295.htm)
阅读量:30
收藏*

---

[登录](https://www.solidot.org/login) [注册](https://www.solidot.org/register)

* 文章

  [往日文章](https://www.solidot.org/?issue=20230430)
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

**本文已被查看 362 次**

## sudo 和 su 正用 Rust 重写

[![开源](https://icon.solidot.org/images/topics/topicopensource.png)](https://www.solidot.org/search?tid=3 "开源")

[Wilson](https://www.solidot.org/~Wilson) (42865)发表于 2023年05月01日 21时55分 星期一

在亚马逊 AWS 的资助下，类 Unix 操作系统广泛使用的工具 sudo 和 su 正用 Rust 语言重写，以提高软件在内存方面的安全性，进一步增强 Linux 和开源生态系统的安全性。sudo 的开发始于 1980 年代，过去几十年里它已经成为一种必不可少的工具，但它是用 C 语言编写的，遭遇过许多与内存安全问题相关的漏洞。为了确保关键软件的安全性，防止内存安全漏洞，Ferrous Systems 和 Tweede Golf 正在联合将 sudo 从 C 移植到 Rust，他们的项目 sudo-rs 托管在 GitHub 上。

https://www.memorysafety.org/blog/sudo-and-su/

[回复](https://www.solidot.org/comments?sid=74836&op=reply&type=story)

﻿

你自己的代码如果超过6个月不看，再看的时候也一样像是别人写--伊格尔森定律

* [首页](https://www.solidot.org/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](https://www.solidot.org/?issume=20230430)
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

文章来源: https://www.solidot.org/story?sid=74836
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)