---
title: 谷歌推出首款量子弹性 FIDO2 安全密钥
url: https://www.freebuf.com/news/375205.html
source: FreeBuf网络安全行业门户
date: 2023-08-18
fetch_date: 2025-10-04T11:59:42.426941
---

# 谷歌推出首款量子弹性 FIDO2 安全密钥

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

谷歌推出首款量子弹性 FIDO2 安全密钥

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

谷歌推出首款量子弹性 FIDO2 安全密钥

2023-08-17 11:06:15

所属地 上海

![](https://image.3001.net/images/20230817/1692239032_64dd84b8e0b1f69c8d0ca.png!small)

谷歌在本周二宣布推出首个量子弹性 FIDO2 安全密钥，作为其 OpenSK 安全密钥计划的一部分。

Elie Bursztein和Fabian Kaczmarczyck表示：这一开源硬件优化的实现采用了一种新颖的ECC/Dilithium混合签名模式，它结合了ECC抵御标准攻击的安全性和Dilithium抵御量子攻击的弹性。

OpenSK是用Rust编写的安全密钥，支持FIDO U2F和FIDO2标准。

在不到一周前，谷歌表示，它计划在 Chrome 116 中增加对抗量子加密算法的支持，以便在 TLS 连接中设置对称密钥。

这也是未来转向可抵御量子攻击努力的一部分，因此有必要尽早采用此类技术，以便进一步推广。

谷歌表示：随着包括 Dilithium 算法在内的公钥量子弹性加密技术实现了标准化，我们现在有了一条明确的途径来确保安全密钥免受量子攻击。

与 Chrome 浏览器的混合机制（X25519 和 Kyber-768 的组合）类似，谷歌提出的 FIDO2 安全密钥椭圆曲线数字签名算法（ECDSA）和最近标准化的抗量子签名算法 Dilithium 的结合。

这种混合签名模式是与苏黎世联邦理工学院（ETH Zürich）合作开发的，是一种基于 Rust 的内存优化实现，只需要 20 KB 内存，非常适合在安全密钥受限的硬件上运行。

最后谷歌表示，希望看到这种组合实现（或其变体）被标准化，成为FIDO2密钥规范的一部分，并得到主流网络浏览器的支持，从而保护用户的凭证免受量子攻击。

参考链接：https://thehackernews.com/2023/08/google-introduces-first-quantum.html

# 资讯

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