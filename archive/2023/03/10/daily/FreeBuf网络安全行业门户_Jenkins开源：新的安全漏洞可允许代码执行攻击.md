---
title: Jenkins开源：新的安全漏洞可允许代码执行攻击
url: https://www.freebuf.com/news/359871.html
source: FreeBuf网络安全行业门户
date: 2023-03-10
fetch_date: 2025-10-04T09:08:51.825327
---

# Jenkins开源：新的安全漏洞可允许代码执行攻击

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

Jenkins开源：新的安全漏洞可允许代码执行攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Jenkins开源：新的安全漏洞可允许代码执行攻击

2023-03-09 14:54:23

所属地 上海

![](https://image.3001.net/images/20230309/1678339381_64096d357d59cf2363035.png!small)

Jenkins开源自动化服务器中披露了两个严重的安全漏洞，利用此漏洞可在目标系统上执行任何代码。

这些漏洞被追踪为CVE-2023-27898和CVE-2023-27905，影响Jenkins服务器和更新中心，并被云安全公司Aqua统称为CorePlague。2.319.2之前所有版本的Jenkins都存在这个漏洞并可被利用。

该公司在一份报告中说："利用这些漏洞可以让未经认证的攻击者在受害者的Jenkins服务器上执行任意代码，有可能导致Jenkins服务器完全被破坏“。

这些漏洞是Jenkins处理更新中心的插件造成的，致使攻击者上传带有恶意有效载荷的插件并触发跨站脚本（XSS）攻击。

Aqua说："一旦受害者在他们的Jenkins服务器上打开可用插件管理器，XSS就会被触发，允许攻击者利用脚本控制台API在Jenkins服务器上运行任意代码”。

同时，这些漏洞也可能影响到托管的Jenkins服务器，甚至在服务器不能通过互联网公开访问的情况下被利用，因为公共Jenkins更新中心也可能被 "攻击者注入"。

然而，这种攻击的前提条件是，流氓插件与Jenkins服务器兼容，并显示在 "可用的插件管理器 "页面上。

在该漏洞情况被披露之后，目前Jenkins已经为更新中心和服务器发布了补丁。建议用户将他们的Jenkins服务器更新到最新的可用版本，以减少潜在风险。

> 参考链接：thehackernews.com/2023/03/jenkins-security-alert-new-security.html

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