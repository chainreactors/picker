---
title: TPM 2.0 爆出漏洞，数十亿物联网设备受到严重威胁！
url: https://www.freebuf.com/news/359428.html
source: FreeBuf网络安全行业门户
date: 2023-03-07
fetch_date: 2025-10-04T08:49:08.931460
---

# TPM 2.0 爆出漏洞，数十亿物联网设备受到严重威胁！

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

TPM 2.0 爆出漏洞，数十亿物联网设备受到严重威胁！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

TPM 2.0 爆出漏洞，数十亿物联网设备受到严重威胁！

2023-03-06 13:54:45

所属地 香港

The Hacker News 网站消息，可信平台模块 ( TPM ) 2.0 参考库规范中爆出一个严重安全漏洞，这些漏洞可能会导致设备信息泄露或权限提升。![1678082222_640580ae53d137fdd4310.png!small?1678082223588](https://image.3001.net/images/20230306/1678082222_640580ae53d137fdd4310.png!small?1678082223588)

## 漏洞或影响数十亿物联网设备

2022 年 11 月，网络安全公司 Quarkslab 发现并报告漏洞问题，其中一个漏洞被追踪为 CVE-2023-1017（涉及越界写入），另一个漏洞追踪为 CVE-2023-1018（可能允许攻击者越界读取）。

Quarkslab 指出，使用企业计算机、服务器、物联网设备、TPM 嵌入式系统的实体组织以及大型技术供应商可能会受到这些漏洞的影响，并一再强调，漏洞可能会影响数十亿设备。

## 可信平台模块 (TPM)

可信平台模块 (TPM) 技术是一种基于硬件的解决方案，可为现代计算机上的操作系统提供安全的加密功能，使其能够抵抗篡改。

微软表示，最常见的 TPM 功能用于系统完整性测量以及密钥创建和使用，在系统启动过程中，可以测量加载的启动代码（包括固件和操作系统组件）并将其记录在 TPM 中，完整性测量值可用作系统启动方式的证据，并确保仅在使用正确的软件启动系统时才使用基于 TPM 的密钥。

## 可信计算组织（TCG）

漏洞事件发酵后，可信计算组织（简称：TCG，由 AMD、惠普、IBM、英特尔和微软组成）指出，由于缺乏必要的检查，出现漏洞问题，最终或引起本地信息泄露或权限升级。![](https://image.3001.net/images/20230306/1678083110_64058426630cfa849171d.jpg!small)CERT 协调中心（CERT/CC）在一份警报中表示，受影响的用户应该考虑使用 TPM 远程验证来检测设备变化，并确保其 TPM 防篡改。

最后，安全专家建议用户应用 TCG 以及其它供应商发布的安全更新，以解决这些漏洞并减轻供应链风险。

**参考文章：**

> https://thehackernews.com/2023/03/new-flaws-in-tpm-20-library-pose-threat.html

# 漏洞利用

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

漏洞或影响数十亿物联网设备

可信平台模块 (TPM)

可信计算组织（TCG）

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