---
title: 神兵利器 | 利用 EHole 进行红队快速批量打点（附下载）
url: https://www.secpulse.com/archives/198462.html
source: 安全脉搏
date: 2023-04-01
fetch_date: 2025-10-04T11:20:27.038159
---

# 神兵利器 | 利用 EHole 进行红队快速批量打点（附下载）

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

# 神兵利器 | 利用 EHole 进行红队快速批量打点（附下载）

[工具](https://www.secpulse.com/archives/category/tools)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-31

19,146

## 0x01 前言

最近看到了关于很多红队方面的文章，如何进行信息收集，从单一目标或多个目标中进行快速查找漏洞。今天提供一种针对较多资产或目标的情况下进行批量识别目标框架进行针对性漏洞挖掘的方式。用得好可能其它队伍还在辛辛苦苦打点的时候，你已经进内网了。

## 0x02 正文

最近 EHole 更新了3.0版本，提供了 finger 与 fofaext 参数，fofaext参数主要从fofa进行批量获取 IP 的端口情况，而 finger 则进行批量进行指纹验证识别。目前开源的指纹将近1000条，基本上都是比较常遇到的系统，另外 finger 参数则可以直接识别下面格式的地址：

```
IP:PORT
HTTP(s)://URL
HTTP(s)://IP
HTTP(s)://IP:PORT
```

在红队场景下首先对多个目标进行了资产收集，如同时几千上万个IP，如何快速的从这些资产中进行获取重要的系统或者直接能 RCE 的系统呢？

可以先从fofa进行批量提取IP+PORT：

```
./Ehole-darwin fofaext -l /Users/r1ng/Downloads/ip.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-1680242087.jpeg)

测试六万个IP从FOFA提取大约需要15-20分钟左右。提取后会自动生成 results.xlsx 文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-16802420871.jpeg)

随后可直接将 host 列 copy 至 txt 文本中进行识别重要的系统（最终获取HTTP服务将3万条，识别10分钟左右）：

PS：指纹可自定义添加，如手里有某个系统的 0day 可指定添加指纹进行识别。

```
./Ehole-darwin finger -l /Users/r1ng/Downloads/url.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-1680242088.jpeg)

最终输出的效果如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-1680242089.jpeg)

各类重点系统可直接进行筛选后按指定目标进行攻击获取权限，比如shiro：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-1680242090.jpeg)

**某OA：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-1680242091.jpeg)

**海康威视 rce等：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198462-16802420911.jpeg)

........

接下来就可以进入内网随意发挥了~

## 0x03 总结

在红队作战中，信息收集是必不可少的环节。EHole可以帮助红队人员快速从网络中以及大量杂乱的资产中精准定位到易被攻击的系统和脆弱资产，从而实施进一步攻击。

```
文章来源：先知社区（牛爱花）
原文地址：https://xz.aliyun.com/t/10442
项目地址：https://github.com/EdgeSecurityTeam/EHole
```

**侵权请私聊公众号（****LemonSec****）删文**

****欢迎关注LemonSec****

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198462.html**](https://www.secpulse.com/archives/198462.html)

Tags: [EHole](https://www.secpulse.com/archives/tag/ehole)、[Fofa](https://www.secpulse.com/archives/tag/fofa)、[红队](https://www.secpulse.com/archives/tag/%E7%BA%A2%E9%98%9F)、[资产收集](https://www.secpulse.com/archives/tag/%E8%B5%84%E4%BA%A7%E6%94%B6%E9%9B%86)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战！记一次超简单渗透过程笔记](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685526754726-300x191.png)

  实战！记一次超简单渗透过程笔记](https://www.secpulse.com/archives/201229.html "详细阅读 实战！记一次超简单渗透过程笔记")
* [![域名资产收集整理实践篇](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196669-1677218839-300x193.png)

  域名资产收集整理实践篇](https://www.secpulse.com/archives/196669.html "详细阅读 域名资产收集整理实践篇")
* [![记一次安服仔薅洞实战过程](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1673510213980-300x228.png)

  记一次安服仔薅洞实战过程](https://www.secpulse.com/archives/194921.html "详细阅读 记一次安服仔薅洞实战过程")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/f43a6447ea66cf84915afd0ca2631f09.png)](https://www.secpulse.com/newpage/author?author_id=5109aaa) | [Lemon ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=5109) | |
| 文章数：68 | 积分： 647 |
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

![安全问答社区](https://www.secpulse.c...