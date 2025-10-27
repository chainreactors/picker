---
title: Xcode 14 意外导致应用体积大增
url: https://www.solidot.org/story?sid=73334
source: 奇客Solidot–传递最新科技情报
date: 2022-11-12
fetch_date: 2025-10-03T22:32:29.891207
---

# Xcode 14 意外导致应用体积大增

[登录](/login) [注册](/register)

* 文章

  [往日文章](/?issue=20251002)
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

**本文已被查看 9217 次**

## Xcode 14 意外导致应用体积大增

[![苹果](https://icon.solidot.org/images/topics/topicapple.png?123)](/search?tid=12 "苹果")

[WinterIsComing](/~WinterIsComing) (31822)发表于 2022年11月11日 14时27分 星期五 [新浪微博分享](//service.weibo.com/share/share.php?url=//www.solidot.org/story?sid=73334&appkey=1370085986&title=Xcode%2014%20%E6%84%8F%E5%A4%96%E5%AF%BC%E8%87%B4%E5%BA%94%E7%94%A8%E4%BD%93%E7%A7%AF%E5%A4%A7%E5%A2%9E "新浪微博分享")
![](https://icon.solidot.org/images/a7c7.png)

**来自镜中世界**

苹果在 9 月 12 日发布了 Xcode 14，称它的速度更快，体积还缩小了 30%。但使用 Xcode 14 构建的应用被发现体积大增：耐克 iOS 应用安装文件的大小从 182.2 MB 增长到了 322.1 MB；美航应用从 182.2 MB 增加到了 389.1 MB，Chime 从 162.8 MB 增加到 212.8 MB。为什么会出现这种情况？Xcode 14 默认禁用了位码(bitcode)。位码是封装应用的一种替代方法，应用递交到 App Store 之后它将部分构建过程留给苹果完成。而苹果做的一件事是剥离二进制符号。所谓二进制符号剥离是指在生产中某些类型的元数据对于运行应用是不需要的，因此从二进制文件里移除。这些元数据在生产前是有用的但在产品构建中只会膨胀体积。Xcode 14 禁用位码意味着在产品构建中二进制符号不再被剥离，导致了应用体积膨胀。
https://www.emergetools.com/blog/posts/how-xcode14-unintentionally-increases-app-size

﻿

所谓现实只不过是一个错觉，虽然这个错觉非常持久。--爱因斯坦

* [首页](/)
* [至顶网](http://www.zhiding.cn)
* [往日文章](/?issume=20251002)
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