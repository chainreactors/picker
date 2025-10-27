---
title: 黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件
url: https://www.freebuf.com/news/360040.html
source: FreeBuf网络安全行业门户
date: 2023-03-11
fetch_date: 2025-10-04T09:16:10.289653
---

# 黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件

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

黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客正在利用远程桌面软件漏洞部署 PlugX 恶意软件

2023-03-10 14:08:52

所属地 香港

The Hacker News 网站披露，威胁攻击者正在利用 Sunlogin 和 AweSun 等远程桌面程序上存在的安全漏洞，部署 PlugX 恶意软件。![1678428553_640ac989241029d471377.png!small](https://image.3001.net/images/20230310/1678428553_640ac989241029d471377.png!small)

值得注意的是，AhnLab 安全应急响应中心（ASEC）曾在一份分析文件中指出，威胁攻击者利用漏洞安装了包括 Sliver 后开发框架、XMRig 加密货币矿工、Gh0st RAT 和 Paradise 勒索软件等多种恶意负载，现在 PlugX 成为了名单上的“新成员”。

现阶段，模块化恶意软件被威胁攻击者广泛使用，并不断添加新功能，以帮助其控制受害者系统控制并盗取信息。

从 ASEC 观察到的攻击活动中可以看出，一旦攻击者成功利用漏洞，立刻执行 PowerShell 命令，从远程服务器检索可执行文件和 DLL 文件。![1678428565_640ac9954d93c06ddfc76.png!small](https://image.3001.net/images/20230310/1678428565_640ac9954d93c06ddfc76.png!small)

这些可执行文件是网络安全公司 ESET 的合法 HTTP 服务器服务，主要用于通过 DLL 侧加载技术加载 DLL 文件，并最终在内存中运行 PlugX 恶意软件有效负载。

2022 年 9 月，Security Joes 在一份报告中强调，PlugX 恶意软件背后的运营商使用大量易受 DLL 侧加载攻击的受信任二进制文件，其中包括许多防病毒可执行文件。此外，PlugX 恶意软件还以其启动任意服务、从外部源下载和执行文件以及删除可以使用远程桌面协议（RDP）获取数据和传播插件的能力而闻名。

最后，ASEC 表示即使在当下，PlugX 恶意软件仍在增加新功能。一旦安装了恶意软件 PlugX 时，威胁攻击者便可在用户不知情的情况下控制受感染的系统。

**参考文章：**

> https://thehackernews.com/2023/03/hackers-exploiting-remote-desktop.html

# 恶意软件

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