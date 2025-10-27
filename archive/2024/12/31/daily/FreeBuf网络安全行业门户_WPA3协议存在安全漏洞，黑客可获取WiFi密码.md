---
title: WPA3协议存在安全漏洞，黑客可获取WiFi密码
url: https://www.freebuf.com/news/418757.html
source: FreeBuf网络安全行业门户
date: 2024-12-31
fetch_date: 2025-10-06T19:40:49.128862
---

# WPA3协议存在安全漏洞，黑客可获取WiFi密码

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

WPA3协议存在安全漏洞，黑客可获取WiFi密码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

WPA3协议存在安全漏洞，黑客可获取WiFi密码

2024-12-30 13:39:23

所属地 上海

研究人员成功结合中间人攻击（MITM）和社会工程学技术，绕过了Wi - Fi保护协议——WPA3 ，进而获取网络密码。此次研究由西印度大学的Kyle Chadee、Wayne Goodridge和Koffka Khan开展，这一研究揭示了最新无线安全标准存在的安全漏洞。

![](https://image.3001.net/images/20241230/1735537217_67723241defe14c586390.jpg!small)

WPA3于2018年推出，其目的是弥补前身WPA2的缺陷，为Wi - Fi网络提供更强的安全性。其中，“对等同时认证”（SAE）协议是其关键功能之一，该协议旨在让密码能够抵御离线字典攻击。研究人员证实，可利用WPA3过渡模式中的弱点来达成目的，这种过渡模式允许与WPA2设备向后兼容。

![](https://image.3001.net/images/20241230/1735537244_6772325c597407b0b84bb.jpg!small)

借助降级攻击，他们能够捕获部分WPA3交互信息，再结合社会工程技术恢复网络密码。

这种攻击方法主要包含三个步骤：

* 其一，运用降级攻击捕获交互信息；
* 其二，将用户从原始的WPA3网络中解除认证；
* 其三，创建带有强制门户的虚假账号接入点以获取密码。

![](https://image.3001.net/images/20241230/1735537282_677232821da3658b04494.jpg!small)

研究人员利用树莓派模拟WPA3接入点，并借助Airgeddon等开源工具创建恶意接入点。当不知情的用户尝试连接伪造网络时，就会被提示输入Wi - Fi密码，随后该密码会与捕获的交互信息进行验证。

这项研究引发了对WPA3安全性的担忧，特别是在其过渡模式下。研究发现，如果未实施保护管理，攻击就会成功，而很多用户可能并不清楚或者没有启用这一设置。有趣的是，研究人员还发现一些设备无法连接到WPA3网络，这与Wi - Fi联盟所说的与WPA2向后兼容的说法相互矛盾。

尽管这种攻击需要特定条件并且要有用户交互，但它展示了保护无线网络面临的持续挑战。研究人员强调了用户教育以及正确配置WPA3网络以降低此类风险的重要性。

网络安全专家呼吁进一步调查WPA3的漏洞，并开发额外的保护措施。随着Wi - Fi网络不断成为企业和个人的关键基础设施，确保其安全性至关重要。

这项研究的结果提醒我们，即便最先进的安全协议也可能受到技术漏洞与社会工程学巧妙组合的影响。随着WPA3的普及，用户和制造商都必须保持警惕，并实施最佳实践，从而保护无线网络免受潜在攻击。

参考来源：<https://cybersecuritynews.com/researchers-bypass-wpa3-password/#google_vignette>

# 数据安全

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