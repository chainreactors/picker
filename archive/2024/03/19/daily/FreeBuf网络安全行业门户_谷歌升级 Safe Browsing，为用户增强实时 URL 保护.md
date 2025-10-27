---
title: 谷歌升级 Safe Browsing，为用户增强实时 URL 保护
url: https://www.freebuf.com/news/395061.html
source: FreeBuf网络安全行业门户
date: 2024-03-19
fetch_date: 2025-10-04T12:12:19.852313
---

# 谷歌升级 Safe Browsing，为用户增强实时 URL 保护

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

谷歌升级 Safe Browsing，为用户增强实时 URL 保护

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌升级 Safe Browsing，为用户增强实时 URL 保护

2024-03-18 10:23:19

所属地 上海

上周四（3月15日），谷歌宣布宣布升级 Google Safe Browsing，为用户提供实时 URL 保护功能，降低用户受到恶意网站攻击的风险。

![1710728684_65f7a5eccdb4f99c94eee.png!small](https://image.3001.net/images/20240318/1710728684_65f7a5eccdb4f99c94eee.png!small)

桌面版和 iOS 版 Chrome 浏览器的标准保护模式将根据谷歌服务器端的已知不良网站列表对网站进行实时检查。通过匹配主列表，帮助用户防范网络钓鱼攻击、恶意软件和潜在有害程序。

Chrome 浏览器用户在 Standard 级别保护下，在设备本地存储一份不良网站黑名单，每隔 30 到 60 分钟和谷歌云服务器同步，而现在谷歌将这项安全方案挪到谷歌服务器端，这样可以实现实时检测。
谷歌新闻稿中前后对比图如下：
![1710728828_65f7a67c0bd7c47c58a56.png!small](https://image.3001.net/images/20240318/1710728828_65f7a67c0bd7c47c58a56.png!small)
此前方案为每隔 30 到 60 分钟同步：
![1710728837_65f7a685c3f9d248becd4.png!small](https://image.3001.net/images/20240318/1710728837_65f7a685c3f9d248becd4.png!small)
新方案可实时保护 URL，图源谷歌

去年 9 月，谷歌表示会尝试在不与公司共享用户浏览历史记录的情况下切换到实时服务器端检查。之所以做出这样的改变，是因为有害网站的列表数量正在快速增长，而且 60% 的钓鱼域名存在时间不到 10 分钟，因此很难对其进行拦截。但并非所有设备都有必要来维护这个不断增长的列表，也并非所有设备都能以必要的频率接收和应用列表更新。
因此，在新的架构下，用户每次尝试访问一个网站时，都会根据浏览器的全局和本地缓存（包含已知的安全 URL 和以前的安全浏览检查结果）对 URL 进行检查，以确定网站的状态。如果缓存中没有访问过的 URL，就会进行实时检查，将 URL 混淆成 32 字节的完整哈希值，然后截断成 4 字节长的哈希前缀，加密后发送到隐私服务器。
谷歌解释称：隐私服务器会移除潜在的用户标识符，并通过 TLS 连接将加密的哈希前缀转发给安全浏览服务器，该连接会将请求与许多其他 Chrome 浏览器用户的请求混合在一起。安全浏览服务器随后会解密哈希前缀，并将其与服务器端数据库进行匹配，返回与浏览器发送的哈希前缀之一相匹配的所有不安全 URL 的完整哈希值。在客户端，完整哈希值会与访问过的 URL 的完整哈希值进行比较，如果发现匹配，就会显示警告信息。
此外，Chrome 浏览器用户还可以选择 Enhanced Protection 模式，这是一种安全浏览模式，使用人工智能来阻止攻击，并提供针对恶意 Chrome 扩展程序的保护。

谷歌最近还更新了 iOS 设备上的密码检查功能。除了让用户意识到密码泄露外，它还会标记弱密码和重复使用的密码。

> 参考来源：[Google Introduces Enhanced Real-Time URL Protection for Chrome Users](https://thehackernews.com/2024/03/google-introduces-enhanced-real-time.html)

# 谷歌 Chrome # URL安全

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