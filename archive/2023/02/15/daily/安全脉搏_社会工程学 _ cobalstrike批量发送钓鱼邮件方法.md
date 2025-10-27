---
title: 社会工程学 | cobalstrike批量发送钓鱼邮件方法
url: https://www.secpulse.com/archives/195833.html
source: 安全脉搏
date: 2023-02-15
fetch_date: 2025-10-04T06:34:57.647577
---

# 社会工程学 | cobalstrike批量发送钓鱼邮件方法

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

# 社会工程学 | cobalstrike批量发送钓鱼邮件方法

[社会工程](https://www.secpulse.com/archives/category/articles/social-engineering)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-14

11,006

声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息安全、企业安全、国家安全。

Cobaltstrike批量发送钓鱼邮件，需要导入邮件模板eml文件、提前准备好的免杀木马或钓鱼网站地址、配置好mail server，使用Yadex需要提前开启imap协议和app登录授权码，然后将STMP信息配置到mailserver中，就可以批量发送钓鱼邮件了。

*1*

Yandex SMTP配置

1、转到 Email 中，选择设置，然后 Email clients，把  `From the imap.yandex.com server via IMAP`  和  `App passwords and OAuth tokens`  打开并保存。

         ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356566.png)

2、点击自己的头像，选择Account management

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356568.png)

3、下拉，选择APP password

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356569.png)

4、选择creat new password

        ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356570.png)

5、选择mail

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-16763565701.png)

6、设置一个登录密码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356571.png)

SMTP 服务器地址：smtp.yandex.com

SMTP 端口：465

SMTP 加密方式：SSL

SMTP 账户：你的 yandex 邮箱（确保 mail 的设置中开启了 IMAP）

SMTP 密码：你刚刚设置的 APP Passwords

*2*

CobaltStrike批量发送钓鱼邮件

1、打开qq邮箱，编写一个邮件的模板，并下载：        ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-16763565711.png)

2、把之前收集的邮件写道一个txt文档中。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356578.png)

3、在Cobaltstrike工具，点击攻击->邮件钓鱼

* Targets 选择上面准备好的那个目标邮箱列表文件
* Template选择上面准备好的那个钓鱼邮件模板
* Attachment 选择带有payload
* Embed URL用上面准备好的那个钓鱼链接来替换邮件原文中所有a标签中的href地址
* Mailserver 指定用于发信的smtp服务器
* Bounce to此处最好和你用于发信的那个邮箱完全保持一致,不然邮件可能发不出去

此处需要注意的是，要将邮件模板eml文件的头的发送地址，改成实际地址，否则会产生Failed: 550 5.7.0 Sender or From header address rejected: not owned by authod告警！。

 ![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356580.png)

4、点击send就可以批量发送钓鱼邮件了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195833-1676356584.png)

-END-

▎经典文章精选

[社会工程学 | office宏分离免杀及应急处置](http://mp.weixin.qq.com/s?__biz=Mzg4MzA4Nzg4Ng==&mid=2247506273&idx=1&sn=f1c833f39fd03fd75954a0e1b52c7cd0&chksm=cf4e5600f839df16a24e9c8be24a6c50843e6e1d8bba6227001fa49806456bf2b8f751a360c7&scene=21#wechat_redirect)

[社会工程学 | gophish批量发送邮件配置](http://mp.weixin.qq.com/s?__biz=Mzg4MzA4Nzg4Ng==&mid=2247506195&idx=1&sn=7f1a13775abd4180f6a2087a94a06fe3&chksm=cf4e5672f839df645281953603a0ae7adce3a42f49ae63aa2c879ec710b2721005c4adaa7567&scene=21#wechat_redirect)

[社会工程学 | Yandex mail捆绑域名方法](http://mp.weixin.qq.com/s?__biz=Mzg4MzA4Nzg4Ng==&mid=2247506197&idx=1&sn=43b9f3e527a694ad867830c1d2e63802&chksm=cf4e5674f839df62c7fc2a67da2637669acef444c264c9e53de0a71162fbd794939a4a62e210&scene=21#wechat_redirect)

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195833.html**](https://www.secpulse.com/archives/195833.html)

Tags: [CobalStrike](https://www.secpulse.com/archives/tag/cobalstrike)、[STMP](https://www.secpulse.com/archives/tag/stmp)、[Yadex](https://www.secpulse.com/archives/tag/yadex)、[钓鱼邮件](https://www.secpulse.com/archives/tag/%E9%92%93%E9%B1%BC%E9%82%AE%E4%BB%B6)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![钓鱼邮件攻击分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685429063311-300x172.png)

  钓鱼邮件攻击分析](https://www.secpulse.com/archives/201168.html "详细阅读 钓鱼邮件攻击分析")
* [![【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678350974041-300x185.png)

  【恶意文件】AgentTesla 贼心不…](https://www.secpulse.com/archives/197248.html "详细阅读 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来")
* [![疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832266-300x186.png)

  疑似 Kasablanka 组织针对阿塞…](https://www.secpulse.com/archives/196928.html "详细阅读 疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/08/1db8ec186f5e122a1420ccb5499c476d-150x150.png)](https://www.secpulse.com/newpage/author?author_id=9525aaa) | [贝塔安全实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=9525) | |
| 文章数：29 | 积分： 65 |
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

####...