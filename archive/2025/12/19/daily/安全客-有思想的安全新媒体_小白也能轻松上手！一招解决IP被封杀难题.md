---
title: 小白也能轻松上手！一招解决IP被封杀难题
url: https://www.anquanke.com/post/id/311754
source: 安全客-有思想的安全新媒体
date: 2025-12-19
fetch_date: 2025-12-20T03:13:45.873715
---

# 小白也能轻松上手！一招解决IP被封杀难题

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 小白也能轻松上手！一招解决IP被封杀难题

阅读量**17269**

发布时间 : 2025-12-19 10:13:26

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

在攻防演练准备中，扫描目标资产时最头疼的问题是什么？

**是大量的访问导致使用的ip被封！手动更换IP不仅耗时费力，还可能导致任务中断、得分下降。**

给大家推荐一款轻松简单，小白也能上手搭建的代理池——**fir-proxy**。这款开源高可用代理池能在多个IP中智能自动轮换新IP，大幅降低手动操作时间，让你专注于攻击策略，提升演练得分效率。(该项目一个星期的时间就已经有三位数的star，可见质量之高。)

![]()

文件下载后，项目需由python编写，按照requirements所需的环境安装，完成并运行main.py就能进入到如图所示界面，功能一目了然，下面就对项目的优点做个简单介绍。

![]()

代理获取途径多样化：支持获取在线代理，也可以自己导入代理（上图中的可用代理文件夹里面有作者自己私藏的ip而且还会更新）。什么你说这都满足不了你？作者还自己写了个爬取的脚本，可以自己去爬取。

![]()

该代理池的**核心优势**在于：

**智能轮换**与筛选功能。它支持按区域、质量自动筛选代理。还有两种更换IP方式：设定时间间隔轮换IP和智能轮换IP两种。前者是设置秒数后到时间后更换，后者是根据关键词判断是否更换ip，无缝衔接，省去手动查找和配置的麻烦。结合其**高质量验证**机制（通过延迟、速度和国际连通性测试），确保每个代理都真实可用，避免因无效IP导致的二次封禁风险。

在检验代理是否可用时可以取消验证防止卡死；全部测试就是将已经在代理列表中的IP进行再次检验；还可以导出可用代理；在设置中设置验证线程数，失败代理清理设置以及自动重测设置。

![]()

这一切都通过直观的**图形化界面**实现，基于ttkbootstrap设计，操作简单直观。动手能力强的朋友可以自己去探索，魔改一下源码。该项目还在持续优化当中，未来可期，觉得好用可以点个赞~

下载地址：https://github.com/11firefly11/fir-proxy

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**易安联零信任**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/311754](/post/id/311754)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻防](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E9%98%B2)

**+1**1赞

收藏

![](https://thirdwx.qlogo.cn/mmopen/vi_32/A3kqgGia9rQIy3l1cFbKHrE3pb8Tv2lpHD4kUKKdThKyRias2oTicNUYzsaslHia7O3zVvykHkGPMF0Iv6QEzsibgog/132)易安联零信任

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t0111cf816530802ac9.png)

[![](https://thirdwx.qlogo.cn/mmopen/vi_32/A3kqgGia9rQIy3l1cFbKHrE3pb8Tv2lpHD4kUKKdThKyRias2oTicNUYzsaslHia7O3zVvykHkGPMF0Iv6QEzsibgog/132)](/member.html?memberId=167464)

[易安联零信任](/member.html?memberId=167464)

专注零信任，指路公号【权说安全】、【江苏易安联】

* 文章
* **37**

* 粉丝
* **1**

### TA的文章

* ##### [小白也能轻松上手！一招解决IP被封杀难题](/post/id/311754)

  2025-12-19 10:13:26
* ##### [安全与效率的平衡术：安全空间](/post/id/312117)

  2025-12-19 10:13:12
* ##### [AI智能体终结运维"狼来了"](/post/id/308218)

  2025-06-09 18:02:34
* ##### [关于OT & IIOT系统远程访问的零信任安全](/post/id/307723)

  2025-05-27 16:27:41
* ##### [易安联完成C1轮融资，加速领跑国内零信任安全市场化](/post/id/307493)

  2025-05-26 16:14:56

### 相关文章

* ##### [安全与效率的平衡术：安全空间](/post/id/312117)

  2025-12-19 10:13:12
* ##### [【原创首发】首个“AI勒索软件”--纽约大学团队“PromptLock”深度剖析](/post/id/312173)

  2025-12-18 10:11:37
* ##### [Win10停服，系统将“裸奔”？金融、交通等关键行业用户该如何有效地做好终端防护](/post/id/312590)

  2025-12-18 10:11:05

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)