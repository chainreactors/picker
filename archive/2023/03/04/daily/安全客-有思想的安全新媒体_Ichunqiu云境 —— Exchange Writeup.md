---
title: Ichunqiu云境 —— Exchange Writeup
url: https://www.anquanke.com/post/id/286967
source: 安全客-有思想的安全新媒体
date: 2023-03-04
fetch_date: 2025-10-04T08:35:55.636216
---

# Ichunqiu云境 —— Exchange Writeup

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

# Ichunqiu云境 —— Exchange Writeup

阅读量**653570**

发布时间 : 2023-03-03 14:30:36

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Author:小离-xiaoli

## 0x00 Intro

1. OSCP 渗透风格，脱离C2和MSF之类的工具
2. Box 难度不高

## 0x01 Info

* Tag: JDBC, Exchange, NTLM, Coerce Authentication, DCSync
  ![]()

## 0x02 Recon

1. Target external IP
   `39.98.179.149`
2. Nmap results
   ![]()
3. 直接关注8000端口，前面我已经怼过80了，没东西直接过
   ![]()
4. 华夏ERP，有很多漏洞的，入口点卡了很久，后面看到JDBC，直接谷歌一搜就搜到大哥的文章了
   Fastjson高版本的奇技淫巧 – Bmth (bmth666.cn)(<http://www.bmth666.cn/bmth_blog/2022/10/19/Fastjson%E9%AB%98%E7%89%88%E6%9C%AC%E7%9A%84%E5%A5%87%E6%8A%80%E6%B7%AB%E5%B7%A7/#%E8%93%9D%E5%B8%BD%E6%9D%AF2022%E5%86%B3%E8%B5%9B-%E8%B5%8C%E6%80%AA>)
5. 构造payload
   ![]()
6. Configure MySQL\_Fake\_Server
   ![]()
7. 未授权 + MySQL Connector JDBC反序列化组合拳直接RCE
   ![]()
8. RCE后直接获取 Flag01
   ![]()

## 0x03 入口点：172.22.3.12

1. SMB扫描内网主机，看到Exchange关键字 (EXC01)，尝试访问
   ![]()
2. 172.22.3.9 为 Exchange
   ![]()
3. Proxylogon 直接打死，获取system权限
   ![]()
   ![]()
4. flag02（后续凭据收集略过）
   ![]()

## 0x04 入口点：172.22.3.9

* 快进1：已经收集到了exchange机器账户的hash
* 快进2：同时收集到了一个域账户凭据：Zhangtong

1. 这边已经通过上面的操作收集到了exchange的机器账户hash，exchang的机器账户在域内对整个domain-object有writedacl权限，那我们直接使用dacledit.py给Zhangtong加dcsync权限（其实你也可以给自己加上dcsync）
   ![]()
2. Dcsync，获取到域管和用户lumia的hashes
   ![]()
3. 进入 172.22.3.2 获取flag04
   ![]()

## 0x05 Final：172.22.3.26

1. 172.22.3.26上面的Lumia用户文件夹里面有个secret.zip
   ![]()
2. 直接PTH Exchange导出Lumia mailbox里面的全部邮件以及附件
   ![]()
3. item-0.eml，提示密码是手机号
   ![]()
4. 刚好导出的附件里面有一个csv，里面全是手机号
   ![]()
5. 常规操作，转换成pkzip格式的hash再跑字典，跑出密码
   ![]()
   ![]()
   ![]()
6. flag03
   ![]()
   ![]()

## 0x06 Outro

1. Exchange 后渗透那，作者本意是想让我们用 NTLM Relay去完成DCSync提权，获取Exchange SYSTEM权限后，触发webdav回连中继到ldap，这里的话就不尝试了，有兴趣的话可以看我上一篇文章 Spoofing
2. Lumia用户登录exchange那，作者也是想让你改掉Lumia用户的密码，但是我就懒了，直接PTH

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Gcow安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286967](/post/id/286967)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [CTF](/tag/CTF)

**+1**1赞

收藏

![](https://p3.ssl.qhimg.com/t0143ca032175423a1f.png)Gcow安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p3.ssl.qhimg.com/t0143ca032175423a1f.png)](/member.html?memberId=146916)

[Gcow安全团队](/member.html?memberId=146916)

致力于APT抓捕分析，渗透测试，红蓝对抗，RedTeam，病毒样本分析

* 文章
* **27**

* 粉丝
* **22**

### TA的文章

* ##### [Ichunqiu云境 —— Exchange Writeup](/post/id/286967)

  2023-03-03 14:30:36
* ##### [赏金猎人：IChunQiu云境-Spoofing Writeup](/post/id/285771)

  2023-02-01 16:00:41
* ##### [Ichunqiu云境 - Delegation Writeup](/post/id/284201)

  2023-01-06 10:30:50
* ##### [Ichunqiu云境 —— Tsclient Writeup](/post/id/284260)

  2023-01-05 10:30:31
* ##### [某内网域渗透靶场的writeup](/post/id/259602)

  2021-11-18 12:00:11

### 相关文章

* ##### [2024字节跳动“安全范儿”高校挑战赛报名开启！CTF、AI、HACK三大赛道等你来战！](/post/id/299640)

  2024-08-30 14:39:48
* ##### [培养云上安全人才 | 阿里云2023首届CTF大赛重磅启动](/post/id/288353)

  2023-04-24 19:17:46
* ##### [Ichunqiu云境 - Delegation Writeup](/post/id/284201)

  2023-01-06 10:30:50
* ##### [Ichunqiu云境 —— Tsclient Writeup](/post/id/284260)

  2023-01-05 10:30:31
* ##### [活动 | 长亭科技2023第五届 Real World CTF 战火已燃，等你来战！](/post/id/284307)

  2022-12-21 17:00:34
* ##### [从一道题入门 UEFI PWN](/post/id/283073)

  2022-11-11 15:30:05
* ##### [2022年工业信息安全技能大赛“望岳杯”锦标赛 wp](/post/id/282335)

  2022-10-31 15:30:36

### 热门推荐

文章目录

* [0x00 Intro](#h2-0)
* [0x01 Info](#h2-1)
* [0x02 Recon](#h2-2)
* [0x03 入口点：172.22.3.12](#h2-3)
* [0x04 入口点：172.22.3.9](#h2-4)
* [0x05 Final：172.22.3.26](#h2-5)
* [0x06 Outro](#h2-6)

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