---
title: 年末购物季将至，一复杂钓鱼工具正针对北美消费者
url: https://www.freebuf.com/news/350147.html
source: FreeBuf网络安全行业门户
date: 2022-11-19
fetch_date: 2025-10-03T23:13:33.180650
---

# 年末购物季将至，一复杂钓鱼工具正针对北美消费者

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

年末购物季将至，一复杂钓鱼工具正针对北美消费者

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

年末购物季将至，一复杂钓鱼工具正针对北美消费者

2022-11-18 11:44:07

所属地 上海

据BleepingCompuer 11月17日消息，自 9 月中旬以来，一个复杂的网络钓鱼工具包一直以北美用户为目标，利用劳动节和万圣节等假期，对消费者发动攻击。

根据Akamai安全研究人员的说法，该工具包使用多种逃避检测技术，并结合了多种机制，其中最为独特的功能是能基于令牌系统，确保每个受害者都被重定向到一个唯一的 URL钓鱼页面。

## 活动概览

Akamai 发现该钓鱼活动始于 2022 年 9 月，通过发送“有机会赢得知名品牌的奖品”为主题的钓鱼邮件，吸引那些企图寻找节日特惠的消费者上钩。

![](https://image.3001.net/images/20221118/1668751800_637721b83f65de71360eb.png!small)钓鱼邮件示例

钓鱼邮件中的链接不会引发任何安全告警，在经过一系列重定向，以及借助URL 缩短器隐藏大多数 URL后，大多防病毒软件无法识别其有害性，而攻击者滥用 Google、AWS 和 Azure 等具有良好声誉的合法云服务，也为绕过保护机制提供了便利。

这些钓鱼邮件假冒的品牌包括体育用品公司 Dick's、高端行李箱制造商 Tumi、达美航空、山姆超市会员店、开市客等。当受害者来到钓鱼页面，都会提示需完成一份限时5分钟的调查问卷来获得奖品。由于时间的紧迫性，让不少受奖品驱使的受害者没有时间过多犹豫。此外，为进一步打消受害者顾虑，攻击者还炮制出带有奖品实物图片的虚假用户评价，从而增加了钓鱼的成功率。

![](https://image.3001.net/images/20221118/1668753488_63772850d0368cddc8161.png!small)虚假的用户晒单评价

在获得所谓的“奖品”后，受害者会被要求输入付款的详细信息，以支付奖品运费。这些信息会被攻击者窃取，用于其他的网上消费。

Akamai 表示，大约 89% 的受害者来自美国和加拿大，并根据他们的确切位置，重定向至不同的网络钓鱼站点，以冒充当地品牌。

## 每个受害者都有一个唯一的 URL

通常，URL地址中的“#”用于将访问者引导至链接页面的特定部分，而在此钓鱼邮件活动中，锚标记代表 JavaScript 在网络钓鱼登陆时使用的令牌，将目标重定向至一个新的URL。

“HTML 锚点之后的值不会被视为 HTTP 参数，也不会被发送到服务器，但受害者浏览器上运行的 JavaScript 代码可以访问该值，”Akamai解释称。“在网络钓鱼诈骗的背景下，当验证它是否是恶意的安全产品扫描时，放置在 HTML 锚点之后的值可能会被忽略或忽略。”

Akamai 分享了如下两图，展示网络钓鱼链接锚点如何用于创建重定向链接。

![](https://image.3001.net/images/20221118/1668753557_63772895802dbe6a7c800.png!small)基于锚令牌的重定向

安全产品和网络流量检测工具会忽略此令牌，因此不会给攻击者带来风险，并且能规避研究人员、分析师和其他非受害人群对钓鱼页面的访问。而对于受害者，该令牌还能对其活动进行追踪。总体而言，该工具包结合了几乎所有已知的有效性和检测规避技术，使其成为针对北美网络用户一个不可忽视的潜在威胁。

随着黑色星期五和圣诞节购物季的临近，专家提示，消费者在收到有关促销和特别优惠的信息时应格外警惕。

> 参考来源：<https://www.bleepingcomputer.com/news/security/phishing-kit-impersonates-well-known-brands-to-target-us-shoppers/>

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

活动概览

每个受害者都有一个唯一的 URL

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