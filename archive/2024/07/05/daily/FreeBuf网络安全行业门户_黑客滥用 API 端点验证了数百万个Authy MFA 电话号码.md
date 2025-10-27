---
title: 黑客滥用 API 端点验证了数百万个Authy MFA 电话号码
url: https://www.freebuf.com/news/405195.html
source: FreeBuf网络安全行业门户
date: 2024-07-05
fetch_date: 2025-10-06T17:43:20.727267
---

# 黑客滥用 API 端点验证了数百万个Authy MFA 电话号码

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

黑客滥用 API 端点验证了数百万个Authy MFA 电话号码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

黑客滥用 API 端点验证了数百万个Authy MFA 电话号码

2024-07-04 15:07:52

所属地 上海

![1720076760_668649d881710856c9193.png!small](https://image.3001.net/images/20240704/1720076760_668649d881710856c9193.png!small)

近日，Twilio 称发现了一个不安全的 API 端点，允许威胁行为者非法验证数百万 Authy 多因素身份验证用户的电话号码，这可能导致他们收到短信钓鱼，同时还可能会遭遇 SIM 卡交换攻击。

Authy 是一款移动应用程序，可在启用了 MFA 的网站上生成多因素验证码。

6 月底，一个名为 ShinyHunters 的威胁行为者泄露了一个 CSV 文本文件，其中包含他们在 Authy 服务注册的 3300 万个电话号码。

![shinyhunters-twilio.jpg](https://image.3001.net/images/20240705/1720191056_6688085045022fa41fb64.jpg!small)

ShinyHunters 在黑客论坛上分享 Twilio Authy 数据来源：BleepingComputer

CSV 文件包含 33420546 行内容，每一行都包含账户 ID、电话号码、"over\_the\_top "列、账户状态和设备数量。

Twilio 表示，有威胁分子使用了一个未经验证的 API 端点编译了电话号码列表。目前，Twilio 检测到由于使用了未经身份验证的端点，威胁行为者能够识别与 Authy 账户相关的数据，包括电话号码。Twilio 现已采取措施保护该端点的安全，不再允许未经身份验证的请求。

目前还没有任何证据表明威胁行为者获取了 Twilio 的系统或其他敏感数据。不过作为预防措施，Twilio 要求所有 Authy 用户更新到最新的 Android 和 iOS 应用程序，以获取最新的安全更新，并敦促所有 Authy 用户保持警惕，提高对网络钓鱼和网络诈骗攻击的防范意识。

2022 年Twilio 曾披露过两起漏洞攻击事件，当时有威胁行为者入侵了其基础设施并访问 Authy 客户信息。

## 滥用不安全的 API

据悉，这些数据是通过不安全的 API 端点输入大量电话号码列表编制而成的。如果号码有效，端点就会返回在 Authy 注册的相关账户信息。

这种技术与此前威胁行为者滥用Twitter API 和 Facebook API 编译数千万用户配置文件的方式类似。

ShinyHunters 在帖子中称：虽然 Authy 只获取电话号码，但这对于那些想实施诈骗、SIM 卡交换攻击入侵账户的用户仍然有利。并暗示威胁行为者将电话号码列表与据称 Gemini 和 Nexo 数据泄露事件中泄露的电话号码进行比较。

如果发现匹配，威胁者可能会尝试执行 SIM 卡交换攻击或网络钓鱼攻击，入侵加密货币交易所账户并窃取所有资产。

Twilio 目前已经发布了新的安全更新，并建议用户升级到 Authy Android（v25.1.0）和 iOS App（v26.1.0），其中包括安全更新。

> 参考来源：[Hackers abused API to verify millions of Authy MFA phone numbers (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/hackers-abused-api-to-verify-millions-of-authy-mfa-phone-numbers/)

# API安全

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

滥用不安全的 API

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