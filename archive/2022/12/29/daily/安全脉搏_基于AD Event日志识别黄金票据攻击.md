---
title: 基于AD Event日志识别黄金票据攻击
url: https://www.secpulse.com/archives/194220.html
source: 安全脉搏
date: 2022-12-29
fetch_date: 2025-10-04T02:38:45.897458
---

# 基于AD Event日志识别黄金票据攻击

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

# 基于AD Event日志识别黄金票据攻击

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-28

8,082

**01、简介**

黄金票据(Golden Ticket)是基于Kerberos认证的一种攻击方式，常用来做域控权限维持。当攻击者获取到域内krbtgt帐户的SID和HASH，就可以随意伪造域内管理员用户，再加上域帐户krbtgt的密码基本不会更改，即使域管修改了密码，攻击者依然可以通过黄金票据获取域管理员权限。

在域环境中，黄金票据无疑是一种特别危险的攻击，是域控权限失陷的特征，基于AD Event日志如何检测黄金票据攻击，我们来研究一下。

**02、黄金票据攻击实例**

黄金票据(Golden Ticket)的原理就是用krbtgt的hash来伪造TGT，只要拥有了高权限的TGT，就可以发送给TGS换取任意服务的ST。

（1）利用mimikatz在域控服务器导出krbtgt的SID值和哈希值。

```
lsadump::dcsync /domain:evil.com /user:krbtgt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215870.png)

（2）在域用户的服务器上使用mimikatz伪造TGT。

```
kerberos::golden /admin:ceshi /domain:evil.com /sid:S-1-5-21-3269078399-3211204512-295171886 /krbtgt:51a721beadd396571257fd2d825be455 /ticket:golden.kiribi
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215872.png)

（3）清空域用户服务器本地票据缓存，导入伪造的黄金票据。

```
kerberos::purge  #清空本地票据缓存
kerberos::ptt golden.kiribi #导入伪造的黄金票据
kerberos::list   #重新查看本地保存的票据
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215873.png)

（4）查看域控服务器的目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215874.png)

**03、黄金票据攻击检测**

从kerberos认证流程来看，正常的用户认证登录生成对应的日志是：4768(请求TGT，服务名称krbtgt) -->4769（请求TGS，服务名称WIN-DC01$）--> 4624（登录帐户，登录进程Kerberos），但是由于黄金票据攻击已经离线生成了TGT，跳过了请求TGT这一步，日志里只会有 4769（请求TGS）-->4624（登录帐户），我们重点来看一下这两条日志里对应的具体的值。

当注入黄金票据访问服务，会出现两次4769的事件，其中第一个4769事件请求的服务名称是WIN-DC01$，第二个4769事件请求的krbtgt服务，伴随着还有登录用户和来源ip地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-16722158741.png)

**4624事件：**记录了黄金票据伪造的帐户名ceshi在192.168.28.20通过kerberos进行网络登录，这里的帐户与SID并不一致，500代表了域管帐户，SID以500结尾可作为特征，通过帐户与SID的对应关系，可以找到伪造的用户，但是如果用户伪造的是administrator用户就可以绕过检测，所以需要把登录IP地址作为判定条件，收集域管理员登录IP地址后，识别出异常登录IP。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215876.png)

黄金票据攻击检测规则：监测4624中LogonType为3的Kerberos登录且SID以500结尾的日志事件，关联到4769的请求事件，并注意观察ServiceName的值。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215880.png)

实时告警效果如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194220-1672215886.png)

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194220.html**](https://www.secpulse.com/archives/194220.html)

Tags: [AD Event](https://www.secpulse.com/archives/tag/ad-event)、[golden ticket](https://www.secpulse.com/archives/tag/golden-ticket)、[Kerberos](https://www.secpulse.com/archives/tag/kerberos)、[黄金票据](https://www.secpulse.com/archives/tag/%E9%BB%84%E9%87%91%E7%A5%A8%E6%8D%AE)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![基于AD Event日志监测域委派后门](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1675837613234-300x200.png)

  基于AD Event日志监测域委派后门](https://www.secpulse.com/archives/195560.html "详细阅读 基于AD Event日志监测域委派后门")
* [![基于AD Event日志监测域内信息探测行为](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1672219350206-300x209.png)

  基于AD Event日志监测域内信息探测…](https://www.secpulse.com/archives/194230.html "详细阅读 基于AD Event日志监测域内信息探测行为")
* [![域0day-(CVE-2022-33679)容易利用吗](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193699-1671158962-300x219.png)

  域0day-(CVE-2022-3367…](https://www.secpulse.com/archives/193699.html "详细阅读 域0day-(CVE-2022-33679)容易利用吗")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2018/03/535dc13ea81e426db897effda78f9aac-290x290.png)](https://www.secpulse.com/newpage/author?author_id=6275aaa) | [Bypass007 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=6275) | |
| 文章数：94 | 积分： 218 |
| 一个网络安全爱好者，对技术有着偏执狂一样的追求。 | |

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comeven...