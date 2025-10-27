---
title: 警惕！通过谷歌和必应搜索广告传播的新型恶意活动
url: https://www.freebuf.com/articles/373279.html
source: FreeBuf网络安全行业门户
date: 2023-07-29
fetch_date: 2025-10-04T11:54:00.554158
---

# 警惕！通过谷歌和必应搜索广告传播的新型恶意活动

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

警惕！通过谷歌和必应搜索广告传播的新型恶意活动

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

警惕！通过谷歌和必应搜索广告传播的新型恶意活动

2023-07-28 11:13:04

所属地 上海

![](https://image.3001.net/images/20230728/1690511658_64c3292aa5efd5e4a0f25.jpg!small)

据观察，一种新的恶意广告活动利用谷歌搜索和必应的广告，以AnyDesk、Cisco AnyConnect VPN和WinSCP等IT工具的用户为目标，诱骗他们下载木马安装程序，目的是入侵企业网络，并可能在未来实施勒索软件攻击。

Sophos在周三的一份分析报告中称，这种 "机会主义 "活动被称为 "**Nitrogen**"，旨在部署Cobalt Strike等第二阶段攻击工具。

eSentire 在 2023 年 6 月首次记录了 Nitrogen，详细描述了一个感染链，它将用户重定向到受攻击的 WordPress 网站，最终将 Python 脚本和 Cobalt Strike Beacons 发送到目标系统上。

Sophos 研究人员表示："在整个感染链中，威胁方使用不常见的导出转发和 DLL 预加载技术来掩盖其恶意活动“。

Python 脚本一旦启动，就会建立一个 Meterpreter 反向 TCP 外壳，从而允许攻击者在受感染的主机上远程执行代码，并下载一个 Cobalt Strike Beacon 以便后期利用。

研究人员说：搜索引擎内显示的广告已成为攻击者常用的手段。通过广撒网的方式，诱使毫无戒心的用户点击并下载。

这其中包括，网络犯罪分子利用付费广告引诱用户访问恶意网站，诱使他们下载 BATLOADER、EugenLoader（又名 FakeBat）和 IcedID 等多种恶意软件，然后利用这些恶意软件传播信息窃取程序和其他有效载荷。

不仅如此，Sophos 还说它在著名的暗网市场上发现了 "大量关于SEO中毒，恶意广告和相关服务的广告和讨论”，以及提供受损Google Ads帐户的卖家。

这也进一步说明 "攻击者对 SEO 中毒和恶意广告有着浓厚的兴趣"。

> 参考链接：https://thehackernews.com/2023/07/new-malvertising-campaign-distributing.html

# 资讯 # 木马 # 恶意软件

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