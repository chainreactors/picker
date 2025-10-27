---
title: 超2000万的安装量，Google Play已成恶意广告程序的温床
url: https://www.freebuf.com/news/347844.html
source: FreeBuf网络安全行业门户
date: 2022-10-26
fetch_date: 2025-10-03T20:54:28.343393
---

# 超2000万的安装量，Google Play已成恶意广告程序的温床

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

超2000万的安装量，Google Play已成恶意广告程序的温床

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

超2000万的安装量，Google Play已成恶意广告程序的温床

2022-10-25 17:26:43

所属地 上海

McAfee的安全研究人员发现，GooglePlay官方商店里有16个恶意点击的应用程序，安装次数超过2000万次。其中一个名为DxClean的应用程序的安装次数更是超过500万次，搞笑的是，其用户评级竟然还有4.1分(满分5分)。

这类伪装成应用程序的广告软件，常常表现为在不可见的框架中或在后台加载广告并点击它们，为背后的攻击者创造收入。

最近，McAfee移动研究小组发现了潜入GooglePlay的新Clicker恶意软件。McAfee发表的报告中说:"总共有16个以前在GooglePlay上的应用程序被证实有恶意的有效载荷，大约有2000万次安装。"

攻击者将恶意点击代码隐藏在较为实用的应用软件中，如手电筒(Torch)、QR阅读器、 Camara、单位转换器和任务管理器。

![](https://image.3001.net/images/20221025/1666689984_6357abc0baf9e2d44faa4.png!small)

恶意点击程序通过FCM消息（Firebase Cloud Messaging）传播，当应用程序收到符合某些条件的FCM消息时，相关功能就会在后台启动。FCM消息包括多种信息，比如要调用的函数和要传递的参数。"

通常情况下，这些功能会指示设备在后台访问网站，同时模仿用户的行为。这可能会消耗大量的网络流量和电力，同时通过在用户不知情的情况下点击广告为攻击者创造利润。

专家们在这些点击器应用程序中发现了两段代码，一个是"comclickcas"库，用于实现自动点击功能，第二个是"com.liveposting"库，作为一个代理，运行隐藏的广告软件服务。

目前安全公司分享了McAfee专家报告的所有16个Clicker应用程序，并且已从GooglePlay中删除。“Clicker恶意软件以非法广告收入为目标，可以破坏移动广告生态系统。恶意行为被巧妙地隐藏起来，难以被用户发现。”

最后，安全专家建议安装并激活一个安全软件，这样用户可及时了解设备上存在的任何移动安全威肋的通知。及时删除这些恶意应用程序，不仅可以延长电池使用时间，也可以大大减少流量的消耗，保护用户个人信息和数据安全。

> 参考来源：<https://securityaffairs.co/wordpress/137549/malware/clicker-apps-google-play.html>

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