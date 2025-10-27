---
title: 英伟达全面转向开源 GPU 内核模块
url: https://www.solidot.org/story?sid=78731
source: 奇客Solidot–传递最新科技情报
date: 2024-07-19
fetch_date: 2025-10-06T17:41:29.844924
---

# 英伟达全面转向开源 GPU 内核模块

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

**本文已被查看 4279 次**

## 英伟达全面转向开源 GPU 内核模块

[![开源](https://icon.solidot.org/images/topics/topicopensource.png?123)](/search?tid=3 "开源")

[Wilson](/~Wilson) (42865)发表于 2024年07月18日 16时21分 星期四 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=78731&appkey=1370085986&title=%E8%8B%B1%E4%BC%9F%E8%BE%BE%E5%85%A8%E9%9D%A2%E8%BD%AC%E5%90%91%E5%BC%80%E6%BA%90%20GPU%20%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自苏珊娜之歌**

英伟达在 2022 年宣布开源其 Linux GPU 内核驱动模块，最初针对的是工作站/数据中心 GPU，随着开源内核驱动的改进，开源驱动模块与闭源驱动的性能相差无几。英伟达通过官方博客现在正式宣布，其开源内核模块最终将取代闭源驱动。英伟达称，对于 Grace Hopper 或 Blackwell 等平台，必须使用开源 GPU 内核模块，因为这些平台不支持私有驱动；对于来自 Turing、Ampere、Ada Lovelace 或 Hopper 架构的较新 GPU，它建议切换到开源的 GPU 内核模块；对于 Maxwell、Pascal 或 Volta 架构中的旧版 GPU，开源 GPU 内核模块不兼容，只能继续使用私有驱动。英伟达没有开源其用户空间驱动。
https://developer.nvidia.com/zh-cn/blog/nvidia-transitions-fully-towards-open-source-gpu-kernel-modules/

﻿

我并不同意你的观点，但是我誓死捍卫你说话的权利——伏尔泰

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