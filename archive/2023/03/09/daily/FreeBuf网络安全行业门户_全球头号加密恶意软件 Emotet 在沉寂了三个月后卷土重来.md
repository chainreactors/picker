---
title: 全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来
url: https://www.freebuf.com/news/359723.html
source: FreeBuf网络安全行业门户
date: 2023-03-09
fetch_date: 2025-10-04T09:01:49.736514
---

# 全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来

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

全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

全球头号加密恶意软件 Emotet 在沉寂了三个月后卷土重来

2023-03-08 14:39:35

所属地 上海

![](https://image.3001.net/images/20230308/1678253865_64081f2936279cc29108d.png!small)

Emotet恶意软件在沉寂了三个月后，从本周二上午开始再次发送恶意电子邮件，并感染世界各地的设备。

Emotet是一种臭名昭著的恶意软件，通过含有病毒的Word和Excel的电子邮件传播。当用户打开这些文档并启用时，Emotet DLL将被下载并加载到内存中。一旦Emotet被加载，该恶意软件将潜伏等待来自远程命令和控制服务器的指示。

最终，该恶意软件将窃取受害者的电子邮件和联系人，用于后续的Emotet活动或下载额外的有效载荷，例如Cobalt Strike或其他的恶意软件。

虽然Emotet在过去被认为是分布最广的恶意软件，但它已经逐渐放缓，其最后一次恶意邮件活动还是在2022年11月，而且垃圾邮件也仅仅持续了两个星期。

## Emotet在2023年回归

3月7日，网络安全公司Cofense和Emotet追踪小组Cryptolaemus警告说，Emotet僵尸网络再次开始发送恶意电子邮件。

Cofense表示，"我们看到的第一封邮件是在美国东部时间早上7点左右。由于他们需要重建和收集新的证书，目前的恶意邮件的数量还比较低。

攻击者没有像以前的活动那样使用回复链电子邮件，而是利用冒充是发票的电子邮件，如下图所示。

![](https://image.3001.net/images/20230308/1678253922_64081f62527b8526077fd.png!small)

Emotet 钓鱼邮件

这些电子邮件的附件是ZIP压缩包，其中包含Word文档，大小超过500MB。它们被填充了未使用的数据，以使文件更大，这让查杀软件更难扫描和检测到它们是否是包含病毒的。

这些Word文档使用Emotet的'红色黎明'文档模板，提示用户启用文档上的内容才能正确看到它。

![](https://image.3001.net/images/20230308/1678253993_64081fa9d949e780b34ac.png!small)

使用 "红色黎明 "模板的恶意微软Word文档

这些文档包含了乱七八糟的宏，会从被攻击的网站上下载Emotet加载器作为DLL，其中很多是被黑的WordPress博客。

![](https://image.3001.net/images/20230308/1678254110_6408201eb88dfdde476b5.png!small)

Emotet Word文档中混乱的恶意宏程序

下载后，Emotet会被保存到%LocalAppData%下的一个随机命名的文件夹，并使用regsvr32.exe启动。

![](https://image.3001.net/images/20230308/1678254149_640820456c6a61a6eb021.png!small)

由Regsvr32.exe启动的Emotet加载器

与Word文档一样，Emotet DLL也被填充为526MB，以阻碍杀毒软件对恶意软件的检测能力。

这种规避技术目前来看是成功的，正如VirusTotal扫描显示的那样，在64个引擎中，该恶意软件只被一个安全厂商检测到，该厂商只将其检测为 "Malware.SwollenFile"。

![](https://image.3001.net/images/20230308/1678254207_6408207f0aa7e54788cb7.png!small)

大型Emotet DLL以逃避检测

一旦运行，恶意软件将在后台运行，等待命令，这可能会在设备上安装更多的有效载荷。这些有效载荷允许其他攻击者远程访问该设备，然后在被攻击的网络中进一步传播。这些攻击通常会导致数据被盗。

Cofense表示，他们现在还没有看到任何额外的有效载荷被安装，该恶意软件目前还只是在为垃圾邮件活动收集数据。

## 微软的调整

虽然Emotet正在重建其网络，但随着微软在最近的调整后，目前的方法可能不会有太大成功。

2022年7月，微软终于在从互联网下载的微软Office文档中默认禁用了宏。

由于这一变化，打开Emotet文件的用户将收到一条信息，说明由于文件的来源不受信任，宏程序被禁用。

ANALYGENCE高级漏洞分析师Will Dormann表示，这一变化也影响电子邮件中保存的附件。对于大多数收到Emotet电子邮件的用户来说，这项功能可以有效的保护他们，除非他们执意要打开附件。

由于微软的这一调整导致其他攻击者不再使用Word和Excel文档，而是滥用其他文件格式，如微软OneNote、ISO图像和JS文件。

这一调整也打乱了Emotet的计划，目前Emotet也开始转向不同的附件类型。

参考链接：https://www.bleepingcomputer.com/news/security/emotet-malware-attacks-return-after-three-month-break/

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

Emotet在2023年回归

微软的调整

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