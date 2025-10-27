---
title: 简单操作实现冰蝎jsp webshell 阿里云免杀
url: https://www.secpulse.com/archives/193780.html
source: 安全脉搏
date: 2022-12-21
fetch_date: 2025-10-04T02:03:22.910278
---

# 简单操作实现冰蝎jsp webshell 阿里云免杀

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

# 简单操作实现冰蝎jsp webshell 阿里云免杀

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-20

11,978

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519427.png)

# 前言

前段时间模仿csroad师傅思路写了一个webhsell免杀生成工具但在某云 webshell检测平台败北，无意间在先知社区文章评论下发现一个哥斯拉的免杀思路，虽然当时给出的哥斯拉webshell已被记录查杀，但借助此思路稍微修改仍然可行。

# 实现

某云webshell检测平台是基于静态特征检测的如自定义类加载器、base64解码、AES解密等特征。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519428.png "null")

常规的免杀手段如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-16715194281.png "null")

进行如上修改的webshell依然没有逃过查杀。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519430.png "null")

先知社区师傅的思路，将class文件落地至WEB-INF/classes目录下，反射实例化该恶意类，在该恶意类内实现常规webshell所需的编解码、加解密、恶意类加载等操作绕过污点特征检查。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519431.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519432.png "null")

原封不动的webshell已被查杀，最后的pageContext也已被加入特征。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519435.png "null")

根据前面的冰蝎客户端解析pageContext对象用于request、response、seesion对象的获取。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519438.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519440.png "null")

那么略过pageContext对象直接传入所需对象数组即可绕过此特征，只需修改冰蝎源码中fillContext方法（所有payload/java下的java文件）在其中添加一个if判断并使用对象数组将pageContext替换即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519441.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519444.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-16715194441.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519446.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193780-1671519449.gif)

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193780.html**](https://www.secpulse.com/archives/193780.html)

Tags: [AES解密](https://www.secpulse.com/archives/tag/aes%E8%A7%A3%E5%AF%86)、[base64解码](https://www.secpulse.com/archives/tag/base64%E8%A7%A3%E7%A0%81)、[jsp](https://www.secpulse.com/archives/tag/jsp)、[webshell](https://www.secpulse.com/archives/tag/webshell)、[免杀](https://www.secpulse.com/archives/tag/%E5%85%8D%E6%9D%80)、[冰蝎](https://www.secpulse.com/archives/tag/%E5%86%B0%E8%9D%8E)、[自定义类加载器](https://www.secpulse.com/archives/tag/%E8%87%AA%E5%AE%9A%E4%B9%89%E7%B1%BB%E5%8A%A0%E8%BD%BD%E5%99%A8)、[阿里云](https://www.secpulse.com/archives/tag/%E9%98%BF%E9%87%8C%E4%BA%91)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![一次暴露面全开的红帽渗透测试【getshell】](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1691635073413-300x186.png)

  一次暴露面全开的红帽渗透测试【getsh…](https://www.secpulse.com/archives/202971.html "详细阅读 一次暴露面全开的红帽渗透测试【getshell】")
* [![实战！一次平平无奇内网渗透记录](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686636814877-300x152.png)

  实战！一次平平无奇内网渗透记录](https://www.secpulse.com/archives/201867.html "详细阅读 实战！一次平平无奇内网渗透记录")
* [![Windows版宝塔bypass到RDP登录](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686117734105-300x189.png)

  Windows版宝塔bypass到RDP…](https://www.secpulse.com/archives/201484.html "详细阅读 Windows版宝塔bypass到RDP登录")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/43b12cc12b9dbbe6a010c40d69088feb-300x298.png)](https://www.secpulse.com/newpage/author?author_id=26366aaa) | [TideSec ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=26366) | |
| 文章数：145 | 积分： 185 |
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

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.q...