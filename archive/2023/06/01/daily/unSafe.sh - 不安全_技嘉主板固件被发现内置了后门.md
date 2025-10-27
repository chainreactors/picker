---
title: 技嘉主板固件被发现内置了后门
url: https://buaq.net/go-166667.html
source: unSafe.sh - 不安全
date: 2023-06-01
fetch_date: 2025-10-04T11:45:09.683331
---

# 技嘉主板固件被发现内置了后门

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

技嘉主板固件被发现内置了后门

登录 注册
*2023-5-31 22:23:3
Author: [www.solidot.org(查看原文)](/jump-166667.htm)
阅读量:61
收藏*

---

[登录](https://www.solidot.org/login) [注册](https://www.solidot.org/register)

* 文章

  [往日文章](https://www.solidot.org/?issue=20230531)
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

**本文已被查看 1041 次**

## 技嘉主板固件被发现内置了后门

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png)](https://www.solidot.org/search?tid=100 "安全")

[Wilson](https://www.solidot.org/~Wilson) (42865)发表于 2023年05月31日 22时23分 星期三

固件安全公司 Eclypsium 的研究人员披露，技嘉出售的主板固件含有一个隐藏的机制。每当计算机重启时，固件代码会启动一个更新程序，然后下载和执行另一个软件。其更新工具的实现是不安全的，有可能被劫持安装恶意程序。271 个型号的技嘉主板受到影响，其数量数以百万计。Eclypsium 的研究人员称，技嘉的更新机制没有正确验证就下载代码到用户计算机上，部分情况下甚至是通过 HTTP 而不是 HTTPS 下载的，这容易遭到中间人攻击。技嘉已经表示它计划修复研究人员发现的问题。

https://eclypsium.com/blog/supply-chain-risk-from-gigabyte-app-center-backdoor/
https://www.wired.com/story/gigabyte-motherboard-firmware-backdoor/

[回复](https://www.solidot.org/comments?sid=75115&op=reply&type=story)

﻿

真正的无知不是知识的缺乏，而是拒绝获取知识。——卡尔·波普尔

* [首页](https://www.solidot.org/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](https://www.solidot.org/?issume=20230531)
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

文章来源: https://www.solidot.org/story?sid=75115
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)