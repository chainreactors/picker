---
title: 奔驰、宝马等汽车品牌存在 API 漏洞，可能暴露车主个人信息
url: https://www.freebuf.com/news/354346.html
source: FreeBuf网络安全行业门户
date: 2023-01-06
fetch_date: 2025-10-04T03:10:27.904782
---

# 奔驰、宝马等汽车品牌存在 API 漏洞，可能暴露车主个人信息

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

奔驰、宝马等汽车品牌存在 API 漏洞，可能暴露车主个人信息

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

奔驰、宝马等汽车品牌存在 API 漏洞，可能暴露车主个人信息

2023-01-05 13:19:08

所属地 上海

Bleeping Computer 网站披露，近 20 家汽车制造商和服务机构存在 API 安全漏洞，这些漏洞允许黑客进行远程解锁、启动车辆、跟踪汽车行踪，窃取车主个人信息的恶意攻击活动。

![1672901585_63b673d168fb827001901.jpg!small](https://image.3001.net/images/20230105/1672901585_63b673d168fb827001901.jpg!small)

据悉，API 漏洞主要影响宝马、罗尔斯、奔驰、法拉利、保时捷、捷豹、路虎、福特、起亚、本田、英菲尼迪、日产、讴歌、现代、丰田和创世纪等其知名汽车品牌。此外，漏洞还影响汽车技术品牌 Spireon 和 Reviver 以及流媒体服务 SiriusXM。

## ****谁发现了 AP I安全漏洞？****

网络安全研究员 Sam Curry 和其研究团队，在数十家顶级汽车制造商生产的车辆和车联网服务中，发现了API 漏洞问题。 此前，Sam Curry于 2022 年 11 月披露了现代、Genesis、本田、讴歌、日产、英菲尼迪和 SiriusXM 的安全问题。

目前，受影响的供应商已经修复所有漏洞问题，现在无法利用这些漏洞。在经过了 90 天的漏洞披露期后，Curry 团队发表了一篇关于更详细的 API 漏洞博客文章，展示了黑客如何利用这些漏洞来解锁和启动汽车。

## ****攻击者可以利用漏洞，访问内部系统****

宝马和奔驰中发现了最严重的 API 漏洞，这些漏洞受到 SSO（单点登录）漏洞的影响，攻击者可以利用访问内部业务系统。 例如在对梅赛德斯-奔驰的测试中，研究人员可以访问多个私有 GitHub 实例、Mattermost 上的内部聊天频道、服务器、Jenkins 和 AWS 实例，并成功连接到客户汽车的 XENTRY 系统 等。![1672902136_63b675f805d1ba126598a.jpg!small?1672902136138](https://image.3001.net/images/20230105/1672902136_63b675f805d1ba126598a.jpg!small?1672902136138)

梅赛德斯-奔驰内部系统（资料来源：Sam Curry）

在对宝马的测试中，研究人员可以访问内部经销商门户网站，查询任何汽车的 VIN，并检索包含敏感车主信息的销售文件。此外，攻击者还可以利用 SSO 漏洞，以员工或经销商的身份登录账户，访问保留给内部使用的应用程序。![1672902223_63b6764f068aed56b82b7.jpg!small?1672902223009](https://image.3001.net/images/20230105/1672902223_63b6764f068aed56b82b7.jpg!small?1672902223009)

访问宝马门户网站上的车辆详细信息（资料来源：Sam Curry）

## ****暴露车主详细信息****

研究人员利用其它 API 漏洞，可以访问起亚、本田、英菲尼迪、日产、讴歌、梅赛德斯-奔驰、现代、创世纪、宝马、劳斯莱斯、法拉利、福特、丰田、保时捷等汽车品牌车主的个人身份信息。

对于豪华品牌汽车来讲，披露车主信息特别危险，因为在某些情况下，数据中包括销售信息、物理位置和客户居住地址。例如法拉利在其 CMS 上的 SSO 漏洞，暴露了后端 API 路线，使其有可能从 JavaScript 片段中提取凭据。攻击者可以利用这些漏洞访问、修改或删除任何法拉利客户账户，管理他们的车辆资料，甚至可以将自己设定为车主。![1672902400_63b67700019a622039c51.jpg!small?1672902400338](https://image.3001.net/images/20230105/1672902400_63b67700019a622039c51.jpg!small?1672902400338)

披露法拉利用户数据细节（资料来源：Sam Curry）

## ****跟踪********车辆 GPS****

API 漏洞可能允许黑客实时跟踪汽车，带来潜在的物理风险，并影响到数百万车主的隐私，其中保时捷是最受影响的品牌之一，其远程信息处理系统漏洞使攻击者能够检索车辆位置并发送指令。

GPS 跟踪解决方案 Spireon 也易受汽车位置泄露的影响，涉及到 1550 万辆使用其服务的车辆，甚至允许管理员访问其远程管理面板，使攻击者能够解锁汽车、启动引擎或禁用启动器。![1672902565_63b677a572b82f517699b.jpg!small?1672902565633](https://image.3001.net/images/20230105/1672902565_63b677a572b82f517699b.jpg!small?1672902565633)

Spireon 管理面板上的历史 GPS 数据（资料来源：Sam Curry）

值得一提的是，数字车牌制造商 Reviver 也容易受到未经验证的远程访问其管理面板的影响，该面板可能允许任何人访问 GPS 数据和用户记录、更改车牌信息等。

Curry 表示这些漏洞或允许攻击者在 Reviver 面板上将车辆标记为 “被盗”，这会自动将事件通知警方，从而使车主/驾驶员面临不必要的风险。![1672902776_63b6787882f9fb71527c1.jpg!small?1672902776854](https://image.3001.net/images/20230105/1672902776_63b6787882f9fb71527c1.jpg!small?1672902776854)

远程修改 Reviver 车牌（资料来源：Sam Curry）

## ****最大限度地减少安全风险****

车主可以通过最大限度减少存储在车辆或汽车 APP 中的个人信息,来保护自己免受此类漏洞的影响。此外，将车载远程信息处理设置为最高私密等级，并阅读汽车厂家的隐私政策,以了解其数据的使用方式也至关重要。

最后，Sam Curry 着重强调，当购买二手车时，请确保前车主的帐户已被彻底删除。如果有条件的话，尽量使用强密码，并为车辆的应用程序和服务设置双因素认证。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/toyota-mercedes-bmw-api-flaws-exposed-owners-personal-info/

# API # API安全

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

谁发现了 AP I安全漏洞？

攻击者可以利用漏洞，访问内部系统

暴露车主详细信息

跟踪车辆 GPS

最大限度地减少安全风险

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