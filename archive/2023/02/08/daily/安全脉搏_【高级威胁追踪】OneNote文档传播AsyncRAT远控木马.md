---
title: 【高级威胁追踪】OneNote文档传播AsyncRAT远控木马
url: https://www.secpulse.com/archives/195468.html
source: 安全脉搏
date: 2023-02-08
fetch_date: 2025-10-04T05:56:30.522547
---

# 【高级威胁追踪】OneNote文档传播AsyncRAT远控木马

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【高级威胁追踪】OneNote文档传播AsyncRAT远控木马

[资讯](https://www.secpulse.com/archives/category/news)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-07

10,347

**前言**

**从2022年12月到2023年1月31日，攻击者使用 OneNote 附带文件的邮件攻击活动数量显着增加，传播的相关恶意软件有Redline、AgentTesla、Quasar RAT、AsyncRAT、XWorm、Netwire、DOUBLEBACK和Qbot等**。

OneNote是Microsoft创建的数字笔记本，可通过Microsoft 365产品套件获得，攻击者使用OneNote主要是为了绕过威胁检测，自从Microsoft在2022年后开始默认阻止宏之后，攻击者已经尝试使用多个新的策略、技术和程序(TTP)，包括使用以前不常观察到的文件类型，例如虚拟硬盘(VHD)、编译的HTML(CHM)等，使用OneNote算是攻击者使用的一种新的TTP攻击技术，可以预测使用OneNote文件的恶意攻击活动在2023年会越来越流行，同时黑客组织也会不断研究新的TTP技术进行攻击，黑客组织与安全研究人员的安全对抗一直在升级，深信服高级威胁团队通过外部渠道捕获到相关的样本，并对其中的一个案例进行了深入的分析。

**分析**

**1.从外部渠道捕获到的攻击样本，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755074.png)

**2.邮件中使用了一个附带 OneNote 文档，下载OneNote文档之后，使用解析工具对 OneNote 文档进行解包之后，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755075.png)

OneNote文档格式，可以参考链接：

https://learn.microsoft.com/en-us/openspecs/office\_file\_formats/ms-onestore/405b958b-4cb7-4bac-81cc-ce0184249670

解析脚本，可以参考链接：

https://blog.didierstevens.com/2023/01/22/analyzing-malicious-onenote-documents/

**3.OneNoteAttachments 文件夹下存在一个混淆的 update.bat 恶意脚本，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-16757550751.png)

**4.对里面的代码去混淆之后，得到一段代码，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755079.png)

**5.该代码会对 update.bat 脚本中的部分数据进行Base64+AES 解密并加载执行，解密后的数据为一个 PE恶意，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755081.png)

**6.对解密后的数据进行动态分析，会再次解密出里面的 payload 代码并调用执行，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755082.png)

**7.分析解密后的 payload 代码，发现是 AsyncRAT 远控木马，如下所示：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195468-1675755085.png)

黑客远程服务器地址为：95.216.102.32

**IOCs**

**HASH**

E78B26D7034394FD775493CFA552E3A3

000AA2353C74B13057A73ACBA92FADEC

**IP**

95.216.102.32

**总结**

深信服高级威胁团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对APT组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个APT以及网络犯罪威胁组织的详细画像，并成功帮助客户应急响应处置过多个APT及网络犯罪威胁组织攻击事件，未来逐着安全对抗的不断升级，黑客组织会研究和使用更多新型的TTP，**深信服高级威胁团队会持续监控，并对全球发现的新型安全事件进行深入分析与研****究。**

参考链接：

https://www.proofpoint.com/us/blog/threat-insight/onenote-documents-increasingly-used-to-deliver-malware

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195468.html**](https://www.secpulse.com/archives/195468.html)

Tags: [AgentTesla](https://www.secpulse.com/archives/tag/agenttesla)、[AsyncRAT](https://www.secpulse.com/archives/tag/asyncrat)、[AsyncRAT远控木马](https://www.secpulse.com/archives/tag/asyncrat%E8%BF%9C%E6%8E%A7%E6%9C%A8%E9%A9%AC)、[DOUBLEBACK](https://www.secpulse.com/archives/tag/doubleback)、[NetWire](https://www.secpulse.com/archives/tag/netwire)、[onenote](https://www.secpulse.com/archives/tag/onenote)、[QBot](https://www.secpulse.com/archives/tag/qbot)、[Quasar RAT](https://www.secpulse.com/archives/tag/quasar-rat)、[RedLine](https://www.secpulse.com/archives/tag/redline)、[XWorm](https://www.secpulse.com/archives/tag/xworm)、[远控木马](https://www.secpulse.com/archives/tag/%E8%BF%9C%E6%8E%A7%E6%9C%A8%E9%A9%AC)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【恶意文件】沉寂之后，Emotet木马再次来袭](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1681724018362-300x186.png)

  【恶意文件】沉寂之后，Emotet木马再…](https://www.secpulse.com/archives/199128.html "详细阅读 【恶意文件】沉寂之后，Emotet木马再次来袭")
* [![【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678350974041-300x185.png)

  【恶意文件】AgentTesla 贼心不…](https://www.secpulse.com/archives/197248.html "详细阅读 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来")
* [![通过视频网站传播的RedLine窃密木马跟进分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1668581456255-300x190.png)

  通过视频网站传播的RedLine窃密木马…](https://www.secpulse.com/archives/191105.html "详细阅读 通过视频网站传播的RedLine窃密木马跟进分析")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=9241aaa) | [Further\_eye ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=9241) | |
| 文章数：319 | 积分： 2105 |
| 深信服科技旗下安全实验室，致力于网络安全攻防技术的研究和积累，深度洞察未知网络安全威胁，解读前沿安全技术。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会]...