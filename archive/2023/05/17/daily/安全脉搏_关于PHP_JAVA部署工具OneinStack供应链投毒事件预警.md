---
title: 关于PHP/JAVA部署工具OneinStack供应链投毒事件预警
url: https://www.secpulse.com/archives/200488.html
source: 安全脉搏
date: 2023-05-17
fetch_date: 2025-10-04T11:37:07.706139
---

# 关于PHP/JAVA部署工具OneinStack供应链投毒事件预警

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

# 关于PHP/JAVA部署工具OneinStack供应链投毒事件预警

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-16

30,761

**事件概要：**

OneinStack供应链投毒事件

**威胁等级：**

高危

**影响范围：**

近期使用OneinStack部署于RedHat的站点

**攻击类型：**

供应链投毒攻击

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224717.gif)

**事件描述**

据深信服安全运营中心（MSS）安服应急响应团队和深信服蓝军高级威胁（APT）团队监测，监测到PHP/JAVA部署工具OneinStack遭受供应链投毒攻击，官方网站下载安装包被植入恶意链接，已发现境内受感染用户，截止发布时间，相关恶意IoC情报尚未被多数威胁情报平台标记。（oneinstack-full.tar.gz，fc897d5abba2dbff00fb6b88da878ba8）

官网OneinStack安装程序中/usr/local/src/oneinstack/include/openssl.sh被攻击者植入恶意代码。用户从恶意地址下载oneinstack.jpg后，oneinstack.jpg会解压并执行./cron目录下load（只在RedHat服务器运行）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224718.png)

受害主机中同时存在后续下载的t.jpg，s.jpg，install，cr.jpg，libaudit.so.2等恶意文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224724.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224728.png)

通过crond、yasio等进程建立DNS隧道通信。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224730.png)

目前作者已确认该事件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200488-1684224764.png)

更多相关事件技术分析详情近日将在公众号发布。

**参考链接**

https://github.com/oneinstack/oneinstack/issues/487

**IoC**

|  |  |
| --- | --- |
| 8.210.226.191 | |
| 47.243.39.207 | |
| oneinstack.cnoneinstack.com | |
| 123.56.51.37 | |
| download.cnoneinstack.com | |
| load | d892764619456d107894eb4220774d0b |
| libaudit.so.2 | ec868c324e8778d8b3f9d77096720def |
| oneinstack.jpg | 52448a6b782d12adc7b9ce2e54a11802 |
| oneinstack-full.tar.gz | fc897d5abba2dbff00fb6b88da878ba8 |

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200488.html**](https://www.secpulse.com/archives/200488.html)

Tags: [java](https://www.secpulse.com/archives/tag/java)、[OneinStack](https://www.secpulse.com/archives/tag/oneinstack)、[OneinStack供应链](https://www.secpulse.com/archives/tag/oneinstack%E4%BE%9B%E5%BA%94%E9%93%BE)、[php](https://www.secpulse.com/archives/tag/php)、[供应链](https://www.secpulse.com/archives/tag/%E4%BE%9B%E5%BA%94%E9%93%BE)、[供应链投毒攻击](https://www.secpulse.com/archives/tag/%E4%BE%9B%E5%BA%94%E9%93%BE%E6%8A%95%E6%AF%92%E6%94%BB%E5%87%BB)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Java反序列化：URLDNS的反序列化调试分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1689306075699-300x217.png)

  Java反序列化：URLDNS的反序列化…](https://www.secpulse.com/archives/202757.html "详细阅读 Java反序列化：URLDNS的反序列化调试分析")
* [![6月-7月红蓝对抗实战训练营](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688103742245-300x195.png)

  6月-7月红蓝对抗实战训练营](https://www.secpulse.com/archives/202625.html "详细阅读 6月-7月红蓝对抗实战训练营")
* [![6月-7月红蓝对抗实战训练营](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688103742245-300x195.png)

  6月-7月红蓝对抗实战训练营](https://www.secpulse.com/archives/202471.html "详细阅读 6月-7月红蓝对抗实战训练营")

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

#### 2020-01-...