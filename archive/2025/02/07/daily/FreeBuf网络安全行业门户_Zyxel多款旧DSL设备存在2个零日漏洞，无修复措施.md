---
title: Zyxel多款旧DSL设备存在2个零日漏洞，无修复措施
url: https://www.freebuf.com/news/421152.html
source: FreeBuf网络安全行业门户
date: 2025-02-07
fetch_date: 2025-10-06T20:36:58.944822
---

# Zyxel多款旧DSL设备存在2个零日漏洞，无修复措施

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

Zyxel多款旧DSL设备存在2个零日漏洞，无修复措施

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Zyxel多款旧DSL设备存在2个零日漏洞，无修复措施

2025-02-06 14:50:03

所属地 上海

Zyxel周二发布消息称，涉及多款旧DSL用户端设备（CPE）产品中的两个零日漏洞将不再提供修复措施。此前，威胁情报公司GreyNoise曾发出警告，有1500多台设备受到一个严重的命令注入漏洞影响，而且这个漏洞正在被基于Mirai的僵尸网络大肆利用。

![](https://image.3001.net/images/20250206/1738824689_67a45bf104b3e825bfe39.jpg!small)

GreyNoise公司表示：“在发现利用CVE - 2024 - 40891的IP地址与被归类为Mirai的IP地址存在显著重叠后，我们对Mirai的一个近期变种展开了调查，结果确认利用CVE - 2024 - 40891的能力已经被整合到某些Mirai变种之中。”

CVE - 2024 - 40891这个漏洞，于2024年中旬和CVE - 2024 - 40890（也是一个类似的命令注入漏洞）一同被披露出来。它们的主要区别在于攻击向量，一个是HTTP，另一个是Telnet。

攻击者能够利用这些安全漏洞，在易受攻击的设备上执行任意命令，进而完全掌控设备并窃取数据，这极有可能危及部署这些产品的所在网络。

周二当天，Zyxel 明确表示，这两个问题会影响到多款DSL CPE型号，具体包含VMG1312 - B10A、VMG1312 - B10B、VMG1312 - B10E、VMG3312 - B10A、VMG3313 - B10A、VMG3926 - B10B、VMG4325 - B10A、VMG4380 - B10A、VMG8324 - B10A、VMG8924 - B10A、SBG3300以及SBG3500。

Zyxel 还指出，在这些设备上，广域网（WAN）接入和用于利用漏洞的Telnet功能，默认是处于禁用状态的。而且，攻击者若要利用这些漏洞，需要使用被攻破的凭据登录受影响的设备才行。

按照供应商的说法，由于受影响的型号是多年前就已经停止支持的老旧设备，所以针对这两个漏洞都不会发布补丁。对于在这些DSL CPE产品中新发现的一个漏洞（编号CVE - 2025 - 0890，该漏洞允许攻击者使用默认凭据登录管理界面），同样也不会有补丁发布。

VulnCheck公司向合勤科技报告了这些漏洞，并且解释说，受影响的设备预先配置有三个硬编码账户，分别是“supervisor”、“admin”和“zyuser”。

其中，supervisor在网络界面不可见，但在Telnet界面具备相应功能，包括能够访问一个隐藏命令，通过这个命令它可以获得对系统的无限制访问权限。而zyuser账户在用户表中是可见的，并且具有提升后的权限，攻击者可利用它通过已被利用的CVE - 2024 - 40891漏洞实现完全远程代码执行。

VulnCheck公司表示：“虽然这些设备已经老化，按道理应该停止支持了，但目前仍有数千台设备处于在线暴露的状态。默认凭据与命令注入这两者相结合，使得它们成为容易被攻击的目标，这也凸显出不安全默认配置以及糟糕的漏洞透明度所带来的危险。”

据Zyxel 称，VulnCheck公司在2024年7月就报告了CVE - 2024 - 40890和CVE - 2024 - 40891这两个漏洞，不过当时并没有提供详细报告，而是直接公开披露了这些漏洞。直到GreyNoise上周发出野外利用警告之后，VulnCheck公司才发送了关于所有三个漏洞的详细信息。

供应商还发出警告，受影响的设备“是已经达到产品生命周期终止（EOL）状态多年的老旧产品。按照行业产品生命周期管理惯例，合勤科技建议客户用新一代设备替换这些老旧产品，这样才能实现最佳保护。”

参考来源：<https://www.securityweek.com/zyxel-issues-no-patch-warning-for-exploited-zero-days/>

# 漏洞 # 安全漏洞 # 零日漏洞

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