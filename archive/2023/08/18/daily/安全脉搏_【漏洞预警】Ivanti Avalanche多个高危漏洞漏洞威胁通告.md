---
title: 【漏洞预警】Ivanti Avalanche多个高危漏洞漏洞威胁通告
url: https://www.secpulse.com/archives/203055.html
source: 安全脉搏
date: 2023-08-18
fetch_date: 2025-10-04T11:58:55.820390
---

# 【漏洞预警】Ivanti Avalanche多个高危漏洞漏洞威胁通告

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

# 【漏洞预警】Ivanti Avalanche多个高危漏洞漏洞威胁通告

[资讯](https://www.secpulse.com/archives/category/news)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-08-17

18,953

##

1. **通告信息**

近日，安识科技A-Team团队监测到Ivanti Avalanche中修复了多个安全漏洞，这些漏洞可能导致身份验证绕过、文件上传、目录遍历和远程代码执行等。

对此，安识科技建议广大用户及时升级到安全版本,并做好资产自查以及预防工作，以免遭受黑客攻击。

##

2. **漏洞概述**

CVE-2023-32560：Ivanti Avalanche基于堆栈的缓冲区溢出（高危）

该漏洞存在于Ivanti Avalanche WLAvalancheService.exe中，未经身份验证的远程威胁者可通过向TCP 端口 1777发送特制消息，可能导致在目标系统上执行任意代码或造成服务中断，该漏洞的细节已公开。

CVE-2023-32561：Ivanti Avalanche身份验证绕过漏洞（高危）

该漏洞存在于Ivanti Avalanche dumpHeap方法中，由于权限分配不正确，远程威胁者可利用该漏洞绕过系统上的身份验证。

CVE-2023-32562：Ivanti Avalanche文件上传漏洞（高危）

该漏洞存在于Ivanti Avalanche FileStoreConfig端点中，由于对用户提供的数据缺乏适当验证，经过身份验证的威胁者可利用该漏洞上传任意文件，导致远程代码执行。

CVE-2023-32563：Ivanti Avalanche目录遍历漏洞（严重）

该漏洞存在于Ivanti Avalanche updateSkin方法中，由于在文件操作中使用用户提供的路径之前未对其进行正确验证，导致目录遍历漏洞，未经身份验证的威胁者可利用该漏洞远程执行代码。

CVE-2023-32564：Ivanti Avalanche文件上传漏洞（高危）

该漏洞存在于Ivanti Avalanche FileStoreConfig中，由于对用户提供的数据缺乏适当验证，经过身份验证的威胁者可利用该漏洞上传任意文件，导致远程代码执行。

CVE-2023-32565：Ivanti Avalanche SecureFilter Content-Type身份验证绕过漏洞（高危）

该漏洞存在于Ivanti Avalanche SecureFilter类中，由于在授权逻辑中不正确地使用 Content-Type HTTP 标头，远程威胁者可通过发送特制请求，绕过系统上的部分身份验证。

CVE-2023-32566：Ivanti Avalanche SecureFilter allowedPassThrough身份验证绕过漏洞（高危）

该漏洞存在于Ivanti Avalanche SecureFilter allowedPassThrough方法中，由于做出授权决策时字符串匹配不正确，远程威胁者可通过发送特制请求，绕过系统上的部分身份验证。

##

3. **漏洞危害**

攻击者可利用该漏洞触发缓冲区溢出并在目标系统上执行任意代码，或绕过身份认证。

##

4. **影响版本**

Ivanti Avalanche版本 <= 6.4.0

##

5. **解决方案**

目前这些漏洞已经修复，受影响用户可升级到以下版本：

Ivanti Avalanche版本 >= 6.4.1.207

下载链接：

https://forums.ivanti.com/s/avalanche-powered-by-wavelink?language=en\_US

##

6. **时间轴**

【-】2023年08月16日 安识科技A-Team团队监测到Ivanti Avalanche多个高危漏洞

【-】2023年08月16日 安识科技A-Team团队根据漏洞信息分析

【-】2023年08月17日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/203055.html**](https://www.secpulse.com/archives/203055.html)

点赞：
10
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![靶场战神为何会陨落？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/09/VCG41N952384318.png)](https://www.secpulse.com/archives/205395.html "详细阅读 靶场战神为何会陨落？")
* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-210x140.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上](https://www.secpulse.com/archives/204824.html "详细阅读 《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）")
* [![重磅发布 | 《数据安全调研报告》](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/02/beepress-image-204715-1709117527-210x140.jpeg)

  重磅发布 | 《数据安全调研报告》](https://www.secpulse.com/archives/204715.html "详细阅读 重磅发布 | 《数据安全调研报告》")

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

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 友情链接

---

* [网络尖刀](http://www.ijiandao.com/)
* |
* [Sec-Wiki](https://www.sec-wiki.com/)
* |
* [独自等待](https://www.waitalone.cn/)
* |
* [中国红客联盟](https://www.ihonker.org/)
* |
* [娜迦信息](http://www.nagain.com/)
* |
* [SecSilo](https://www.secsilo.com/)
* |
* [易安在线](http://www.e365.org/)
* |
* [i春秋](https://www.ichunqiu.com)
* |
* [铁匠运维网](http://www.tiejiang.org...