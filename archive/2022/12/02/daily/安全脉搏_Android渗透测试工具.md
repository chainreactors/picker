---
title: Android渗透测试工具
url: https://www.secpulse.com/archives/192623.html
source: 安全脉搏
date: 2022-12-02
fetch_date: 2025-10-04T00:15:54.684191
---

# Android渗透测试工具

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

# Android渗透测试工具

[工具](https://www.secpulse.com/archives/category/tools)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-12-01

12,174

**0x01 【Zanti简介】**

* Zanti是由Zimperium公司打造的Android平台下的渗透测试工具包。
* Zanti支持两种中间人攻击方式，分别为MIMT攻击和ARP攻击，中间人内带有多个攻击模块，例如MAC地址欺骗，会话劫持，漏洞检查，密码审核，网络扫描，SSL条等等...
* Zanti除中间人外，还有许多小功能，例如MAC地址转换器，开钓鱼热点，路由器后门大全，WiFi信号检测器，HTTP服务器等等...
* 想使用zanti必须要有root，另外zanti内置busybox阉割版，无需额外安装busybox。

## **0x02 【功能】**

用zANTI，您可以执行各种类型的攻击。

```
-劫持HTTP会话。
-审核密码
-MIMT
-网络扫描。
-捕获下载。
-利用路由器
-MAC地址欺骗。
-创建一个假的wifi热点。
-修改HTTP请求。
```

**使用示例1：****修改MAC地址**

当我们经常进行网络扫描，往往会被一些WIFI网络设备拦截扫描，这时我们可以修改MAC地址进行绕过进行扫描。同时此处的MAC改变并非所有android设备都支持该功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192623-1669866726.jpeg)

### ****使用示例2：**重新扫描网络**

对于网络发生更改的WIFI或者对于新加入的一些设备，我们往往需要重新扫描网络发现新加入的的设备。这时的操作如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192623-16698667261.jpeg)

**参考链接**

```
https://cloud.tencent.com/developer/article/1151888
https://zhuanlan.zhihu.com/p/29743099
```

**侵权请私聊公众号删文**

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192623.html**](https://www.secpulse.com/archives/192623.html)

Tags: [Android](https://www.secpulse.com/archives/tag/Android)、[ARP攻击](https://www.secpulse.com/archives/tag/arp%E6%94%BB%E5%87%BB)、[MIMT攻击](https://www.secpulse.com/archives/tag/mimt%E6%94%BB%E5%87%BB)、[Zanti](https://www.secpulse.com/archives/tag/zanti)、[Zimperium](https://www.secpulse.com/archives/tag/zimperium)、[渗透测试](https://www.secpulse.com/archives/tag/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-300x300.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上…](https://www.secpulse.com/archives/204824.html "详细阅读 《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）")
* [![实战|记一次校内站点的渗透测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684822359737-300x175.png)

  实战|记一次校内站点的渗透测试](https://www.secpulse.com/archives/200867.html "详细阅读 实战|记一次校内站点的渗透测试")
* [![Privilege Escalation 权限提升](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/16811117785231-300x227.png)

  Privilege Escalation…](https://www.secpulse.com/archives/198765.html "详细阅读 Privilege Escalation 权限提升")

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
* [铁匠运维网](http://www.tiejiang.org/)
* |
* [吾爱漏洞](http://www.52bug.cn/)
* |
* [ChaMd5安全团队](http://www.chamd5.org/team/)
* |
* [黑白网](http://www.heibai.org)
* |
* [ms08067](http://www.ms08067.com/)
* |
* [华盟网](https://www.77169.net/)
* |
* [攻防世界](https://adworld.xctf.org.cn)
* |
* [安世加](http://www...