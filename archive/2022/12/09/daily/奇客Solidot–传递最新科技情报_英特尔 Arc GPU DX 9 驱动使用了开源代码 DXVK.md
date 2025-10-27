---
title: 英特尔 Arc GPU DX 9 驱动使用了开源代码 DXVK
url: https://www.solidot.org/story?sid=73594
source: 奇客Solidot–传递最新科技情报
date: 2022-12-09
fetch_date: 2025-10-04T01:00:26.667431
---

# 英特尔 Arc GPU DX 9 驱动使用了开源代码 DXVK

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

**本文已被查看 9408 次**

## 英特尔 Arc GPU DX 9 驱动使用了开源代码 DXVK

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")
[![Intel](https://icon.solidot.org/images/topics/topicintel.png?123)](/search?tid=80 "Intel")

[Wilson](/~Wilson) (42865)发表于 2022年12月08日 14时56分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73594&appkey=1370085986&title=%E8%8B%B1%E7%89%B9%E5%B0%94%20Arc%20GPU%20DX%209%20%E9%A9%B1%E5%8A%A8%E4%BD%BF%E7%94%A8%E4%BA%86%E5%BC%80%E6%BA%90%E4%BB%A3%E7%A0%81%20DXVK "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自尘埃记**

英特尔 Arc GPU 独显在 DX 9 游戏下的性能相当差，它最近对 Arc 的 DX 9 驱动进行了大更新，结果发现新 DX 9 驱动使用了开源代码 DXVK，而英特尔的官方博客根本没有提到 DXVK，只有查看 readme 文件才发现是 DXVK。DXVK 是 Steam Play Proton 的一部分，而 Proton 是 Windows 兼容层项目 Wine 的分支，它能将 Direct3D 9、Direct3D 10 和 Direct3D 11 翻译到 Vulkan，它有 Linux 的原生实现，也支持 Windows。英特尔使用 DXVK 并不太意外，英伟达也在 RTX Remix 中使用了 DXVK。
https://downloadmirror.intel.com/761751/readme.txt
https://www.gamingonlinux.com/2022/12/intel-using-dxvk-part-of-steam-proton-for-their-windows-arc-gpu-dx-9-drivers/

﻿

人们还往往把真理和错误混在一起去教人，而坚持的却是错误。--歌德

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