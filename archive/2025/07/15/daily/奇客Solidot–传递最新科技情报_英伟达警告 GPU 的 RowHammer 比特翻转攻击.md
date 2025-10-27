---
title: 英伟达警告 GPU 的 RowHammer 比特翻转攻击
url: https://www.solidot.org/story?sid=81784
source: 奇客Solidot–传递最新科技情报
date: 2025-07-15
fetch_date: 2025-10-06T23:27:04.994285
---

# 英伟达警告 GPU 的 RowHammer 比特翻转攻击

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

**本文已被查看 5335 次**

## 英伟达警告 GPU 的 RowHammer 比特翻转攻击

[![安全](https://icon.solidot.org/images/topics/topicsecurity.png?123)](/search?tid=100 "安全")

[Wilson](/~Wilson) (42865)发表于 2025年07月14日 13时55分 星期一 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=81784&appkey=1370085986&title=%E8%8B%B1%E4%BC%9F%E8%BE%BE%E8%AD%A6%E5%91%8A%20GPU%20%E7%9A%84%20RowHammer%20%E6%AF%94%E7%89%B9%E7%BF%BB%E8%BD%AC%E6%94%BB%E5%87%BB "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自月光狂想曲**

英伟达发布安全通知，警告其高端 GPU 使用的 GDDR6 显存在未启用 ECC 的情况下易受 RowHammer 比特翻转攻击。RowHammer 攻击指的是通过反复访问内存芯片的特定区域导致比特翻转。比特翻转（Bitflips）是指储存在电子设备上的个别比特发生翻转的事件，比如从 0 变为 1 或反之亦然。 RowHammer 比特翻转攻击已经存在了很多年，英伟达建议如果 GPU 支持 ECC 就启用该功能。GDDR7 和 HBM3 内置了 ECC 因此能自动抵御 RowHammer 攻击。
nvidia.custhelp.com/app/answers/detail/a\_id/5671/~/security-notice%3A-rowhammer---july-2025

﻿

所谓现实只不过是一个错觉，虽然这个错觉非常持久。--爱因斯坦

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