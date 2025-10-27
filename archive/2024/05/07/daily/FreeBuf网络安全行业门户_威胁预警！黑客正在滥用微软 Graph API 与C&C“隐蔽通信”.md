---
title: 威胁预警！黑客正在滥用微软 Graph API 与C&C“隐蔽通信”
url: https://www.freebuf.com/news/399970.html
source: FreeBuf网络安全行业门户
date: 2024-05-07
fetch_date: 2025-10-06T17:17:47.917787
---

# 威胁预警！黑客正在滥用微软 Graph API 与C&C“隐蔽通信”

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

威胁预警！黑客正在滥用微软 Graph API 与C&C“隐蔽通信”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

威胁预警！黑客正在滥用微软 Graph API 与C&C“隐蔽通信”

2024-05-06 10:31:04

所属地 上海

![1714962325_66383f950bc814855d7ad.png!small](https://image.3001.net/images/20240506/1714962325_66383f950bc814855d7ad.png!small)

如今，越来越多黑客开始利用微软Graph API逃避安全检测。博通公司旗下的赛门铁克威胁猎人团队在一份报告中提到，这样做是为了方便与托管在微软云服务上的命令与控制（C&C）基础设施进行通信。

自2022年1月以来，已观察到多个与国家结盟的黑客组织使用微软图形API进行C&C。其中包括被追踪为 APT28、REF2924、Red Stinger、Flea、APT29 和 OilRig 等黑客组织。

在微软图形应用程序接口（Graph API）被更广泛地采用之前，第一个已知的微软图形应用程序接口滥用实例可追溯到 2021 年 6 月。当时一个被称为 Harvester 的组织使用了一个名为 Graphon 的定制植入程序，该植入程序利用 API 与微软基础架构进行通信。

赛门铁克称最近检测到了针对乌克兰一个未具名组织使用了相同的技术，其中涉及部署一个以前未记录的名为BirdyClient（又名OneDriveBirdyClient）的恶意软件。

这是一个名称为 "vxdiff.dll "的 DLL 文件，与一个名为 Apoint 的应用程序（"apoint.exe"）的合法 DLL 文件相同，其目的是连接到 Microsoft Graph API，并将 OneDrive 用作 C&C 服务器，从中上传和下载文件。

目前尚不清楚 DLL 文件的确切传播方式，也不知道是否涉及 DLL 侧载，具体威胁方以及最终目的是什么目前也是未知。

赛门铁克表示：攻击者与 C&C 服务器的通信通常会引起目标组织的警惕。Graph API之所以受到攻击者的青睐，可能是因为他们认为这种通信方式不太会引起怀疑。

除了看起来不显眼之外，它还是攻击者廉价而安全的基础设施来源，因为OneDrive等服务的基本账户是免费的。Permiso揭示了拥有特权访问权限的攻击者如何利用云管理命令在虚拟机上执行命令。

这家云安全公司表示：大多数情况下，攻击者会利用信任关系，通过入侵第三方外部供应商或承包商，在连接的虚拟机或混合环境中执行命令，而这些外部供应商或承包商拥有管理内部云环境的权限。

通过入侵这些外部实体，攻击者可以获得高级访问权限，从而在虚拟机或混合环境中执行命令。

> 参考来源：[Hackers Increasingly Abusing Microsoft Graph API for Stealthy Malware Communications](https://thehackernews.com/2024/05/hackers-increasingly-abusing-microsoft.html)

# 恶意软件 # 通信安全

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