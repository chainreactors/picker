---
title: 从spring boot泄露到接管云服务器平台
url: https://www.secpulse.com/archives/198838.html
source: 安全脉搏
date: 2023-04-13
fetch_date: 2025-10-04T11:33:25.238857
---

# 从spring boot泄露到接管云服务器平台

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

# 从spring boot泄露到接管云服务器平台

[资讯](https://www.secpulse.com/archives/category/news)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-12

10,452

**0x1前言**

在打野的时候意外发现了一个站点存在spring boot信息泄露，之前就有看到一些文章可以直接rce啥的，今天刚好试试。通过敏感信息发现存在accesskey泄露，就想直接通过解密，获取敏感信息，接管云平台。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263344.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263345.png "null")

首先说下这个漏洞的产生。主要是因为程序员开发时没有意识到暴露路由可能会造成安全风险，或者没有按照标准流程开发，忘记上线时需要修改/切换生产环境的配置。我们是可以通过访问/v2/api-docs和/swagger-ui.html去验证是否存在的。

**0x2漏洞利用**

本次我们想获取/actuator/env里面的明文信息，那么有三种方法可以获取。

**第一种：通过/jolokia接口获取明文**

利用条件：

1. 1. 目标网站存在 /jolokia 或 /actuator/jolokia 接口
2. 2. 目标使用了 jolokia-core 依赖（版本要求暂未知）

**第二种：通过/env接口发送明文到你vps上**

1. 1. 可以 GET 请求目标网站的 /env
2. 2. 可以 POST 请求目标网站的 /env
3. 3. 可以 POST 请求目标网站的 /refresh 接口刷新配置（存在 spring-boot-starter-actuator依赖）
4. 4. 目标使用了 spring-cloud-starter-netflix-eureka-client 依赖
5. 5. 目标可以请求攻击者的服务器（请求可出外网）

**第三种：和第二种差不多，只是方式不一样**

1. 1. 通过 POST /env 设置属性触发目标对外网指定地址发起任意 http 请求
2. 2. 目标可以请求攻击者的服务器（请求可出外网）

**第四种：通过/heapdump下载到本地解密**

1、可正常 GET 请求目标 /heapdump 或 /actuator/heapdump 接口

而我这边采用第四种方法去获取。先下载一个heapdump文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263346.png "null")

其实我看了好多篇文章，使用jvisualvm.exe尝试去解开heapdump，但是都无法正常获取，可能也是我操作有问题，后续使用Eclipse Memory Analyzer，完美解决。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-16812633461.png "null")

使用Eclipse Memory Analyzer去查询对应的字段：

```
  select * from java.util.LinkedHashMap $Entry x WHERE (toString(x.key).contains("accessKeySecret"))
```

注意：这边默认是不支持模糊查询的，必须字段完全匹配才能查询到字段。如仅输入accessKey是查询不到accessKeySecret的字段值的。

**0x3接管云平台**

成功获取accessKeySecret和accessKeyId后，接下来我们就可以使用cf进行接管云平台了。

链接：https://github.com/teamssix/cf

使用cf config配置accessKeySecret和accessKeyId：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263351.png "null")

配置完直接一键接管：cf alibaba console

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-16812633511.png "null")

这边会生成地址和账号密码，拿去登录即可获取云平台账号权限：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263352.png "null")

这边可以看到，他是有5台服务器实例的，直接获取5台服务器权限。

**0x4结尾**

其实我之前不只尝试了第四种，而是被迫使用第四种方式获取明文信息。尝试前面三种，都是以500报错结束，具体也不知道是什么原因，有大佬知道的可以教一下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198838-1681263353.png "null")

本文其实只是想让大家了解一下一些漏洞和一些信息泄露的用法，其实很多东西都是没有含金量的，说破不值钱。自己最近接触了很多刚开始学习安全的人，都不知道从何入手。对于刚刚开始学习的人，个人建议可以多看看漏洞原理和别人的文章，从中吸取经验和渗透思路，很多实力其实都是经验累积出来的。可能有时候看到别人文章，会觉得就是一帆风顺的，很简单，但是其实很多人只是没把自己走了多少弯路，踩了多少坑说出来罢了。本人也只是刚开始摸索的小白，本身学习是学无止境的，纯靠兴趣去驱动。

本文参考：https://github.com/LandGrey/SpringBootVulExploit

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198838.html**](https://www.secpulse.com/archives/198838.html)

Tags: [Spring boot](https://www.secpulse.com/archives/tag/spring-boot)、[云平台](https://www.secpulse.com/archives/tag/%E4%BA%91%E5%B9%B3%E5%8F%B0)、[信息泄露](https://www.secpulse.com/archives/tag/%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)

点赞：
0
[评论：0](#goComment)
收藏：
1

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![泛微ecology9 ofsLogin.jsp 信息泄露与前台任意用户登录漏洞分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684481531661-300x183.png)

  泛微ecology9 ofsLogin.…](https://www.secpulse.com/archives/200741.html "详细阅读 泛微ecology9 ofsLogin.jsp 信息泄露与前台任意用户登录漏洞分析")
* [![实战 | 记一次Spring boot任意文件上传](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678870715338-300x242.png)

  实战 | 记一次Spring boot任…](https://www.secpulse.com/archives/197601.html "详细阅读 实战 | 记一次Spring boot任意文件上传")
* [![记一次微信小程序渗透实战记录](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671092207427-300x187.png)

  记一次微信小程序渗透实战记录](https://www.secpulse.com/archives/193629.html "详细阅读 记一次微信小程序渗透实战记录")

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

#### 2020-1...