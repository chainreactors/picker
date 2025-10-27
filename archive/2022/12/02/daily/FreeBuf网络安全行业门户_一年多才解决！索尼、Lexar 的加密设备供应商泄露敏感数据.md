---
title: 一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据
url: https://www.freebuf.com/news/351241.html
source: FreeBuf网络安全行业门户
date: 2022-12-02
fetch_date: 2025-10-04T00:17:55.574676
---

# 一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据

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

一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

一年多才解决！索尼、Lexar 的加密设备供应商泄露敏感数据

2022-12-01 11:16:34

所属地 上海

##

当用户购买 Sony、Lexar 或 Sandisk USB 密钥或其它任何存储设备时，都会附带一个加密解决方案，以确保数据安全。

据悉，该方案由第三方供应商 ENC Security 开发，然而 近日Cybernews 研究小组披露，该公司在一年多时间里一直在泄露其配置和证书文件。

![1669864989_63881e1d0c2cdb589ea04.jpg!small?1669864989250](https://image.3001.net/images/20221201/1669864989_63881e1d0c2cdb589ea04.jpg!small?1669864989250)

随着事件发酵，ENC Security 迅速做出回复，声称泄露事件原因是第三方供应商的错误配置，在收到通知后已立刻修复漏洞。

> ENC Security 是一家位于荷兰的公司，在全球拥有 1200 万用户，通过其流行 DataVault 加密软件提供“军用级数据保护”解决方案。

## ****Cybernews 发现安全问题****

从 Cybernews 披露的内容来看， 泄漏服务器内的数据主要包括销售渠道的简单邮件传输协议（SMTP）凭证、单一支付平台的 Adyen 密钥、电子邮件营销公司的 Mailchimp API 密钥、许可支付 API 密钥、HMAC 消息验证码以及以 .pem 格式存储的公共和私人密钥。

2021 年 5 月 27 日到 2022 年 11 月 9日 ，一年多的时间里，任何人都可以公开访问这些数据，直到 Cybernews 向 ENC Security 披露该漏洞后，该服务器才被关闭。

安全研究人员 Vareikis 表示，数据暴露长达一年多时间，潜在网络攻击者可利用上述数据进行从网络钓鱼、勒索软件等各种形势的网络攻击。![1669865002_63881e2ac7fea317f8704.jpg!small?1669865003225](https://image.3001.net/images/20221201/1669865002_63881e2ac7fea317f8704.jpg!small?1669865003225)

举个简单的例子，攻击者可能通过销售沟通渠道向客户发送假发票或通过可信的电子邮件地址传播恶意软件来欺骗客户。

此外，由于 Mailchimp API 密钥允许攻击者发送大规模营销活动并查看、收集线索，对攻击者来说无疑具有更大价值。不仅如此，勒索软件运营商也能够利用 .pem 文件里面的密钥开展未经授权的访问，甚至是服务器被接管。Vareikis 一再强调，泄漏一年多的数据对威胁者来说不亚于一个“金矿”。

## ****ENC Security**** ****公司回应****

在收到并仔细分析 Cybernews 研究小组报告后，ENC Security 迅速采取措施，解决安全问题。ENC Security 发言人表示，公司始终认真对待数据的安全和保护，每一个安全问题都会被彻底研究并采取适当的措施进行补救，必要时也会通知客户进一步加强安全。

## ****ENC Security 也曾********出现其它安全事件****

Cybernews 研究小组的发现与 2021 年 12 月研究人员 Sylvain Pelissier 的发现一样令人担忧。

去年，Pelissier 演示了在 ENC Security  DataVault 加密软件中发现的几个漏洞，这些漏洞可能允许攻击者在未经检测的情况下，获取用户密码并修改 vault 中的文件。不止于此，DataVaul 软件还使用了“计算工作量不足的密码哈希”，这可能会让攻击者暴力破解用户密码。

当时，ENC Security 承认 DataVault 软件 6 和 7.1 及其衍生版本易受攻击，不久后通过发布升级解决了漏洞。

Vareikis 告诫用户，一些“超级”安全公司喜欢使用类似“军用级”加密等词汇，过度夸大产品能力，进行虚假宣传，对于这种宣传，用户应当始终持怀疑态度。

**参考文章：**

> https://cybernews.com/security/encsecurity-leaked-sensitive-data/

# 系统安全 # 数据泄漏

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

Cybernews 发现安全问题

ENC Security 公司回应

ENC Security 也曾出现其它安全事件

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