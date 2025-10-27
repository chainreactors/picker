---
title: 值得警惕，攻击者仍在利用已修复的Exchange漏洞
url: https://www.freebuf.com/news/357966.html
source: FreeBuf网络安全行业门户
date: 2023-02-18
fetch_date: 2025-10-04T07:23:09.214133
---

# 值得警惕，攻击者仍在利用已修复的Exchange漏洞

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

值得警惕，攻击者仍在利用已修复的Exchange漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

值得警惕，攻击者仍在利用已修复的Exchange漏洞

2023-02-17 16:49:30

所属地 上海

据BleepingComputer 2月16日消息，一种名为“ProxyShellMiner”的新型恶意软件正利用微软 Exchange ProxyShell 漏洞，在整个 Windows 域中部署加密货币矿工。

![](https://image.3001.net/images/20230217/1676623800_63ef3fb81bd2d329dc34c.png!small)

ProxyShell 是微软在 2021 年发现并修复的三个 Exchange 漏洞的统称。当这些漏洞链接在一起时，能够允许未经身份验证的远程代码执行，使攻击者可以完全控制 Exchange 服务器并进行横向移动。

## 攻击链概览

在由安全公司 Morphisec 发现的攻击中，攻击者利用被跟踪为 CVE-2021-34473 和 CVE-2021-34523 的 ProxyShell 漏洞来获得对目标组织网络的初始访问权限。接下来，攻击者将 .NET 恶意软件负载放入域控制器的 NETLOGON 文件夹中，以确保网络上的所有设备都运行恶意软件。

在激活恶意软件时，攻击者会输入一个特殊的命令行参数，该参数也被称为 XMRig 矿工组件的密码。

![](https://image.3001.net/images/20230217/1676623862_63ef3ff60eb62f5796e56.png!small)特殊命令行参数 （Morphisec）

在下一阶段，恶意软件下载名为“DC\_DLL”的文件并执行 .NET 反射以提取任务计划程序、XML 和 XMRig 密钥的参数，DLL 文件用于解密其他文件。

为了获得持久性，恶意软件创建一个配置为在用户登录时就会自动运行的计划任务，并从远程下载第二个加载程序，该程序将决定通过哪一个浏览器把挖矿木马植入内存空间，并使用一种称为process hollowing（进程挖空）的技术，从硬编码列表中随机选择一个矿池进行挖矿活动。

攻击链的最后一步是创建一个防火墙规则来阻止所有传出流量，该规则适用于所有 Windows 防火墙配置文件。这样能让受害者不太容易检测到感染标记或收到有潜在危害的任何警报。

![](https://image.3001.net/images/20230217/1676623930_63ef403abdfca5bc4cfb7.png!small)添加防火墙规则以阻止所有传出流量 (Morphisec)

Morphisec 警告称，挖矿恶意软件的影响不仅仅是导致服务中断、服务器性能下降和设备过热，一旦攻击者在网络中站稳脚跟，就可以进一步实施从后门部署到代码执行的任何操作。

为了应对 ProxyShellMiner 感染的风险，Morphisec 建议所有系统管理员安装最新的安全更新，并启用多方面的威胁检测和防御策略。

> 参考来源：[Microsoft Exchange ProxyShell flaws exploited in new crypto-mining attack](https://www.bleepingcomputer.com/news/security/microsoft-exchange-proxyshell-flaws-exploited-in-new-crypto-mining-attack/)

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

攻击链概览

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)