---
title: 小皮面板RCE复现
url: https://www.anquanke.com/post/id/286115
source: 安全客-有思想的安全新媒体
date: 2023-02-15
fetch_date: 2025-10-04T06:35:42.333200
---

# 小皮面板RCE复现

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

# 小皮面板RCE复现

阅读量**292871**

发布时间 : 2023-02-14 17:30:38

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

免责声明：文中提到的所有技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途，否则后果自行承担！

## 漏洞成因

小皮面板登录失败时会将失败的用户名记录，并输出到面板首页，而这一过程没有对用户输入的字符做过滤，导致存在任意XSS，攻击者可以利用小皮面板自带的计划任务功能配合XSS实现RCE。

## 环境搭建

小皮官网下载面板，在本地安装。注意是面板，不是phpstudy。安装完成后会自动弹出管理端地址和账号密码的文本。

![]()

## 漏洞测试

先测试一下xss漏洞，用户名输入`<script>alert(1)</script>`，密码任意，验证码输入正确，点击登录。

![]()

然后登录管理员账号，页面弹窗，证明漏洞存在。

![]()

## RCE复现

脚本参考的是ZAC大佬编写的，感谢大佬。

利用XSS调用我们事先准备好的命令执行脚本。这里执行的命令是`echo hkqy > web目录/1.txt`

![]()

登录管理员账号，成功写入文件。

![]()

实际应用可以写webshell，反弹，或者上马等，根据自己喜好。

公众号回复 phpstudy 获取脚本

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**黑客前沿**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286115](/post/id/286115)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [漏洞复现](/tag/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

**+1**1赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)黑客前沿

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=167984)

[黑客前沿](/member.html?memberId=167984)

这个人太懒了，签名都懒得写一个

* 文章
* **5**

* 粉丝
* **1**

### TA的文章

* ##### [CVE-2023-0669 GoAnywhereMFT反序列化漏洞复现](/post/id/286390)

  2023-02-17 15:30:42
* ##### [解决win7嵌入式系统无法DoublePulsar问题](/post/id/285776)

  2023-02-16 17:30:52
* ##### [导出域用户hash姿势总结](/post/id/286257)

  2023-02-15 17:30:43
* ##### [小皮面板RCE复现](/post/id/286115)

  2023-02-14 17:30:38
* ##### [实战记录之曲线救国](/post/id/284600)

  2023-01-11 17:30:42

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51

### 热门推荐

文章目录

* [漏洞成因](#h2-0)
* [环境搭建](#h2-1)
* [漏洞测试](#h2-2)
* [RCE复现](#h2-3)

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