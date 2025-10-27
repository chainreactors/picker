---
title: HW工具|一个IP资产风险巡查工具
url: https://www.secpulse.com/archives/198983.html
source: 安全脉搏
date: 2023-04-15
fetch_date: 2025-10-04T11:31:39.469821
---

# HW工具|一个IP资产风险巡查工具

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

# HW工具|一个IP资产风险巡查工具

[工具](https://www.secpulse.com/archives/category/tools)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2023-04-14

19,703

##

##

> ## 作者：EnnioX，转载于github。
>
> ## https://github.com/EnnioX/IPWarden

## **简介**

##

IPWarden（守望者）是一个IP资产风险巡查工具。持续发现系统、Web两个维度的资产和安全风险。所有扫描结果可通过API访问json数据，方便二次开发或数据整理。适合甲方安全人员用于监控管理公网/内网IP资产风险暴露面。

**使用方式：**输入监控IP范围，扫描模块按顺序自动化完成，通过API读取数据

**开发目的：**做安全运营工作时，用不同工具获取，整理数据比较繁琐，通过此工具可将安全工作自动化。用API的方式将数据用于自动生成告警、日周月报、与其它部门对接等。（集成了nmap、masscan、TideFinger、nuclei、xray、rad等安全工具）

**功能**

1. 主机、端口、协议发现
2. 风险端口管理
3. 未授权访问服务漏洞扫描
4. Web站点探测
5. Web管理后台识别
6. xray融合rad漏洞扫描
7. nuclei漏洞扫描
8. Web组件指纹信息收集
9. Web CMS识别
10. SSL证书信息扫描
11. 首页汇总数据生成统计图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198983-1681450539.png)

**下载地址：**

**https://github.com/EnnioX/IPWarden**

**本文作者：[hackctf](newpage/author?author_id=34005)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198983.html**](https://www.secpulse.com/archives/198983.html)

Tags: [HW工具](https://www.secpulse.com/archives/tag/hw%E5%B7%A5%E5%85%B7)、[IP](https://www.secpulse.com/archives/tag/IP)、[IPWarden](https://www.secpulse.com/archives/tag/ipwarden)、[IP资产风险巡查工具](https://www.secpulse.com/archives/tag/ip%E8%B5%84%E4%BA%A7%E9%A3%8E%E9%99%A9%E5%B7%A1%E6%9F%A5%E5%B7%A5%E5%85%B7)、[守望者](https://www.secpulse.com/archives/tag/%E5%AE%88%E6%9C%9B%E8%80%85)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![HVV的艺术系列 之 打点的艺术](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687243139579-300x192.png)

  HVV的艺术系列 之 打点的艺术](https://www.secpulse.com/archives/202287.html "详细阅读 HVV的艺术系列 之 打点的艺术")
* [![从注入到上线](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199441-1682305038-300x200.png)

  从注入到上线](https://www.secpulse.com/archives/199441.html "详细阅读 从注入到上线")
* [![如何在TG群中获取用户真实IP？这些手段教你轻松实现【附代码】](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199003-1681709551-300x260.png)

  如何在TG群中获取用户真实IP？这些手段…](https://www.secpulse.com/archives/199003.html "详细阅读 如何在TG群中获取用户真实IP？这些手段教你轻松实现【附代码】")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/06/04/6bfc834beda6e9debb9f6b48a215b4bc-290x290.jpeg)](https://www.secpulse.com/newpage/author?author_id=34005aaa) | [hackctf](https://www.secpulse.com/newpage/author?author_id=34005) | |
| 文章数：40 | 积分： 80 |
| 微信公众号：hackctf | |

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
* [安世加](http://www.anquanjia.net.cn/)
* |
* [kkQa](https://kkqa.net/)
* |
* [IOTsec-Zone](https://www.iotsec-zone.com)

### 关注我们

* 官方微信

  ![安全脉搏](https://www.secpulse.com/wp-content/themes/secpulse2017/img/qrcode.jpg)
* 安全问答

  ![安全问答](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
* [新浪微博](https://weibo.com/311057789)
* [知乎专栏](https://zhuanlan.zhihu.com/secpulse)

### SecPluse

* [关于我们](/aboutus#abo...