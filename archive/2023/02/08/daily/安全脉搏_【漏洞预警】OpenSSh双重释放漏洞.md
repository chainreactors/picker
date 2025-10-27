---
title: 【漏洞预警】OpenSSh双重释放漏洞
url: https://www.secpulse.com/archives/195421.html
source: 安全脉搏
date: 2023-02-08
fetch_date: 2025-10-04T05:56:31.962133
---

# 【漏洞预警】OpenSSh双重释放漏洞

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

# 【漏洞预警】OpenSSh双重释放漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[安识科技](https://www.secpulse.com/newpage/author?author_id=3871)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-07

12,009

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-1675740290.png)

1. **通告信息**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402901.png)

##

近日，安识科技A-Team团队监测到OpenSSH Server版本9.1中存在一个双重释放漏洞，漏洞编号：CVE-2023-25136，漏洞等级：高危。

对此，安识科技建议广大用户及时升级到安全版本，并做好资产自查以及预防工作，以免遭受黑客攻击。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-1675740291.png)

2. **漏洞概述**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402911.png)

漏洞名称：OpenSSH双重释放漏洞

CVE编号：CVE-2023-25136

简述：OpenSSH server (sshd) 9.1在options.kex\_algorithms处理过程中错误地引入了一个双重释放漏洞，可能导致在未经身份验证的情况下在OpenSSH server (sshd)的默认配置中触发双重释放。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402912.png)

3. **漏洞危害**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402913.png)

OpenSSH是SSH（Secure SHell）协议的开源实现，它通过不安全的网络在两个不受信任的主机之间提供安全的加密通信。OpenSSH 广泛用于基于Unix 的系统，通常用于安全远程登录和远程文件传输，以及其它网络服务。

该漏洞可能会导致应用程序崩溃，信息泄露，任意代码执行等后果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402914.png)

4. **影响版本**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402915.png)

OpenSSH版本  9.1

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-1675740292.png)

5. **解决方案**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402921.png)

目前该漏洞已经修复，受影响用户可升级到 OpenSSH 9.2。

下载链接：https://www.openssh.com/

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402922.png)

6. **时间轴**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195421-16757402923.png)

【-】2023年02月05日 安识科技A-Team团队监测到漏洞公布信息

【-】2023年02月06日 安识科技A-Team团队根据漏洞信息分析

【-】2023年02月07日 安识科技A-Team团队发布安全通告

**本文作者：[安识科技](newpage/author?author_id=3871)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195421.html**](https://www.secpulse.com/archives/195421.html)

Tags: [CVE-2023-25136](https://www.secpulse.com/archives/tag/cve-2023-25136)、[OpenSSH](https://www.secpulse.com/archives/tag/openssh)、[OpenSSh双重释放漏洞](https://www.secpulse.com/archives/tag/openssh%E5%8F%8C%E9%87%8D%E9%87%8A%E6%94%BE%E6%BC%8F%E6%B4%9E)、[双重释放漏洞](https://www.secpulse.com/archives/tag/%E5%8F%8C%E9%87%8D%E9%87%8A%E6%94%BE%E6%BC%8F%E6%B4%9E)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【漏洞预警】OpenSSH 权限提升漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/09/16327365511-300x130.png)

  【漏洞预警】OpenSSH 权限提升漏洞](https://www.secpulse.com/archives/167021.html "详细阅读 【漏洞预警】OpenSSH 权限提升漏洞")
* [![CVE-2020-15778：OpenSSH命令注入漏洞复现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/10/16027414831-300x205.png)

  CVE-2020-15778：OpenS…](https://www.secpulse.com/archives/143302.html "详细阅读 CVE-2020-15778：OpenSSH命令注入漏洞复现")
* [![OpenSSH 命令注入漏洞通告（CVE-2020-15778）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/08/15964351061-300x198.png)

  OpenSSH 命令注入漏洞通告（CVE…](https://www.secpulse.com/archives/136455.html "详细阅读 OpenSSH 命令注入漏洞通告（CVE-2020-15778）")

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

[CSDI summit中国软件研发管理行业技术峰会](https://ww...