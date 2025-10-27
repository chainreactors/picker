---
title: 实战|记一次简单的src挖掘
url: https://www.secpulse.com/archives/200144.html
source: 安全脉搏
date: 2023-05-10
fetch_date: 2025-10-04T11:37:42.182929
---

# 实战|记一次简单的src挖掘

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

# 实战|记一次简单的src挖掘

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2023-05-09

23,903

> 作者：Alpaca，转载于先知社区。

## 一.起

开局一个登录框，简单测试了几个弱口令无果后

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614608.png)

注意力转到找回密码处

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614613.png)

先输入两个非法的参数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614615.png)

点击获取验证码，抓包，查看响应代码返回0，前端显示未查询到账户信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614617.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614618.png)

再来一次，抓包并修改响应包，将0改为1，放包后成功来到第二步，前端自动请求了一个后端接口发送验证码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614619.png)

查看该接口的响应，发现验证码作为响应体被返回了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614630.png)

填入验证码，直接跳转到第三步修改新密码，填入新密码后，点击提交

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614634.png)

发现请求体里只有userIds和password两个参数，前者是要修改密码用户的uid，后者是新密码的值，猜测这里可能存在任意账户密码重置，而后又意识到我们传入的用户不存在，所以前端存储的userid变量为0，于是我们将请求包中userIds字段修改为1，尝试重置管理员密码。
后端响应为1，证明密码重置成功了，走到这里只觉喜出望外，赶紧拿着新密码去登录管理员账户

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614636.png)

结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614638.png)

想不通，难道是管理员的账户名不是admin？接连试了几个常见管理员用户名都失败后，想到还有个注册点，兴许可以爆破出管理员账号呢？
结果还是不行：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-16836146381.png)

## 二.承

无奈，此路不通另寻他路，注意到有个APP下载的二维码，解析之，而后下载到apk

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614639.png)

用工具快速扫描一下，发现两个移动端的接口地址有点不同寻常

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614640.png)

访问之，好家伙，竟然返回了所有用户的uid和电话号码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614641.png)

## 三.转

惊喜之余突然回过神来，马上到接口中去检索uid为1的用户

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614644.png)

结果证明uid=1的用户不是管理员权限，而是一个普普通通的员工id，之前由于太过笃定管理员的uid就是1，导致我们在这个点上浪费了太多时间。

## 四.合

随后也是通过这个未授权的接口找到了管理员的id

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614646.png)

但是为了不对业务系统造成严重破坏，我们仅重置了一个普通用户的密码，随后成功登录以验证漏洞的存在：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200144-1683614647.png)

**本文作者：[hackctf](newpage/author?author_id=34005)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200144.html**](https://www.secpulse.com/archives/200144.html)

Tags: [src挖掘](https://www.secpulse.com/archives/tag/src%E6%8C%96%E6%8E%98)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战|记一次简单的src挖掘](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1667273100988-300x213.png)

  实战|记一次简单的src挖掘](https://www.secpulse.com/archives/190162.html "详细阅读 实战|记一次简单的src挖掘")
* [![这你敢信，复习PHP意外搞出一个免杀WebShell](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/5e54ae58-65a2-4f71-99db-5eb61b292b6f.png)

  这你敢信，复习PHP意外搞出一个免杀We](https://www.secpulse.com/archives/206392.html "详细阅读 这你敢信，复习PHP意外搞出一个免杀WebShell")
* [![Windows远程桌面的奇技淫巧](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520540.png)

  Windows远程桌面的奇技淫巧](https://www.secpulse.com/archives/205196.html "详细阅读 Windows远程桌面的奇技淫巧")

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_ur...