---
title: 渗透测试之巧用工具搞定sharepoint
url: https://www.secpulse.com/archives/202586.html
source: 安全脉搏
date: 2023-07-06
fetch_date: 2025-10-04T11:52:38.941920
---

# 渗透测试之巧用工具搞定sharepoint

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

# 渗透测试之巧用工具搞定sharepoint

[工具](https://www.secpulse.com/archives/category/tools)

[知微攻防实验室](https://www.secpulse.com/newpage/author?author_id=40030)

2023-07-05

26,034

**背  景**

在一次实战演练中**goby扫描到一个sharepoint的getshell漏洞**，漏洞cve编号为CVE-2019-0604，本想着一把梭，直接渗透内网，没想到有waf之类的防护，最后还是想办法解决了。

现在网络上各类漏洞利用工具很多，每天都有新的漏洞出来，也不是每个漏洞我们都详细的研究复现过，这些工具的payload大多数都是固定的，如果遇到waf之类的防护就很不爽了，在实战演练中时间紧任务重比的就是手速，重新去搭建相关程序的环境复现就太耽误时间了，其实可以借助抓包提取这类工具的payload，自己再编码进行绕过。

**实 战 演 练**

我这次遇到的程序是微软的知名程序**SharePoint**，SharePoint是微软面向企业市场推的一个集成化平台，可以帮助企业集中管理数据、文档、流程，并和其他企业业务系统进行集成。

未更新版本的Microsoft SharePoint 存在远程代码执行漏洞（CVE-2019-0594、CVE-2019-0604，高危），攻击者可在SharePoint应用程序池和SharePoint服务器中执行任意代码。

* **影响版本：**

Microsoft SharePoint Enterprise Server 2016

SharePoint Foundation 2013 SP1

harePoint Server 2010 SP2

SharePoint Server 2019。

* **攻击入口url：**

/\_layouts/15/Picker.aspx

回到正题，扫描器提示如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545150.png)

这里我直接利用**goby exploit进行getshell**，可以看到提示文件写入成功，如下图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-16885451501.png)

这里写入的shell为菜刀默认的一句话webshell，webshell工具连接失败，服务器端有不知名的waf，这里我想通过修改goby的插件代码上传哥斯拉或者冰蝎webshell来绕过waf，但是goby封装的插件我也改不了也看不到代码。

在网上找到了k8gege的python exploit但是运行也直接报错了，hw过程中也没有时间来具体分析报错原因。这里我只需要知道**发送的exp数据包**即可，直接打开wireshark，在goby中点击验证抓取goby数据包：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545151.png)

直接找到写入shell的http数据包：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545153.png)

**选择fllow->http stream。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545155.png)

**拷贝数据包到burpsuite发包**，如下图，页面虽然报错但是这里有**返回长度264**其实就表示成功：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545157.png)

这里面的加密数据怎么修改呢？

在这里提供个编码工具，具体分析写入payload加密方式：

https://github.com/boxhg/CVE-2019-0604/releases/download/1.0/CVE20190604-Payload.7z

其实就是将如下的xml加密后进行提交，这里直接修改shell内容再加密回去即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545160.png)

*小提示：**这里需要注意xml里面出现<会报错要用html实体转码一下。*

工具的使用很简单直接转码即可，如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545162.png)

服务器有waf 这些语句写进去后 shell 还是连接不上。在这里不断的尝试写shell，期间也遇到一些问题，<> % 写不进去的，一旦出现上传上去的页面就是空白。

这里有人会说都能执行命令了为何不直接下载cs木马执行，当时这个机器是不出网的，终究还是要写文件。后来想到思路是:利用windows系统自带的certutil写入转码后的代码*（不会出现特殊符号，可以写入复杂的webshell）*，再利用certutil在服务器上进行解码生成正常的webshell即可。

**命令如下**：certutil -encode aaa.aspx encode.aspx （本地编码）

先将加密后代码写入服务器，如下图访问正常：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-1688545166.png)将如下代码编码后发包到服务器端再执行：

* ```
  cmd /c certutil -decode "%CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\TEMPLATE\\LAYOUTS\\ua999.aspx"
  ```
* "%CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\TEMPLATE\\LAYOUTS\\ua7771.aspx"

```

```

访问获取命令执行webshell：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202586-16885451661.png)

后续用同样的方式写入其他变形类的webshell进行了内网渗透。

***END***

作者 | vm

编辑 |Ann

**本文作者：[知微攻防实验室](newpage/author?author_id=40030)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/202586.html**](https://www.secpulse.com/archives/202586.html)

Tags: [代码](https://www.secpulse.com/archives/tag/%E4%BB%A3%E7%A0%81)、[内网](https://www.secpulse.com/archives/tag/%E5%86%85%E7%BD%91)、[微软](https://www.secpulse.com/archives/tag/%E5%BE%AE%E8%BD%AF)、[数据包](https://www.secpulse.com/archives/tag/%E6%95%B0%E6%8D%AE%E5%8C%85)、[服务器](https://www.secpulse.com/archives/tag/%E6%9C%8D%E5%8A%A1%E5%99%A8)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)

点赞：
9
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
* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-300x167.png)

  内网信息搜集神器—searc…](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/09/77f2313ca75ff2bf2b5f141b7ca70c2e-290x290.jpg)](https://www.secpulse.com/newpage/author?author_id=40030aaa) | [知微攻防实验室](https://www.secpulse.com/newpage/author?author_id=40030) | |
| 文章数：22 | 积分： 70 |
| 专注物联网安全研究，于细微处下功夫，构筑物联网安全防御体系 | |

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

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-eve...