---
title: 取证 | 获取PC端微信个人信息工具
url: https://www.secpulse.com/archives/189100.html
source: 安全脉搏
date: 2022-10-15
fetch_date: 2025-10-03T19:54:20.558069
---

# 取证 | 获取PC端微信个人信息工具

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

# 取证 | 获取PC端微信个人信息工具

[工具](https://www.secpulse.com/archives/category/tools)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-14

14,158

|  |
| --- |
| **声明：**该公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。 |

微信客户端取证，可获取用户个人信息（昵称/账号/手机/邮箱/数据库密钥(用来解密聊天记录)）；

支持获取多用户信息，不定期更新新版本偏移，目前支持所有新版本、正式版本。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189100-1665728296.png)

**利用场景**

```
钓鱼攻击(通过钓鱼控到的机器通常都是登录状态)
渗透到运维机器(有些运维机器会日常登录自己的微信)
某些工作需要取证(数据库需要拷贝到本地)
自行备份(日常备份自己留存)
等等...............
```

**支持功能**

1. 支持微信多开场景，获取多用户信息等
2. 微信需要登录状态才能获取数据库密钥
3. 没有动态获取功能，已将偏移地址写入代码内，会不定期更新，如有需要的版本请提交Issues
4. 请用x86编译生成

**版本差异**

1. < 3.7.0.30 只运行不登录能获取个人信息，登录后可以获取数据库密钥
2. > 3.7.0.30 只运行不登录不能获取个人信息，登录后都能获取

**下载地址**

https://github.com/AdminTest0/SharpWxDump

**本文作者：[HACK\_Learn](newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189100.html**](https://www.secpulse.com/archives/189100.html)

Tags: [PC端](https://www.secpulse.com/archives/tag/pc%E7%AB%AF)、[微信](https://www.secpulse.com/archives/tag/%E5%BE%AE%E4%BF%A1)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![如何复现网传微信csv注入漏洞？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683601873856-300x176.png)

  如何复现网传微信csv注入漏洞？](https://www.secpulse.com/archives/200060.html "详细阅读 如何复现网传微信csv注入漏洞？")
* [![WECHAT二维码闪退分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1683184162259-300x201.png)

  WECHAT二维码闪退分析](https://www.secpulse.com/archives/199777.html "详细阅读 WECHAT二维码闪退分析")
* [![钓鱼场景下微信聊天记录回传](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1682058454144-300x209.png)

  钓鱼场景下微信聊天记录回传](https://www.secpulse.com/archives/199362.html "详细阅读 钓鱼场景下微信聊天记录回传")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1ca91da9312f04fadf4ab539bb3cb881.png)](https://www.secpulse.com/newpage/author?author_id=8971aaa) | [HACK\_Learn ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=8971) | |
| 文章数：142 | 积分： 323 |
| 微信公众号：HACK学习呀 | |

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

* [关于我们](/aboutus#about_Us)
* [加入我们](/aboutus#join_Us)
* [联系我们](/aboutus#contact_Us)

### 合作伙伴

* [![云众可信](https://www.secpulse.com/wp-content/themes/secpulse2017/img/customer/yunzhongkexin.png)](https://www.cloudcro...