---
title: 【漏洞预警】Samba 12月多个安全漏洞
url: https://www.secpulse.com/archives/194050.html
source: 安全脉搏
date: 2022-12-28
fetch_date: 2025-10-04T02:35:39.729946
---

# 【漏洞预警】Samba 12月多个安全漏洞

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

# 【漏洞预警】Samba 12月多个安全漏洞

[资讯](https://www.secpulse.com/archives/category/news)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-12-27

9,151

1. **通告信息**

近日，安识科技A-Team团队监测到Samba团队发布了多个版本更新，修复了Samba软件中的4个安全漏洞，成功利用这些漏洞可能导致权限提升或执行恶意操作。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

2. **漏洞概述**

##

漏洞名称：Samba 12月多个安全漏洞

简述：Samba是用于Linux和Unix的标准Windows互操作性程序套件，旨在提供安全、稳定和快速的文件和打印服务。

本次Samba更新修复的4个漏洞如下：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| CVE | 标题 | 评分 | 说明 | 影响范围 | 修复版本 |
| CVE-2022-37966 | Windows Kerberos RC4-HMAC 特权提升漏洞 | 8.1 | 可在未经验证的情况下利用RFC 4757（Kerberos加密类型RC4-HMAC-MD5）和MS-PAC（特权属性证书数据结构规范）中的加密协议漏洞，绕过Windows AD环境中的安全功能，成功利用该漏洞可以获得管理员权限。注：微软于2022年11月8日首次披露该漏洞。 | 使用Kerberos的所有Samba版本 | Samba 4.15.13、4.16 .8 、4.17.4 |
| CVE-2022-37967 | Windows Kerberos 特权提升漏洞 | 7.2 | 经过身份验证的用户可以利用Windows Kerberos中的加密协议漏洞，如果其获得对允许委派的服务的控制权，则可以修改Kerberos PAC以提升其权限，成功利用该漏洞可以获得管理员权限。注：微软于2022年11月8日首次披露该漏洞。 | Samba AD DC的所有版本 | Samba 4.15.13、4.16.8 、 4.17.4 |
| CVE-2022-45141 | Samba AD  DC Heimdal编码漏洞 | 8.1 | 使用Heimdal的Samba AD DC可以被强制发行RC4-HMAC加密的Kerberos票证。 | Samba AD DC在Samba 4.16之前的Heimdal构建版本 | Samba 4.15.13 |
| CVE-2022-38023 | Netlogon RPC 特权提升漏洞 | 8.1 | 当使用RPC签名而不是RPC密封时，经过身份验证的用户可以利用Windows Netlogon协议中的加密协议漏洞，可能导致获得服务的控制权，然后修改Netlogon协议流量以提升其权限。注：该漏洞源于NetLogon 安全通道的RC4 模式加密/ HMAC-MD5弱加密。微软于2022年11月8日首次披露该漏洞。 | Samba 的所有版本 | Samba 4.15.13、4.16.8 、 4.17.4 |

3. **漏洞危害**

##

成功利用这些漏洞可能导致权限提升或执行恶意操作。

4. **影响版本**

##

目前受影响的Samba版本：

CVE-2022-37966：使用Kerberos的所有Samba版本

CVE-2022-37967：Samba AD DC的所有版本

CVE-2022-45141：Samba AD DC在Samba 4.16之前的Heimdal构建版本

CVE-2022-38023：Samba 的所有版本

5. **解决方案**

##

微软已在2022年11月发布了这些漏洞的安全更新，受影响用户可及时安装补丁；Samba团队已经修复了这些漏洞，相关用户可升级到Samba 版本4.17.4、4.16.8 或 4.15.13。

下载链接：

https://www.samba.org/samba/history/security.html

6. **时间轴**

##

【-】2022年12月24日 安识科技A-Team团队监测到漏洞公布信息

【-】2022年12月25日 安识科技A-Team团队根据漏洞信息分析

【-】2022年12月26日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194050.html**](https://www.secpulse.com/archives/194050.html)

Tags: [CVE-2022-37966](https://www.secpulse.com/archives/tag/cve-2022-37966)、[CVE-2022-37967](https://www.secpulse.com/archives/tag/cve-2022-37967)、[CVE-2022-38023](https://www.secpulse.com/archives/tag/cve-2022-38023)、[CVE-2022-45141](https://www.secpulse.com/archives/tag/cve-2022-45141)、[Samba](https://www.secpulse.com/archives/tag/samba)

点赞：
7
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![SambaCry 野外利用分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2017/06/SambaCry_small-300x160.jpg)](https://www.secpulse.com/archives/58701.html "详细阅读 SambaCry 野外利用分析")
* [![运维工程师必须掌握的基础技能有哪些？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2015/03/linux1.png)

  运维工程师必须掌握的基础技能有哪些？](https://www.secpulse.com/archives/5287.html "详细阅读 运维工程师必须掌握的基础技能有哪些？")
* [![Samba全系版本远程命令执行漏洞(CVE-2015-0240)检测方法及修复建议](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2015/02/0ea5476add2554a6f75c54385353051a.png)

  Samba全系版本远程命令执行漏洞(CV…](https://www.secpulse.com/archives/4900.html "详细阅读 Samba全系版本远程命令执行漏洞(CVE-2015-0240)检测方法及修复建议")

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

![安全问答社区](https://www.secpulse.com/wp-content/the...