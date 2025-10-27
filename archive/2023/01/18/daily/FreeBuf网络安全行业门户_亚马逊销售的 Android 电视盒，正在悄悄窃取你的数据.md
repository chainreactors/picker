---
title: 亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据
url: https://www.freebuf.com/news/355537.html
source: FreeBuf网络安全行业门户
date: 2023-01-18
fetch_date: 2025-10-04T04:09:22.406842
---

# 亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据

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

亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

亚马逊销售的 Android 电视盒，正在悄悄窃取你的数据

2023-01-17 16:00:45

所属地 上海

安全研究员 Daniel Milisic 发现他在亚马逊上购买的 T95 Android 电视盒感染了复杂的预装恶意软件。

![](https://image.3001.net/images/20230117/1673941735_63c652e73a5ced7e32818.png!small)

这款 Android 电视盒型号可在亚马逊和全球速卖通上以低至 40 美元的价格购买。

该设备配备了 Android 10（带有可用的 Play 商店）和 Allwinner H616 处理器。Milisic 在其固件中发现了预加载的恶意软件。

Milisic 购买了 T95 Android 电视盒来运行 Pi-hole，这是一个 Linux 网络级广告和互联网跟踪器拦截应用程序。

运行 Pi-hole 后，他注意到该盒子正在到达与恶意软件活动相关的地址。

![](https://image.3001.net/images/20230117/1673941774_63c6530e6cb89d138f3d5.png!small)

“在搜索完成后，专家试图删除该恶意软件。在使用 tcpflow 和 nethogs 监控流量的恶意软件层之上发现了有问题的进程/APK，然后将其从 ROM 中删除。但有些无法追踪的恶意软件已经深深地嵌入到 ROM 中。它是非常复杂的恶意软件，其运行方式类似于 CopyCatin。

该设备使用使用测试密钥签名的 Android 10 操作系统。专家还发现它具有可通过以太网端口访问的 Android 调试桥 (ADB)。

设备固件中嵌入的恶意代码类似于 Android CopyCat恶意软件。专家指出，他测试的所有 AV 产品都无法检测到威胁。

Milisic 还设计了一个技巧来阻止恶意软件使用 Pi-hole 将命令和控制服务器 YCXRL.COM 的 DNS 更改为 127.0.0.2。

他还创建了一个 iptables 规则，将所有 DNS 重定向到 Pi-hole，因为恶意软件/病毒/任何无法解析的东西都会使用外部 DNS。

通过这样做，C&C 服务器最终会攻击 Pi-hole 网络服务器，而不是将我的登录名、密码和其他 PII 发送到 Linode（在撰写本文时目前 **为 139.162.57.1​​35**）。

请注意，Milisic 提出的解决方案并没有删除恶意代码或禁用它，它只是消除了它对其操作的干扰。

为了确定 s T95 Android 电视盒是否已被感染，研究人员建议检查是否存在名为：

> `/data/system/Corejava`

和一个名为

> `/data/system/shared_prefs/open_preference.xml`？

Milisic 无法测试来自同一供应商或型号的其他设备以确定它们的固件是否也被感染。

最后，米利西奇总结道：“不要相信 AliExpress 或亚马逊上的廉价 Android 盒子，它们的固件带有测试密钥签名。他们正在窃取您的数据（除非您可以查看 DNS 日志）并且不留痕迹！”

> 参考链接：https://securityaffairs.com/140866/security/t95-android-tv-box-malware.html?\_gl=1\*xyes7s\*\_ga\*MzM0ODQ4Njk4LjE2NjY2NjUyMzU.\*\_ga\_NPN4VEKBTY\*MTY3Mzk0MDcxNS4yLjAuMTY3Mzk0MDcxNS42MC4wLjA.\*\_ga\_8ZWTX5HC4Z\*MTY3Mzk0MDcxNi4xMDkuMC4xNjczOTQwNzE2LjAuMC4w\*\_ga\_P62M3QN974\*MTY3Mzk0MDcxNi4xMDcuMC4xNjczOTQwNzE2LjAuMC4w&\_ga=2.226772445.1960127043.1673940716-334848698.1666665235

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