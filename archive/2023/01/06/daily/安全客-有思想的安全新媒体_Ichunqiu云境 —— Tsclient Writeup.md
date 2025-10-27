---
title: Ichunqiu云境 —— Tsclient Writeup
url: https://www.anquanke.com/post/id/284260
source: 安全客-有思想的安全新媒体
date: 2023-01-06
fetch_date: 2025-10-04T03:08:35.758945
---

# Ichunqiu云境 —— Tsclient Writeup

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

# Ichunqiu云境 —— Tsclient Writeup

阅读量**744701**

发布时间 : 2023-01-05 10:30:31

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0x1 Info

Tag:
MSSQL，Privilege Escalation，Kerberos，域渗透，RDP

![]()

靶场地址：<https://yunjing.ichunqiu.com/ranking/summary?id=BzMFNFpvUDU> 从web到内网再到域的靶场环境都全，且出题的思路很好，感兴趣的可以去玩玩

## 0x2 Recon

1. Target external ip
   `47.92.82.196`
2. nmap
   ![]()
3. MSSQL 弱口令爆破，爆破出有效凭据，权限为服务账户权限（MSSQLSERVER）
   `sa:1qaz!QAZ`
   ![]()

## 0x3 入口点 MSSQL – 172.22.8.18

* 前言，该机器不在域内

1. 直接MSSQL shell（这里做完了忘记截图了..）
   ![]()
2. 提权，这里直接获取Clsid暴力怼potato（前面几个clsid是用不了的）
   修改GetClsid.ps1，添加执行potato
   ![]()
   Potato和GetClsid.ps1
   ![]()
   执行GetClsid.ps1
   ![]()
   获取到有效clsid以及命令执行结果
   ![]()
3. 导出SAM，SYSTEM，Security
   ![]()
   解出凭据，用administrator + psexec 139横向（外网没有开445）就能获取到 flag01
   `administrator 2caf35bb4c5059a3d50599844e2b9b1f`
   ![]()
4. qwinsta和端口连接看到有机器rdp过来
   ![]()
   ![]()

1. 这边使用administrator psexec后上msf（system权限），使用incognito模块，模拟至john（本人实测，只有msf的incognito能完成后续操作，f-secure lab等其他的模拟令牌工具没成功）
   ![]()
2. 使用john的token执行 net use 看到 \\tsclient\C 共享
   ![]()
3. 直接获取 \\tsclient\C 下面的 credential.txt，同时提示 hijack image (镜像劫持)
   `xiaorang.lab\Aldrich:Ald[@rLMWuy7Z](https://github.com/rLMWuy7Z "@rLMWuy7Z")!#`
   ![]()

* 快进，略过搭建代理过程

1. CME 扫描 172.22.8.0/24，有三个机器提示密码过期了
   ![]()
2. 测试一下 DC01 88端口是否开启（测是否域控），DC01为域控
   ![]()
3. smbpasswd.py 远程修改一下过期密码，改成111qqq…
   ![]()
4. ldapshell.py 验证，登录域成功
   ![]()
5. CME 枚举 RDP，显示能登录进入 172.22.8.46（用CME官方的RDP模块不会扫出有效RDP凭据，这边自己写了一个基于xfreerdp的CME模块）
   [XiaoliChan/CrackMapExec-Extension](https://github.com/XiaoliChan/CrackMapExec-Extension)
   ![]()

## 0x4 域渗透 – 入口 – 172.22.8.46

1. 登录进入，查看到 xiaorang.lab\Aldrich 不是这台机器的管理员，只是普通用户
   ![]()

* 提权，两种方法
  Priv-ESC1：镜像劫持提权（常规）
  Get-ACL查看到任何用户都可以对注册表 “HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\” 进行写入，创建操作
  ![]()
  创建一个劫持magnify.exe（放大镜）的注册表，执行CMD.exe
  ![]()
  锁定用户
  ![]()
  点击放大镜
  ![]()
  提权至system
  ![]()
  Priv-ESC2：krbrelayup提权
  域普通权限用户在域内机器，直接带走（非常规，推荐）
  ![]()
  ![]()

1. 快进mimikatz，获取到当前机器的机器账户 win2016$

   ```
   xiaorang.lab\WIN2016$ 4ba974f170ab0fe1a8a1eb0ed8f6fe1a
   ```

## 0x5 域渗透 – DC Takeover

* 两种方法

1. 观察 WIN2016$ 的组关系，发现处于 Domain Admins 组，直接使用 Dcsync 带走 DC01 （过程略）
   ![]()
2. 约束委派（非常规）
   Bloodhound收集域信息，分析，发现存在约束委派
   ![]()
   使用 getST.py 进行约束委派攻击
   ![]()
   带走 DC01![]()

## 0x6 Outro

* 个人比较手残，不懂C，incognito那个部分，按照作者解释来说，常规是要自己写一个impersonate token的工具（还是没脱离MSF.. TAT）

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Gcow安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284260](/post/id/284260)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [CTF](/tag/CTF)

**+1**5赞

收藏

![](https://p3.ssl.qhimg.com/t0143ca032175423a1f.png)Gcow安全团队

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

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
* ##### [Ichunqiu云境 —— Exchange Writeup](/post/id/286967)

  2023-03-03 14:30:36
* ##### [Ichunqiu云境 - Delegation Writeup](/post/id/284201)

  2023-01-06 10:30:50
* ##### [活动 | 长亭科技2023第五届 Real World CTF 战火已燃，等你来战！](/post/id/284307)

  2022-12-21 17:00:34
* ##### [从一道题入门 UEFI PWN](/post/id/283073)

  2022-11-11 15:30:05
* ##### [2022年工业信息安全技能大赛“望岳杯”锦标赛 wp](/post/id/282335)

  2022-10-31 15:30:36

### 热门推荐

文章目录

* [0x1 Info](#h2-0)
* [0x2 Recon](#h2-1)
* [0x3 入口点 MSSQL - 172.22.8.18](#h2-2)
* [0x4 域渗透 - 入口 - 172.22.8.46](#h2-3)
* [0x5 域渗透 - DC Takeover](#h2-4)
* [0x6 Outro](#h2-5)

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