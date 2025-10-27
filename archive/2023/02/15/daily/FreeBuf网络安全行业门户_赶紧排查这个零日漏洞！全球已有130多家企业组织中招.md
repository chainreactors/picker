---
title: 赶紧排查这个零日漏洞！全球已有130多家企业组织中招
url: https://www.freebuf.com/news/357487.html
source: FreeBuf网络安全行业门户
date: 2023-02-15
fetch_date: 2025-10-04T06:37:41.405294
---

# 赶紧排查这个零日漏洞！全球已有130多家企业组织中招

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

赶紧排查这个零日漏洞！全球已有130多家企业组织中招

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

赶紧排查这个零日漏洞！全球已有130多家企业组织中招

2023-02-14 10:31:58

所属地 上海

据BleepingComputer 2月10日消息，Clop 勒索软件组织最近利用 GoAnywhere MFT 安全文件传输工具中的零日漏洞，从 130 多个企业组织中窃取了数据。

![](https://image.3001.net/images/20230214/1676342089_63eaf3498c369b553903f.png!small)

该安全漏洞被追踪为 CVE-2023-0669，攻击者能够在未修补的 GoAnywhere MFT 实例上远程执行代码，并将其管理控制台暴露在互联网中。

Clop向BleepingComputer透露，他们在攻击系统服务器10天后窃取了相应数据，并称还可以通过受害者网络横向移动，从而部署勒索软件有效负载来加密系统。但他们并没有这么做，只窃取了存储在受感染的 GoAnywhere MFT 服务器上的数据。当BleepingComputer向他们询问何时开始攻击、索要多少赎金时，该组织拒绝透露这些信息。

BleepingComputer 无法独立证实 Clop 的说法，GoAnywhere MFT的开发商 Fortra（以前称为 HelpSystems）也未提供有关漏洞利用和勒索软件组织的更多信息。

2月6日， CVE-2023-0669漏洞的PoC代码被公开，Fortra在2月7日和2月8日分别发布了紧急更新，称其部分 MFTaaS 实例也在攻击中遭到破坏。CISA 已在2月10日正式将漏洞 添加到其已知被利用漏洞目录中。

虽然 Shodan 显示有超过 1000 个 GoAnywhere 实例被暴露，但只有 135 个在易受攻击的 8000 和 8001端口上。

![](https://image.3001.net/images/20230214/1676342033_63eaf311c0c621ac9b2b4.png!small)暴露于互联网的 GoAnywhere MFT 设备 (Shodan)

此次Clop 勒索软件攻击被指与他们在 2020 年 12 月使用的策略非常相似，当时他们发现并利用Accellion FTA 零日漏洞窃取了大约 100 家公司的数据，包括能源巨头壳牌公司（Shell）、零售巨头克罗格（Kroger）、网络安全公司 Qualys以及全球多所高校。

2021 年 6 月，在代号为“旋风行动”的国际执法行动之后，Clop 的部分基础设施被封，当时 6 名为 Clop 勒索软件团伙提供服务的人员在乌克兰被捕。

> 参考来源：[Clop ransomware claims it breached 130 orgs using GoAnywhere zero-day](https://www.bleepingcomputer.com/news/security/clop-ransomware-claims-it-breached-130-orgs-using-goanywhere-zero-day/)

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