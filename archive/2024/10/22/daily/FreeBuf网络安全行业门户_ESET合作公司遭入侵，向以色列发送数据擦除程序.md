---
title: ESET合作公司遭入侵，向以色列发送数据擦除程序
url: https://www.freebuf.com/news/413257.html
source: FreeBuf网络安全行业门户
date: 2024-10-22
fetch_date: 2025-10-06T18:51:27.418096
---

# ESET合作公司遭入侵，向以色列发送数据擦除程序

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

ESET合作公司遭入侵，向以色列发送数据擦除程序

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

ESET合作公司遭入侵，向以色列发送数据擦除程序

2024-10-21 10:14:37

所属地 上海

据BleepingComputer消息，有黑客入侵了 ESET 在以色列的独家合作公司，并向以色列企业发送网络钓鱼电子邮件，其中暗藏数据擦除器以进行系统破坏性攻击。

据观察，这一钓鱼活动从10月8日开始，这些邮件带有ESET 徽标且从合法的 eset.co.il 域发送，表明以色列分部的电子邮件服务器在攻击中遭到破坏，ESET 告诉 BleepingComputer，他们位于以色列的分销商由Comsecure 运营。

这些电子邮件显示来自ESET 高级威胁防御团队，警告收件企业由政府支持的攻击者正试图以他们的设备为目标。为了帮助保护设备，ESET 提供了一个名为“ESET Unleashed”的更高级防病毒工具来抵御威胁。

![](https://image.3001.net/images/20241021/1729476967_6715b967d2e16c770c30b.png!small)钓鱼邮件正文

从网络钓鱼电子邮件标头中，BleepingComputer 已确认该电子邮件来自合法的邮件服务器 eset.co.il，并通过了 SPF、DKIM 和 DMARC 身份验证测试。为了进一步增加攻击的合法性，下载链接托管在 eset.co.il 域的 URL 上，目前已被禁用。

![](https://image.3001.net/images/20241021/1729477038_6715b9ae3ef937b0727c4.png!small)分析显示钓鱼邮件通过了身份验证检查

下载的ZIP 存档包含4个由 ESET 的合法代码签名证书进行数字签名的 DLL 文件和1个未签名的 Setup.exe。这4个 DLL 是作为 ESET 防病毒软件的一部分分发的合法文件。但是Setup.exe 实为恶意数据擦除程序。

![](https://image.3001.net/images/20241021/1729477124_6715ba0489346dc761784.png!small)包含数据擦除器的 ESET Unleashed 文档

BleepingComputer 尝试在虚拟机上测试擦除器，但可执行文件会自动崩溃。网络安全专家凯文-博蒙特（Kevin Beaumont）则在实体 PC 上成功运行了该擦除器，他发现，该恶意程序使用了多种技术来规避安全检测，并调用了各种恶意程序。

目前尚不清楚有多少以色列企业成为此网络钓鱼活动的目标，也不知道 ESET 的以色列分销商 Comsecure 是如何被入侵的。

虽然这次攻击没有被归咎于任何特定的黑客或组织，但数据擦除器长期以来一直是攻击以色列的流行工具。2017年，一个有反以色列和亲巴勒斯坦背景的数据擦除器IsraBye在对以色列组织的攻击中被发现；2023 年，以色列企业遭受了一波BiBi 擦除器攻击，包括教育和技术部门。

**参考来源：**

> [ESET partner breached to send data wipers to Israeli orgs](https://www.bleepingcomputer.com/news/security/eset-partner-breached-to-send-data-wipers-to-israeli-orgs/)

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