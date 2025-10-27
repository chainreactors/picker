---
title: 【漏洞预警】OpenLiteSpeed Web Server多个安全漏洞
url: https://www.secpulse.com/archives/191153.html
source: 安全脉搏
date: 2022-11-17
fetch_date: 2025-10-03T22:59:18.594842
---

# 【漏洞预警】OpenLiteSpeed Web Server多个安全漏洞

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

# 【漏洞预警】OpenLiteSpeed Web Server多个安全漏洞

[资讯](https://www.secpulse.com/archives/category/news)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-16

9,899

1. **通告信息**

近日，安识科技A-Team团队监测到OpenLiteSpeed Web Server和企业版LiteSpeed Web Server中多个漏洞的细节，这些漏洞可能导致信息泄露、权限提升和远程代码执行。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

##

2. **漏洞概述**

漏洞名称：OpenLiteSpeed目录遍历漏洞

CVE编号：CVE-2022-0072

简述：OpenLiteSpeed Web Server和LiteSpeed Web Server仪表板中存在目录遍历漏洞，可能导致绕过安全措施并访问被禁止的文件。

漏洞名称：OpenLiteSpeed远程代码执行漏洞

CVE编号：CVE-2022-0073

简述：OpenLiteSpeed Web Server和LiteSpeed Web Server管理仪表板容易受到命令注入漏洞的影响，获得仪表板凭据的恶意用户可以利用该漏洞在服务器上执行代码。

漏洞名称：OpenLiteSpeed权限提升漏洞

CVE编号：CVE-2022-0074

简述：OpenLiteSpeed Web Server和LiteSpeed Web Server容器中存在不受信任的搜索路径漏洞，可能导致权限提升为root。

##

3. **漏洞危害**

OpenLiteSpeed是LiteSpeed Technologies 开发的高性能、轻量级的开源 HTTP 服务器，它是LiteSpeed Web Server Enterprise的开源版本。

OpenLiteSpeed Web Server及其企业版中存在3个漏洞，可以通过组合利用这些漏洞远程执行代码并将权限提升为root。

##

4. **影响版本**

目前受影响的OpenLiteSpeed Web Server和LiteSpeed Web Server版本：

1.5.11 <= OpenLiteSpeed Web Server <= 1.7.16

5.4.6 <=LiteSpeed Web Server<=6.0.11

##

5. **解决方案**

目前LiteSpeed Technologies已经修复了这些漏洞，受影响用户可升级到OpenLiteSpeed v1.7.16.1、LiteSpeed 6.0.12 或更高版本。

OpenLiteSpeed下载链接：

https://github.com/litespeedtech/openlitespeed/tags

LiteSpeed下载链接：

https://store.litespeedtech.com/store/index.php?rp=/announcements/451

##

6. **时间轴**

【-】2022年11月14日 安识科技A-Team团队监测到漏洞公布信息

【-】2022年11月15日 安识科技A-Team团队根据漏洞信息分析

【-】2022年11月16日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/191153.html**](https://www.secpulse.com/archives/191153.html)

Tags: [CVE-2022-0072](https://www.secpulse.com/archives/tag/cve-2022-0072)、[CVE-2022-0073](https://www.secpulse.com/archives/tag/cve-2022-0073)、[CVE-2022-0074](https://www.secpulse.com/archives/tag/cve-2022-0074)、[OpenLiteSpeed](https://www.secpulse.com/archives/tag/openlitespeed)、[Web Server](https://www.secpulse.com/archives/tag/web-server)

点赞：
2
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
* [i春秋](https://...