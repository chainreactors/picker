---
title: 记录一次通过不断FUZZ从而获取万元赏金
url: https://www.secpulse.com/archives/198172.html
source: 安全脉搏
date: 2023-03-25
fetch_date: 2025-10-04T10:35:37.977711
---

# 记录一次通过不断FUZZ从而获取万元赏金

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

# 记录一次通过不断FUZZ从而获取万元赏金

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[网络安全之旅](https://www.secpulse.com/newpage/author?author_id=49612)

2023-03-24

7,815

## 0x01 前言

      下午，一个老朋友发来一批资产让我找个有效漏洞，原因是厂商弄活动，提交有效漏洞可获取其奖品，那个奖品对朋友很有吸引力。

## 0x02 漏洞背景

      一个后台系统，称其为https://manager.target.com。

## 0x03 漏洞挖掘过程

      目标站点如下图所示，可以看到不仅要用户名密码，还需要正确的手机号，以及验证码才可登录。

## ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198172-1679636212.png)

      对目标站点进行目录探测，未发现有用接口。进一步对其目录探测，使用wfuzz对https://manager.target.com/进行探测，

wfuzz -w dict/test.txt https://manager.target.com/h5FUZZ也无果。至于为什么这样设置目录探测，因为在日常渗透中，我发现大多数h5站点登录都无需验证码，可能是方便手机端用户登录吧。

wfuzz -w dict/test.txt https://manager.target.com/h5-FUZZ，发现https://manager.target.com/h5-mobile返回302状态码，

其跳转到https://manager.target.com/h5-mobile/，发现页面空白，通过burp发现其加载了js文件。

从app.js文件发现mobileapi/login接口。从chunk.js文件中找到其参数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198172-1679636214.png)

构造post报文进行登录，返回账户密码错误，使用burp对其进行暴力破解，成功爆破出一组账号，返回一个token值。eyJadGadad1UxMiJ9.eyJsb2dpbl91c2VyX2tlfasdcLTYwYzasdsgzLThkM2Y5NDdiN2FiNSJ9.Mnp7HxlGHdadseN9wmW5vKMe19ffYRGwMYl4WeJJBkAEdj-d6h2HGF0oadqqwasm-brXrvG5q2p5rQ。

将其token值拼接在头部，构造post报文，访问https://manager.target.com/mobileapi/get/orderall(app.js中提取出来的接口）,发现还是返回状态码401，怀疑是token头部字段问题，使用字典对token进行暴力破解，burp暴力破解模块设置如下图所示，其token常用的字段为token,access-token,Authenticator等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198172-1679636215.png)

发现头部身份认证字段为access-token。其返回了大量用户订单。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198172-1679636216.png)

## 0x04 厂商反馈

      漏洞交给了朋友提交，十分钟就得到了厂商反馈，本来以为算高危，厂商给了个严重，良心厂商。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198172-1679636217.png)

## 0x05 总结

     FUZZ的艺术还是需要不停地探索。

**本文作者：[网络安全之旅](newpage/author?author_id=49612)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198172.html**](https://www.secpulse.com/archives/198172.html)

Tags: [Fuzz](https://www.secpulse.com/archives/tag/fuzz)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/c16e6151dd764121514de708ea47cbe6_1-290x290.jpg)](https://www.secpulse.com/newpage/author?author_id=49612aaa) | [网络安全之旅](https://www.secpulse.com/newpage/author?author_id=49612) | |
| 文章数：8 | 积分： 0 |
|  | |

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
* ...