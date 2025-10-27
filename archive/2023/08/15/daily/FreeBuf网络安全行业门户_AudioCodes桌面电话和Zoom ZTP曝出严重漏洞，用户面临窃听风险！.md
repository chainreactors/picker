---
title: AudioCodes桌面电话和Zoom ZTP曝出严重漏洞，用户面临窃听风险！
url: https://www.freebuf.com/news/374724.html
source: FreeBuf网络安全行业门户
date: 2023-08-15
fetch_date: 2025-10-04T12:02:42.515356
---

# AudioCodes桌面电话和Zoom ZTP曝出严重漏洞，用户面临窃听风险！

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

AudioCodes桌面电话和Zoom ZTP曝出严重漏洞，用户面临窃听风险！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

AudioCodes桌面电话和Zoom ZTP曝出严重漏洞，用户面临窃听风险！

2023-08-14 10:56:56

所属地 上海

近日，AudioCodes桌面电话和Zoom的Zero Touch Provisioning (ZTP)被曝存在多个安全漏洞，恶意攻击者可能利用这些漏洞进行远程攻击。

SySS安全研究员Moritz Abrell在周五（8月11日）发表的一份分析报告中提到：外部攻击者可利用在AudioCodes公司的桌面电话和Zoom公司的Zero Touch Provisioning功能中发现的漏洞远程控制这些设备。

这种不受约束的访问权限可以通过设备透视和攻击企业网络窃听房间或电话，甚至建立一个由受感染设备组成的僵尸网络。这项研究已在上周早些时候举行的美国黑帽安全大会上发表。

这个问题的根源其实在于 Zoom 的 ZTP，它允许 IT 管理员以集中的方式配置 VoIP 设备，从而使企业能够在需要时轻松地监控、排除故障和更新设备。这是通过部署在本地网络中的网络服务器为设备提供配置和固件更新来实现的。

具体来说，在从 ZTP 服务检索配置文件时，发现它缺乏客户端验证机制，从而导致攻击者有可能触发从恶意服务器下载恶意固件。

![1691981792_64d997e0d1e0b764fdb88.png!small](https://image.3001.net/images/20230814/1691981792_64d997e0d1e0b764fdb88.png!small)

该研究进一步揭示了AudioCodes VoIP桌面电话(支持Zoom ZTP)的加密例程中存在不适当的身份验证问题，这些例程允许解密敏感信息，例如密码和配置文件，这些信息通过电话使用的重定向服务器传输，以获取配置。

这两个弱点，即未经验证的所有权错误和认证硬件中的缺陷，可能会被塑造成一个漏洞链，通过滥用Zoom的ZTP并触发任意设备安装它来提供恶意固件。

当这些漏洞结合在一起时，可以用来远程接管任意设备。由于这种攻击具有高度可扩展性，因此可能构成重大的安全风险。

大约一年前，这家德国网络安全公司发现了微软Teams Direct Routing功能中的一个安全问题，该问题可能使安装容易受到收费欺诈攻击。

Abrell当时就曾表示过：外部未经身份验证的攻击者能够发送特制的SIP消息，并假扮这些消息是来自微软。这样受害者的会话边界控制器就会将这些消息正确分类。从而让那些未经授权的外部电话通过受害者的电话进行拨打。

> 参考来源：[Zoom ZTP & AudioCodes Phones Flaws Uncovered, Exposing Users to Eavesdropping (thehackernews.com)](https://thehackernews.com/2023/08/zoom-ztp-audiocodes-phones-flaws.html)

# 安全漏洞 # 未授权访问漏洞

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