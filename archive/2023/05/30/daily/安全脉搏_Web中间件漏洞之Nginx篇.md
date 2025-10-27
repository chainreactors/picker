---
title: Web中间件漏洞之Nginx篇
url: https://www.secpulse.com/archives/201042.html
source: 安全脉搏
date: 2023-05-30
fetch_date: 2025-10-04T11:38:26.419535
---

# Web中间件漏洞之Nginx篇

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

# Web中间件漏洞之Nginx篇

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-29

29,613

Nginx简介

Nginx 是一款轻量级的 Web 服务器、反向代理服务器及电子邮件（IMAP/POP3）代理服务器，并在一个 BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上 nginx 的并发能力确实在同类型的网页服务器中表现较好。

文件解析

漏洞介绍及成因

对任意文件名，在后面添加/任意文件名 .php 的解析漏洞，比如原本文件名是 test.jpg，可以添加 test.jpg/x.php 进行解析攻击。

漏洞复现

在网站根目录下新建一个 i.gif 的文件，在里面写入 phpinfo( )

在浏览器中打开

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338674.jpg)

利用文件解析漏洞，

输入192.168.139.129:100/i.gif.2.php,发现无法解析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338675.png)

将/etc/php5/fpm/pool.d/www.conf中security.limit\_extensions = .php 中的 .php 删除

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338675.jpg)

再次在浏览器中打开，成功解析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338676.jpg)

漏洞介绍及成因

1  将 php.ini 文件中的 cgi.fix\_pathinfo 的值设为 0 .这样 php 在解析 1.php/1.jpg 这样的目录时，只要 1.jpg 不存在就会显示 404

2  将 /etc/php5/fpm/pool.d/www.conf 中 security.limit\_ectensions 后面的值设为 .php

目录遍历

漏洞简介及成因

Nginx 的目录遍历与 Apache 一样，属于配置方面的问题，错误的配置可到导致目录遍历与源码泄露。

漏洞复现

打开 test 目录，发现无法打开

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338677.png)

修改/etc/nginx/sites-avaliable/default ，在如下图所示的位置添加 autoindex on

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338677.jpg)

再次访问

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338678.jpg)

漏洞修复

将 /etc/nginx/sites-avaliable/default 里的 autoindex on 改为 autoindex off

CRLF注入

漏洞简介及成因

CRLF 时“回车+换行”（rn）的简称。

HTTP Header 与 HTTP Body 时用两个 CRLF 分隔的，浏览器根据两个 CRLF 来取出 HTTP 内容并显示出来。

通过控制 HTTP 消息头中的字符，注入一些恶意的换行，就能注入一些会话 cookie 或者 html 代码，由于 Nginx 配置不正确，导致注入的代码会被执行。

漏洞复现

访问页面，抓包

请求加上 /%0d%0a%0d%0a<img src=1 onerror=alert(/xss/)>

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338679.jpg)

由于页面重定向，并没有弹窗

漏洞修复

Nginx 的配置文件 /etc/nginx/conf.d/error1.conf 修改为使用不解码的 url 跳转。

目录穿越

漏洞介绍及成因

Nginx 反向代理，静态文件存储在 /home/ 下，而访问时需要在 url 中输入 files ，配置文件中 /files 没有用/闭合，导致可以穿越至上层目录。

漏洞复现

访问：http://192.168.139.128:8081/files/

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338679.png)

访问：http://192.168.139.128:8081/files../

成功实现目录穿越

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201042-1685338680.png)

漏洞修复

Nginx 的配置文件/etc/nginx/conf.d/error2.conf 的 /files 使用/闭合。

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/201042.html**](https://www.secpulse.com/archives/201042.html)

Tags: [CRLF注入](https://www.secpulse.com/archives/tag/crlf%E6%B3%A8%E5%85%A5)、[nginx](https://www.secpulse.com/archives/tag/nginx)、[Web中间件](https://www.secpulse.com/archives/tag/web%E4%B8%AD%E9%97%B4%E4%BB%B6)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)、[目录穿越](https://www.secpulse.com/archives/tag/%E7%9B%AE%E5%BD%95%E7%A9%BF%E8%B6%8A)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1a3b6dd6d88ce8675bf30bc03975bab1_ce6692cb75dd2998ff4d70b9690c28a5.jpeg)](https://www.secpulse.com/newpage/author?author_id=49738aaa) | [第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738) | |
| 文章数：15 | 积分： 0 |
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

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcH...