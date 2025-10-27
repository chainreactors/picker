---
title: 一个隐藏在图片中的恶意软件正在亚、非地区泛滥
url: https://www.freebuf.com/news/349816.html
source: FreeBuf网络安全行业门户
date: 2022-11-15
fetch_date: 2025-10-03T22:45:38.547123
---

# 一个隐藏在图片中的恶意软件正在亚、非地区泛滥

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

一款极善隐藏的恶意软件，悄悄在亚、非地区泛滥

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

一款极善隐藏的恶意软件，悄悄在亚、非地区泛滥

2022-11-14 19:52:24

所属地 上海

![](https://image.3001.net/images/20221114/1668422652_63721bfcac58d3400af91.jpg!small)

最近，一个被称为Worok的网络间谍组织被发现在看似无害的图像文件中隐藏恶意软件，它的存在是攻击者感染链中的一个关键环节。

捷克网络安全公司Avast表示，PNG（图片格式）文件作为隐藏信息盗窃的有效载荷，有很大的隐蔽性。

"该公司说："值得注意的是，攻击者通过使用Dropbox存储库从受害者的机器上收集数据，并用Dropbox API与最终阶段进行通信。

在ESET披露Worok对位于亚洲和非洲的高知名度公司和地方政府进行了攻击。

斯洛伐克网络安全公司还记录了Worok的破坏序列，它利用了一个名为CLRLoad的基于C++的加载器，为嵌入PNG图像的未知PowerShell脚本铺平道路，这种技术被称为隐写术。

也就是说，尽管某些入侵行为需要使用微软Exchange服务器中的ProxyShell漏洞来部署恶意软件，但最初的攻击载体仍然是未知的。

Avast的研究结果表明，该组织在获得初始访问权后利用DLL侧载来执行CLRLoad恶意软件，但在受感染环境中进行横向移动之前并没有。

![](https://image.3001.net/images/20221114/1668422729_63721c49d22c3d55be40f.jpg!small)

据称，由CLRLoad（或另一个名为PowHeartBeat的第一阶段）启动的PNGLoad有两个变体，每个变体负责解码图像内的恶意代码，以启动PowerShell脚本或基于.NET C#的有效载荷。

虽然网络安全公司指出，它能够标记一些属于第二类的PNG文件，这些文件分发了一个隐藏的C#恶意软件，但PowerShell脚本仍然是难以捉摸的。

之所以，这些PNG图片看起来很无害。是因为，PNG文件位于C:\Program Files\Internet Explorer中，图片不会引起注意，而且Internet Explorer也有一个类似的主题。

这种新的恶意软件，代号为DropboxControl，作为一种信息窃取工具，它使用Dropbox账户进行命令和控制，使攻击者能够上传和下载文件到特定的文件夹，以及运行存在于某个文件中的命令。

其中一些值得注意的命令包括执行任意可执行文件、下载和上传数据、删除和重命名文件、捕获文件信息、嗅探网络通信和渗出系统元数据的能力。

Avast说，柬埔寨、越南和墨西哥的公司和政府机构是受DropboxControl影响的几个主要国家，而且，由于 "这些有效载荷的代码质量明显不同"，该恶意软件的作者可能与CLRLoad和PNGLoad的作者也不同。

无论如何，通过嵌入式病毒工具来收集感兴趣的文件，都清楚地表明了Worok的情报收集目的。

研究人员总结说：Worok的工具在流行率很低，所以它可以表明该工具集是一个APT项目，侧重于亚洲、非洲和北美的私营和公共部门的高知名度实体。

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