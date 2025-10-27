---
title: CISA在三星和D-Link设备中发现8个被积极利用的漏洞
url: https://www.freebuf.com/articles/371012.html
source: FreeBuf网络安全行业门户
date: 2023-07-05
fetch_date: 2025-10-04T11:54:02.540169
---

# CISA在三星和D-Link设备中发现8个被积极利用的漏洞

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

CISA在三星和D-Link设备中发现8个被积极利用的漏洞

* ![]()
* 关注

CISA在三星和D-Link设备中发现8个被积极利用的漏洞

2023-07-04 11:05:10

所属地 上海

![](https://image.3001.net/images/20230704/1688437111_64a3817708014da78bf30.png!small)

美国网络安全和基础设施安全局（CISA）根据已有的证据，将8个被积极利用的漏洞列入已知的漏洞（KEV）目录中。

这8个被积极利用的漏洞包括影响三星智能手机的六个漏洞和影响D-Link设备的两个漏洞。以下是这八个漏洞：

* CVE-2021-25394（CVSS评分：6.4）--三星移动设备条件竞争漏洞
* CVE-2021-25395（CVSS评分：6.4）--三星移动设备的条件竞争漏洞
* CVE-2021-25371 (CVSS score: 6.7) - 三星移动设备中使用的DSP驱动程序存在未指明的漏洞，允许加载任意ELF库
* CVE-2021-25372 (CVSS score: 6.7) - 三星移动设备中的DSP驱动程序中存在不适当的边界检查
* CVE-2021-25487 (CVSS score: 7.8) - 三星移动设备的越界读取漏洞，导致任意代码执行
* CVE-2021-25489 (CVSS score: 5.5) - 三星移动设备不恰当的输入验证漏洞导致内核崩溃
* CVE-2019-17621 (CVSS评分：9.8) - D-Link DIR-859路由器中存在未经授权的远程代码执行漏洞
* CVE-2019-20500（CVSS评分：7.8）--D-Link DWL-2600AP中的一个认证的操作系统命令注入漏洞

在增加这两个D-Link漏洞之前，Palo Alto Networks Unit 42上个月报告了与Mirai僵尸网络变体有关的攻击者利用几个物联网设备的漏洞，在2023年3月开始的一系列攻击中传播恶意软件。

然而，现在还不清楚三星设备的漏洞是如何在野外被利用的。但考虑到目标的性质，它们很可能已经被一个商业间谍软件供应商用于高度有针对性的攻击。

值得注意的是，谷歌 "零点计划 "在2022年11月披露了一组漏洞，并表示这些漏洞作为针对三星手机漏洞链的一部分被武器化。

鉴于以上漏洞被积极的利用，联邦民事行政部门（FCEB）机构被要求在2023年7月20日之前实施必要的修复，以确保其网络免受潜在威胁。

> 参考链接：https://thehackernews.com/2023/07/cisa-flags-8-actively-exploited-flaws.html

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