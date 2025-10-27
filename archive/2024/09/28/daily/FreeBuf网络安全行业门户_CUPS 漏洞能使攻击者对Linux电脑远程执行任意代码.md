---
title: CUPS 漏洞能使攻击者对Linux电脑远程执行任意代码
url: https://www.freebuf.com/news/411893.html
source: FreeBuf网络安全行业门户
date: 2024-09-28
fetch_date: 2025-10-06T18:27:09.245171
---

# CUPS 漏洞能使攻击者对Linux电脑远程执行任意代码

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

CUPS 漏洞能使攻击者对Linux电脑远程执行任意代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

CUPS 漏洞能使攻击者对Linux电脑远程执行任意代码

2024-09-27 11:38:01

所属地 上海

据BleepingComputer消息， Linux 系统中广泛使用的打印系统CUPS（Common UNIX Printing System）存在漏洞，能在受攻击的电脑上远程执行任意代码。目前该漏洞尚未有修复补丁。

![](https://image.3001.net/images/20240927/1727408315_66f628bba0188cc9e0287.png!small)

这些安全漏洞由 Simone Margaritelli 发现，被跟踪为 CVE-2024-47076 （libcupsfilters）、CVE-2024-47175 （libppd）、CVE-2024-47176 （cups-browsed） 和 CVE-2024-47177 （cups-filters），主要涉及到CUPS中的一个组件 cups-browsed。

Cups-browsed 是一个守护进程，可以在本地网络中搜索网络打印机或共享打印机，并使它们可用于在计算机上打印。这类似于 Windows 和 Mac 在网络中搜索需要打印到的远程网络打印机。

Margaritelli 发现，如果启用了 Cups-browsed 守护进程（大多数系统都没有启用），它就会监听 UDP 631 端口，默认情况下还允许从网络上的任何设备创建新打印机的远程连接。如果攻击者创建一个恶意 PostScript 打印机描述（PPD），就可手动将其公布给在 UDP 631 端口上运行的 cups-browsed 进程，从而导致远程设备自动安装恶意打印机，并使其可用于打印。如果该暴露服务器上的用户使用这些新打印机进行打印，PPD 中的恶意命令就会在计算机本地执行。

虽然这是一个远程代码执行攻击，但攻击者必须克服一些障碍才能利用漏洞并真正实现远程代码执行。

首先，目标系统必须启用 cups-browsed 守护程序（默认情况下通常不启用），才能在网络上公开其 UDP 端口。之后，攻击者必须诱骗用户从其本地网络上使用新出现的恶意打印机服务器进行打印。此外，UDP 在网络入口时被广泛禁用，并且该服务通常默认不开启。出于这些原因，Red Hat 已将这些缺陷评级为“重要”而非“严重”级别。

虽然目前漏洞补丁仍在开发中，但 Red Hat分享了缓解措施，管理员可使用以下命令阻止 cups-browsed 服务运行并防止其在重启时自动启用：

> sudo systemctl stop cups-browsed
>
> sudo systemctl disable cups-browsed

此外还可以使用以下命令来查明系统是否正在运行 cups-browsed：

> sudo systemctl status cups-browsed

如果结果显示 “Active： inactive ”，表明 cups-browsed 已被禁止。如果结果显示 “running” 或 “enabled”，并且 “BrowseRemoteProtocols” 指令在配置文件 /etc/cups/cups-browsed.conf 中包含值 “cups”，表明 cups-browsed正在运行，需要将其关闭。

**参考来源：**

> [CUPS flaws enable Linux remote code execution, but there’s a catch](https://www.bleepingcomputer.com/news/security/cups-flaws-enable-linux-remote-code-execution-but-theres-a-catch/)

# 系统安全

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