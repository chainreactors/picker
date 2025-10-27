---
title: 关键的联发科芯片组漏洞影响15亿手机用户
url: https://www.freebuf.com/news/417104.html
source: FreeBuf网络安全行业门户
date: 2024-12-07
fetch_date: 2025-10-06T19:39:25.614781
---

# 关键的联发科芯片组漏洞影响15亿手机用户

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

关键的联发科芯片组漏洞影响15亿手机用户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

关键的联发科芯片组漏洞影响15亿手机用户

2024-12-06 19:01:01

所属地 上海

联发科（MediaTek）是全球领先的Android平板电脑和智能手机芯片供应商，同时也是全球第二大智能手机芯片制造商，拥有超过15亿活跃的Android设备。该公司以其集成的先进5G、人工智能、成像、连接和游戏技术而闻名，致力于提供高性能解决方案，以增强全球范围内各种设备的用户体验。

![](https://image.3001.net/images/20241206/1733482993_6752d9f1ef33d290f34eb.jpg!small)

然而，最近联发科在其芯片组中发现了一系列的安全漏洞，这些漏洞不仅影响了多个版本的Android系统，还波及到了其他相关软件平台。这些安全漏洞被详细记录在最新的安全公告中，它们带来了重大风险，包括权限提升和服务拒绝攻击。

其中，一个被标记为CVE-2024-20125的关键漏洞涉及到视频解码组件（vdec）中的越界写入问题。这个缺陷可能导致本地权限提升，使得攻击者能够在无需用户交互的情况下获得系统执行权限。联发科在安全公告中指出：“在vdec组件中，由于缺少边界检查，可能发生越界写入，这可能导致具有系统执行权限的本地权限提升，攻击者可以无需用户交互即可利用这一漏洞。”

受影响的芯片组包括MT6580、MT6761、MT6765、MT6768等，这些漏洞主要影响运行Android 13.0和14.0操作系统的设备。

具体漏洞列表与影响如下：

![](https://image.3001.net/images/20241206/1733482926_6752d9ae1975115e7a119.png!small)

除此之外，还有一些额外的漏洞影响范围超出了Android系统，涉及到openWRT、Yocto和RDK-B等平台。例如，CVE-2024-20136是一个存在于DA（数据聚合）组件中的越界读取漏洞，可能导致本地信息泄露，影响包括openWRT 19.07和Yocto 4.0在内的广泛芯片组和软件版本。CVE-2024-20137、CVE-2024-20138和CVE-2024-20139则是涉及wlan和蓝牙组件的问题，可能导致客户端断开连接和信息泄露，影响SDK版本和其他平台。

联发科已经承认了这些安全漏洞，并强烈敦促相关组织立即更新受影响的系统以防范潜在风险。为了帮助用户及时发现并报告新的安全问题，该公司在其官方网站上提供了一个报告机制，以便用户披露任何其他发现的安全漏洞。

参考来源：<https://cybersecuritynews.com/mediatek-chipset-bluetooth-vulnerabilities/>

# 漏洞 # 系统安全

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