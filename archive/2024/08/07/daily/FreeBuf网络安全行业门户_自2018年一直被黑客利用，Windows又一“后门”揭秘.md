---
title: 自2018年一直被黑客利用，Windows又一“后门”揭秘
url: https://www.freebuf.com/news/407876.html
source: FreeBuf网络安全行业门户
date: 2024-08-07
fetch_date: 2025-10-06T18:03:50.060235
---

# 自2018年一直被黑客利用，Windows又一“后门”揭秘

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

自2018年一直被黑客利用，Windows又一“后门”揭秘

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

自2018年一直被黑客利用，Windows又一“后门”揭秘

2024-08-06 11:50:58

所属地 上海

Windows智能应用控制（Smart App Control）和智能屏幕（SmartScreen）存在一个设计缺陷，该缺陷允许攻击者在不触发安全警告的情况下启动程序，至少自2018年以来一直在被利用。

![Windows](https://image.3001.net/images/20240806/1722922176_66b1b4c0e1c82535dc203.jpg!small)

智能应用控制是一项基于信任的安全功能，它使用微软的应用智能服务进行安全预测，并利用Windows的代码完整性功能来识别和阻止不受信任的（未签名的）或潜在危险的二进制文件和应用程序。

它在Windows 11中取代了智能屏幕，智能屏幕是Windows 8中引入的一个类似功能，旨在保护用户免受潜在恶意内容的侵害（当智能应用控制未启用时，智能屏幕将接管）。当用户尝试打开带有“Web标记”（MotW）标签的文件时，这两个功能都会被激活。

正如Elastic安全实验室所发现的，LNK文件处理中的一个错误（被称为LNK踩踏）可以帮助威胁行为者绕过智能应用控制的安全控制，这些控制旨在阻止不受信任的应用程序。

LNK踩踏包括创建具有非标准目标路径或内部结构的LNK文件，当用户点击这样的文件时，explorer.exe会自动修改LNK文件以使用正确的规范格式。

![MotW security warning](https://image.3001.net/images/20240806/1722922180_66b1b4c424ad8b24855fa.png!small)打开下载文件时的警告(BleepingComputer)

但是，这也从下载的文件中移除了MotW（Web标记），Windows安全功能使用该标签来触发安全检查。

要利用这个设计缺陷，可以向目标可执行文件路径添加一个点或空格（例如，在二进制文件的扩展名后加一个点，如"powershell.exe."），或创建一个包含相对路径的LNK文件，如".\target.exe"。

当用户点击链接时，Windows资源管理器将查找并识别匹配的.exe名称，修正完整路径，通过更新磁盘上的文件来移除MotW，并启动可执行文件。

Elastic安全实验室认为，这一漏洞多年来一直被滥用，因为他们在VirusTotal中发现了多个利用此漏洞的样本，其中最早的提交时间超过六年。

![](https://image.3001.net/images/20240806/1722922934_66b1b7b6bbd955594da90.png!small)智能应用控制LNK踩踏演示（Elastic安全实验室）

他们已经将这些发现与微软安全响应中心共享，后者表示问题可能在未来的Windows更新中得到解决。

此外，Elastic安全实验室还描述了其他可以被攻击者利用来绕过智能应用控制和SmartScreen的弱点，包括：

* 签名恶意软件：使用代码签名或扩展验证（EV）签名证书签署恶意负载
* 信誉劫持：寻找并重新利用信誉良好的应用程序以绕过系统
* 信誉种植：在系统中部署攻击者控制的二进制文件（例如，带有已知漏洞的应用程序或仅在满足特定条件时才会触发的恶意代码）
* 信誉篡改：在不丢失相关信誉的情况下向二进制文件注入恶意代码

Elastic安全实验室警告说，智能应用控制和智能屏幕存在一些基本设计缺陷，可以允许在没有安全警告和用户交互最少的情况下进行初始访问。

安全团队应该仔细审查他们的检测堆栈中的下载内容，而不是仅仅依赖操作系统的原生安全功能来提供这方面的保护。

Elastic安全实验室发布相关信息及检测逻辑和应对措施，旨在帮助防御者在补丁可用之前识别这种活动。该实验室的研究员Joe Desimone已经发布了一个开源工具，用于检查文件的智能应用控制信任级别。

**参考来源：**

> https://www.bleepingcomputer.com/news/microsoft/windows-smart-app-control-smartscreen-bypass-exploited-since-2018/

# windows # windows漏洞 # LNK文件

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