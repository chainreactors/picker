---
title: 拉拢受害者对付保险公司，这款勒索软件套路满满
url: https://www.freebuf.com/news/358342.html
source: FreeBuf网络安全行业门户
date: 2023-02-23
fetch_date: 2025-10-04T07:51:13.211988
---

# 拉拢受害者对付保险公司，这款勒索软件套路满满

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

拉拢受害者对付保险公司，这款勒索软件套路满满

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

拉拢受害者对付保险公司，这款勒索软件套路满满

2023-02-22 11:54:01

所属地 上海

套路千千万，唯独这家很特殊，一个新型勒索软件组织的攻击策略竟是离间受害者与保险公司。

据Security Affairs 2月21日消息，于去年10月出现的名为HardBit的勒索软件组织试图通过这一策略，让受害者的保险公司承担勒索赎金。

![](https://image.3001.net/images/20230222/1677043915_63f5a8cb0067077f36f9e.png!small)

在HardBit勒索软件看来，遭受勒索攻击后，受害者的保险公司大多会以各种理由推脱，拒绝足额赔付，如果受害者能够与HardBit分享保险范围的可用性和条款，便能合伙商量如何让保险公司足额赔付，赎金金额不会超过受害者的投保金额。这样让看似受损的只有保险公司。

可见，该策略的核心是防止保险公司协商降低赔付赎金，在表面上拉拢受害者的同时让自身的经济利益最大化。

但同样的，为了防止受害者恢复加密文件，该勒索软件使用服务控制管理器和Windows备份工具目录删除了卷影复制服务（VSS）以及任何影子副本。

研究人员注意到，该恶意软件会加密许多文件，在 Windows 重新启动时可能会导致错误。为了避免在后续启动时出现问题，恶意软件会编辑启动配置以启用“忽略任何故障”选项并禁用恢复选项。

为了防止 Windows Defender Antivirus 阻止勒索软件进程，它对 Windows 注册表进行了多项更改以禁用许多 Windows Defender 功能（即篡改保护、反间谍软件功能、实时行为监控、实时访问（文件）保护、和实时进程扫描）。勒索软件还会将软件副本复制到受害者的“启动”文件夹（如果不存在）来实现持久性，可执行文件名会模仿合法服务主机可执行文件 svchost.exe，以避免检测。

> 参考来源：[HardBit ransomware gang adjusts their demands so the insurance company would cover the ransom cost](https://securityaffairs.com/142538/cyber-crime/hardbit-ransomware-insurance.html)

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