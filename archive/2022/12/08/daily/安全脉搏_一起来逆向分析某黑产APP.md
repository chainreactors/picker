---
title: 一起来逆向分析某黑产APP
url: https://www.secpulse.com/archives/193066.html
source: 安全脉搏
date: 2022-12-08
fetch_date: 2025-10-04T00:50:45.017443
---

# 一起来逆向分析某黑产APP

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

# 一起来逆向分析某黑产APP

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[小道安全](https://www.secpulse.com/newpage/author?author_id=11697)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-12-07

14,636

首先这是一个挂羊皮卖狗肉的黑产APP,它通过文字和图片展示几个主流游戏和各种游戏皮肤可以实现作弊功能的APP，还有每次抽奖必中一箱茅台或一百元的话费福利。这一系列的钓鱼手法下来总有人愿意为这些诱惑买单。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395899.png)

下面就分析下这个黑产APP的一些功能和一些赚钱模式。

基础分析

这个APP伪装成为一个安逸防闪框架，从界面展示实际上是一个作弊APP的集合，该APP也并没有采用市面上那些提供免费版本的加固厂商提供的加固或者开源的加固进行对核心功能的保护，实际上是没有什么核心功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395902.png)

下面是该APP所申请的所有权限信息，通过这些权限信息可以大概知道APP大概会做哪些敏感的操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395903.png)

Java层的基本保护：类名混淆、函数名混淆、变量名混淆，这种混淆的保护在现在就是一种掩耳盗铃的方式。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395904.png)

防作弊分析

在APP中实现防作弊方案之一，一般就是采用构建用户画像模型，然后基于用户画像数据进行判别用户是否有作弊的行为。构建用户画像就离不开设备指纹信息的采集以用于实现一机一码的功能。通过一机一码保证功能业务的正常花。

在APP中实现防作弊方案之二，通过检测识别APP运行过程中是否有被第三方分析工具注入到自身进程中，还有识别当前环境是否是危险的环境。

这个APP主要集成了友盟的SDK和快手联盟的SDK，这两个SDK都有做一些防作弊的行为，友盟的sdk主要实现设备指纹信息的采取和崩溃信息的手机，快手联盟的SDK在防作弊方面主要实现了对运行环境信息 的识别和第三方注入工具的识别检测。

**友盟SDK功能**

友盟中用于构建用户画像，获取设备指纹属性有：包签名MD5，包签名SHA-1，APP名称，APP版本号，CPU，anroid\_id，IMEI，GPU，IMSI，wifi，meid，GUID，IDFA，MIUI，serial，ICCID，OAID，IP地址、MAC地址，GPS地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395905.png)

**快手SDK防作弊**

快手sdk中主要分为两部分一个是快手联盟的功能一个是访问设置拉取快手视频播放的功能，这里面主要集成了通过用特殊文件、特殊路径、特殊包名进行做识别检测运行是否在root环境下、是否有被xposed和frida注入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395906.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395908.png)

赚钱模式

基于对APP的分析，想下载利用该黑产APP所展示的那些具有作弊功能的APP，需要先看15秒的快手联盟广告视频，还有要下载注册使用15秒以上捆绑在视频中的APP应用。通过这一系列的事情后才能获取都网络搬运收集集成的那些可以作弊的APP应用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395909.png)

https://u.kuaishou.com/ 这个快手联盟就是个用于接投广告的平台，这个APP主要通过集成这个快手联盟的sdk，然后实现用于推广快手联盟里面视频广告任务和推广APP下载任务(都要15秒及以上才算有效)。

这个快手联盟接推广任务的时候需要先提交公司名称、APP应用名称、域名信息。门槛还是相对比较高的，一般个人想这个推广联盟平台上赚取一笔收益还是比较难的(虽然有各种充斥着500块钱可以注册一家公司的广告)。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395911.png)

各种可以进行作弊的APP，不就是那15秒视频吗，看下就可以获取到，不心动？

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395912.png)

简单溯源

通过APP中的java代码部分(SO部分主要crash捕获还有推广的SO，没有其他过多功能)，分析到该APP采用明文硬编码方式，通过固定链接进行下载并安装具有威胁性的APP。

这个APP在网络通信方面也是没有采取相关的混淆或者校验保护，都是基于明文的方式进行的，这其实也正常因为这些APP上不了台面，不需要合规审查，只要能割韭菜就可以了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-1670395915.png)

通过360威胁情报中心 https://ti.360.cn/#/homepage 进行查询，可以通过下图看到该域名已经被检测出属于黑灰产信息并且具有不良的信息的标识了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193066-16703959151.png)

其实这个可以延伸挖掘该作者更多固定资产信息。然后再对这个服务器去做入侵或渗透的一些事情。

总结

网络上充斥着各种各样诱惑，总有些人会把持不住，自己还傻傻的不知道已经在为网络攻击者赚钱，最终不得不为自己的行为买单。

前面的那些分析，只是简单的分析该黑产的实际模式，并没有涉及过多的技术方案和对抗分析方案。这种模式其实和早些年在window端上那些网络上一键安装系统、2345浏览器、360安全卫士的各种推广一模一样，但是由于移动端的快速发展，这些搞广告联盟接推广的就开始将重心转移到移动端，这些只不过是换汤不换药的一个模式。

结束

**本文作者：[小道安全](newpage/author?author_id=11697)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193066.html**](https://www.secpulse.com/archives/193066.html)

Tags: [java](https://www.secpulse.com/archives/tag/java)、[SDK](https://www.secpulse.com/archives/tag/sdk)、[函数名混淆](https://www.secpulse.com/archives/tag/%E5%87%BD%E6%95%B0%E5%90%8D%E6%B7%B7%E6%B7%86)、[变量名混淆](https://www.secpulse.com/archives/tag/%E5%8F%98%E9%87%8F%E5%90%8D%E6%B7%B7%E6%B7%86)、[安逸防闪框架](https://www.secpulse.com/archives/tag/%E5%AE%89%E9%80%B8%E9%98%B2%E9%97%AA%E6%A1%86%E6%9E%B6)、[类名混淆](https://www.secpulse.com/archives/tag/%E7%B1%BB%E5%90%8D%E6%B7%B7%E6%B7%86)、[逆向](https://www.secpulse.com/archives/tag/%E9%80%86%E5%90%91)、[防作弊](https://www.secpulse.com/archives/tag/%E9%98%B2%E4%BD%9C%E5%BC%8A)、[黑产APP](https://www.secpulse.com/archives/tag/%E9%BB%91%E4%BA%A7app)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Java反序列化：URLDNS的反序列化调试分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1689306075699-300x217.png)

  Java反序列化：URLDNS的反序列化…](https://www.secpulse.com/archives/202757.html "详细阅读 Java反序列化：URLDNS的反序列化调试分析")
* [![界面劫持之拖放劫持](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688004080281-300x168.png)

  界面劫持之拖放劫持](https://www.secpulse.com/archives/202412.html "详细阅读 界面劫持之拖放劫持")
* [![Java 反序列化之 XStream 反序列化](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687854074464-300x280.png)

  Java 反序列化之 XStream 反…](https://www.secpulse.com/archives/202377.html "详细阅读 Java 反序列化之 XStream 反序列化")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/07/16/e6a1736ccb19220a63d5403b14ce91c9-290x290.jpeg)](https://www.secpulse.com/newpage/author?author_id=11697aaa) | [小道安全 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=11697) | |
| 文章数：31 | 积分： 0 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/...