---
title: jwt伪造身份组组组合拳艰难通关
url: https://www.secpulse.com/archives/205302.html
source: 安全脉搏
date: 2025-01-01
fetch_date: 2025-10-06T20:06:12.772620
---

# jwt伪造身份组组组合拳艰难通关

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

# jwt伪造身份组组组合拳艰难通关

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-31

12,736

## 前言

现在的攻防演练不再像以往那样一个漏洞直捣黄龙，而是需要各种组合拳才能信手拈来，但是有时候使尽浑身解数也不能称心如意。

## 前期信息收集

首先是拿到靶标的清单

![image-20240713174727680](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551650.png)

访问系统的界面，没有什么能利用的功能点

![image-20240713175618935](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551651.png)

首先进行目录扫描，扫描发现存在xxx.zip的文件放置在web目录上

一般zip文件大部分情况都是开发运维人员做系统维护时留下的备份文件，在系统上线后并没有将其删除，于是底裤（即源代码）都直接给到了攻击者

来到这一步都以为是一路高歌，轻松拿下，没想象到是跌宕起伏伏伏伏伏......

先使用wget下载zip文件，文件总共200+mb，很有概率是源代码的打包

![image-20240713180248221](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551653.png)

从文件内容可判断，该系统是使用的.net开发，可通过dnspy进行审计

![image-20240713180925791](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551654.png)

## 文件上传漏洞审计

拿到源码后的第一个思路是寻找文件上传漏洞

果不其然在源码中找到`uploadimg`接口，发现未对上传的文件格式进行过滤

![image-20240713190953131](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551655.png)

实际访问接口发现，怎么改变文件格式、文件内容、Content-Type、还是各种变种传输都无济于事。

返回包永远是`{"Status":1,"Data""null}`

运维实在是坏呀~

![image-20240713192151353](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551656.png)

## Sql注入漏洞审计

第二个思路就是找注入

但是代码中定义了一个`SqlChecker`全局的类，强制处理所有用户传参，找注入这个方向有有点难啃了

![image-20240713231705777](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551657.png)

## 系统用户信息遍历

找到`/api/user/getusers`接口

![image-20240714124940252](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551658.png)

接口没有做鉴权，构造请求包发送，返回包返回系统所有用户信息

其中用户信息包括姓名、出生日期、微信账号、手机号码、邮箱、密码等等

![image-20240714111059711](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551659.png)

## 伪造jwt\_token获取系统管理员-拿下靶标

源码获取到jwt\_token的secret

![image-20240714111521463](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551660.png)

但是该secret不是可读性文本，估计是随机生成的byte字节序列，因此不能自行使用cyberchief或者其他工具将token直接生成

这里有个坑点：开始是使用gpt生成的脚本进行secret的读取和token的生成，发现gpt在处理字节上面有点问题，生成的jwt\_token不能使用，于是自行编写了个py脚本进行jwt\_token的构造，首先我们将字节序列做16进制的转化，为了python能够使用`bytes.fromhex()`函数读取16进制化的secret，然后根据上面读出的用户信息，伪装admin账号身份，并设置一个较长的`ExpireTime`

![image-20240714112945210](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551661.png)

拿到jwt\_token之后，要如何使用才能拿到后台呢，这里首先要明白该系统的登录鉴权机制

由于他存在注册功能，我们便可在自行注册一个账号，然后进行登录，查看认证处理流程

从数据包里面得知，登录成功后会返回**jwt\_token和一些与用户相关的一些信息**，前端会根据返回的身份信息，跳转到对应的页面，并且功能接口都会带上**jwt\_token**进行请求以便获取系统数据

![image-20240714113814520](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551662.png)

了解清楚后，就开始进行身份伪造，首先去后台登录系统

![image-20240714114400235](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551663.png)

将登录返回包的内容替换为管理员账号的token（从python脚本中生成）和管理员用户的身份信息

![image-20240714114752568](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551664.png)

通过鉴权后，终于成功获取管理员后台，靶标5000分到手，哈哈

![image-20240714121818513](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408071551665.png)

## 总结

本次渗透从惊喜到怀疑到失落，总的来说就是“山穷水尽疑无路，柳暗花明又一村”。

如果只是死磕文件上传、SQL注入这些能够快速获取权限的洞，反而有时会错过一些有用的信息，毕竟比赛中分数才是最要紧的，如何高效快速拿下靶标才是第一要领。

同时，代码审计的过程中要结合系统功能来多方面评估，本次挖洞也是先认真理解了系统的登录认证机制，才知道有jwt鉴权这种方式，从而萌生在代码中找jwt secret的想法，也才能把快到手的分数牢牢抓在自己手中。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205302.html**](https://www.secpulse.com/archives/205302.html)

点赞：
1
[评论：0](#goComment)
收藏：
1

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

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

[全球敏捷运维峰会（Gdevops2020）](https://www.bagev...