---
title: 【漏洞预警】Apache Tomcat信息泄露漏洞
url: https://www.secpulse.com/archives/198143.html
source: 安全脉搏
date: 2023-03-24
fetch_date: 2025-10-04T10:27:47.562996
---

# 【漏洞预警】Apache Tomcat信息泄露漏洞

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

# 【漏洞预警】Apache Tomcat信息泄露漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-23

13,872

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-1679560927.png)

1. **通告信息**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609271.png)

近日，安识科技A-Team团队监测到Apache官方发布安全公告，修复了Apache Tomcat中的一个信息泄露漏洞，漏洞编号：CVE-2023-28708，漏洞等级：高危。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

##

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-1679560928.png)

2. **漏洞概述**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609281.png)

漏洞名称：Apache Tomcat信息泄露漏洞

CVE编号：CVE-2023-28708

简述：当Apache Tomcat的RemoteIpFilter和HTTP反向代理一起使用时，如果请求中包含设置为https的X-Forwarded-Proto标头，则Tomcat创建的会话cookie未包括安全属性，可能导致用户代理通过不安全的通道传输会话cookie，造成敏感信息泄露。

##

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609282.png)

3. **漏洞危害**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609283.png)

Apache Tomcat是一个流行的开源的Web服务器和Java代码的Servlet容器。

该漏洞可能会泄露用户信息，系统信息等，攻击者可通过该漏洞进行更深入的攻击。

##

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609284.png)

4. **影响版本**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609285.png)

Apache Tomcat版本：11.0.0-M1 - 11.0.0-M2

Apache Tomcat版本：10.1.0-M1 - 10.1.5

Apache Tomcat版本：9.0.0-M1 - 9.0.71

Apache Tomcat版本：8.5 .0 - 8.5.85

##

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609286.png)

5. **解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609287.png)

目前该漏洞已经修复，受影响用户可升级到以下版本：

Apache Tomcat版本：>= 11.0.0-M3

Apache Tomcat版本：>= 10.1.6

Apache Tomcat版本：>=9.0.72

Apache Tomcat版本：>=8.5.86

下载链接：https://tomcat.apache.org/

##

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609288.png)

6. **时间轴**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198143-16795609289.png)

【-】2023年03月21日 安识科技A-Team团队监测到漏洞公布信息

【-】2023年03月22日 安识科技A-Team团队根据漏洞信息分析

【-】2023年03月23日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198143.html**](https://www.secpulse.com/archives/198143.html)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")
* [![DedeBIZ系统审计小结](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502121526395.png)

  DedeBIZ系统审计小结](https://www.secpulse.com/archives/205891.html "详细阅读 DedeBIZ系统审计小结")

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

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.n...