---
title: 高危 AMI MegaRAC 漏洞影响 AMD、ARM、HPE、Dell 等众多服务器
url: https://www.freebuf.com/news/351686.html
source: FreeBuf网络安全行业门户
date: 2022-12-07
fetch_date: 2025-10-04T00:41:16.283708
---

# 高危 AMI MegaRAC 漏洞影响 AMD、ARM、HPE、Dell 等众多服务器

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

高危 AMI MegaRAC 漏洞影响 AMD、ARM、HPE、Dell 等众多服务器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

高危 AMI MegaRAC 漏洞影响 AMD、ARM、HPE、Dell 等众多服务器

2022-12-06 11:45:13

Bleeping Computer 网站披露，Eclypsium 的研究人员发现美国 Megatrends  MegaRAC 基板管理控制器（BMC）软件中存在三个漏洞，这些漏洞影响许多云服务和数据中心运营商使用的服务器设备。![1670298330_638ebada3150f97d09ea3.jpg!small?1670298330543](https://image.3001.net/images/20221206/1670298330_638ebada3150f97d09ea3.jpg!small?1670298330543)

据悉，研究人员在检查泄露的美国 Megatrends专有代码，以及 MegaRAC BMC 固件后发现了这些漏洞，某些条件下，攻击者一旦成功利用漏洞，便可以执行任意代码、并绕过身份验证，执行用户枚举。

MegaRAC BMC 作为一个远程系统管理解决方案，允许管理员像站在设备前面一样远程排除服务器故障。目前， MegaRAC BMC 固件至少有 15 家服务器制造商使用，其中主要包括 AMD、Ampere Computing、ASRock、华硕、ARM、Dell EMC、Gigabyte、Hewlett-Packard Enterprise、华为、浪潮、联想、英伟达、高通、Quanta 和 Tyan 等。

## ****漏洞详细信息********：****

Eclypsium 发现并向美国 Megatrends 和受影响供应商报告的三个漏洞如下：

CVE-2022-40259（CVSS v3.1评分：9.9“严重”）Redfish API 存在任意代码执行缺陷。

CVE-2022-40242（CVSS v3.1评分：8.3“高”）:sysadmin 用户的默认凭据，允许攻击者建立管理 shell。

CVE-2022-2827（CVSS v3.1评分：7.5“高”），请求操作漏洞，允许攻击者枚举用户名并确定帐户是否存在。

这三个漏洞中最严重的一个漏洞是 CVE-2022-40259，尽管它需要事先访问至少一个低特权帐户才能执行 API回调。

## ****漏洞产生的********影响****

CVE-2022-40259 和 CVE-2022-40242 这两个漏洞非常严重，因为攻击者可以利用它们无需进一步升级，即可访问管理外壳。一旦攻击者成功利用了这些漏洞，可能会引起数据操纵、数据泄露、服务中断、业务中断等。

Eclypsium 在报告中强调，由于数据中心倾向于在特定硬件平台上实现标准化，任何 BMC 级别的漏洞都很可能适用于大量设备，并可能影响整个数据中心及其提供的服务。

更糟糕的是，服务器组件上托管和云提供商的标准化意味着这些漏洞可以轻易影响数十万，甚至数百万系统。因此，建议系统管理员立刻禁用远程管理选项，并在可能的情况下添加远程身份验证步骤。

此外，管理员应尽量减少 Redfish 等服务器管理界面的外部暴露，并确保所有系统上都安装了最新的可用固件更新。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/severe-ami-megarac-flaws-impact-servers-from-amd-arm-hpe-dell-others/

# 漏洞

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

漏洞详细信息：

漏洞产生的影响

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