---
title: 新型Linux恶意软件“Auto-Color”允许黑客彻底远程控制受感染系统
url: https://www.freebuf.com/articles/system/422976.html
source: FreeBuf网络安全行业门户
date: 2025-02-27
fetch_date: 2025-10-06T20:36:02.945927
---

# 新型Linux恶意软件“Auto-Color”允许黑客彻底远程控制受感染系统

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

新型Linux恶意软件“Auto-Color”允许黑客彻底远程控制受感染系统

* ![]()
* 关注

* [系统安全](https://www.freebuf.com/articles/system)

新型Linux恶意软件“Auto-Color”允许黑客彻底远程控制受感染系统

2025-02-26 16:34:00

所属地 上海

根据Palo Alto Networks Unit 42的最新发现，北美洲和亚洲的大学及政府机构在2024年11月至12月期间遭受了一种名为Auto-Color的Linux系统恶意软件攻击。

“一旦安装，Auto-Color允许威胁行为者完全远程访问受感染的机器，这使得在没有专用软件的情况下很难移除它，”安全研究员Alex Armstrong在对该恶意软件的技术说明中表示。

## Auto-Color的工作原理与攻击目标

Auto-Color的命名源自初始有效载荷在安装后重命名的文件名。目前尚不清楚它是如何到达其目标的，但已知的是它需要受害者在他们的Linux机器上显式运行它。

该恶意软件的一个显著特点是它用来逃避检测的诸多技巧。这包括使用看似无害的文件名（如door或egg），隐藏命令和控制（C2）连接，以及利用专有加密算法来掩盖通信和配置信息。

一旦以root权限启动，它会安装一个名为“libcext.so.2”的恶意库，将自己复制并重命名为/var/log/cross/auto-color，并修改“/etc/ld.preload”以确保在主机上持久存在。

![image](https://image.3001.net/images/20250226/1740571292735304_3acdce69dbe74618a019eb847f31d084.png!small)

“如果当前用户没有root权限，恶意软件将不会继续在系统上安装逃避检测的库，”Armstrong说。“它会在后续阶段尽可能多地执行操作，而不依赖这个库。”

## Auto-Color的高级功能与自我保护机制

该库能够被动地hook libc中使用的函数，以拦截open()系统调用，并通过修改“/proc/net/tcp”来隐藏C2通信，该文件包含所有活动网络连接的信息。类似的策略也被另一个名为Symbiote的Linux恶意软件所采用。

它还通过保护“/etc/ld.preload”防止进一步修改或删除，从而阻止恶意软件的卸载。

Auto-Color随后会联系C2服务器，授予操作者生成反向shell、收集系统信息、创建或修改文件、运行程序、将机器用作远程IP地址与特定目标IP地址之间的通信代理，甚至通过kill开关自行卸载的能力。

“在执行时，恶意软件试图从命令服务器接收远程指令，该服务器可以在受害者的系统上创建反向shell后门，”Armstrong表示。“威胁行为者使用专有算法分别编译和加密每个命令服务器的IP。”

**参考来源：**

> [New Linux Malware ‘Auto-Color’ Grants Hackers Full Remote Access to Compromised Systems](https://thehackernews.com/2025/02/new-linux-malware-auto-color-grants.html)

# 网络安全 # 终端安全

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

Auto-Color的工作原理与攻击目标

Auto-Color的高级功能与自我保护机制

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