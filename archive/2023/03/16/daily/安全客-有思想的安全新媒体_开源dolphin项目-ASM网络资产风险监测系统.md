---
title: 开源dolphin项目-ASM网络资产风险监测系统
url: https://www.anquanke.com/post/id/287246
source: 安全客-有思想的安全新媒体
date: 2023-03-16
fetch_date: 2025-10-04T09:42:09.769968
---

# 开源dolphin项目-ASM网络资产风险监测系统

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

# 开源dolphin项目-ASM网络资产风险监测系统

阅读量**1507188**

|评论**2**

发布时间 : 2023-03-15 16:30:19

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 项目简介

dolphin 是一个的资产风险分析系统,用户仅需将一个主域名添加到系统中,dolphin会自动抓取与该域名相关的信息进行分析;

例如同ICP域名,子域名,对应IP,端口,URL地址,站点截图,端口协议,邮箱地址,泄露信息等.

前端使用了bootstrap框架,控制台使用的ThinkPHP; 底层数据来自于蜻蜓平台的数据聚合系统,调用了各类框架和API.

GitHub地址: <https://github.com/StarCrossPortal/dolphin>

## 使用方法

将公司的主域名填进去,dolphin能采集到`同ICP域名`,`子域名`,`IP`,`端口`,`URL`,`站点截图`,`漏洞`,`产品指纹`,`泄露信息`,`邮箱`,`证书`

## 安装方法

1. 下载代码:`git clone --depth=1 https://github.com/StarCrossPortal/dolphin.git && cd dolphin`
2. 启动docker`docker run -it -d -p 80:80 -v $(pwd):/root/code --name dolphin daxia/qingting:dolphin`
3. 安装依赖`docker exec -it dolphin bash -c 'cd /root/code && composer install'`
4. 新建MySQL数据库,把`xinxishouji.sql`文件导入进去
5. 复制`.example.env`为`.env`,并修改数据库地址信息
6. 浏览器打开地址:`http://xxxx/admin/home/index`

## 感谢

1. 项目UI体验,灵感来自于0xbug大佬的biu系统`https://github.com/0xbug/Biu`
2. 数据由蜻蜓驱动,地址`http://qingting.starcross.cn/scenario/detail?id=2054`

## 效果图

![]()

![]()

![]()

![]()

![]()

![]()

![]()

![]()

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**qingsongboy**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/287246](/post/id/287246)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)

**+1**28赞

收藏

![](https://p0.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)qingsongboy

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhmsg.com/dm/200_200_100/t0165c1e612a26d7a12.jpg)](/member.html?memberId=128405)

[qingsongboy](/member.html?memberId=128405)

这个人太懒了，签名都懒得写一个

* 文章
* **7**

* 粉丝
* **2**

### TA的文章

* ##### [开源dolphin项目-ASM网络资产风险监测系统](/post/id/287246)

  2023-03-15 16:30:19
* ##### [高效率开发Web安全扫描器之路（一）](/post/id/283900)

  2023-01-06 14:00:19
* ##### [GitLab结合fortify实现自动化代码审计实践](/post/id/284200)

  2023-01-05 16:30:23
* ##### [蜻蜓低代码安全工具平台开发之路](/post/id/275235)

  2022-06-27 10:30:50
* ##### [CIS 2021网络安全创新大会《代码安全体系建设》实录](/post/id/270173)

  2022-05-30 15:30:57

### 相关文章

* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据](/post/id/308092)

  2025-06-04 15:31:41
* ##### [新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备](/post/id/307967)

  2025-05-29 14:59:17
* ##### [APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信](/post/id/307963)

  2025-05-29 14:55:27
* ##### [TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件](/post/id/307915)

  2025-05-28 14:05:13

### 热门推荐

文章目录

* [项目简介](#h2-0)
* [使用方法](#h2-1)
* [安装方法](#h2-2)
* [感谢](#h2-3)
* [效果图](#h2-4)

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