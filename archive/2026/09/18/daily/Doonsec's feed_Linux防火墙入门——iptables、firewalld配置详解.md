---
title: Linux防火墙入门——iptables、firewalld配置详解
url: https://mp.weixin.qq.com/s/EbLDgvy-hgo_CF9dQTb9MA
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:55:08.659182
---

# Linux防火墙入门——iptables、firewalld配置详解

# Linux防火墙入门——iptables、firewalld配置详解

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

合理的防火墙是你的计算机防止网络入侵的第一道屏障。你在家里上网，通常互联网服务提供会在路由中搭建一层防火墙。当你离开家时，那么你计算机上的那层防火墙就是仅有的一层，所以配置和控制好你 Linux 电脑上的防火墙很重要。

很多 Linux 发行版本已经自带了防火墙，通常是iptables，它很强大并可以自定义，但配置起来有点复杂,firewalld也是用于管理Linux机器上的防火墙规则的工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9Eh7sSJcDibawngUicwmyDMlptf6dVIqbibNOZTibiarUxibNb2vptDWT9Kpn6r5vXia29TGkQ2zGYbPIWDZA/640?&wx_fmt=png#imgIndex=0)

**今天分享的这份资料称得上入门****Linux防火墙的极佳教程****。一共53页，从最基础的防火墙概念开始讲解，涵盖了****iptables、****SNAT、DNAT、firewalld以及rich规****则****等知识点。**

**还有****实战案例：****马哥教育原校区的防火墙配置设置****，还包括iptable******s**超详细思维导图，****干货满满！**

## 目录

* 防火墙的概念
* iptables的基本认识
* iptables的组成
* iptables的基本语法
* iptables之forward的概念
* iptables之地址转换法则
* SNAT源地址转换的具体实现
* DNAT目标地址转换的具体实现
* firewalld介绍
* firewalld配置命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibticIAvQCRPoncoKibqUicicYRntKq4KqtJnQtqCR1hppj7XibEbpF8P5Spew/640?wx_fmt=png#imgIndex=1)

防火墙概念全解

这部分介绍了什么是防火墙，防火墙分类又可以分为主机防火墙、网络层防火墙、硬件防火墙。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtwMsBj4W97o3cjU9D2bLibCKMOZPUiccXc3SF0pa4L5eeicwooBJlgPbMg/640?wx_fmt=png#imgIndex=2)

防火墙的基本认识

第二大部分内容介绍了三种常见防火墙工具：iptables， firewalld以及nftables

* **2.1 Netfilter**
* ****2.2 防火墙工具介绍****

+ **2.2.1 iptables**
+ **2.2.2 firewalld**
+ **2.2.3 nftables**

* **2.3 netfilter 中五个勾子函数和报文流向**
* **2.4 iptables的组成**
* **2.5 netfilter 完整流程**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtHOiaktPGoTvU2eI4NA6ZQ8hxz2ibgU3siaARurne5Q7gho7rZD5WvcJQw/640?wx_fmt=png#imgIndex=3)**

iptables

第三大部分内容主要介绍了iptables：

* **3 iptables**

+ **3.1 iptables 规则说明**

- **3.1.1 iptables 规则组成**
- **3.1.2 iptables规则添加时考量点**
- **3.1.3 本章学习环境准备**

+ **3.2 iptables 用法说明**
+ **3.3 iptables 基本匹配条件**
+ **3.4 iptables 扩展匹配条件**

- **3.4.1 隐式扩展**
- **3.4.2 显式扩展及相关模块**
- **3.4.2.1 multiport扩展**
- **3.4.2.2 iprange扩展**
- **3.4.2.3 mac扩展**
- **3.4.2.4 string扩展**
- **3.4.2.5 time扩展**
- **3.4.2.6 connlimit扩展**
- **3.4.2.7 limit扩展**
- **3.4.2.8 state扩展**

+ **3.5 Target**
+ **3.6 规则优化最佳实践**
+ **3.7 iptables规则保存**
+ **3.8 网络防火墙**

- **3.8.1 FORWARD 链实现内外网络的流量控制**
- **3.8.2 NAT 表**
- **3.8.3 SNAT**
- **3.8.4 DNAT**
- **3.8.5 REDIRECT 转发**

+ **实战案例：马哥教育原校区的防火墙配置设置**

还包括iptables超详细思维导图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtRI3CCiccqOSibjU8Dv7XQzDDVCB3b9tg0QWBianOUHDK9aNPG575J4ibJQ/640?wx_fmt=png#imgIndex=4)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtsIq4XLn4Ng12f2NnX8JgTZhSKWew2Lagexib6tUwTlGxOKecqibBBtkw/640?wx_fmt=png#imgIndex=5)

## 思维导图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtRgtcbO4ib9qtGSiamoJlcB7hSrfMNwfibzbN5hVIfRwJBuuqhlUeQMOlA/640?wx_fmt=png#imgIndex=6)

**数据包处理路线图**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtv9oCbaqlXdgTfEmXxbvA0bkOsrMX8CnE9iblRs1ECUIfjutkUk4Svcw/640?wx_fmt=png#imgIndex=7)

**表和通用匹配**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtgCHbQ4iaeqm94S73JhNyxFjuKXy4cCLjefJ8L6to0DmdpjicN2XED1uA/640?wx_fmt=png#imgIndex=8)

**状态（跟踪连接）机制和相关参数**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtEo1rHBpbOFicsJIPbsYWHnC3tLp8hl5LqNjia2RT5ribw1sFqsVHx9bBg/640?wx_fmt=png#imgIndex=9)

**连接协议**

**完整高清版思维导图下拉文末直达领取！**

firewalld服务

firewalld是CentOS 7.0新推出的管理netfilter的工具，firewalld是配置和监控防火墙规则的系统守护进程。可以实现iptables,ip6tables,ebtables等功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtthic4dglgrfBvCklA6ZQ75JdeENrEZSRlzET1RVH9Y1Kq1YceS4MA0g/640?wx_fmt=gif#imgIndex=10)

其他规则

rich规则比基本的firewalld语法实现更强的功能，不仅实现允许/拒绝，还可以实现日志syslog和auditd，也可以实现端口转发，伪装和限制速率。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/O9D0kmTL9EgbibXBiaZNWZiaicneN3XCelibtM3BJxS9Fp5l7XmAkJYwSzD8G3T3duFIQkgLUQTWMx8jqbGnc62iayzQ/640?wx_fmt=gif#imgIndex=11)

无论对小白还是有一定基础的人，这都是一本实用性很强，具有指导意义的资料，认真读完它，相信你一定会有所受益！

**如何获取以上资源**

![](https://mmbiz.qpic.cn/mmbiz_png/2I159AwKj56GWlFpAuJBpDq9xgZp8de9R91BMgAgGaf5D4gwsyWl1FR9RN64BiaJqzxqDicCAgoKtwb9LPrZm4c15qTds6Ux29Cda2avFL0mY/640?wx_fmt=png&from=appmsg)

********▲****▲****▲********

**识别二维码**

**即可打包全部带走**

\*声明：部分资料源自网络，PDF版仅做分享学习，侵删

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过