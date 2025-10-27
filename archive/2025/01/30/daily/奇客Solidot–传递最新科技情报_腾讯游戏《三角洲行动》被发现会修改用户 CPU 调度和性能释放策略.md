---
title: 腾讯游戏《三角洲行动》被发现会修改用户 CPU 调度和性能释放策略
url: https://www.solidot.org/story?sid=80446
source: 奇客Solidot–传递最新科技情报
date: 2025-01-30
fetch_date: 2025-10-06T20:11:03.490288
---

# 腾讯游戏《三角洲行动》被发现会修改用户 CPU 调度和性能释放策略

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

**本文已被查看 9442 次**

## 腾讯游戏《三角洲行动》被发现会修改用户 CPU 调度和性能释放策略

[![游戏](https://icon.solidot.org/images/topics/topicgames.png?123)](/search?tid=13 "游戏")
[![Bug](https://icon.solidot.org/images/topics/topicbug.png?123)](/search?tid=53 "Bug")

[Wilson](/~Wilson) (42865)发表于 2025年01月29日 20时58分 星期三 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=80446&appkey=1370085986&title=%E8%85%BE%E8%AE%AF%E6%B8%B8%E6%88%8F%E3%80%8A%E4%B8%89%E8%A7%92%E6%B4%B2%E8%A1%8C%E5%8A%A8%E3%80%8B%E8%A2%AB%E5%8F%91%E7%8E%B0%E4%BC%9A%E4%BF%AE%E6%94%B9%E7%94%A8%E6%88%B7%20CPU%20%E8%B0%83%E5%BA%A6%E5%92%8C%E6%80%A7%E8%83%BD%E9%87%8A%E6%94%BE%E7%AD%96%E7%95%A5 "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自神们自己**

英特尔 13-14 代酷睿处理器去年爆出因电压过高而导致的系统不稳定问题，芯片巨人为此释出了多轮微码以缓解该问题。游戏通常对 CPU 有高性能要求，为避免出现不稳定问题，今天很多游戏在运行前会检测下 CPU 类型以及其使用的微码版本，如果英特尔 CPU 的微码版本过低，游戏会弹出警告建议用户升级。腾讯去年 12 月上线了 FPS 多人对战游戏《三角洲行动》，根据社交媒体和论坛上的谈论，以及视频博主上传的视频，WeGame 版本的 《三角洲行动》（Steam 版本未知）会主动帮助用户“解决”潜在不稳定问题，方法是修改 CPU 调度与 CPU 性能释放策略，而且不检测 CPU 类型以及微码版本号，一刀切的应用于所有 CPU。AMD CPU 本来不存在该问题，但腾讯也修改了 AMD CPU 的性能释放策略，显著降低其性能。玩家在退出《三角洲行动》之后，这一修改仍然有效，意味着此后你的所有程序都会显著降低性能。对此问题，腾讯尚未公开予以回应。

﻿

我爱你，与你无关。--歌德

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