---
title: 第二届阿里云RASP挑战赛开启
url: https://www.anquanke.com/post/id/286459
source: 安全客-有思想的安全新媒体
date: 2023-02-17
fetch_date: 2025-10-04T06:49:52.066926
---

# 第二届阿里云RASP挑战赛开启

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

# 第二届阿里云RASP挑战赛开启

阅读量**694925**

发布时间 : 2023-02-16 16:30:12

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

RASP（Runtime Application Self-Protection）技术，通过在应用运行时检测攻击并进行应用保护，为应用提供安全防御。开发无需修改应用代码，只需在实例中安装应用防护探针，即可为应用提供强大的安全防护能力，并抵御绝大部分未知漏洞所使用的攻击手法。在大型攻防演练中，RASP广泛应用于系统的安全防御。
应用防护运行在应用程序内部，通过钩子（Hook）关键函数，实时监测应用在运行时与其他系统的交互过程。当应用出现可疑行为时，RASP会根据当前上下文环境识别并阻断攻击。

![]()

RASP已广泛应用于企业的安全建设中，是阻断入侵行为的一把好手。
为了促进安全对抗技术的发展，阿里云安全于2022年2月开启第一期RASP靶场绕过挑战赛，相关赛事得到了众多专家的支持。如今第二期RASP靶场挑战赛来啦，欢迎大家参与！

**活动时间：**2023年2月16日12:00 ～2月23日12:00
**活动奖励：**报告基础奖励为2000元/个有效报告，根据绕过程度会有浮动，具体见规则
**提交方式：**请在<https://security.alibaba.com/online/detail?type=1&id=148&tab=1> 报名并提交相关的报告，报名无需审核
**活动规则详情：**

## 1.SQL注入

### 1.1 数据库版本

Mysql 8.0.31
Oracle 11g
Psql 12-alpine

mybatis框架，三种数据库的语句均如下，

![]()

### 1.2 得分规则

写入文件到 /usr/local/check 目录下（文件类型不限） -获得80%奖金
读取到数据库flag表中的文件内容 -获得100%奖金
成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生成文件 -获得120%奖金

## 2.XXE

任意目录遍历 50%
读取到服务器上的/flag文件内容 100%

## 3.命令执行

包括log4j、ognl表达式注入、spel表达式注入、el表达式注入
读取到服务器上的/flag文件内容 60%
成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生成文件 100%

## 4.反序列化

包括ois、fastjson两个环境
读取到服务器上的/flag文件内容 60%
成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生产文件 100%

## 5.dependency信息

![]()

![]()

## 6.注意事项

● 报告需至少包含利用成功的Poc、token 信息、成功证明截图三部分信息
● 可将文档内容放到语雀中（<http://www.yuque.com> ）提交到ASRC，语雀文档分享时，请选择【需要密码访问】，也可直接在ASRC的漏洞页面编写详情内容提交。
● 禁止伪造提交，我们会核实相关内容、活动规则较为复杂，请仔细查阅
● 禁止恶意攻击靶场，相关恶意攻击行为会导致奖金被取消、IP被封禁，并可能引起云的业务拉黑关联云账号，请不要进行绕过测试之外的恶意攻击行为

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**阿里云安全**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286459](/post/id/286459)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [活动](/tag/%E6%B4%BB%E5%8A%A8)
* [挑战赛](/tag/%E6%8C%91%E6%88%98%E8%B5%9B)
* [阿里云RASP](/tag/%E9%98%BF%E9%87%8C%E4%BA%91RASP)

**+1**91赞

收藏

![](https://p1.ssl.qhimg.com/t01d437704d9b31097b.png)阿里云安全

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t01d437704d9b31097b.png)](/member.html?memberId=158578)

[阿里云安全](/member.html?memberId=158578)

徜徉云上世界，仰望安全星空。 Welcome on board !

* 文章
* **84**

* 粉丝
* **11**

### TA的文章

* ##### [《2023年度阿里云勒索攻防态势报告》发布](/post/id/292869)

  2024-01-31 16:54:20
* ##### [第三届恶意代码检测挑战赛报名通道开启！等你来战](/post/id/292288)

  2024-01-03 18:25:41
* ##### [阿里云成为Gartner® WAAP市场指南报告云WAAP代表厂商](/post/id/292320)

  2024-01-03 18:11:02
* ##### [回放“阿里云安全2023”](/post/id/292279)

  2023-12-29 16:52:53
* ##### [行业首发！《阿里云产品安全基线白皮书》定义云产品安全标准](/post/id/292086)

  2023-12-22 17:14:30

### 相关文章

* ##### [手慢无！ISC.AI 2025 早鸟票100张限时6折，赠泡泡玛特乐园门票](/post/id/308736)

  2025-06-20 18:22:35
* ##### [聚焦数智孪生下的人才培养！360亮相数字中国建设峰会分享创新实践](/post/id/307226)

  2025-05-08 19:39:58
* ##### [共赴商用密码盛事，开启创新发展新篇--2025第三届商用密码展将于6月11日-13日在上海举办！](/post/id/303497)

  2025-01-14 13:45:35
* ##### [字节跳动技术沙龙第十期：白帽技术专场](/post/id/288942)

  2023-05-30 19:02:56
* ##### [1个漏洞可达2万元，平安银行众测活动千万别错过！](/post/id/287718)

  2023-03-23 17:00:18
* ##### [平安产险最新活动！1.5倍+额外现金奖励，可冲](/post/id/287442)

  2023-03-15 18:00:08
* ##### [从挑战赛看阿里云RASP防御优势与云上最佳实践](/post/id/287383)

  2023-03-14 14:53:27

### 热门推荐

文章目录

* [1.SQL注入](#h2-0)
  + [1.1 数据库版本](#h3-1)
  + [1.2 得分规则](#h3-2)
* [2.XXE](#h2-3)
* [3.命令执行](#h2-4)
* [4.反序列化](#h2-5)
* [5.dependency信息](#h2-6)
* [6.注意事项](#h2-7)

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