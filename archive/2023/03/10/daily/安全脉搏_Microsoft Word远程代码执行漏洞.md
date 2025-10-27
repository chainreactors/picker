---
title: Microsoft Word远程代码执行漏洞
url: https://www.secpulse.com/archives/197273.html
source: 安全脉搏
date: 2023-03-10
fetch_date: 2025-10-04T09:06:08.591599
---

# Microsoft Word远程代码执行漏洞

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

# Microsoft Word远程代码执行漏洞

[资讯](https://www.secpulse.com/archives/category/news)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-09

10,211

##

1. **通告信息**

近日，安识科技A-Team团队监测到一则 Microsoft Word 组件存在远程代码执行漏洞的信息，漏洞编号：CVE-2023-21716，漏洞威胁等级：高危。

该漏洞是由于 Word 组件中的RTF解析器在解析字体表的时候存在堆损坏漏洞。攻击者可以通过社会工程说服受害者打开精心制作的恶意文件来触发此漏洞，在成功利用的情况下可能造成远程代码执行。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

2. **漏洞概述**

CVE：CVE-2023-21716

简述：Microsoft Word 是包含在 Microsoft Office 中的文字处理应用程序。在默认配置下，Microsoft Word 可以处理富文本格式（RTF）文件。RTF 文件主要由基于 ASCII 的关键词组成，这些关键词可以囊括各种各样的丰富内容。该漏洞是由于 Word 组件中的RTF解析器在解析字体表的时候存在堆损坏漏洞。攻击者可以通过社会工程说服受害者打开精心制作的恶意文件来触发此漏洞，在成功利用的情况下可能造成远程代码执行。

##

3. **漏洞危害**

攻击者可以通过社会工程说服受害者打开精心制作的恶意文件来触发此漏洞，在成功利用的情况下可能造成远程代码执行。

##

4. **影响版本**

目前受影响的Office版本：

SharePoint Server Subscription Edition Language Pack

Microsoft Word 2016 (64-bit edition)

Microsoft Word 2016 (32-bit edition)

Microsoft Word 2013 Service Pack 1 (64-bit editions)

Microsoft Word 2013 Service Pack 1 (32-bit editions)

Microsoft Word 2013 RT Service Pack 1

Microsoft SharePoint Server Subscription Edition

Microsoft SharePoint Server 2019

Microsoft SharePoint Foundation 2013 Service Pack 1

Microsoft SharePoint Enterprise Server 2016

Microsoft SharePoint Enterprise Server 2013 Service Pack 1

Microsoft Office Web Apps Server 2013 Service Pack 1

Microsoft Office Online Server

Microsoft Office LTSC for Mac 2021

Microsoft Office LTSC 2021 for 64-bit editions

Microsoft Office LTSC 2021 for 32-bit editions

Microsoft Office 2019 for Mac

Microsoft Office 2019 for 64-bit editions

Microsoft Office 2019 for 32-bit editions

Microsoft 365 Apps for Enterprise for 64-bit Systems

Microsoft 365 Apps for Enterprise for 32-bit Systems

##

5. **解决方案**

当前官方已发布最新版本，建议受影响的用户及时更新升级到最新版本。链接如下： https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21716

##

6. **时间轴**

【-】2023年02月15日 安识科技A-Team团队监测到微软官方发布安全补丁

【-】2023年02月15日 安识科技A-Team团队发布微软补丁公告

【-】2023年03月09日 安识科技A-Team团队发布漏洞通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197273.html**](https://www.secpulse.com/archives/197273.html)

Tags: [CVE-2023-21716](https://www.secpulse.com/archives/tag/cve-2023-21716)、[Microsoft Word](https://www.secpulse.com/archives/tag/microsoft-word)、[远程代码执行漏洞](https://www.secpulse.com/archives/tag/%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![某应用虚拟化系统远程代码执行](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199708-1682584786-300x200.png)](https://www.secpulse.com/archives/199708.html "详细阅读 某应用虚拟化系统远程代码执行")
* [![【漏洞预警】Apache Hadoop YARN远程代码执行漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/1661741820-300x213.png)

  【漏洞预警】Apache Hadoop …](https://www.secpulse.com/archives/186403.html "详细阅读 【漏洞预警】Apache Hadoop YARN远程代码执行漏洞")
* [![【漏洞预警】Mitel MiVoice Connect远程代码执行漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/07/1657177841900-300x168.png)

  【漏洞预警】Mitel MiVoice …](https://www.secpulse.com/archives/182735.html "详细阅读 【漏洞预警】Mitel MiVoice Connect远程代码执行漏洞")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2017/12/logo11.png)](https://www.secpulse.com/newpage/author?author_id=3871aaa) | [安识科技 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=3871) | |
| 文章数：190 | 积分： 135 |
| 安识科技：专业的企业安全解决方案提供商。官网：https://www.duoyinsu.com/ | |

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

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KCTF 春季赛](https://ctf.pediy.com)

#### 2020-01-09

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpu...