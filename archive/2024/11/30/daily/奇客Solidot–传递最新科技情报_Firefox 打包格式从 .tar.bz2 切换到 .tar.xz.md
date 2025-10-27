---
title: Firefox 打包格式从 .tar.bz2 切换到 .tar.xz
url: https://www.solidot.org/story?sid=79912
source: 奇客Solidot–传递最新科技情报
date: 2024-11-30
fetch_date: 2025-10-06T19:15:43.252450
---

# Firefox 打包格式从 .tar.bz2 切换到 .tar.xz

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

**本文已被查看 7916 次**

## Firefox 打包格式从 .tar.bz2 切换到 .tar.xz

[![Firefox](https://icon.solidot.org/images/topics/topicfirefox.png?123)](/search?tid=39 "Firefox")

[Wilson](/~Wilson) (42865)发表于 2024年11月29日 17时17分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=79912&appkey=1370085986&title=Firefox%20%E6%89%93%E5%8C%85%E6%A0%BC%E5%BC%8F%E4%BB%8E%20.tar.bz2%20%E5%88%87%E6%8D%A2%E5%88%B0%20.tar.xz%20 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自最后的独角兽**

Mozilla 宣布，Firefox 的 Linux 二进制版本打包格式从 .tar.bz2 切换到 .tar.xz。这一改变将减少下载的文件容量缩短解压缩时间。Firefox 的 .tar.xz 包平均比 .tar.bz2 包小 25%，意味着能更快完成下载，节省时间和带宽。此外 tar.xz 包解压所需时间只需要 .tar.bz2 的二分之一。Mozilla 解释说，选择.tar.xz 而不是 Zstandard (.zst)的原因是虽然 Zstandard 解压更快，但压缩率低于 .tar.xz，而且 Linux 发行版基本都支持 .tar.xz，兼容性更胜一筹。
https://blog.nightly.mozilla.org/2024/11/28/announcing-faster-lighter-firefox-downloads-for-linux-with-tar-xz-packaging/

﻿

真正的无知不是知识的缺乏，而是拒绝获取知识。——卡尔·波普尔

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