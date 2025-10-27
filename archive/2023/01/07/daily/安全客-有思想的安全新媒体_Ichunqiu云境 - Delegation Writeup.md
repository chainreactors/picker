---
title: Ichunqiu云境 - Delegation Writeup
url: https://www.anquanke.com/post/id/284201
source: 安全客-有思想的安全新媒体
date: 2023-01-07
fetch_date: 2025-10-04T03:14:41.264435
---

# Ichunqiu云境 - Delegation Writeup

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

# Ichunqiu云境 - Delegation Writeup

阅读量**724505**

发布时间 : 2023-01-06 10:30:50

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 0x1 Info

![]()

## 0x2 Recon

1. Target external IP
   `39.98.34.149`
2. Nmap results
   ![]()
3. 关注80端口的http服务，目录爆破（省略）找到 /admin
   ![]()
4. 使用弱口令登录进入后台，去到模板页面，编辑header.html，添加php一句话

   ```
    用户名: admin, 密码：123456
   ```

   ![]()
5. 命令执行
   ![]()

## 0x03 入口点：172.22.4.36

1. 弹shell
   ![]()
   快速过一下：
   * 入口机器没特别的东西
   * 没能提权到root权限（也不需要提权到root权限）
   * stapbpf suid利用失败
     找到diff suid
     ![]()
2. flag01
   `diff --line-format=%L /dev/null /home/flag/flag01.txt`
   ![]()
3. flag01 里面有提示用户名
   `WIN19\Adrian`
4. 挂代理扫 445
   ![]()
   获取到三个机器信息172.22.4.19 fileserver.xiaorang.lab
   172.22.4.7 DC01.xiaorang.lab
   172.22.4.45 win19.xiaorang.lab
5. 用 Flag01提示的用户名 + rockyou.txt 爆破，爆破出有效凭据 (提示密码过期)
   `win19\Adrian babygirl1`
6. xfreerdp 远程登录上 win19 然后改密码
   ![]()
   ![]()

## 0x04 Pwing WIN19 – 172.22.4.45

前言：当前机器除了机器账户外，完全没域凭据，需要提权到system获取机器账户

1. 桌面有提示
   ![]()
2. 关注这一栏，当前用户Adrian对该注册表有完全控制权限
   ![]()
   ![]()
3. 提权
   msfvenom生成服务马，执行 sam.bat
   ![]()
   sam.bat
   ![]()
   修改注册表并且启用服务，然后桌面就会获取到 sam，security，system
   ![]()
4. 获取 Administrator + 机器账户 凭据Administrator:500:aad3b435b51404eeaad3b435b51404ee:ba21c629d9fd56aff10c3e826323e6ab:::
   $MACHINE.ACC: aad3b435b51404eeaad3b435b51404ee:917234367460f3f2817aa4439f97e636
   ![]()
5. flag02
   ![]()
6. 使用机器账户收集域信息
   ![]()

## 0x05 DC takeover – 172.22.4.7

1. 分析 Bloodhound，发现 WIN19 + DC01都是非约束委派
   ![]()
2. 使用Administrator登录进入 WIN19，部署rubeus
   ![]()
3. 使用DFSCoerce强制触发回连到win19并且获取到DC01的TGT
   ![]()
   ![]()
4. Base64的tgt 解码存为 DC01.kirbi
   ![]()
5. DCSync 获取域管凭据
   ![[![]()]]
6. psexec – flag04
   ![]()

## 0x06 Fileserver takeover – 172.22.4.19

1. psexec – flag03
   ![]()

## 0x07 Outro

* 感谢Alphabug师傅的提示（0x03 – 0x04），大哥已经把入口点都打完了，我只是跟着进来而已
* 感谢九世师傅的合作
* Spoofing已经打完了，walkthrough也写完了，等1000奖励到手后新年释出，个人感觉Spoofing更好玩，出题的思路很妙

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**Gcow安全团队**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284201](/post/id/284201)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [CTF](/tag/CTF)

**+1**4赞

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
* ##### [Ichunqiu云境 —— Exchange Writeup](/post/id/286967)

  2023-03-03 14:30:36
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

* [0x1 Info](#h2-0)
* [0x2 Recon](#h2-1)
* [0x03 入口点：172.22.4.36](#h2-2)
* [0x04 Pwing WIN19 - 172.22.4.45](#h2-3)
* [0x05 DC takeover - 172.22.4.7](#h2-4)
* [0x06 Fileserver takeover - 172.22.4.19](#h2-5)
* [0x07 Outro](#h2-6)

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