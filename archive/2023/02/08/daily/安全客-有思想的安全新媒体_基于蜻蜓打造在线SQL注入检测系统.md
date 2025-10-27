---
title: 基于蜻蜓打造在线SQL注入检测系统
url: https://www.anquanke.com/post/id/286061
source: 安全客-有思想的安全新媒体
date: 2023-02-08
fetch_date: 2025-10-04T05:55:28.319672
---

# 基于蜻蜓打造在线SQL注入检测系统

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

# 基于蜻蜓打造在线SQL注入检测系统

阅读量**1114551**

发布时间 : 2023-02-07 12:00:32

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 背景

一般情况下我们都是使用命令行方式去调用SQLMap，但在一些场景下用界面操作SQLMap更方便,还可以保留检测结果，在一些开源项目中也发现了SQLMAP-Web-GUI，不过我觉得还是不太方便，比如部署必须要有一台公网服务器才能24小时提供服务，这往往需要买云服务器，而用云服务器进行检测容易被服务商封锁。

我不想买公网服务器,又需要有一个24小时能为我提供服务的平台，还不想被封公网IP；于是自己造了一个轮子把sqlmap安装在蜻蜓平台中，这样我不需要关注购买公网IP服务器问题,而且需要用的时候直接打开蜻蜓页面操作即可。

## 克隆SQLMap应用

写好的应用我共享到了蜻蜓市场中，如果要使用可以直接去市场应用里克隆即可，下面是我的使用方法，主要是手工界面操作和调用API操作。

![]()

## 手工界面检测

从市场克隆应用之后，会出现在工作台界面，运行之前需要填写要检测的URL地址，这里找一个靶场从里面找一个有参数的URL地址放进去。

![]()

> 注意:一定要有参数,没有参数意味着不存在注入点，SQLMap肯定是检测不出结果的。

点击运行按钮，就会开始对URL进行检测，检测时间会根据网络质量和漏洞类型等因素出结果时间也不同。需要耐心等待一下。

![]()

在运行历史记录里面状态为已完成的时候，可以点击结果按钮，查看这次检测的结果，会跳转到数据中心来。

![]()

如果想看详情，可以点击查看按钮可以看到数据的详细信息。

![]()

## 调用API检测

有些场景下，你可能想把这个功能集成到你自己的项目中，蜻蜓里面内置了API接口，你可以直接通过接口运行工作流。

### **启动工作流**

启动工作流你可以通过CURL的方式来运行，如果工作流里需要填写参数，可以通过–from的方式来提交参数。

curl –request POST \

–url ‘http://qingting.starcross.cn/api/index/start?usce\_id=2945’ \

–header ‘content-type: multipart/form-data’ \

–header ‘token: 78b2e04f519b4axxx202fe457cb’ \

–form ‘scan\_url=http://10.1.1.140:6789/home/index.php?m=tiezi&a=index&bk=7’

调用成功，会返回版本号信息。

{

“code”: 0,

“msg”: “启动成功”,

“data”: {“task\_version”:”1672798589″}

}

### **获取执行状态**

获取任务执行状态的命令，参数中需要有工作流ID和执行版本号。

curl –request GET \

–url ‘http://qingting.starcross.cn/api/index/getStatus?task\_version=1672798589&flow\_id=2945’ \

–header ‘token: 78b2e04f519b4axxx202fe457cb’

获取执行状态的返回信息，1代表执行中。

{

“code”: 0,

“msg”: “执行中”,

“data”: 1

}

### **获取执行结果**

请求获取结果的CURL命令如下所示。

curl –request GET \

–url ‘http://qingting.starcross.cn/api/index/getResult?flow\_id=2945’ \

–header ‘token: 78b2e04f519b4axxx202fe457cb’

获得SQLMap执行的结果。

{

“code”: 0,

“msg”: “”,

“data”: [

{

“raw”: “sqlmap identified the following injection point(s) with a total of 205 HTTP(s) requests:\n—\nParameter: bk (GET)\n Type: time-based blind\n Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)\n Payload: m=tiezi&a=index&bk=7 AND (SELECT 2330 FROM (SELECT(SLEEP(5)))klfn)\n—\nweb server operating system: Linux Ubuntu\nweb application technology: PHP, Nginx 1.14.0\nback-end DBMS: MySQL >= 5.0.12\n”

},

{

“raw”: “sqlmap identified the following injection point(s) with a total of 205 HTTP(s) requests:\n—\nParameter: bk (GET)\n Type: time-based blind\n Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)\n Payload: m=tiezi&a=index&bk=7 AND (SELECT 2671 FROM (SELECT(SLEEP(5)))kzvf)\n—\nweb server operating system: Linux Ubuntu\nweb application technology: PHP, Nginx 1.14.0\nback-end DBMS: MySQL >= 5.0.12\n”

}

]

}

**GitHub地址：**https://github.com/StarCrossPortal/QingTing

**官网地址：**http://qingting.starcross.cn/

**微信交流群：**

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286061](/post/id/286061)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全工具](/tag/%E5%AE%89%E5%85%A8%E5%B7%A5%E5%85%B7)
* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [api安全](/tag/api%E5%AE%89%E5%85%A8)

**+1**22赞

收藏

![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)星阑科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t010136e53e1b35516c.png)

[![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)](/member.html?memberId=147620)

[星阑科技](/member.html?memberId=147620)

星阑科技

* 文章
* **119**

* 粉丝
* **46**

### TA的文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [解密与探究：理解WebSocket协议与报文格式](/post/id/290500)

  2023-08-30 14:36:15
* ##### [创新护航：萤火助力守护数据跨境安全](/post/id/290512)

  2023-08-29 16:10:15

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

* [背景](#h2-0)
* [克隆SQLMap应用](#h2-1)
* [手工界面检测](#h2-2)
* [调用API检测](#h2-3)
  + [启动工作流](#h3-4)
  + [获取执行状态](#h3-5)
  + [获取执行结果](#h3-6)

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